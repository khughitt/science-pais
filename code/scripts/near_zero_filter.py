#!/usr/bin/env python3
"""Near-zero log_mu filter for GSE130353 (t035 WP4) — contrast-blind KDE antimode.

Implements the LOCKED, verdict-affecting procedure (pre-reg:0002 3rd amendment;
plan:0003 KD9). This is a PROCEDURE, not a fixed constant: the threshold τ is
DERIVED from the pooled, group-blind density — never chosen by hand, and it never
falls back to a fixed τ.

  1. Pooled group-blind summary: per-gene MEDIAN log_mu across all 40 donors
     (labels are never read here).
  2. Estimate the density of that pooled summary by a fixed method: Gaussian KDE,
     Silverman bandwidth.
  3. τ := the antimode = lowest-density grid point STRICTLY BETWEEN the two
     highest modes (the unexpressed mode near log_mu≈-14 and the expressed mode).
  4. Retain gene g iff #{donors : log_mu(g) > τ} >= min_donors (one full group),
     so a gene expressed in any single group survives — no cross-group-shared bias.

Build-fatal halt (t037 STRUCTURAL): if the pooled density is NOT clearly bimodal
the sentinel is WITHHELD and the DAG halts (a recorded amendment is required) —
it must NOT silently fall back to a fixed τ. "Not clearly bimodal" is the locked
three-part guard (config preprocessing.near_zero_filter.bimodality):
  - require_interior_antimode: < 2 KDE modes, or the antimode is not interior to
    the two highest modes;
  - min_mode_separation: the two highest modes are < min_mode_separation natural-
    log units apart;
  - min_antimode_mass_fraction: the antimode split is too lopsided — the minority
    side of τ (by gene count of the pooled per-gene medians) holds < this fraction
    of the mass, i.e. min(frac<=τ, frac>τ) < min_antimode_mass_fraction.
The derived τ, the mode/antimode geometry, the guard outcomes, and the
retained/dropped counts are all logged to cohort_audit.json (evidence is written
even on a structural halt; only the sentinel is withheld).
"""
from __future__ import annotations

import argparse
import gzip
import json
import sys
from pathlib import Path

import numpy as np
from scipy.signal import find_peaks
from scipy.stats import gaussian_kde

GRID_N = 2048   # fixed evaluation grid → deterministic τ (no RNG anywhere)


def read_matrix(path: Path) -> tuple[list[str], list[str], np.ndarray]:
    """Return (gene_ids, sample_cols, values[n_genes×n_samples]); '' / 'NA' → nan."""
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split("\t")
        samples = header[1:]
        genes: list[str] = []
        rows: list[list[float]] = []
        for line in fh:
            parts = line.rstrip("\n").split("\t")
            genes.append(parts[0])
            rows.append([np.nan if v in ("", "NA") else float(v) for v in parts[1:]])
    return genes, samples, np.asarray(rows, dtype=float)


def derive_antimode(pooled: np.ndarray, cfg: dict) -> dict:
    """Derive τ from the pooled per-gene median density; evaluate the bimodality guard.

    Returns a dict with τ, the two-highest-mode geometry, the three guard facts,
    and a list of structural failures (empty iff the density is clearly bimodal).
    """
    lo, hi = float(pooled.min()), float(pooled.max())
    grid = np.linspace(lo, hi, GRID_N)
    kde = gaussian_kde(pooled, bw_method="silverman")
    dens = kde(grid)

    peak_idx, _ = find_peaks(dens)
    failures: list[str] = []
    facts: dict = {
        "kde_bandwidth": "silverman",
        "grid_n": GRID_N,
        "grid_range": [round(lo, 6), round(hi, 6)],
        "n_modes": int(peak_idx.size),
    }

    if peak_idx.size < 2:
        failures.append(f"density is not bimodal: found {peak_idx.size} KDE mode(s), need >= 2")
        facts["structural_failures"] = failures
        facts["tau"] = None
        return facts

    # the two HIGHEST modes (by density), ordered by position on the axis
    top2 = peak_idx[np.argsort(dens[peak_idx])[-2:]]
    m_lo, m_hi = int(min(top2)), int(max(top2))
    # antimode = lowest-density grid point strictly between the two highest modes
    between = np.arange(m_lo + 1, m_hi)
    if between.size == 0:
        failures.append("no interior grid points between the two highest modes (antimode not interior)")
        facts["structural_failures"] = failures
        facts["tau"] = None
        return facts
    anti = int(between[np.argmin(dens[between])])
    tau = float(grid[anti])

    mode_sep = float(grid[m_hi] - grid[m_lo])
    n = pooled.size
    frac_below = float(np.count_nonzero(pooled <= tau)) / n
    frac_above = float(np.count_nonzero(pooled > tau)) / n
    minority_mass = min(frac_below, frac_above)

    req_interior = bool(cfg.get("require_interior_antimode", True))
    min_sep = float(cfg["min_mode_separation"])
    min_mass = float(cfg["min_antimode_mass_fraction"])

    # antimode is interior by construction here; the flag stays a guard knob.
    if req_interior and not (m_lo < anti < m_hi):
        failures.append("antimode is not interior to the two highest modes")
    if mode_sep < min_sep:
        failures.append(f"two highest modes separated by {mode_sep:.3f} < min_mode_separation {min_sep} (nat-log)")
    if minority_mass < min_mass:
        failures.append(f"antimode split lopsided: minority mass {minority_mass:.4f} < min_antimode_mass_fraction {min_mass}")

    facts.update({
        "mode_positions_top2": [round(float(grid[m_lo]), 6), round(float(grid[m_hi]), 6)],
        "mode_densities_top2": [round(float(dens[m_lo]), 8), round(float(dens[m_hi]), 8)],
        "mode_separation": round(mode_sep, 6),
        "min_mode_separation": min_sep,
        "antimode_density": round(float(dens[anti]), 8),
        "frac_pooled_below_tau": round(frac_below, 6),
        "frac_pooled_above_tau": round(frac_above, 6),
        "antimode_minority_mass_fraction": round(minority_mass, 6),
        "min_antimode_mass_fraction": min_mass,
        "tau": round(tau, 6),
        "structural_failures": failures,
    })
    return facts


