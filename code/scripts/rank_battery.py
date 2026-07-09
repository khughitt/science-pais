# science:code
# status: workflow-owned
# task_ids: [t117]
# science:end

#!/usr/bin/env python3
"""rank_battery.py — WP3 effective-rank battery + t116 structural co-primary + LODO/LOCO
(task:t117; plan:0010 Stage 3/3b, review Findings A, B, C).

Consumes one pathway x contrast matrix (WP2) + its grouping metadata and reports:
  {matrix}.rank.json       R + CI from >=3 rotation-invariant estimators (parallel
                           analysis, bi-cross-validation SVD, split-half) + a row-
                           bootstrap CI + the participation-ratio effective dimension.
  {matrix}.structural.json the t116 discriminating statistic (off-diagonal pairwise
                           Spearman concordance SD) — what interpretation:0037 actually
                           characterized (Finding B); reported as a CO-PRIMARY, and
                           consumed by calibration_3c to match the synthetic concordance.
  {matrix}.stability.json  leave-one-dataset-out (LODO) + leave-one-condition-out
                           (LOCO) folds with PRE-LOCKED pass/fail (Stage 3b), the
                           long-COVID-out fold reported first-class as a power/CI curve
                           (Finding A), and compartment-stratified R (Finding C).

Identifiability is t116-grounded (Finding A): a fold is NON-IDENTIFIABLE iff it retains
< min_triggers (3) distinct triggers — the K>=3 structural-axis floor. Contrast and
platform counts are POWER covariates attached to each fold's CI, NOT binary gates. A
non-identifiable fold is reported explicitly (never silently dropped) and excluded from
pass/fail.

All estimators come from rank_estimators.py — the SAME module calibration_3c.py uses,
so the calibrated procedure and the applied procedure are one code path (Finding B).
All knobs originate in config.yaml; this script hard-codes no design value.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

import rank_estimators as re


# ----------------------------------------------------------------- IO + helpers
def load_matrix(path: Path, grouping: dict):
    """Load the pathway x contrast matrix as (X, columns, gene_sets) with columns in
    the grouping's declared order (the single source of column identity/metadata)."""
    df = pd.read_csv(path, sep="\t", index_col=0)
    cols = [c["contrast"] for c in grouping["columns"]]
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise SystemExit(f"[rank_battery] grouping columns absent from matrix: {missing}")
    df = df[cols]
    return df.to_numpy(dtype=float), cols, df.index.to_numpy()


def regime_of(R: int, bands: dict) -> str:
    for name, (lo, hi) in bands.items():
        if lo <= R <= hi:
            return name
    return "below_low" if R < min(b[0] for b in bands.values()) else "unclassified"


