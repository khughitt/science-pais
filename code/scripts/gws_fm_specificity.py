# science:code
# status: workflow-owned
# task_ids: [t117]
# science:end

#!/usr/bin/env python3
"""gws_fm_specificity.py — WP4b non-infectious specificity read-across
(task:t117; plan:0010 review Finding D; the t116 Q-D infection-specificity test).

Question: is the learned PAIS shared pathway-response subspace ALSO recovered by a
NON-infectious illness (fibromyalgia / Gulf War Illness)? If a non-infectious
condition recovers the PAIS subspace as well as a genuine held-out PAIS trigger
does, that is evidence for a GENERIC sickness/fatigue manifold, not an
infection-specific attractor (the t116 Q-D ceiling). If it recovers it no better
than a random direction, the subspace is infection-specific.

Method (composition — reuses the WP4 projection machinery verbatim):
  - Build the PAIS shared subspace U_ref from the reference (strict) pathway x
    contrast matrix: standardize columns, take the leading-r left-singular vectors
    (the SAME construction artifact_adjudication.recovered_control_specificity used).
  - Project each admissible non-infectious specificity NES column onto U_ref and
    report its subspace-recovery fraction = ||U_refᵀ z||² / ||z||², against two
    references:
      * random-direction NULL  = r / P (the floor a random column projects to);
      * in-domain HELD-OUT PAIS = project each PAIS column onto U_ref rebuilt from
        the OTHER PAIS columns (how much a genuine PAIS trigger recovers the
        subspace when it did NOT help define it) — the fair ceiling.
  - U_ref (and every held-out reference) is rebuilt on the rows usable for THAT
    projection (PAIS-complete AND the projected column non-NaN), so it stays
    orthonormal on exactly the rows projected.

Reading is CONSERVATIVE by construction. WP3/WP4 established the PAIS subspace is
itself weakly identified (Stage-3c FAILED; R is LOO-fragile; the structural
co-primary shows no homogeneous shared axis). So the emitted status is
`exploratory_flagship`, NOT `validated_specificity`, and a "recovers like PAIS"
reading is only meaningful RELATIVE to the (weak) held-out PAIS baseline, which is
reported alongside. The reverse projection (build U from >=2 non-infectious columns,
project PAIS) is DEFERRED until the queued replication panel is built — one FM
column cannot define a >1-dim non-infectious subspace.

All knobs originate in config.yaml; this script hard-codes no design value.
Fail-early: a requested specificity NES that is absent/malformed HALTs; an
unavailable prong is recorded explicitly (never a silent skip).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import yaml

import rank_estimators as re
import rank_battery as rb
# reuse the WP4 projection primitives verbatim (single source, not a re-implementation)
from artifact_adjudication import read_nes, projection_fraction


def halt(msg: str):
    raise SystemExit(f"[gws_fm_specificity] HALT: {msg}")


def _standardize_vec(z: np.ndarray) -> np.ndarray:
    """Center+scale a single external column exactly as standardize_columns does the
    PAIS columns U_ref is built from (so the projection is on a common basis)."""
    return re.standardize_columns(z.reshape(-1, 1))[:, 0]


def _leading_subspace(Z: np.ndarray, R: int) -> tuple[np.ndarray, int]:
    """Leading-r left-singular vectors of a standardized column block (P x k)."""
    r = max(1, min(R, Z.shape[1], Z.shape[0]))
    U = np.linalg.svd(Z, full_matrices=False)[0][:, :r]
    return U, r


def heldout_pais_projection(Zr: np.ndarray, R: int) -> dict:
    """Fair in-domain ceiling: project each PAIS column onto U_ref rebuilt from the
    OTHER PAIS columns (leave-one-column-out). Returns per-column fractions + summary."""
    K = Zr.shape[1]
    if K < 2:
        return {"applicable": False, "note": "need >=2 PAIS columns for a held-out projection"}
    fracs = {}
    for j in range(K):
        others = [i for i in range(K) if i != j]
        Uj, _ = _leading_subspace(Zr[:, others], R)
        fracs[j] = round(projection_fraction(Uj, Zr[:, j]), 4)
    vals = list(fracs.values())
    return {
        "applicable": True,
        "per_column_fraction": fracs,
        "mean": round(float(np.mean(vals)), 4),
        "min": round(float(np.min(vals)), 4),
        "max": round(float(np.max(vals)), 4),
    }


def specificity_for(spec_id, nes_path, X, R, cols, rec_cfg):
    """Project one non-infectious specificity NES column onto the PAIS subspace."""
    z_full = read_nes(Path(nes_path), spec_id, _GENE_SETS)
    pais_ok = ~np.isnan(X).any(axis=1)
    spec_ok = ~np.isnan(z_full)
    rows = pais_ok & spec_ok
    P = int(rows.sum())
    if P < X.shape[1] + 1:
        halt(f"{spec_id}: only {P} rows usable (PAIS-complete AND column non-NaN) — "
             f"too few to project onto a rank-{R} subspace of {X.shape[1]} columns")

    Xr = X[rows]
    Zr = re.standardize_columns(Xr)
    zr_s = _standardize_vec(z_full[rows])
    if float(zr_s @ zr_s) <= 0:
        halt(f"{spec_id}: projected column is degenerate (zero variance) on the usable rows")

    U_ref, r = _leading_subspace(Zr, R)
    recovery = projection_fraction(U_ref, zr_s)
    null_expectation = r / P

    heldout = heldout_pais_projection(Zr, R)
    insample = {cols[j]: round(projection_fraction(U_ref, Zr[:, j]), 4)
                for j in range(Zr.shape[1])}  # context: PAIS cols on their own subspace

    null_mult = rec_cfg.get("null_multiple", 3.0)
    generic_frac = rec_cfg.get("generic_manifold_frac", 0.70)
    above_random = bool(recovery > null_mult * null_expectation)
    mean_heldout = heldout.get("mean")
    recovers_like_pais = bool(
        above_random and mean_heldout is not None and recovery >= generic_frac * mean_heldout)
    if not above_random:
        verdict = "not_recovered_infection_specific_consistent"
    elif recovers_like_pais:
        verdict = "recovered_like_pais_generic_manifold_consistent"
    else:
        verdict = "partially_recovered_indeterminate"

    return {
        "contrast": spec_id,
        "n_gene_sets_total": int(X.shape[0]),
        "n_rows_used": P,
        "reference_subspace_rank_r": int(r),
        "subspace_recovery_fraction": round(recovery, 4),
        "random_direction_null_expectation": round(null_expectation, 5),
        "recovery_vs_null_ratio": round(recovery / null_expectation, 3) if null_expectation else None,
        "heldout_pais_projection": heldout,
        "recovery_vs_mean_heldout_ratio": (round(recovery / mean_heldout, 3)
                                           if mean_heldout else None),
        "insample_pais_projection_context": insample,
        "above_random": above_random,
        "recovers_like_heldout_pais": recovers_like_pais,
        "verdict": verdict,
        "verdict_reading": {
            "not_recovered_infection_specific_consistent":
                "the non-infectious column does NOT recover the PAIS subspace beyond a random "
                "direction — consistent with an infection-specific axis (but see caveats: the "
                "PAIS subspace is weakly identified, so this is not a strong positive claim).",
            "recovered_like_pais_generic_manifold_consistent":
                "the non-infectious column recovers the PAIS subspace about as well as a genuine "
                "HELD-OUT PAIS trigger — consistent with a GENERIC sickness/fatigue manifold "
                "rather than an infection-specific attractor (the t116 Q-D ceiling).",
            "partially_recovered_indeterminate":
                "recovery is above random but below the held-out-PAIS ceiling — indeterminate; "
                "neither cleanly infection-specific nor a full generic-manifold recovery.",
        }[verdict],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", type=Path, required=True)
    ap.add_argument("--pais-matrix", type=Path, required=True)
    ap.add_argument("--pais-grouping", type=Path, required=True)
    ap.add_argument("--pais-rank", type=Path, required=True)
    ap.add_argument("--spec-nes", nargs="*", default=[],
                    help="buildable non-infectious specificity NES paths (build_now columns)")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    cfg = yaml.safe_load(args.config.read_text())
    spec_cfg = cfg["specificity_readacross"]
    if not spec_cfg.get("enabled"):
        halt("specificity_readacross.enabled is false but the rule ran — flip it or gate the rule")
    rec_cfg = spec_cfg.get("recovery", {})

    grouping = json.loads(args.pais_grouping.read_text())
    full_rank = json.loads(args.pais_rank.read_text())
    R = full_rank.get("R_primary") or 1
    X, cols, gene_sets = rb.load_matrix(args.pais_matrix, grouping)
    global _GENE_SETS
    _GENE_SETS = gene_sets  # read_nes aligns each extra column to this pinned index

    # map provided (buildable) NES paths back to their contrast id by basename
    provided = {Path(p).name.rsplit(".nes.tsv", 1)[0]: p for p in args.spec_nes}
    build_now = list(spec_cfg.get("build_now", []))
    missing = [c for c in build_now if c not in provided]
    if missing:
        halt(f"build_now columns have no NES producer wired: {missing} "
             f"(provided: {sorted(provided)})")

    columns = {c: specificity_for(c, provided[c], X, R, cols, rec_cfg) for c in build_now}

    # verdict rollup over the built columns (only the flagship this pass)
    verdicts = {c: v["verdict"] for c, v in columns.items()}
    candidates = spec_cfg.get("candidates", [])
    queued = [c for c in candidates if c.get("build") != "now"]

    out = {
        "finding": "WP4b non-infectious specificity read-across (plan:0010 review Finding D; "
                   "t116 Q-D infection-specific-attractor vs generic-sickness-manifold test)",
        "status": spec_cfg.get("status_label", "exploratory_flagship"),
        "pais_reference_subspace": {
            "matrix": spec_cfg.get("reference_matrix"),
            "R_primary": R,
            "n_pais_columns": len(cols),
            "pais_columns": cols,
            "weak_identification_caveat": (
                "The PAIS subspace projected onto is WEAKLY IDENTIFIED: Stage-3c calibration "
                "FAILED (no t116-grid license), R is LOO-fragile, and the structural co-primary "
                "shows a heterogeneous (finite-repertoire-like), NOT single-attractor, signature. "
                "Recovery is therefore read RELATIVE to the (also weak) held-out-PAIS baseline, "
                "never as an absolute specificity claim."),
        },
        "specificity_columns": columns,
        "verdicts": verdicts,
        "candidate_panel": candidates,
        "queued_replication": queued,
        "sorted_stratum_note": spec_cfg.get("sorted_stratum_note"),
        "pacvs_gap": spec_cfg.get("pacvs_gap"),
        "reverse_projection": spec_cfg.get("reverse_projection"),
        "caveats": [
            "exploratory_flagship: ONE non-infectious column (fibromyalgia, GSE221921) built; the "
            "rest of the admissible panel is queued replication (see queued_replication).",
            "The PAIS reference subspace is weakly identified (Stage-3c FAIL) — see "
            "pais_reference_subspace.weak_identification_caveat.",
            "NES pooled only at the gene-set level over the same pinned Hallmark∪Reactome universe; "
            "expression never merged. The non-infectious deposit passed the SAME admissibility gates "
            "as the primary corpus (blood-bulk WB/PBMC, public, downloadable, sample-level case-vs-control).",
        ],
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, indent=2))
    line = " ".join(f"{c}={columns[c]['subspace_recovery_fraction']}"
                    f"(null={columns[c]['random_direction_null_expectation']},"
                    f"heldout_mean={columns[c]['heldout_pais_projection'].get('mean')},"
                    f"{verdicts[c]})" for c in build_now)
    print(f"[gws_fm_specificity] status={out['status']} {line}")


if __name__ == "__main__":
    main()
