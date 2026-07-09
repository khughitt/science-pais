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
project PAIS) ACTIVATES once >=2 columns are built (currently gse221921_fm PBMC-RNAseq
+ gse67311_fm WB-microarray) but is UNDER-RESOLVED at 2 columns: the rank-matched
leave-one-out ceiling caps at r_eff=min(R,n_noninf-1)=1 < PAIS R, so its verdict is
`under_resolved_need_more_noninfectious_columns` until a 3rd cross-condition,
compartment-matched column is built. NB the 2 FM columns differ in compartment (PBMC
vs whole blood) and platform, and forward recovery tracks compartment — a confound
flagged in the caveats, not FM biology.

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


def _loo_projection(Zr: np.ndarray, R: int, groups, labels=None) -> dict:
    """In-domain replication ceiling: for each leave-out GROUP of column indices, build
    U_ref from the columns NOT in the group and project each column IN the group. The
    group partitions decide what "held out" means:
      - column-LOO: singleton groups (each column its own group) — a within-trigger
        column can still project onto a subspace containing its OWN trigger's other
        columns, so with LC dominating this OVERSTATES the trigger-independent ceiling;
      - trigger-LOO: groups = all columns of a trigger — the held-out trigger's columns
        project onto a subspace built ONLY from the OTHER triggers, i.e. a genuinely
        trigger-independent replication ceiling (the fair comparator for an external,
        wholly-novel non-infectious trigger). USE THIS for infection-specificity."""
    K = Zr.shape[1]
    fracs, meta = {}, {}
    group_fracs = {}  # held-out group label -> [per-column fractions in that group]
    for gi, g in enumerate(groups):
        others = [i for i in range(K) if i not in g]
        if len(others) < 1 or not g:
            continue
        Uo, r_o = _leading_subspace(Zr[:, others], R)
        glabel = labels[gi] if labels else gi
        for j in g:
            f = round(projection_fraction(Uo, Zr[:, j]), 4)
            fracs[j] = f
            meta[j] = {"n_ref_columns": len(others), "ref_rank_r": int(r_o),
                       "held_out_group": glabel}
            group_fracs.setdefault(str(glabel), []).append(f)
    if not fracs:
        return {"applicable": False, "note": "no leave-out group projectable"}
    vals = list(fracs.values())
    # per-group (per-trigger for trigger-LOO) mean, then average GROUPS with equal weight
    # so a trigger contributing many columns (e.g. LC = 5 of 7 strict cols) does NOT
    # dominate the ceiling. For column-LOO (singleton groups) group- == column-weighted.
    per_group_mean = {k: round(float(np.mean(v)), 4) for k, v in group_fracs.items()}
    return {
        "applicable": True,
        "per_column_fraction": fracs,
        "per_column_meta": meta,
        "per_group_mean": per_group_mean,
        "n_groups": len(per_group_mean),
        "column_weighted_mean": round(float(np.mean(vals)), 4),
        "group_weighted_mean": round(float(np.mean(list(per_group_mean.values()))), 4),
        "min": round(float(np.min(vals)), 4),
        "max": round(float(np.max(vals)), 4),
        "n_projected": len(vals),
    }


def _permutation_null(U_ref: np.ndarray, z: np.ndarray, obs_recovery: float,
                      n_perm: int, seed: int) -> dict:
    """Empirical null for the recovery fraction: permute the column's entries ACROSS
    pathways (breaking its alignment with U_ref while preserving its marginal NES
    distribution), reproject, repeat. Much harder to misread than the analytic
    isotropic floor r/P — a real column that merely has heavy-tailed NES will project
    above r/P by construction, but a permuted version of ITSELF will not exceed the
    observed recovery unless the observed alignment is genuine (review Finding 3)."""
    rng = np.random.default_rng(seed)
    draws = np.empty(n_perm)
    for i in range(n_perm):
        draws[i] = projection_fraction(U_ref, rng.permutation(z))
    obs_ge = int(np.sum(draws >= obs_recovery))
    return {
        "n_perm": int(n_perm),
        "null_mean": round(float(draws.mean()), 5),
        "null_p95": round(float(np.quantile(draws, 0.95)), 5),
        "null_max": round(float(draws.max()), 5),
        "empirical_p": round((obs_ge + 1) / (n_perm + 1), 5),  # add-one (never 0)
        "method": "row-permutation of the projected column over the common pathways",
    }