def estimate_rank(X_cols: np.ndarray, cfg: dict, seeds: dict, *, with_ci: bool,
                  struct_cols: np.ndarray | None = None):
    """Full rotation-invariant battery on a column-subset matrix X_cols (P x K').
    Returns the per-estimator Rs, a consensus R (median), the structural SD, the
    leading left-singular subspace (P x r, for cross-fold principal angles), and — when
    `with_ci` — a row-bootstrap CI on the parallel-analysis R.

    X_cols is expected to be a COMMON complete-case matrix (rows complete across ALL
    columns of the parent matrix) so that folds computed on column subsets share a row
    set and their left-singular subspaces are comparable. The structural co-primary is
    computed on `struct_cols` (the original NA-carrying columns) under the pairwise-
    complete rule, to use maximal data per pair (matches concordance.py / pre-reg:0002);
    it falls back to X_cols when struct_cols is None."""
    rb = cfg["rank_battery"]
    X_cc, n_dropped, _ = re.complete_case(X_cols)
    P, K = X_cc.shape
    out: dict = {"n_columns": int(X_cols.shape[1]), "n_gene_sets_complete_case": int(P),
                 "n_gene_sets_dropped_na": int(n_dropped)}

    # structural co-primary on the pairwise-complete original columns (maximal data)
    struct = re.spearman_offdiag(struct_cols if struct_cols is not None else X_cols)
    out["structural_offdiag_concordance"] = struct

    if K < 2 or P < 3:
        out.update({"R_parallel_analysis": None, "R_bicv_svd": None,
                    "R_split_half": None, "R_consensus": None,
                    "note": "too few columns/rows for rank estimation"})
        return out, None

    Z = re.standardize_columns(X_cc)

    pa_rng = np.random.default_rng(seeds["parallel_analysis_perm"])
    band = re.pa_null_band(Z, rb["parallel_analysis"]["n_perm"],
                           rb["parallel_analysis"]["quantile"], pa_rng)
    pa = re.parallel_analysis(Z, 0, rb["parallel_analysis"]["quantile"], pa_rng, band=band)

    cv_rng = np.random.default_rng(seeds["cv_svd_fold"])
    cv = re.bicv_svd(Z, rb["cv_svd"]["row_folds"], rb["cv_svd"]["col_folds"], cv_rng)

    sh_rng = np.random.default_rng(seeds["split_half"])
    sh = re.split_half(Z, rb["split_half"]["n_splits"],
                       cfg["folds"]["pass_rule"]["subspace_angle_max_deg"], sh_rng)

    # Parallel analysis is the PRIMARY estimator: it alone carries a permutation null +
    # a row-bootstrap CI and is the estimator Stage-3c calibrates. bicv/split-half are
    # corroborating, but at small K they can be uninformative (bicv error monotone to the
    # feasible ceiling -> no interior optimum; split-half unstable past the leading run) —
    # flagged so an inflated corroborator does not silently drive the consensus. R_primary
    # (PA) drives the regime band + fold pass/fail; R_consensus (median of the three) and
    # the disagreement are reported first-class (plan:0010 Stage 3: divergence is evidence).
    Rs = [pa["R"], cv["R"], sh["R"]]
    consensus = int(np.median(Rs))
    disagreement = int(max(Rs) - min(Rs))
    out.update({
        "R_primary": pa["R"], "R_parallel_analysis": pa["R"], "R_bicv_svd": cv["R"],
        "R_split_half": sh["R"], "R_consensus": consensus,
        "estimator_disagreement_range": disagreement,
        "bicv_informative": cv["informative"],
        "participation_ratio": round(re.participation_ratio(Z), 3),
        "parallel_analysis_detail": pa,
        "bicv_detail": {"R": cv["R"], "informative": cv["informative"],
                        "feasible_max_rank": cv["feasible_max_rank"],
                        "error_curve": cv["error_curve"]},
        "split_half_angle_curve": sh["mean_max_principal_angle_deg"],
    })

    if with_ci:
        bt_rng = np.random.default_rng(seeds["bootstrap"])
        out["parallel_analysis_bootstrap_ci"] = re.bootstrap_pa_rank(
            Z, rb["bootstrap"]["n_boot"], rb["parallel_analysis"]["quantile"], band, bt_rng)

    # leading left-singular subspace (P x R_primary) for cross-fold principal angles
    r = max(1, pa["R"])
    U = np.linalg.svd(Z, full_matrices=False)[0][:, :r]
    return out, U


def fold_metadata(columns_meta: list[dict]):
    triggers = sorted({c["trigger"] for c in columns_meta})
    platforms = sorted({c["platform"] for c in columns_meta})
    compartments = sorted({c["compartment"] for c in columns_meta})
    n_units = [int(c.get("n_case_units") or 0) + int(c.get("n_control_units") or 0)
               for c in columns_meta]
    return {"n_columns": len(columns_meta), "n_triggers": len(triggers),
            "triggers": triggers, "n_platforms": len(platforms), "platforms": platforms,
            "compartments": compartments, "min_column_N": (min(n_units) if n_units else None),
            "median_column_N": (int(np.median(n_units)) if n_units else None)}


def score_fold(Xc, Xo, colmeta, keep_idx, cfg, seeds, full):
    """Score one LODO/LOCO/LC-out fold against the pre-locked pass/fail rule (Stage 3b).
    Xc = common complete-case matrix (shared rows -> comparable subspaces); Xo = the
    original NA-carrying matrix (pairwise-complete structural). Identifiability = K>=3
    triggers (Finding A); below that the fold is reported non-identifiable and excluded
    from pass/fail. PASS iff |R_fold - R_full|<=r_band AND same regime band AND leading-
    subspace principal angle (full vs fold, in pathway space) <= subspace_angle_max_deg."""
    sub = [colmeta[i] for i in keep_idx]
    meta = fold_metadata(sub)
    pr = cfg["folds"]["pass_rule"]
    bands = {k: tuple(v) for k, v in pr["regime_bands"].items()}
    min_trig = cfg["folds"]["identifiability"]["min_triggers"]

    res, U_fold = estimate_rank(Xc[:, keep_idx], cfg, seeds, with_ci=False,
                                struct_cols=Xo[:, keep_idx])
    row = {"dropped": None, **meta,
           "R_primary": res.get("R_primary"),
           "R_consensus": res.get("R_consensus"),
           "R_parallel_analysis": res.get("R_parallel_analysis"),
           "structural_offdiag_sd": res["structural_offdiag_concordance"]["sd"],
           "power_covariates": {"n_contrasts": meta["n_columns"],
                                "n_platforms": meta["n_platforms"],
                                "min_column_N": meta["min_column_N"]}}

    if meta["n_triggers"] < min_trig:
        row.update({"identifiable": False, "verdict": "non_identifiable",
                    "reason": f"retains {meta['n_triggers']} < {min_trig} triggers (t116 K>=3 floor)"})
        return row

    R_full, R_fold = full["R_primary"], res["R_primary"]
    if R_full is None or R_fold is None:
        row.update({"identifiable": True, "verdict": "unscored",
                    "reason": "primary R undefined on full or fold"})
        return row
    dR = abs(R_fold - R_full)
    same_band = regime_of(R_fold, bands) == regime_of(R_full, bands)
    r = max(1, min(R_full, R_fold))
    ang = float(np.degrees(re.subspace_angles(full["U"][:, :r], U_fold[:, :r])).max())
    passed = (dR <= pr["r_band"]) and same_band and (ang <= pr["subspace_angle_max_deg"])
    row.update({"identifiable": True, "R_full": R_full, "delta_R": dR,
                "same_regime_band": same_band,
                "leading_subspace_angle_deg": round(ang, 3),
                "verdict": "PASS" if passed else "FAIL"})
    return row


