# science:code
# status: workflow-owned
# task_ids: [t117, t119]
# science:end

"""assemble_matrix.py — WP2 (plan:0010): pivot per-contrast fgsea NES tables into
ONE pathway x contrast matrix for a rank matrix (strict | sensitivity), plus the
grouping metadata the rank battery needs and the NES-comparability check the WP2
DoD requires.

Config-driven (single source = config.yaml), mirroring stage_matrix.py: the script
reconstructs the rank matrix's columns from `contrasts[*].matrix` + the nested
two-matrix composition (sensitivity = strict + ME/CFS additions), splits them into
BUILT (parse produced the uniform contract) vs OMITTED (parse `status: deferred`, or
the salmon decoy's run subset unresolved), reads each built column's NES vector from
`{proc}/fgsea/{contrast}.nes.tsv`, and writes:

  <out-matrix>    gene_set  x  built-contrast   (NES; "NA" where untestable in a contrast)
  <out-grouping>  per-column condition/trigger/platform/compartment/onset/control tags,
                  the OMITTED columns with their blocker (never a silent drop), and the
                  same-tissue LC RNA-seq NES-comparability report.

Expression is NEVER merged across datasets: deposits meet ONLY here, at the NES level.
Fail-early: a missing/short NES file, a gene-set-set mismatch across columns, or zero
built columns HALTs — no partial matrix.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

# nested two-matrix design (mirrors the Snakefile MATRIX_COMPOSITION): the
# sensitivity rank matrix is strict columns PLUS the ME/CFS additions.
MATRIX_COMPOSITION = {
    "strict": ("strict",),
    "sensitivity": ("strict", "sensitivity"),
}


def halt(msg: str):
    sys.stderr.write(f"[assemble_matrix] HALT: {msg}\n")
    sys.exit(1)


def matrix_columns(cfg: dict, matrix: str) -> list[str]:
    tags = MATRIX_COMPOSITION[matrix]
    return [c for c, spec in cfg["contrasts"].items() if spec.get("matrix") in tags]


def is_buildable(cfg: dict, contrast: str) -> bool:
    """A column is buildable iff its accession produced the uniform expr contract
    (parse block present and not deferred). The salmon decoy needs a resolved run
    subset. Deferred columns are recorded as omitted, never silently dropped."""
    spec = cfg["contrasts"][contrast]
    acc = spec["accession"]
    if spec.get("quantify") == "salmon":
        runs = cfg.get("salmon", {}).get("runs", {}).get(acc, {}).get("accessions", [])
        return bool(runs)
    p = cfg.get("parse", {}).get(acc, {})
    return bool(p) and p.get("status") != "deferred" and p.get("handler") in {"matrix", "tar", "prebuilt"}


def omit_reason(cfg: dict, contrast: str) -> str:
    spec = cfg["contrasts"][contrast]
    acc = spec["accession"]
    if spec.get("quantify") == "salmon":
        return f"salmon decoy — run subset unresolved (WP1b d); {cfg['salmon']['runs'].get(acc, {}).get('note', '')}"
    p = cfg.get("parse", {}).get(acc, {})
    if not p:
        return f"no parse block for {acc}"
    if p.get("status") == "deferred":
        return p.get("deferred_reason", f"parse status: deferred ({acc})")
    return f"handler '{p.get('handler')}' does not produce expr ({acc})"


def read_nes(path: Path, contrast: str) -> pd.Series:
    if not path.exists():
        halt(f"{contrast}: NES table absent: {path}")
    df = pd.read_csv(path, sep="\t", na_values=["", "NA"], keep_default_na=False)
    for col in ("gene_set", "NES"):
        if col not in df.columns:
            halt(f"{contrast}: NES table missing column '{col}' ({path})")
    if df["gene_set"].duplicated().any():
        halt(f"{contrast}: duplicate gene_set rows in {path}")
    return pd.Series(df["NES"].to_numpy(dtype=float), index=df["gene_set"].astype(str), name=contrast)


def spearman(a: np.ndarray, b: np.ndarray, extra: np.ndarray | None = None) -> tuple[float, int]:
    """Spearman rho + n on pairwise-complete observations (average-rank ties, no scipy).
    `extra` optionally restricts to a boolean subset (e.g. the enriched sets)."""
    m = np.isfinite(a) & np.isfinite(b)
    if extra is not None:
        m = m & extra
    n = int(m.sum())
    if n < 3:
        return float("nan"), n
    return float(np.corrcoef(_avg_rank(a[m]), _avg_rank(b[m]))[0, 1]), n


def _avg_rank(x: np.ndarray) -> np.ndarray:
    order = np.argsort(x, kind="mergesort")
    ranks = np.empty(len(x), dtype=float)
    ranks[order] = np.arange(1, len(x) + 1, dtype=float)
    # average ranks within tie groups
    _, inv, counts = np.unique(x, return_inverse=True, return_counts=True)
    sums = np.zeros(len(counts))
    np.add.at(sums, inv, ranks)
    return (sums / counts)[inv]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--matrix", required=True, choices=list(MATRIX_COMPOSITION))
    ap.add_argument("--proc", required=True, help="processed dir (PROC), holds fgsea/<contrast>.nes.tsv")
    ap.add_argument("--out-matrix", required=True)
    ap.add_argument("--out-grouping", required=True)
    args = ap.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text())
    proc = Path(args.proc)

    cols = matrix_columns(cfg, args.matrix)
    built = [c for c in cols if is_buildable(cfg, c)]
    omitted = [c for c in cols if not is_buildable(cfg, c)]
    if not built:
        halt(f"{args.matrix}: no buildable columns (all {len(cols)} deferred/unstaged)")

    # --- read NES vectors, align on the pinned gene-set universe -----------------
    series = [read_nes(proc / "fgsea" / f"{c}.nes.tsv", c) for c in built]
    ref = series[0].index
    for s in series[1:]:
        if not s.index.equals(ref):
            # same pinned universe -> identical gene_set set/order expected
            if set(s.index) != set(ref):
                halt(f"{s.name}: gene-set universe differs from {built[0]} "
                     f"(|only_here|={len(set(s.index) - set(ref))}, "
                     f"|only_ref|={len(set(ref) - set(s.index))})")
    mat = pd.concat([s.reindex(ref) for s in series], axis=1)
    mat.index.name = "gene_set"
    mat.to_csv(args.out_matrix, sep="\t", na_rep="NA")

    # --- grouping metadata (per built column) ------------------------------------
    def col_tags(c: str) -> dict:
        s = cfg["contrasts"][c]
        return {
            "contrast": c,
            "accession": s["accession"],
            "trigger": s.get("trigger"),
            "compartment": s.get("compartment"),
            "platform": s.get("platform"),
            "matrix_tag": s.get("matrix"),
            "onset_certainty": s.get("onset_certainty"),
            "control_type": s.get("control_type"),
            "loo_flag": s.get("loo_flag"),
        }

    columns_meta = [col_tags(c) for c in built]

    # --- NES-comparability check (WP2 DoD): same-tissue LC RNA-seq deposits must
    # produce concordant NES. Computed on the ENRICHED (informative) subset — sets
    # reaching |NES| >= enrichment_threshold in EITHER deposit — because Spearman over
    # ALL sets is diluted toward 0 by the ~700 near-zero-NES noise pathways (which
    # conflates "no shared signal" with genuine discordance). A same-tissue LC group
    # PASSES iff its BEST-matched assessable pair reaches min_concordance; underpowered
    # deposits (< min_enriched_sets enriched) are reported as low_signal, not failed.
    cmp_cfg = cfg.get("nes_comparability", {})
    enr_thr = float(cmp_cfg.get("enrichment_threshold", 1.5))
    min_enr_sets = int(cmp_cfg.get("min_enriched_sets", 30))
    min_conc = float(cmp_cfg.get("min_concordance", 0.20))

    lc_rnaseq = [c for c in built
                 if cfg["contrasts"][c].get("trigger") == "sars-cov-2"
                 and cfg["contrasts"][c].get("platform") == "rnaseq"]
    comparability = {
        "method": "enriched_subset_spearman",
        "enrichment_threshold": enr_thr,
        "min_enriched_sets": min_enr_sets,
        "min_concordance": min_conc,
        "groups": [],
        "concern": False,
    }
    by_comp: dict[str, list[str]] = {}
    for c in lc_rnaseq:
        by_comp.setdefault(cfg["contrasts"][c]["compartment"], []).append(c)
    for comp, members in by_comp.items():
        if len(members) < 2:
            continue
        pairs, assessable_rhos = [], []
        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                a, b = members[i], members[j]
                av, bv = mat[a].to_numpy(), mat[b].to_numpy()
                rho_all, n_all = spearman(av, bv)
                enr = (np.abs(av) >= enr_thr) | (np.abs(bv) >= enr_thr)
                rho_enr, n_enr = spearman(av, bv, enr)
                assessable = n_enr >= min_enr_sets and not np.isnan(rho_enr)
                pairs.append({
                    "a": a, "b": b,
                    "spearman_all": None if np.isnan(rho_all) else round(rho_all, 4),
                    "spearman_enriched": None if np.isnan(rho_enr) else round(rho_enr, 4),
                    "n_all": n_all, "n_enriched": n_enr,
                    "assessable": assessable,
                })
                if assessable:
                    assessable_rhos.append(rho_enr)
        best = round(max(assessable_rhos), 4) if assessable_rhos else None
        low_signal = [m for m in members
                      if int(((np.abs(mat[m].to_numpy()) >= enr_thr)).sum()) < min_enr_sets]
        group_ok = best is not None and best >= min_conc
        comparability["groups"].append({
            "compartment": comp, "members": members,
            "best_enriched_rho": best, "concordant": group_ok,
            "low_signal_deposits": low_signal, "pairs": pairs,
        })
        # concern only if a group with >=1 assessable pair fails to reach min_concordance
        if assessable_rhos and not group_ok:
            comparability["concern"] = True

    grouping = {
        "matrix": args.matrix,
        "composition_tags": list(MATRIX_COMPOSITION[args.matrix]),
        "n_gene_sets": int(mat.shape[0]),
        "n_columns_built": len(built),
        "n_columns_declared": len(cols),
        "columns": columns_meta,
        "omitted_columns": [
            {"contrast": c, "accession": cfg["contrasts"][c]["accession"], "reason": omit_reason(cfg, c)}
            for c in omitted
        ],
        "distinct_triggers": sorted({m["trigger"] for m in columns_meta if m["trigger"]}),
        "distinct_platforms": sorted({m["platform"] for m in columns_meta if m["platform"]}),
        "distinct_compartments": sorted({m["compartment"] for m in columns_meta if m["compartment"]}),
        "nes_comparability": comparability,
    }
    Path(args.out_grouping).write_text(json.dumps(grouping, indent=2) + "\n")

    concern = " [COMPARABILITY CONCERN]" if comparability["concern"] else ""
    best_by_group = {g["compartment"]: g["best_enriched_rho"] for g in comparability["groups"]}
    sys.stderr.write(
        f"[assemble_matrix] {args.matrix}: {mat.shape[0]} gene_sets x {len(built)} built columns "
        f"({len(omitted)} omitted: {[c for c in omitted]}); "
        f"triggers={grouping['distinct_triggers']}; LC-RNAseq best enriched rho={best_by_group}{concern}\n")


if __name__ == "__main__":
    main()