def specificity_for(spec_id, nes_path, X, R, cols, triggers, rec_cfg, seed):
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
    analytic_null = r / P  # isotropic floor — orientation only, NOT calibrated (Finding 3)

    # empirical null (row-permutation) — the defensible "above chance" test (Finding 3)
    perm = _permutation_null(U_ref, zr_s, recovery, rec_cfg.get("n_perm_null", 2000), seed)

    # in-domain replication ceilings (Finding 1): column-LOO OVERSTATES the ceiling when
    # one trigger dominates (a held-out LC column still sees the other LC columns);
    # trigger-LOO is the trigger-INDEPENDENT ceiling and the fair comparator for a wholly
    # novel external non-infectious trigger. The verdict uses TRIGGER-LOO.
    K = Zr.shape[1]
    col_loo = _loo_projection(Zr, R, [[j] for j in range(K)],
                              labels=[cols[j] for j in range(K)])
    uniq_trig = sorted({t for t in triggers})
    trig_groups = [[j for j in range(K) if triggers[j] == t] for t in uniq_trig]
    trig_loo = _loo_projection(Zr, R, trig_groups, labels=uniq_trig)
    insample = {cols[j]: round(projection_fraction(U_ref, Zr[:, j]), 4)
                for j in range(K)}  # context: PAIS cols on their own (all-column) subspace

    generic_frac = rec_cfg.get("generic_manifold_frac", 0.70)
    # "above chance" = the empirical permutation null, not the analytic floor
    above_random = bool(recovery > perm["null_p95"] and perm["empirical_p"] < 0.05)
    # generic-manifold reading is judged against the TRIGGER-INDEPENDENT ceiling, weighted
    # per-TRIGGER (not per-column) so the LC-dominated column count does not inflate it
    # (review Finding: 5 of 7 strict cols are SARS-CoV-2; column-weighting overstates the mean).
    ceiling = trig_loo.get("group_weighted_mean")
    recovers_like_pais = bool(
        above_random and ceiling is not None and ceiling > 0 and recovery >= generic_frac * ceiling)
    # identifiability of the ceiling itself: each leave-one-trigger-out reference is built from
    # (n_triggers - 1) triggers; below the project's K>=3 trigger floor the ceiling is under-identified.
    n_trig = trig_loo.get("n_groups", 0)
    trigger_loo_identifiability_pass = bool((n_trig - 1) >= 3)
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
        "permutation_null": perm,
        "above_random": above_random,
        "analytic_isotropic_null_rp": round(analytic_null, 5),  # orientation only, see Finding 3
        "trigger_loo_ceiling": trig_loo,          # PRIMARY comparator (trigger-independent)
        "trigger_loo_ceiling_used": "group_weighted_mean",  # per-trigger, not per-column (see note)
        "trigger_loo_identifiability_pass": trigger_loo_identifiability_pass,
        "trigger_loo_identifiability_note": (
            f"leave-one-trigger-out references are built from {max(n_trig - 1, 0)} triggers "
            f"(n_triggers={n_trig}); below the K>=3 trigger floor, so the trigger-LOO ceiling is "
            f"itself under-identified — read it as an upper-bound-ish reference, not a calibrated ceiling."),
        "recovery_vs_trigger_loo_mean": (round(recovery / ceiling, 3)
                                         if ceiling else None),  # vs GROUP-weighted (per-trigger) mean
        "recovery_vs_trigger_loo_column_weighted": (
            round(recovery / trig_loo["column_weighted_mean"], 3)
            if trig_loo.get("column_weighted_mean") else None),  # context: vs the LC-inflated mean
        "column_loo_reference": col_loo,          # SECONDARY (overstates the ceiling; context only)
        "recovery_vs_column_loo_mean": (round(recovery / col_loo["column_weighted_mean"], 3)
                                        if col_loo.get("column_weighted_mean") else None),
        "insample_pais_projection_context": insample,
        "recovers_like_trigger_loo_pais": recovers_like_pais,
        "verdict": verdict,
        "verdict_reading": {
            "not_recovered_infection_specific_consistent":
                "the non-infectious column does NOT recover the PAIS subspace beyond its own "
                "row-permutation null — consistent with an infection-specific axis (but the PAIS "
                "subspace is weakly identified, so this is not a strong positive claim).",
            "recovered_like_pais_generic_manifold_consistent":
                "the non-infectious column recovers the PAIS subspace about as well as a genuine "
                "TRIGGER-held-out PAIS trigger — consistent with a GENERIC sickness/fatigue "
                "manifold rather than an infection-specific attractor (the t116 Q-D ceiling).",
            "partially_recovered_indeterminate":
                "recovery is above the permutation null but below the TRIGGER-independent PAIS "
                "ceiling — indeterminate; neither cleanly infection-specific nor a full "
                "generic-manifold recovery. NB if the trigger-LOO ceiling is itself low, the PAIS "
                "subspace is not even trigger-general within PAIS (coheres with the Stage-3c FAIL "
                "/ heterogeneous structural co-primary), and the comparison is correspondingly weak.",
        }[verdict],
    }


