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
    min_trig = cfg["folds"]["identifiability"]["min_triggers"]
    K = len(cols)

    # ---- prong (i): compartment-stratified R (deconvolution-free composition control)
    # Each stratum is held to the SAME K>=3 identifiability rule as the LODO/LOCO folds
    # (review WP4 Finding 1): a <3-trigger stratum is NON-IDENTIFIABLE — its R is
    # reported for reference but is NOT interpretable, and it cannot establish (or
    # refute) compartment invariance.
    stratified = {}
    for comp in sorted({c["compartment"] for c in colmeta}):
        idx = [j for j in range(K) if colmeta[j]["compartment"] == comp]
        n_trig = len({colmeta[j]["trigger"] for j in idx})
        identifiable = n_trig >= min_trig
        res, _ = stratum_R(Xc[:, idx], cfg, seeds, X[:, idx])
        stratified[comp] = {
            "n_columns": len(idx),
            "n_triggers": n_trig,
            "identifiable": identifiable,
            "verdict": ("identifiable" if identifiable else "non_identifiable"),
            "contrasts": [cols[j] for j in idx],
            "R_primary": res.get("R_primary"),
            "R_consensus": res.get("R_consensus"),
            "R_interpretable": (res.get("R_primary") if identifiable else None),
            "regime_band": (rb.regime_of(res["R_primary"], bands)
                            if (identifiable and res.get("R_primary") is not None) else None),
            "structural_offdiag_sd": res["structural_offdiag_concordance"]["sd"],
            "deconvolvable": comp in deconvolvable,
        }
    # Compartment invariance is judged ONLY over strata that clear K>=3. With <2
    # identifiable strata we CANNOT compare -> invariance NOT ESTABLISHED (neither
    # confirmed nor refuted), NOT "R differs -> entangled" (Finding 1).
    ident = {c: v for c, v in stratified.items() if v["identifiable"]}
    ident_Rs = [v["R_primary"] for v in ident.values() if v["R_primary"] is not None]
    if len(ident_Rs) < 2:
        r_agree, comp_status = None, "not_established"
    elif len(set(ident_Rs)) <= 1:
        r_agree, comp_status = True, "invariant"
    else:
        r_agree, comp_status = False, "differs"

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
        "compartment_invariance_status": comp_status,
    }

    note_by_status = {
        "not_established": (
            f"compartment invariance NOT ESTABLISHED: only {len(ident)} stratum/strata "
            f"clear K>={min_trig} (the rest are 1-2 trigger, non-identifiable), so a "
            "cell-composition-shift rival can be neither confirmed nor refuted from these "
            "data — this is an underpowered control, not evidence of entanglement"),
        "invariant": f"R agrees across the identifiable (K>={min_trig}) compartments",
        "differs": (f"R DIFFERS across identifiable (K>={min_trig}) compartments -> shared "
                    "axis is compartment-entangled (a cell-composition-shift rival is live; "
                    "the pooled R is not a single compartment-invariant biology rank)"),
    }
    return {
        "matrix": matrix,
        "finding": "C (compartment/composition control)",
        "identifiability_rule": {
            "min_triggers": min_trig,
            "grounding": ("t116 K>=3 (same as the LODO/LOCO folds); a <3-trigger stratum "
                          "is non-identifiable and cannot establish compartment invariance"),
        },
        "compartment_stratified_R": stratified,
        "n_identifiable_strata": len(ident),
        "compartment_invariance_status": comp_status,
        "compartment_R_agrees": r_agree,
        "R_compartment_invariant_note": note_by_status[comp_status],
        "drop_sorted_sensitivity": drop_sorted,
        "composition_adjustment": composition_adjustment,
    }


