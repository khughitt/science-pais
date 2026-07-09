# science:code
# status: workflow-owned
# task_ids: [t117]
# science:end

#!/usr/bin/env python3
"""grid_placement.py — WP6 t116 R-regime-grid placement (fail-closed).

Mechanizes the pre-locked WP6 gate (plan:0010 Key decision 6 + review Finding B/3):
a descriptive rank R is placed on the t116 R-regime grid ONLY when BOTH
  (1) the Stage-3c calibration passed (`calibration.pass: pass==true` — the SVD-rank
      -> t116-grid substitution is licensed at this corpus width/operating point), AND
  (2) the artifact/compartment adjudication passed (`artifact_controls_pass==true` —
      the R is a clean adjudicated estimate, not a limited/non-arbitrating one).
Either gate false => NO grid verdict is emitted; the rule still writes an explicit
fail-closed record (never a silent skip, never a fabricated band).

Fail-early: a missing/malformed input HALTs. The band classification uses the config
`grid` bands verbatim; this script hard-codes no threshold."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml


def halt(msg: str):
    raise SystemExit(f"[grid_placement] HALT: {msg}")


def classify(R: int, grid: dict) -> str:
    lo = grid["low_rank_arbitrable"]
    hi = grid["high_rank_nonarbitrating"]
    if lo[0] <= R <= lo[1]:
        return "low_rank_arbitrable"
    if hi[0] <= R <= hi[1]:
        return "high_rank_nonarbitrating"
    return "straddle"  # between the bands; reported, not arbitrated (grid.straddle_reported)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--matrix", required=True)
    ap.add_argument("--config", type=Path, required=True)
    ap.add_argument("--calibration", type=Path, required=True)   # calibration.pass (JSON verdict)
    ap.add_argument("--adjudicated", type=Path, required=True)   # artifact/{matrix}.adjudicated.json
    ap.add_argument("--rank", type=Path, required=True)          # rank/{matrix}.rank.json
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    grid = yaml.safe_load(args.config.read_text())["grid"]
    cal = json.loads(args.calibration.read_text())
    adj = json.loads(args.adjudicated.read_text())["summary"]
    rank = json.loads(args.rank.read_text())

    cal_pass = bool(cal.get("pass"))
    acp = bool(adj.get("artifact_controls_pass"))
    R = rank.get("R_primary")
    offdiag = rank.get("structural_offdiag_concordance", {})

    placed = bool(cal_pass and acp)
    if not cal_pass:
        status = "fail_closed_no_verdict"
        band = None
        consequence = (
            "Stage-3c calibration FAILED (the corpus does not identify a rank at its operating point "
            "and/or the SVD-rank->grid substitution is not licensed at this width) — no R is placed on "
            "the t116 grid. q0050: the low-power ceiling is DEMONSTRATED from real data; the public "
            "single-trigger route cannot settle the R regime — a K>=3 harmonized cohort is required.")
    elif not acp:
        status = "limited_or_nonarbitrating"
        band = None
        consequence = (
            "Calibration passed but the artifact/compartment adjudication did NOT "
            "(artifact_controls_pass=false) — R is limited/non-arbitrating and is not read as a clean "
            "adjudicated estimate; no grid band is asserted.")
    else:
        status = "placed"
        band = classify(int(R), grid)
        consequence = (
            f"R={R} placed on the t116 grid in band '{band}'; the q0050 GO/NO-GO consequence follows "
            f"the band (low_rank_arbitrable => the harmonized design can arbitrate at achievable arm "
            f"counts; high_rank_nonarbitrating => it cannot).")

    out = {
        "finding": "WP6 t116 R-regime-grid placement (plan:0010 Key decision 6; fail-closed on the "
                   "pre-locked calibration + artifact-control gates)",
        "matrix": args.matrix,
        "placed_on_grid": placed,
        "status": status,
        "grid_band": band,
        "grid_bands_config": grid,
        "gates": {
            "calibration_pass": cal_pass,
            "artifact_controls_pass": acp,
            "interpretation_status": adj.get("interpretation_status"),
        },
        "descriptive_rank": {
            "R_primary": R,
            "R_point_estimate_basis": adj.get("R_point_estimate_basis"),
            "regime_band_descriptive": adj.get("regime_band"),
            "R_parallel_analysis": rank.get("R_parallel_analysis"),
            "R_bicv_svd": rank.get("R_bicv_svd"),
            "R_split_half": rank.get("R_split_half"),
            "R_consensus": rank.get("R_consensus"),
            "estimator_disagreement_range": rank.get("estimator_disagreement_range"),
            "note": "DESCRIPTIVE geometry only — NOT placed on the grid unless status=='placed'.",
        },
        "structural_co_primary": {
            "offdiag_concordance_mean": offdiag.get("mean"),
            "offdiag_concordance_sd": offdiag.get("sd"),
            "n_pairs": offdiag.get("n_pairs"),
        },
        "calibration_reasons": cal.get("reasons", []),
        "q0050_consequence": consequence,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, indent=2))
    print(f"[grid_placement] matrix={args.matrix} status={status} placed_on_grid={placed} "
          f"band={band} R={R} (cal_pass={cal_pass}, artifact_controls_pass={acp})")


if __name__ == "__main__":
    main()
