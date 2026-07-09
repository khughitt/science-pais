# science:code
# status: workflow-owned
# task_ids: [t117]
# science:end

#!/usr/bin/env python3
"""artifact_adjudication.py — WP4 artifact + compartment adjudication
(task:t117; plan:0010 Stage 5 artifact battery + review Finding C).

Runs the artifact-control + compartment/composition battery BEFORE any biological
reading of R (plan:0010 Key decision 4). Two named rivals for a low-rank shared
signal: a correlated shared ARTIFACT (t116) and a cell-COMPOSITION-shift axis
across mixed blood compartments. Consumes the WP3 rank/structural outputs + the
assembled matrix (+ the sorted-compartment stratum NES, strict only) and writes:

  {matrix}.compartment_stratified.json  Finding C: R within each compartment
                                        stratum (deconvolution-free composition
                                        control), the drop-sorted sensitivity
                                        (does pooling the sorted stratum change the
                                        subspace?), and the composition-adjustment
                                        (deconvolution) prong — recorded note-only
                                        with its exact blocker where a gated tool /
                                        per-sample re-DE is required.
  {matrix}.adjudicated.json             platform-LOO, recovered-control specificity
                                        (directional subspace persistence), the
                                        negative-control-set floor (note-only where
                                        the pinned universe carries no control rows),
                                        the artifact floor already subtracted by the
                                        parallel-analysis null, an omitted-decoy
                                        ledger, and the artifact-adjudicated R the
                                        WP6 grid placement reads.

Reuses the WP3 battery verbatim (composition, not re-implementation): the SAME
rank_estimators primitives and rank_battery.estimate_rank / regime_of / load_matrix,
so any within-stratum or pooled R is the identical procedure the headline R used.
All knobs originate in config.yaml; this script hard-codes no design value. Fail-
early: a requested extra NES that is present but malformed HALTs; an unavailable
prong is recorded explicitly (never a silent skip or fabricated adjustment).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

import rank_estimators as re
import rank_battery as rb


def halt(msg: str):
    raise SystemExit(f"[artifact_adjudication] HALT: {msg}")


# control_type -> reference class for recovered-control specificity. "recovered"
# controls carry infection history + non-recovery differences; "naive" controls do
# not. The test is whether the shared subspace PERSISTS in case-vs-recovered, i.e.
# is not fully explained by the case-vs-healthy (infection-history) axis.
RECOVERED_LIKE = {"infected-recovered", "infected-nonPASC-convalescent",
                  "post-covid-recovered", "recovered"}
NAIVE_LIKE = {"healthy", "baseline"}


def read_nes(path: Path, contrast: str, ref_index) -> np.ndarray:
    """Load one fgsea NES column and align it to the matrix's gene-set index (same
    pinned universe). Mirrors assemble_matrix.read_nes so the extra columns are
    commensurable with the rank matrix. NaN where a set is untestable in the column."""
    if not path.exists():
        halt(f"{contrast}: extra NES table absent: {path}")
    df = pd.read_csv(path, sep="\t", na_values=["", "NA"], keep_default_na=False)
    for col in ("gene_set", "NES"):
        if col not in df.columns:
            halt(f"{contrast}: NES table missing column '{col}' ({path})")
    if df["gene_set"].duplicated().any():
        halt(f"{contrast}: duplicate gene_set rows in {path}")
    s = pd.Series(df["NES"].to_numpy(dtype=float), index=df["gene_set"].astype(str))
    return s.reindex(ref_index).to_numpy(dtype=float)


def stratum_R(Xc_cols, cfg, seeds, Xo_cols):
    """R within a column subset via the SAME battery the headline R used."""
    return rb.estimate_rank(Xc_cols, cfg, seeds, with_ci=False, struct_cols=Xo_cols)


def projection_fraction(U_ref: np.ndarray, z: np.ndarray) -> float:
    """Fraction of a (standardized) contrast column's variance captured by the
    leading shared subspace U_ref (P x r, orthonormal columns). = ||U_refᵀ z||² /
    ||z||². The random-direction expectation is r/P, so a value >> r/P means the
    column loads on the shared axis (directional persistence, not magnitude)."""
    denom = float(z @ z)
    if denom <= 0:
        return float("nan")
    proj = U_ref.T @ z
    return float((proj @ proj) / denom)


def compartment_adjudication(X, Xc, cols, colmeta, gene_sets, cfg, seeds,
                             matrix, full_rank, extra_nes, extra_declared):
    """Finding C three prongs: (i) compartment-stratified R, (ii) drop-sorted
    sensitivity, (iii) composition adjustment (deconvolution) note."""
    comp_cfg = cfg["artifact_controls"]["composition_control"]
    deconvolvable = set(cfg["compartments"]["deconvolvable"])
    bands = {k: tuple(v) for k, v in cfg["folds"]["pass_rule"]["regime_bands"].items()}
    K = len(cols)

    # ---- prong (i): compartment-stratified R (deconvolution-free composition control)
    stratified = {}
    for comp in sorted({c["compartment"] for c in colmeta}):
        idx = [j for j in range(K) if colmeta[j]["compartment"] == comp]
        res, _ = stratum_R(Xc[:, idx], cfg, seeds, X[:, idx])
        stratified[comp] = {
            "n_columns": len(idx),
            "n_triggers": len({colmeta[j]["trigger"] for j in idx}),
            "contrasts": [cols[j] for j in idx],
            "R_primary": res.get("R_primary"),
            "R_consensus": res.get("R_consensus"),
            "regime_band": (rb.regime_of(res["R_primary"], bands)
                            if res.get("R_primary") is not None else None),
            "structural_offdiag_sd": res["structural_offdiag_concordance"]["sd"],
            "deconvolvable": comp in deconvolvable,
        }
    # does R agree across compartments? disagreement => the shared axis is not
    # compartment-invariant (a composition-shift rival is live).
    comp_Rs = [v["R_primary"] for v in stratified.values() if v["R_primary"] is not None]
    r_agree = (len(set(comp_Rs)) <= 1) if comp_Rs else None

    # ---- prong (ii): drop-sorted sensitivity (strict only — the sorted stratum) ----
    # The primary matrix is ALREADY WB/PBMC-only (G1), so the primary R IS the
    # drop-sorted R. The sensitivity asks the mirror question: does POOLING the sorted
    # stratum change the rank / rotate the shared subspace? If it does, that is the
    # on-data justification for holding sorted out (a composition axis injected by a
    # different compartment, not pathway biology).
    drop_sorted = {"applicable": False,
                   "note": "no sorted-compartment stratum declared for this matrix"}
    if extra_declared["stratum"]:
        provided = {c: p for c, p in extra_nes.items()
                    if c in extra_declared["stratum"]}
        omitted = [c for c in extra_declared["stratum"] if c not in provided]
        if not provided:
            drop_sorted = {"applicable": False,
                           "note": "sorted stratum declared but no NES built",
                           "omitted_stratum": omitted}
        else:
            strat_cols = np.column_stack([read_nes(Path(p), c, gene_sets)
                                          for c, p in provided.items()])
            Xpool = np.column_stack([X, strat_cols])
            Xpool_cc, _, _ = re.complete_case(Xpool)
            res_pool, U_pool = rb.estimate_rank(Xpool_cc, cfg, seeds, with_ci=False,
                                                struct_cols=Xpool)
            # leading-subspace principal angle: primary (drop-sorted) vs pooled, on
            # the pooled common complete-case rows so the subspaces are comparable.
            _, U_primary = rb.estimate_rank(Xpool_cc[:, :K], cfg, seeds, with_ci=False,
                                            struct_cols=Xpool[:, :K])
            R_primary = full_rank.get("R_primary")
            R_pool = res_pool.get("R_primary")
            ang = None
            if U_primary is not None and U_pool is not None:
                r = max(1, min(x for x in (R_primary, R_pool) if x) or 1)
                r = min(r, U_primary.shape[1], U_pool.shape[1])
                ang = float(np.degrees(
                    re.subspace_angles(U_primary[:, :r], U_pool[:, :r])).max())
            drop_sorted = {
                "applicable": True,
                "stratum_columns": list(provided.keys()),
                "R_drop_sorted_primary": R_primary,
                "R_pool_sorted": R_pool,
                "delta_R_from_pooling": (abs(R_pool - R_primary)
                                         if (R_pool is not None and R_primary is not None)
                                         else None),
                "leading_subspace_angle_deg": (round(ang, 3) if ang is not None else None),
                "subspace_angle_cutoff_deg": cfg["folds"]["pass_rule"]["subspace_angle_max_deg"],
                "pooling_perturbs_subspace": (
                    None if ang is None else
                    bool(ang > cfg["folds"]["pass_rule"]["subspace_angle_max_deg"])),
                "note": ("primary matrix is WB/PBMC-only (G1) so R_drop_sorted == "
                         "primary R; pooling the sorted stratum is the sensitivity — a "
                         "changed R or rotated subspace justifies holding sorted out."),
                "omitted_stratum": omitted,
            }

    # ---- prong (iii): composition adjustment (deconvolution) — note-only blocker ----
    composition_adjustment = {
        "requested": bool(comp_cfg.get("deconvolution", {}).get("report_before_after")),
        "method": comp_cfg.get("deconvolution", {}).get("method"),
        "status": "deferred_note_only",
        "blocker": ("per-sample deconvolution (CIBERSORTx-LM22) requires a gated "
                    "signature tool + the per-sample expression, then a re-DE per "
                    "deposit; the pooled pathway×contrast NES matrix cannot be "
                    "composition-adjusted post-hoc. Deferred (gated-tool discipline; "
                    "avoid-gated-datasets). The deconvolution-free composition control "
                    "IS prong (i): compartment-stratified R already shows whether the "
                    "shared axis is compartment-invariant."),
        "deconvolution_free_control": "compartment_stratified_R (prong i)",
        "compartment_R_agrees": r_agree,
    }

    return {
        "matrix": matrix,
        "finding": "C (compartment/composition control)",
        "compartment_stratified_R": stratified,
        "compartment_R_agrees": r_agree,
        "R_compartment_invariant_note": (
            "R agrees across compartments" if r_agree else
            "R DIFFERS across compartments -> shared axis is compartment-entangled "
            "(a cell-composition-shift rival is live; the pooled R is not a single "
            "compartment-invariant biology rank)"),
        "drop_sorted_sensitivity": drop_sorted,
        "composition_adjustment": composition_adjustment,
    }


def platform_loo(X, Xc, cols, colmeta, cfg, seeds, full_rank):
    """Re-estimate R dropping each platform in turn. A rank that collapses when a
    platform is removed is a platform axis, not biology. A single-platform corpus
    CANNOT test platform-confounding — recorded as a limitation, not a pass."""
    bands = {k: tuple(v) for k, v in cfg["folds"]["pass_rule"]["regime_bands"].items()}
    platforms = sorted({c["platform"] for c in colmeta})
    K = len(cols)
    if len(platforms) < 2:
        return {"applicable": False, "n_platforms": len(platforms),
                "platforms": platforms,
                "note": ("single-platform corpus: platform-LOO cannot test platform-"
                         "confounding, so the low-rank signal CANNOT be shown platform-"
                         "independent here (a limitation carried to the grid verdict)."),
                "R_full": full_rank.get("R_primary")}
    drops = []
    for p in platforms:
        keep = [j for j in range(K) if colmeta[j]["platform"] != p]
        if len(keep) < 2:
            drops.append({"dropped_platform": p, "n_remaining": len(keep),
                          "R": None, "note": "<2 columns remain"})
            continue
        res, _ = rb.estimate_rank(Xc[:, keep], cfg, seeds, with_ci=False,
                                  struct_cols=X[:, keep])
        R = res.get("R_primary")
        drops.append({
            "dropped_platform": p, "n_remaining": len(keep),
            "remaining_contrasts": [cols[j] for j in keep],
            "R": R,
            "regime_band": (rb.regime_of(R, bands) if R is not None else None),
            "n_triggers_remaining": len({colmeta[j]["trigger"] for j in keep}),
        })
    R_full = full_rank.get("R_primary")
    survives = all(d["R"] is not None and abs(d["R"] - R_full) <= cfg["folds"]["pass_rule"]["r_band"]
                   for d in drops if d["R"] is not None) if R_full is not None else None
    return {"applicable": True, "n_platforms": len(platforms), "platforms": platforms,
            "R_full": R_full, "platform_drops": drops,
            "rank_survives_every_platform_drop": survives}


def recovered_control_specificity(Xc, cols, colmeta, cfg, full_rank):
    """Directional (not magnitude) specificity: does the leading shared subspace
    defined by the case-vs-NAIVE (healthy) columns PERSIST in the case-vs-RECOVERED
    columns? Persistence = the recovered columns still project heavily onto the naive
    shared subspace (not fully explained by the infection-history axis). require_exceed
    is FALSE by config: we do not require case-vs-recovered to exceed case-vs-naive."""
    spec_cfg = cfg["artifact_controls"]["recovered_control_specificity"]
    K = len(cols)
    naive_idx = [j for j in range(K) if colmeta[j].get("control_type") in NAIVE_LIKE]
    rec_idx = [j for j in range(K) if colmeta[j].get("control_type") in RECOVERED_LIKE]
    other = [{"contrast": cols[j], "control_type": colmeta[j].get("control_type")}
             for j in range(K) if j not in naive_idx and j not in rec_idx]

    if len(naive_idx) < 2 or len(rec_idx) < 1:
        return {"applicable": False,
                "n_naive_columns": len(naive_idx), "n_recovered_columns": len(rec_idx),
                "note": ("need >=2 case-vs-naive columns to define the reference shared "
                         "subspace and >=1 case-vs-recovered column to test persistence"),
                "unclassified_control_types": other}

    Z = re.standardize_columns(Xc)
    R = full_rank.get("R_primary") or 1
    r = max(1, min(R, len(naive_idx), Z.shape[0]))
    # leading shared subspace of the NAIVE columns (left-singular vectors, P x r)
    U_ref = np.linalg.svd(Z[:, naive_idx], full_matrices=False)[0][:, :r]
    P = Z.shape[0]
    null_expectation = r / P  # random-direction projection fraction

    def frac_for(idx_list):
        return {cols[j]: round(projection_fraction(U_ref, Z[:, j]), 4) for j in idx_list}

    rec_frac = frac_for(rec_idx)
    naive_frac = frac_for(naive_idx)  # in-sample (defines the subspace) — context
    mean_rec = float(np.mean(list(rec_frac.values())))
    mean_naive = float(np.mean(list(naive_frac.values())))
    min_persist = spec_cfg.get("min_persistence_frac", 0.30)
    # persists iff the recovered columns capture a real share of variance in the naive
    # shared subspace (>= min AND >> the random-direction null), i.e. the subspace is
    # present in case-vs-recovered, not an artifact of the healthy-control contrast.
    persists = bool(mean_rec >= min_persist and mean_rec > 3 * null_expectation)
    return {
        "applicable": True,
        "reference_subspace_rank_r": int(r),
        "n_naive_columns": len(naive_idx), "n_recovered_columns": len(rec_idx),
        "naive_reference_contrasts": [cols[j] for j in naive_idx],
        "recovered_projection_fraction": rec_frac,
        "naive_projection_fraction_insample": naive_frac,
        "mean_recovered_projection": round(mean_rec, 4),
        "mean_naive_projection_insample": round(mean_naive, 4),
        "random_direction_null_expectation": round(null_expectation, 5),
        "min_persistence_frac": min_persist,
        "require_persistence": spec_cfg.get("require_persistence"),
        "require_exceed_naive": spec_cfg.get("require_exceed_naive"),
        "shared_subspace_persists_in_case_vs_recovered": persists,
        "unclassified_control_types": other,
        "note": ("directional persistence, not magnitude: a healthy-control contrast "
                 "can legitimately be larger; the test is whether the shared subspace "
                 "remains present in case-vs-recovered."),
    }


def negative_control_floor(full_rank, structural, cfg):
    """The artifact floor. The pinned universe is Hallmark∪Reactome (biology only):
    housekeeping / platform-associated / GC-confounded negative-control gene sets were
    deliberately NOT scored, so the assembled NES matrix carries no control rows to
    subtract set-wise. Record that as the exact blocker, and report the artifact floor
    that IS available and already applied: the parallel-analysis per-column-permuted
    null (which R_primary already subtracts) + the off-diagonal-SD sampling floor."""
    pa = full_rank.get("parallel_analysis_detail", {})
    sv = pa.get("singular_values", [])
    band = pa.get("null_band", [])
    n_above = int(sum(1 for s, b in zip(sv, band) if s > b))
    return {
        "negative_control_sets_requested": cfg["artifact_controls"]["negative_control_sets"],
        "set_based_subtraction": {
            "status": "deferred_note_only",
            "blocker": ("the pinned universe is Hallmark∪Reactome (biological pathways "
                        "only); housekeeping/platform/GC-confounded negative-control sets "
                        "were not scored through fgsea, so there are no control rows in the "
                        "NES matrix to subtract. Implementing this needs a WP2 re-run "
                        "appending declared negative-control sets to the universe."),
        },
        "artifact_floor_applied": {
            "method": "parallel_analysis_per_column_permuted_null",
            "note": ("R_primary is ALREADY artifact-floor-adjusted: only singular values "
                     "exceeding the per-column-permuted null (which destroys cross-contrast "
                     "structure, preserves marginals) are counted as shared directions."),
            "n_singular_values_above_null": n_above,
            "observed_singular_values": sv,
            "null_band": band,
        },
        "structural_sampling_floor": {
            "off_diagonal_sd": structural.get("sd"),
            "sampling_floor_1_over_sqrt_P_minus_1": structural.get(
                "sampling_floor_1_over_sqrt_P_minus_1"),
            "mean_offdiag_concordance": structural.get("mean"),
        },
    }


def omitted_decoys_ledger(cfg, extra_declared, extra_nes):
    """The acute-infection decoy specificity layer: the post-acute subspace should NOT
    be recovered by an acute-only decoy at the same rank. Both decoys are unbuildable
    (GSE68310 parse deferred; CHIKV salmon deferred), so this prong is note-only —
    recorded explicitly with each blocker, never silently dropped."""
    entries = []
    for c in extra_declared["decoy"]:
        blocker = cfg["contrasts"].get(c, {}).get("note", "unbuildable (deferred)")
        entries.append({"contrast": c,
                        "accession": cfg["contrasts"].get(c, {}).get("accession"),
                        "trigger": cfg["contrasts"].get(c, {}).get("trigger"),
                        "built": c in extra_nes, "blocker": blocker})
    any_built = any(e["built"] for e in entries)
    return {
        "status": "available" if any_built else "deferred_note_only",
        "note": ("acute-decoy specificity (post-acute subspace should NOT be recovered "
                 "by an acute-only decoy at the same rank) requires a built decoy NES "
                 "column; none is available — recorded per-decoy with its blocker."),
        "decoys": entries,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", type=Path, required=True)
    ap.add_argument("--matrix", required=True)
    ap.add_argument("--in-matrix", type=Path, required=True)
    ap.add_argument("--in-grouping", type=Path, required=True)
    ap.add_argument("--in-rank", type=Path, required=True)
    ap.add_argument("--in-structural", type=Path, required=True)
    ap.add_argument("--extra-nes", nargs="*", default=[],
                    help="buildable stratum/decoy NES paths (strict only)")
    ap.add_argument("--out-adjudicated", type=Path, required=True)
    ap.add_argument("--out-stratified", type=Path, required=True)
    args = ap.parse_args()

    cfg = yaml.safe_load(args.config.read_text())
    seeds = cfg["determinism"]["seeds"]
    grouping = json.loads(args.in_grouping.read_text())
    colmeta = grouping["columns"]
    full_rank = json.loads(args.in_rank.read_text())
    structural = json.loads(args.in_structural.read_text())

    X, cols, gene_sets = rb.load_matrix(args.in_matrix, grouping)
    Xc, _, _ = re.complete_case(X)

    # declared stratum/decoy columns for THIS matrix's adjudication (strict pulls the
    # sorted stratum + acute decoys; sensitivity pulls none — mirrors the Snakefile).
    def tagged(tag):
        return [c for c in cfg["contrasts"] if cfg["contrasts"][c].get("matrix") == tag]
    extra_declared = ({"stratum": tagged("stratum"), "decoy": tagged("decoy")}
                      if args.matrix == "strict" else {"stratum": [], "decoy": []})
    # map provided (buildable) NES paths back to their contrast by basename
    extra_nes = {}
    for p in args.extra_nes:
        contrast = Path(p).name.rsplit(".nes.tsv", 1)[0]
        extra_nes[contrast] = p

    # ---- compartment adjudication (Finding C) ----
    comp = compartment_adjudication(X, Xc, cols, colmeta, gene_sets, cfg, seeds,
                                    args.matrix, full_rank, extra_nes, extra_declared)
    args.out_stratified.parent.mkdir(parents=True, exist_ok=True)
    args.out_stratified.write_text(json.dumps(comp, indent=2))

    # ---- artifact controls ----
    ploo = platform_loo(X, Xc, cols, colmeta, cfg, seeds, full_rank)
    rec = recovered_control_specificity(Xc, cols, colmeta, cfg, full_rank)
    neg = negative_control_floor(full_rank, structural, cfg)
    decoys = omitted_decoys_ledger(cfg, extra_declared, extra_nes)

    bands = {k: tuple(v) for k, v in cfg["folds"]["pass_rule"]["regime_bands"].items()}
    R_full = full_rank.get("R_primary")
    # the artifact-adjudicated R the grid reads: R_primary is already null-adjusted; no
    # further set-based floor is available (see negative_control_floor). Carry the
    # compartment + platform + recovered verdicts so WP6 can gate honestly.
    adjudicated_R = R_full
    summary = {
        "artifact_adjudicated_R": adjudicated_R,
        "regime_band": (rb.regime_of(adjudicated_R, bands) if adjudicated_R is not None else None),
        "structural_offdiag_sd": structural.get("sd"),
        "survives_platform_loo": ploo.get("rank_survives_every_platform_drop"),
        "platform_loo_applicable": ploo.get("applicable"),
        "compartment_R_agrees": comp["compartment_R_agrees"],
        "shared_subspace_persists_in_case_vs_recovered":
            rec.get("shared_subspace_persists_in_case_vs_recovered"),
        "set_based_negative_control_available": False,
        "acute_decoy_specificity_available": decoys["status"] == "available",
        "verdict_note": (
            "artifact-adjudicated R equals the null-adjusted R_primary; no set-based "
            "negative-control floor or acute-decoy specificity is available (both note-"
            "only with blockers). The compartment control (stratified R) and platform-LOO "
            "are the binding controls here — read the grid verdict against their limits."),
    }
    adjudicated = {
        "matrix": args.matrix,
        "finding": "artifact + compartment adjudication (plan:0010 Stage 5, WP4)",
        "summary": summary,
        "platform_loo": ploo,
        "recovered_control_specificity": rec,
        "negative_control_floor": neg,
        "compartment_control_ref": f"{args.matrix}.compartment_stratified.json",
        "compartment_R_agrees": comp["compartment_R_agrees"],
        "drop_sorted_sensitivity": comp["drop_sorted_sensitivity"],
        "acute_decoy_specificity": decoys,
    }
    args.out_adjudicated.write_text(json.dumps(adjudicated, indent=2))

    print(f"[artifact_adjudication:{args.matrix}] adjudicated_R={adjudicated_R} "
          f"regime={summary['regime_band']} platform_loo_applicable={ploo.get('applicable')} "
          f"compartment_R_agrees={comp['compartment_R_agrees']} "
          f"recovered_persists={rec.get('shared_subspace_persists_in_case_vs_recovered')}")


if __name__ == "__main__":
    main()