def lc_out_power_curve(Xc, colmeta, cfg, seeds):
    """The contrast-count power/CI curve (Finding A): as the number of retained
    contrast columns K' grows, how does the parallel-analysis R and its subset spread
    behave? For each K' we draw random column subsets (that retain >=3 triggers when
    achievable) and report the R distribution + the fraction identifiable — a power/CI
    curve rather than a single binary LC-out verdict. This is the on-data face of the
    plan's low-power ceiling. Runs on the common complete-case matrix Xc."""
    Xcc, _, _ = re.complete_case(Xc)
    _, K = Xc.shape
    rng = np.random.default_rng(seeds["bootstrap"] + 7)
    pa = cfg["rank_battery"]["parallel_analysis"]
    min_trig = cfg["folds"]["identifiability"]["min_triggers"]
    n_sub = cfg["rank_battery"].get("power_curve_subsets", 200)
    # Each column subset has its OWN marginal distributions, so its per-column-permuted
    # PA null band differs — recompute the band PER SUBSET (not once per K') so a subset's
    # R is scored against its own null (review Finding 2). Uses a reduced permutation count
    # for tractability; this is a coarse power/CI curve, not the headline R.
    pc_perm = cfg["rank_battery"].get("power_curve_n_perm", 300)
    curve = []
    for Kp in range(3, K + 1):
        Rs, ident = [], 0
        for _ in range(n_sub):
            idx = rng.choice(K, size=Kp, replace=False)
            n_tr = len({colmeta[i]["trigger"] for i in idx})
            Zsub = re.standardize_columns(Xcc[:, idx])
            band = re.pa_null_band(Zsub, pc_perm, pa["quantile"], rng)
            R = re.parallel_analysis(Zsub, 0, pa["quantile"], rng, band=band)["R"]
            Rs.append(R)
            if n_tr >= min_trig:
                ident += 1
        Rs = np.array(Rs, dtype=float)
        curve.append({
            "n_contrasts": Kp,
            "R_median": (float(np.median(Rs)) if Rs.size else None),
            "R_ci_lo": (float(np.quantile(Rs, 0.05)) if Rs.size else None),
            "R_ci_hi": (float(np.quantile(Rs, 0.95)) if Rs.size else None),
            "ci_width": (float(np.quantile(Rs, 0.95) - np.quantile(Rs, 0.05)) if Rs.size else None),
            "frac_subsets_identifiable": round(ident / n_sub, 3),
            "n_subsets": n_sub,
        })
    return curve


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", type=Path, required=True)
    ap.add_argument("--matrix", required=True, help="matrix name (strict|sensitivity)")
    ap.add_argument("--in-matrix", type=Path, required=True)
    ap.add_argument("--in-grouping", type=Path, required=True)
    ap.add_argument("--out-rank", type=Path, required=True)
    ap.add_argument("--out-structural", type=Path, required=True)
    ap.add_argument("--out-stability", type=Path, required=True)
    args = ap.parse_args()

    cfg = yaml.safe_load(args.config.read_text())
    seeds = cfg["determinism"]["seeds"]
    grouping = json.loads(args.in_grouping.read_text())
    colmeta = grouping["columns"]
    X, cols, _ = load_matrix(args.in_matrix, grouping)

    # common complete-case rows (complete across ALL columns) — the shared feature set
    # for the rank estimators + subspaces so every fold is comparable. The structural
    # co-primary instead uses the pairwise-complete original X (maximal data per pair).
    Xc, n_common_dropped, _ = re.complete_case(X)

    # ---- full-corpus estimate (with CI) ----
    full, U_full = estimate_rank(Xc, cfg, seeds, with_ci=True, struct_cols=X)
    full["n_gene_sets_total"] = int(X.shape[0])
    full["n_gene_sets_dropped_na_common"] = int(n_common_dropped)
    full_meta = fold_metadata(colmeta)
    bands = {k: tuple(v) for k, v in cfg["folds"]["pass_rule"]["regime_bands"].items()}
    full["regime_band"] = (regime_of(full["R_primary"], bands)
                           if full.get("R_primary") is not None else None)
    full["corpus"] = full_meta
    full["per_column"] = [
        {"contrast": c["contrast"], "trigger": c["trigger"], "compartment": c["compartment"],
         "platform": c["platform"], "n_sig_adj_p05": c.get("n_sig_adj_p05"),
         "n_case_units": c.get("n_case_units"), "n_control_units": c.get("n_control_units")}
        for c in colmeta]
    args.out_rank.parent.mkdir(parents=True, exist_ok=True)
    args.out_rank.write_text(json.dumps({"matrix": args.matrix, **full}, indent=2))

    # ---- structural co-primary ----
    struct = dict(full["structural_offdiag_concordance"])
    struct.update({"matrix": args.matrix, "K": full_meta["n_columns"],
                   "n_triggers": full_meta["n_triggers"],
                   "statistic": cfg["structural_statistic"]["name"],
                   "sampling_floor_1_over_sqrt_P_minus_1": round(
                       1.0 / np.sqrt(max(full["n_gene_sets_complete_case"] - 1, 1)), 4),
                   "note": ("t116 discriminating statistic (interpretation:0037): a LOW off-diagonal "
                            "SD with HIGH mean concordance is the single-shared-axis / shared-artifact "
                            "signature; undefined for K<=2.")})
    args.out_structural.write_text(json.dumps(struct, indent=2))

    # ---- LODO / LOCO / LC-out / power curve / compartment-stratified ----
    full_for_fold = {"R_primary": full["R_primary"], "U": U_full}
    K = len(cols)

    lodo = [score_fold(Xc, X, colmeta, [j for j in range(K) if j != i], cfg, seeds, full_for_fold)
            | {"dropped": cols[i]} for i in range(K)]

    triggers = sorted({c["trigger"] for c in colmeta})
    loco = []
    for t in triggers:
        keep = [j for j in range(K) if colmeta[j]["trigger"] != t]
        if keep:
            loco.append(score_fold(Xc, X, colmeta, keep, cfg, seeds, full_for_fold)
                        | {"dropped": f"trigger:{t}"})

    # long-COVID-out: first-class (LC = sars-cov-2). Reported even when non-identifiable.
    lc_keep = [j for j in range(K) if colmeta[j]["trigger"] != "sars-cov-2"]
    lc_out = (score_fold(Xc, X, colmeta, lc_keep, cfg, seeds, full_for_fold)
              | {"dropped": "trigger:sars-cov-2 (long-COVID-out, first-class)"}) if lc_keep else \
             {"dropped": "trigger:sars-cov-2", "verdict": "no_columns_remain"}

    # compartment-stratified R (Finding C): R within each compartment stratum
    compart = {}
    for comp in sorted({c["compartment"] for c in colmeta}):
        idx = [j for j in range(K) if colmeta[j]["compartment"] == comp]
        res, _ = estimate_rank(Xc[:, idx], cfg, seeds, with_ci=False, struct_cols=X[:, idx])
        compart[comp] = {"n_columns": len(idx),
                         "n_triggers": len({colmeta[j]["trigger"] for j in idx}),
                         "R_primary": res.get("R_primary"),
                         "R_consensus": res.get("R_consensus"),
                         "structural_offdiag_sd": res["structural_offdiag_concordance"]["sd"]}

    stability = {
        "matrix": args.matrix,
        "identifiability_rule": {"min_triggers": cfg["folds"]["identifiability"]["min_triggers"],
                                 "grounding": "t116 K>=3 (Finding A); contrast/platform counts are power covariates, not gates"},
        "pass_rule": cfg["folds"]["pass_rule"],
        "full_corpus": {"R_primary": full["R_primary"], "R_consensus": full["R_consensus"],
                        "regime_band": full["regime_band"], **full_meta},
        "lodo": lodo,
        "loco": loco,
        "lc_out_first_class": lc_out,
        "lc_out_power_curve": lc_out_power_curve(Xc, colmeta, cfg, seeds),
        "compartment_stratified": compart,
    }
    args.out_stability.write_text(json.dumps(stability, indent=2))

    print(f"[rank_battery:{args.matrix}] R_primary(PA)={full['R_primary']} "
          f"(bicv={full['R_bicv_svd']}[info={full['bicv_informative']}] sh={full['R_split_half']} "
          f"consensus={full['R_consensus']}) regime={full['regime_band']} "
          f"offdiag_sd={round(struct['sd'],4) if struct['sd'] is not None else None}")
    lc = lc_out.get("verdict")
    print(f"[rank_battery:{args.matrix}] LC-out: {lc} "
          f"({lc_out.get('reason', lc_out.get('n_triggers', '?'))} triggers)")


if __name__ == "__main__":
    main()