def reverse_projection_for(spec_paths, X, R, cols, rec_cfg, seed):
    """Reverse read-across: build a NON-INFECTIOUS subspace U_noninf from >=2 standardized
    non-infectious columns (its leading-r left-singular vectors), project each PAIS column onto
    it, and ask how well PAIS recovers the non-infectious axis. This is the symmetric complement
    to the forward projection and — crucially — does NOT depend on the weakly-identified PAIS
    subspace: U is defined by the non-infectious columns themselves.

      * NULL: row-permute each projected PAIS column (breaks alignment, keeps marginal NES).
      * CEILING: leave-one-non-infectious-out — how well a genuine HELD-OUT non-infectious column
        recovers U built from the OTHER non-infectious columns (the fair "in-domain" reference; a
        PAIS column recovering U as well as a held-out non-infectious one ⇒ shared axis).
    Reading: PAIS ≈ ceiling ⇒ PAIS lies in the non-infectious subspace (generic-sickness manifold);
    PAIS ≈ null ⇒ the PAIS axis is distinct (infection-specific)."""
    ids = list(spec_paths.keys())
    if len(ids) < 2:
        return {"applicable": False,
                "reason": f"reverse projection needs >=2 non-infectious columns; have {len(ids)} "
                          f"({ids}) — build more of the queued replication panel to activate it"}
    Zcols = {sid: read_nes(Path(p), sid, _GENE_SETS) for sid, p in spec_paths.items()}
    noninf = np.column_stack([Zcols[s] for s in ids])            # P_full x k (pinned gene-set index)
    rows = (~np.isnan(X).any(axis=1)) & (~np.isnan(noninf).any(axis=1))
    P = int(rows.sum())
    if P < len(ids) + 1:
        return {"applicable": False,
                "reason": f"only {P} rows usable across PAIS-complete AND all {len(ids)} non-infectious "
                          f"columns non-NaN — too few to build a rank-{R} non-infectious subspace"}
    # RANK-FAIRNESS (review of the 2-column result): the leave-one-non-infectious-out ceiling
    # projects a held-out column onto a subspace built from the REMAINING (len-1) columns, so it
    # can only support rank <= len(ids)-1. Projecting PAIS onto a HIGHER-rank U than the ceiling
    # can reach makes PAIS beat the ceiling by construction (rank-2 vs rank-1 with 2 columns —
    # exactly the K=2 degeneracy interpretation:0037 names in the forward direction). So cap BOTH
    # the PAIS projection and the ceiling at r_eff = min(R, len(ids)-1); when r_eff < R the reverse
    # test is UNDER-RESOLVED (cannot reach the PAIS rank R) and its verdict is not trustworthy.
    r_eff = max(1, min(R, len(ids) - 1, P))
    underresolved = bool(r_eff < R)
    Nr = re.standardize_columns(noninf[rows])
    U_noninf = np.linalg.svd(Nr, full_matrices=False)[0][:, :r_eff]

    Xr = X[rows]
    rng = np.random.default_rng(seed)
    n_perm = int(rec_cfg.get("n_perm_null", 2000))
    per_pais = {}
    for j in range(X.shape[1]):
        zj = _standardize_vec(Xr[:, j])
        rec = projection_fraction(U_noninf, zj)
        draws = np.fromiter((projection_fraction(U_noninf, rng.permutation(zj)) for _ in range(n_perm)),
                            dtype=float, count=n_perm)
        per_pais[cols[j]] = {
            "recovery": round(rec, 4),
            "empirical_p": round((int(np.sum(draws >= rec)) + 1) / (n_perm + 1), 5),
            "null_p95": round(float(np.quantile(draws, 0.95)), 5),
        }
    # leave-one-non-infectious-out ceiling — rank-matched to the PAIS projection (r_eff)
    loo = {}
    for i, sid in enumerate(ids):
        others = [k for k in range(len(ids)) if k != i]
        Uo = np.linalg.svd(re.standardize_columns(noninf[rows][:, others]), full_matrices=False)[0]
        Uo = Uo[:, :max(1, min(r_eff, len(others)))]
        loo[sid] = round(projection_fraction(Uo, _standardize_vec(noninf[rows][:, i])), 4)
    ceiling = round(float(np.mean(list(loo.values()))), 4) if loo else None

    recs = {c: v["recovery"] for c, v in per_pais.items()}
    mean_pais = round(float(np.mean(list(recs.values()))), 4)
    above = {c: bool(v["recovery"] > v["null_p95"] and v["empirical_p"] < 0.05)
             for c, v in per_pais.items()}
    n_above = int(sum(above.values()))
    ratio = (round(mean_pais / ceiling, 3) if ceiling else None)
    generic_frac = rec_cfg.get("generic_manifold_frac", 0.70)
    like_noninf = bool(ceiling and ceiling > 0 and mean_pais >= generic_frac * ceiling and n_above >= 1)
    if underresolved:
        # cannot reach the PAIS rank R with only len(ids) columns → verdict not trustworthy
        verdict = "under_resolved_need_more_noninfectious_columns"
    elif n_above == 0:
        verdict = "pais_not_in_noninfectious_subspace_infection_specific_consistent"
    elif ratio is not None and ratio > 1.0:
        # PAIS recovers U better than the non-infectious columns recover it themselves — the
        # non-infectious axis is not reproducible (degenerate ceiling), so no manifold claim holds
        verdict = "noninfectious_axis_not_reproducible_indeterminate"
    elif like_noninf:
        verdict = "pais_recovers_noninfectious_subspace_generic_manifold_consistent"
    else:
        verdict = "partially_recovered_indeterminate"
    return {
        "applicable": True,
        "method": "U_noninf = leading-r_eff left-singular vectors of the standardized non-infectious "
                  "column block; project each PAIS column onto it (independent of the PAIS subspace). "
                  "r_eff = min(R, n_noninf-1) so the leave-one-out ceiling is rank-matched.",
        "n_noninfectious_columns": len(ids),
        "noninfectious_columns": ids,
        "n_rows_used": P,
        "pais_R": int(R),
        "noninf_subspace_rank_r_eff": int(r_eff),
        "identifiability_pass": (not underresolved),
        "identifiability_note": (
            f"r_eff={r_eff} (=min(R={R}, n_noninf-1={len(ids)-1})); "
            + ("UNDER-RESOLVED: with only "
               f"{len(ids)} non-infectious columns the subspace rank is capped BELOW the PAIS R={R}, so "
               "the reverse verdict is not trustworthy — build a 3rd+ non-infectious column (queued "
               "replication) for a full-rank, rank-matched test." if underresolved else
               "rank-matched to the PAIS R.")),
        "per_pais_recovery": per_pais,
        "mean_pais_recovery": mean_pais,
        "n_pais_above_null": n_above,
        "leave_one_noninfectious_out_ceiling": loo,
        "ceiling_mean": ceiling,
        "ceiling_is_noninfectious_axis_reproducibility": (
            "low ceiling ⇒ the non-infectious columns disagree (their case-vs-control axis is not "
            "reproducible across cohort/compartment); a ratio>1 means PAIS recovers U better than the "
            "non-infectious columns recover it themselves — an incoherent 'manifold' comparison."),
        "mean_pais_vs_ceiling": ratio,
        "verdict": verdict,
        "caveat": "single-condition U (all fibromyalgia here: PBMC-RNAseq + WB-microarray) tests recovery "
                  "of the FM axis specifically, and the two FM cohorts differ in COMPARTMENT (PBMC vs whole "
                  "blood) — forward recovery tracks compartment (WB 0.23 vs PBMC 0.04), so recovery is "
                  "confounded by blood composition. A cross-condition, compartment-matched U (>=3 columns) "
                  "is required before any generic-non-infectious-manifold reading.",
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
    triggers = [c.get("trigger") for c in grouping["columns"]]  # per-column trigger (for trigger-LOO)
    seed = int(cfg.get("determinism", {}).get("master_seed", 0))
    global _GENE_SETS
    _GENE_SETS = gene_sets  # read_nes aligns each extra column to this pinned index

    # map provided (buildable) NES paths back to their contrast id by basename
    provided = {Path(p).name.rsplit(".nes.tsv", 1)[0]: p for p in args.spec_nes}
    build_now = list(spec_cfg.get("build_now", []))
    missing = [c for c in build_now if c not in provided]
    if missing:
        halt(f"build_now columns have no NES producer wired: {missing} "
             f"(provided: {sorted(provided)})")

    columns = {c: specificity_for(c, provided[c], X, R, cols, triggers, rec_cfg, seed)
               for c in build_now}

    # reverse read-across (activates once >=2 non-infectious columns are built)
    spec_paths = {c: provided[c] for c in build_now}
    reverse = reverse_projection_for(spec_paths, X, R, cols, rec_cfg, seed)

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
        "reverse_projection": reverse,
        "reverse_projection_config_note": spec_cfg.get("reverse_projection"),
        "caveats": [
            f"exploratory_flagship: {len(build_now)} non-infectious column(s) built ({build_now}); the "
            "rest of the admissible panel is queued replication (see queued_replication).",
            "REVERSE PROJECTION is UNDER-RESOLVED at 2 columns (r_eff=1 < PAIS R=2 — the leave-one-out "
            "ceiling can only reach rank n_noninf-1); a 3rd+ non-infectious column is required for a "
            "full-rank, rank-matched reverse test. See reverse_projection.identifiability_note.",
            "COMPARTMENT/PLATFORM CONFOUND: the two FM columns differ in compartment (GSE221921 PBMC vs "
            "GSE67311 whole blood) AND platform (RNA-seq vs microarray) and give ~5x different FORWARD "
            "recovery (0.045 vs 0.234); the strict PAIS corpus is 5 PBMC + 2 whole-blood, so the WB-FM's "
            "high recovery is plausibly shared blood COMPOSITION, not FM biology. Compartment-matched "
            "read-across is a prerequisite for any biological reading.",
            "The PAIS reference subspace is weakly identified (Stage-3c FAIL) — see "
            "pais_reference_subspace.weak_identification_caveat.",
            "NES pooled only at the gene-set level over the same pinned Hallmark∪Reactome universe; "
            "expression never merged. Each non-infectious deposit passed the SAME admissibility gates "
            "as the primary corpus (blood-bulk WB/PBMC, public, downloadable, sample-level case-vs-control).",
        ],
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(out, indent=2))
    line = " ".join(f"{c}=recovery{columns[c]['subspace_recovery_fraction']}"
                    f"(perm_p={columns[c]['permutation_null']['empirical_p']},"
                    f"trigLOO_grpmean={columns[c]['trigger_loo_ceiling'].get('group_weighted_mean')},"
                    f"trigLOO_colmean={columns[c]['trigger_loo_ceiling'].get('column_weighted_mean')},"
                    f"{verdicts[c]})" for c in build_now)
    print(f"[gws_fm_specificity] status={out['status']} {line}")


if __name__ == "__main__":
    main()