def platform_loo(X, Xc, cols, colmeta, cfg, seeds, full_rank):
    """Re-estimate R dropping each platform in turn. A rank that collapses when a
    platform is removed is a platform axis, not biology. A single-platform corpus
    CANNOT test platform-confounding — recorded as a limitation, not a pass."""
    bands = {k: tuple(v) for k, v in cfg["folds"]["pass_rule"]["regime_bands"].items()}
    min_trig = cfg["folds"]["identifiability"]["min_triggers"]
    r_band = cfg["folds"]["pass_rule"]["r_band"]
    platforms = sorted({c["platform"] for c in colmeta})
    K = len(cols)
    if len(platforms) < 2:
        return {"applicable": False, "n_platforms": len(platforms),
                "platforms": platforms,
                "platform_invariance_status": "untestable_single_platform",
                "note": ("single-platform corpus: platform-LOO cannot test platform-"
                         "confounding, so the low-rank signal CANNOT be shown platform-"
                         "independent here (a limitation carried to the grid verdict)."),
                "R_full": full_rank.get("R_primary")}
    # Each platform-drop fold is held to the SAME K>=3 identifiability rule as the
    # LODO/LOCO folds (review WP4 Finding 1): a drop leaving <3 triggers is
    # NON-IDENTIFIABLE — its R is untestable, so a low R there is NOT a "collapse".
    drops = []
    for p in platforms:
        keep = [j for j in range(K) if colmeta[j]["platform"] != p]
        n_trig = len({colmeta[j]["trigger"] for j in keep})
        identifiable = n_trig >= min_trig and len(keep) >= 2
        entry = {"dropped_platform": p, "n_remaining": len(keep),
                 "n_triggers_remaining": n_trig, "identifiable": identifiable,
                 "remaining_contrasts": [cols[j] for j in keep]}
        if not identifiable:
            entry.update({"R": None, "verdict": "non_identifiable",
                          "note": (f"retains {n_trig} < {min_trig} triggers (K>=3 floor)"
                                   if n_trig < min_trig else "<2 columns remain")
                          + " -> platform invariance untestable on this drop"})
            drops.append(entry)
            continue
        res, _ = rb.estimate_rank(Xc[:, keep], cfg, seeds, with_ci=False,
                                  struct_cols=X[:, keep])
        R = res.get("R_primary")
        entry.update({"R": R, "verdict": "identifiable",
                      "regime_band": (rb.regime_of(R, bands) if R is not None else None)})
        drops.append(entry)
    R_full = full_rank.get("R_primary")
    ident_drops = [d for d in drops if d["identifiable"] and d["R"] is not None]
    if not ident_drops or R_full is None:
        survives, status = None, "not_established"
    else:
        survives = all(abs(d["R"] - R_full) <= r_band for d in ident_drops)
        any_nonident = any(not d["identifiable"] for d in drops)
        # invariance is only ESTABLISHED if every drop is identifiable AND survives;
        # if some drops are non-identifiable it is at most PARTIAL (Finding 1).
        status = ("established" if (survives and not any_nonident)
                  else "partial" if survives else "not_established")
    return {"applicable": True, "n_platforms": len(platforms), "platforms": platforms,
            "R_full": R_full, "identifiability_min_triggers": min_trig,
            "platform_drops": drops,
            "platform_invariance_status": status,
            "rank_survives_every_identifiable_platform_drop": survives}


def recovered_control_specificity(Xc, cols, colmeta, cfg, full_rank):
    """Directional (not magnitude) specificity: does the leading shared subspace
    defined by the case-vs-NAIVE (healthy) columns PERSIST in the case-vs-RECOVERED
    columns? Persistence = the recovered columns still project heavily onto the naive
    shared subspace. require_exceed is FALSE by config: we do not require case-vs-
    recovered to exceed case-vs-naive. NOTE the reference is IN-SAMPLE (built from the
    naive columns) and the recovered columns differ by dataset/control composition, so
    a low projection supports only 'the naive-defined subspace is not strongly present
    in the recovered-control contrasts' — NOT a claim that the axis is 'infection-
    history' or 'case-vs-healthy' (review WP4 Finding 5, conservative wording)."""
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
        "n_recovered_triggers": len({colmeta[j]["trigger"] for j in rec_idx}),
        "shared_subspace_persists_in_case_vs_recovered": persists,
        "unclassified_control_types": other,
        "conservative_reading": (
            "supports only: the naive-defined shared subspace is NOT strongly present in "
            "the recovered-control contrasts. It does NOT by itself prove the axis is "
            "'infection-history' or 'case-vs-healthy' — the reference is in-sample and the "
            "recovered columns differ by dataset/control composition (Finding 5)."),
        "note": ("directional persistence, not magnitude: a healthy-control contrast "
                 "can legitimately be larger; the test is whether the naive-defined shared "
                 "subspace remains present in case-vs-recovered."),
    }