def write_matrix(path: Path, genes: list[str], samples: list[str], values: np.ndarray) -> None:
    """Deterministic gzip (mtime=0); rows already sorted by ensembl_gene_id."""
    out = ["ensembl_gene_id\t" + "\t".join(samples) + "\n"]
    for g, row in zip(genes, values):
        cells = ["NA" if np.isnan(v) else repr(float(v)) for v in row]
        out.append(g + "\t" + "\t".join(cells) + "\n")
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as raw, gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as gz:
        gz.write("".join(out).encode("utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser(description="GSE130353 near-zero KDE-antimode filter (WP4)")
    ap.add_argument("--harmonized", required=True, type=Path)
    ap.add_argument("--out-expr", required=True, type=Path)
    ap.add_argument("--out-audit", required=True, type=Path)
    ap.add_argument("--sentinel", required=True, type=Path)
    ap.add_argument("--min-donors", required=True, type=int)
    ap.add_argument("--method", required=True)           # locked: pooled_kde_antimode
    ap.add_argument("--kde-bandwidth", required=True)     # locked: silverman
    ap.add_argument("--require-interior-antimode", required=True)
    ap.add_argument("--min-mode-separation", required=True, type=float)
    ap.add_argument("--min-antimode-mass-fraction", required=True, type=float)
    args = ap.parse_args()

    if args.method != "pooled_kde_antimode":
        sys.exit(f"[near_zero_filter] near_zero_filter.method '{args.method}' not implemented (fail-early)")
    if args.kde_bandwidth != "silverman":
        sys.exit(f"[near_zero_filter] kde_bandwidth '{args.kde_bandwidth}' not implemented (fail-early)")

    genes, samples, values = read_matrix(args.harmonized)
    # pooled, group-blind per-gene summary = median log_mu across all donors
    pooled = np.nanmedian(values, axis=1)
    finite = np.isfinite(pooled)
    n_all_na = int((~finite).sum())
    if n_all_na:
        # a gene with all-NA across donors has no median — exclude from the KDE
        # (it cannot pass the retain rule either) and log the count.
        pooled = pooled[finite]

    cfg = {
        "require_interior_antimode": args.require_interior_antimode.lower() in ("true", "1", "yes"),
        "min_mode_separation": args.min_mode_separation,
        "min_antimode_mass_fraction": args.min_antimode_mass_fraction,
    }
    geom = derive_antimode(pooled, cfg)
    failures = geom["structural_failures"]
    tau = geom["tau"]

    # apply the retain rule only if τ was derived (i.e. density was bimodal)
    if tau is not None:
        donors_above = np.nansum(values > tau, axis=1).astype(int)
        retain = donors_above >= args.min_donors
    else:
        donors_above = np.zeros(len(genes), dtype=int)
        retain = np.zeros(len(genes), dtype=bool)

    n_in, n_retained = len(genes), int(retain.sum())
    audit = {
        "dataset": "GSE130353",
        "canonical_axis": "ensembl_gene_id",
        "estimate_column": "log_mu",
        "procedure": args.method,
        "min_donors": args.min_donors,
        "n_genes_in": n_in,
        "n_genes_all_na_excluded_from_kde": n_all_na,
        "antimode": geom,
        "tau": tau,
        "retain_rule": f"#{{donors : log_mu > tau}} >= {args.min_donors}",
        "n_genes_retained": n_retained,
        "n_genes_dropped": n_in - n_retained,
        "verdict": "PASS" if not failures else "FAIL (structural: density not clearly bimodal)",
    }
    args.out_audit.parent.mkdir(parents=True, exist_ok=True)
    args.out_audit.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")

    if failures:
        for f in failures:
            print(f"[near_zero_filter] STRUCTURAL FAIL {f}", file=sys.stderr)
        print(f"[near_zero_filter] HALT: density not clearly bimodal; sentinel withheld, "
              f"amendment required. See {args.out_audit}", file=sys.stderr)
        return 1

    # write the retained gene × donor matrix (sorted by ensembl for determinism)
    order = np.argsort(np.asarray(genes))
    keep_sorted = [i for i in order if retain[i]]
    out_genes = [genes[i] for i in keep_sorted]
    out_values = values[keep_sorted, :]
    write_matrix(args.out_expr, out_genes, samples, out_values)

    args.sentinel.parent.mkdir(parents=True, exist_ok=True)
    args.sentinel.write_text(
        f"PASS GSE130353 near-zero filter: tau={tau:.4f} (KDE antimode, bimodal); "
        f"retained {n_retained}/{n_in} genes (min_donors={args.min_donors}).\n",
        encoding="utf-8")
    print(f"[near_zero_filter] PASS tau={tau:.4f} bimodal; retained {n_retained}/{n_in} "
          f"(dropped {n_in - n_retained})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