def negative_control_floor(full_rank, structural, cfg):
    """The artifact floor. The pinned universe is Hallmark∪Reactome (biology only):
    housekeeping / platform-associated / GC-confounded negative-control gene sets were
    deliberately NOT scored, so the assembled NES matrix carries no control rows to
    subtract set-wise. Record that as the exact blocker. Separately report the ONE null
    that IS applied — the parallel-analysis per-column-permuted null — but do NOT call it
    an artifact floor (review WP4 Finding 2): it removes only RANDOM cross-column
    structure, and does NOT control correlated platform/batch/control-type/composition
    artifacts. The genuine artifact floor (negative-control / platform / composition) is
    deferred/underpowered here."""
    pa = full_rank.get("parallel_analysis_detail", {})
    sv = pa.get("singular_values", [])
    band = pa.get("null_band", [])
    n_above = int(sum(1 for s, b in zip(sv, band) if s > b))
    return {
        "negative_control_sets_requested": cfg["artifact_controls"]["negative_control_sets"],
        "artifact_floor_status": "not_available",
        "artifact_floor_note": ("no set-based negative-control, platform, or composition "
                                "artifact floor was subtracted (all deferred/underpowered). "
                                "The only null applied is the random-structure null below, "
                                "which is NOT an artifact floor."),
        "set_based_subtraction": {
            "status": "deferred_note_only",
            "blocker": ("the pinned universe is Hallmark∪Reactome (biological pathways "
                        "only); housekeeping/platform/GC-confounded negative-control sets "
                        "were not scored through fgsea, so there are no control rows in the "
                        "NES matrix to subtract. Implementing this needs a WP2 re-run "
                        "appending declared negative-control sets to the universe."),
        },
        "random_structure_null_floor": {
            "method": "parallel_analysis_per_column_permuted_null",
            "controls_for": "random cross-column structure (column permutation) ONLY",
            "does_not_control": ("correlated platform / batch / control-type / "
                                 "cell-composition artifacts — those need the deferred "
                                 "set-based/platform/composition controls"),
            "note": ("R_primary counts only singular values exceeding this per-column-"
                     "permuted null. This is a RANDOM-STRUCTURE floor, NOT an artifact "
                     "floor — it does not subtract correlated (shared) artifacts."),
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

    # declared stratum/decoy columns for THIS matrix's adjudication. The sorted stratum
    # (drop-sorted comparison) is a STRICT-only pooled-column test (mirrors the
    # Snakefile extra_nes). The acute-decoy specificity layer is GLOBAL — it applies to
    # both matrices, so the decoy ledger is recorded for sensitivity too (review WP4
    # Finding 4), never left silently empty.
    def tagged(tag):
        return [c for c in cfg["contrasts"] if cfg["contrasts"][c].get("matrix") == tag]
    extra_declared = {"stratum": tagged("stratum") if args.matrix == "strict" else [],
                      "decoy": tagged("decoy")}
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
    # R_point_estimate is the random-structure-null-adjusted R_primary — NOT a clean
    # artifact-adjudicated estimate (Finding 2/3). The binding available controls are
    # compartment invariance, platform invariance, and recovered-control persistence;
    # the set-based negative-control floor + acute-decoy specificity are unavailable.
    comp_status = comp["compartment_invariance_status"]
    plat_status = ploo.get("platform_invariance_status")
    recovered_persists = rec.get("shared_subspace_persists_in_case_vs_recovered")
    set_based_available = False
    acute_decoy_available = decoys["status"] == "available"
    # artifact_controls_pass is TRUE only if every available binding control passes AND
    # the deferred controls are actually available. Here they are not -> false. WP6
    # grid placement MUST consume this, not R_point_estimate alone (Finding 3).
    controls_pass = bool(
        comp_status == "invariant" and plat_status == "established"
        and recovered_persists and set_based_available and acute_decoy_available)
    interpretation_status = "arbitrable" if controls_pass else "limited_or_nonarbitrating"
    summary = {
        "R_point_estimate": R_full,
        "R_point_estimate_basis": "random_structure_null_adjusted_R_primary (NOT artifact-floor-adjusted)",
        "regime_band": (rb.regime_of(R_full, bands) if R_full is not None else None),
        "structural_offdiag_sd": structural.get("sd"),
        "artifact_controls_pass": controls_pass,
        "interpretation_status": interpretation_status,
        "platform_invariance_status": plat_status,
        "platform_loo_applicable": ploo.get("applicable"),
        "compartment_invariance_status": comp_status,
        "compartment_R_agrees": comp["compartment_R_agrees"],
        "shared_subspace_persists_in_case_vs_recovered": recovered_persists,
        "set_based_negative_control_available": set_based_available,
        "artifact_floor_available": False,
        "acute_decoy_specificity_available": acute_decoy_available,
        "verdict_note": (
            "R_point_estimate is the random-structure-null-adjusted R_primary, NOT a "
            "clean artifact-adjudicated estimate — no set-based negative-control, "
            "platform, or composition artifact floor was subtracted. Of the available "
            "binding controls, compartment invariance is "
            f"'{comp_status}', platform invariance is '{plat_status}', and the naive "
            "shared subspace "
            f"{'persists' if recovered_persists else 'does NOT persist'} in case-vs-"
            "recovered. artifact_controls_pass=false -> interpretation_status="
            f"'{interpretation_status}': WP6 grid placement must consume this flag, not "
            "R_point_estimate alone."),
    }
    adjudicated = {
        "matrix": args.matrix,
        "finding": "artifact + compartment adjudication (plan:0010 Stage 5, WP4)",
        "summary": summary,
        "platform_loo": ploo,
        "recovered_control_specificity": rec,
        "negative_control_floor": neg,
        "compartment_control_ref": f"{args.matrix}.compartment_stratified.json",
        "compartment_invariance_status": comp_status,
        "compartment_R_agrees": comp["compartment_R_agrees"],
        "drop_sorted_sensitivity": comp["drop_sorted_sensitivity"],
        "acute_decoy_specificity": decoys,
    }
    args.out_adjudicated.write_text(json.dumps(adjudicated, indent=2))

    print(f"[artifact_adjudication:{args.matrix}] R_point_estimate={R_full} "
          f"controls_pass={controls_pass} status={interpretation_status} "
          f"compartment_invariance={comp_status} platform_invariance={plat_status} "
          f"recovered_persists={recovered_persists}")


if __name__ == "__main__":
    main()
