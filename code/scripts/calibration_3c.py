# science:code
# status: workflow-owned
# task_ids: [t117]
# science:end

#!/usr/bin/env python3
"""calibration_3c.py — WP3 Stage-3c: calibrate the rank battery against t116's OWN
generative model BEFORE any real-data R is placed on the t116 grid (task:t117;
plan:0010 Stage 3c, review Finding B, Key decision 6).

The rationale (Finding B): the SVD/parallel-analysis effective-rank estimator is NOT the
statistic interpretation:0037 characterized — t116 varied R as a *generative* parameter
and measured the power of a structural single-shared-axis statistic (off-diagonal
concordance SD). Mapping an estimated R onto "the t116 R-regime grid" is therefore a
procedure substitution that must be VALIDATED, not assumed. This stage injects
pathway x contrast matrices at KNOWN rank R in {2,4,8}, drawn from t116's generative
model at the REAL corpus's K (columns) and per-contrast N, with the off-diagonal
concordance MATCHED to the real strict matrix, and confirms:

  (1) the battery recovers R (median R_hat within recovery_tol) for every rank that is
      IDENTIFIABLE at the corpus's K (a rank R>=K cannot be recovered from K columns —
      that ceiling is itself the finding, not a battery failure);
  (2) the row-bootstrap CI has ~nominal coverage of the injected R; and
  (3) the structural co-primary (off-diagonal SD) lands in the correct t116 regime band
      (low R -> HIGH SD / heterogeneous; high R -> LOW SD / homogeneous, mimics an axis).

Generative model (mirrors code/workflows/t116-power-bias-floor/scripts/simulate.py `_gen`,
re-expressed as a P x K matrix with per-column N):

    x_k = shared_k + alpha * a_k + e_k
      shared_k = kappa * sum_r Z_kr g_r   (R orthogonal repertoire axes g; nonneg loadings Z)
      alpha*a_k                            (arm-specific systematic bias; N-invariant)
      e_k, sd = sigma0 / sqrt(N_k)         (within-arm sampling noise; per-column N)

kappa is binary-searched per R so the realized mean off-diagonal Spearman concordance
matches the real matrix's (the t116 adversarial-null discipline: same average overlap,
different rank).

Emits calibration.json (the full record — ALWAYS written; a FAIL is a legitimate finding,
not a pipeline error) and calibration.pass (a JSON sentinel carrying {"pass": bool, ...};
WP6 grid_placement is fail-closed on it — no grid verdict unless pass==true). Uses the
SAME rank_estimators module the real battery uses, so the calibrated and applied
procedures are one code path. All knobs originate in config.yaml.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

import rank_estimators as re


# ---------------------------------------------------- t116 generative model
def fixed_axes(rng: np.random.Generator, P: int, R: int) -> np.ndarray:
    """R repertoire axes g (R x P), each mean 0, unit SD, mutually orthogonalized —
    the t116 `_fixed_axes` construction (Gram-Schmidt)."""
    A = rng.standard_normal((R, P))
    A = A - A.mean(axis=1, keepdims=True)
    for i in range(R):
        for j in range(i):
            A[i] = A[i] - (A[i] @ A[j]) / (A[j] @ A[j]) * A[j]
        A[i] = A[i] / A[i].std()
    return A


def gen_matrix(rng, R, P, N_per_col, kappa, alpha, sigma0, g) -> np.ndarray:
    """One synthetic pathway x contrast matrix (P x K) at generative rank R. Columns =
    contrasts; each gets independent nonneg loadings Z on the R shared axes (t116 H0),
    plus independent arm bias and per-column sampling noise."""
    K = len(N_per_col)
    Z = np.abs(rng.standard_normal((K, R)))
    shared = kappa * (Z @ g).T                       # (P, K)
    a = rng.standard_normal((K, P))
    a = a - a.mean(axis=1, keepdims=True)
    a = a / a.std(axis=1, keepdims=True)
    bias = alpha * a.T                               # (P, K)
    e = rng.standard_normal((P, K)) * (sigma0 / np.sqrt(np.asarray(N_per_col)))[None, :]
    return shared + bias + e


def fast_offdiag(X: np.ndarray):
    """Mean and SD of off-diagonal Spearman concordances between columns, vectorized
    (no NaN in generated matrices): rank-transform each column, then Pearson corr of
    ranks = Spearman — identical to the battery's pairwise-complete statistic on complete
    data, but fast enough for the kappa search + the calibration hot loop. SD undefined
    for K<=2."""
    ranks = np.argsort(np.argsort(X, axis=0), axis=0).astype(float)
    C = np.corrcoef(ranks, rowvar=False)
    iu = np.triu_indices(X.shape[1], k=1)
    off = C[iu]
    return float(off.mean()), (float(off.std(ddof=1)) if off.size >= 2 else float("nan"))


def match_kappa(rng, R, P, N_per_col, target_rho, alpha, sigma0, g, cfg, floor):
    """Binary-search kappa so the realized mean off-diagonal concordance matches
    target_rho (t116 `_match_kappa`). Returns (kappa, achieved_rho, at_floor). The t116
    model's shared axis has NONNEG loadings, so it can only ADD positive concordance: a
    target at/below the sampling floor (1/sqrt(P-1)) is unreachable except at kappa=0
    (no injected structure). That is a corpus property, not a search failure — we clamp
    to kappa=0 and flag at_floor=True (the caller reads it as 'signal at the noise floor
    -> rank non-identifiable at the corpus's signal level', NOT a battery bug)."""
    if target_rho <= floor:
        rho0 = float(np.mean([fast_offdiag(gen_matrix(rng, R, P, N_per_col, 0.0,
                                                       alpha, sigma0, g))[0]
                              for _ in range(int(cfg["match_ensemble"]))]))
        return 0.0, rho0, True
    lo, hi = 0.0, float(cfg["kappa_hi"])
    ens = int(cfg["match_ensemble"])
    achieved = np.nan
    for _ in range(int(cfg["match_iters"])):
        mid = 0.5 * (lo + hi)
        rhos = [fast_offdiag(gen_matrix(rng, R, P, N_per_col, mid, alpha, sigma0, g))[0]
                for _ in range(ens)]
        achieved = float(np.mean(rhos))
        if achieved < target_rho:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi), achieved, False


# ------------------------------------------------------------- calibration
def calibrate_rank(rng, R, P, N_per_col, kappa, alpha, sigma0, g, band, quantile, cfg):
    """Recovery + CI coverage + structural SD distribution for one injected rank R,
    using the SAME parallel-analysis estimator (against the shape `band`) the battery
    applies. Bootstrap-CI coverage is measured on a `coverage_subset` of replicates."""
    reps = int(cfg["replicates"])
    tol = int(cfg["recovery_tol"])
    R_hat = np.empty(reps, dtype=int)
    sd_off = np.empty(reps)
    for i in range(reps):
        X = gen_matrix(rng, R, P, N_per_col, kappa, alpha, sigma0, g)
        Z = re.standardize_columns(X)
        R_hat[i] = re.parallel_analysis(Z, 0, quantile, rng, band=band)["R"]
        sd_off[i] = fast_offdiag(X)[1]

    # bootstrap-CI coverage on a subset (fail-honest frequentist coverage of the CI rule)
    n_cov = min(int(cfg["coverage_subset"]), reps)
    n_boot = int(cfg["coverage_n_boot"])
    covered = 0
    for _ in range(n_cov):
        X = gen_matrix(rng, R, P, N_per_col, kappa, alpha, sigma0, g)
        Z = re.standardize_columns(X)
        ci = re.bootstrap_pa_rank(Z, n_boot, quantile, band, rng)
        if ci["R_ci_lo"] <= R <= ci["R_ci_hi"]:
            covered += 1
    coverage = covered / n_cov

    med = float(np.median(R_hat))
    recovery_rate = float(np.mean(np.abs(R_hat - R) <= tol))
    return {
        "injected_R": R,
        "R_hat_median": med,
        "R_hat_p05": float(np.quantile(R_hat, 0.05)),
        "R_hat_p95": float(np.quantile(R_hat, 0.95)),
        "recovery_rate": round(recovery_rate, 4),
        "ci_coverage": round(coverage, 4),
        "structural_sd_median": round(float(np.median(sd_off)), 4),
        "structural_sd_p05": round(float(np.quantile(sd_off, 0.05)), 4),
        "structural_sd_p95": round(float(np.quantile(sd_off, 0.95)), 4),
        "R_hat_distribution": {int(k): int(v) for k, v in
                               zip(*np.unique(R_hat, return_counts=True))},
    }


def run_arm(rng, arm, target_rho, P, N_per_col, K, cfg, seeds, quantile, n_perm, floor):
    """One calibration arm at a given target off-diagonal concordance. Returns per-R
    recovery/coverage/structural-SD + the arm-level verdicts (band monotonicity,
    identifiable-R recovery). The `reference` arm is the POSITIVE CONTROL (strong signal
    -> the battery MUST recover); the `matched` arm is the corpus's OPERATING POINT."""
    alpha, sigma0 = float(cfg["arm_bias"]), float(cfg["sigma0"])
    tol, cov_target = int(cfg["recovery_tol"]), float(cfg["ci_coverage_target"])
    min_rec = float(cfg["min_recovery_rate"])
    per_R = []
    for R in cfg["inject_R"]:
        g = fixed_axes(rng, P, R)
        kappa, achieved, at_floor = match_kappa(rng, R, P, N_per_col, target_rho,
                                                alpha, sigma0, g, cfg, floor)
        rep = gen_matrix(rng, R, P, N_per_col, kappa, alpha, sigma0, g)
        band = re.pa_null_band(re.standardize_columns(rep), n_perm, quantile,
                               np.random.default_rng(seeds["parallel_analysis_perm"]))
        rec = calibrate_rank(rng, R, P, N_per_col, kappa, alpha, sigma0, g, band,
                             quantile, cfg)
        identifiable = R < K
        recovered = (abs(rec["R_hat_median"] - R) <= tol) and (rec["recovery_rate"] >= min_rec)
        rec.update({
            "kappa": round(kappa, 4), "target_mean_rho": round(target_rho, 4),
            "achieved_mean_rho": round(achieved, 4),
            "signal_at_floor": bool(at_floor),
            "identifiable_at_corpus_K": bool(identifiable),
            "recovered": bool(recovered and identifiable),
            "coverage_ok": bool(rec["ci_coverage"] >= cov_target)})
        per_R.append(rec)

    ident = [r for r in per_R if r["identifiable_at_corpus_K"]]
    sds = sorted(((r["injected_R"], r["structural_sd_median"]) for r in per_R), key=lambda t: t[0])
    band_monotone = all(sds[i][1] >= sds[i + 1][1] for i in range(len(sds) - 1))
    ident_recovered = bool(ident) and all(r["recovered"] and r["coverage_ok"] for r in ident)
    max_ident_R = max((r["injected_R"] for r in ident if r["recovered"]), default=None)
    return {"target_concordance": round(target_rho, 4), "per_injected_R": per_R,
            "structural_band_monotone": bool(band_monotone),
            "identifiable_R": [r["injected_R"] for r in ident],
            "identifiable_R_recovered": ident_recovered,
            "max_identifiable_recovered_R": max_ident_R}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", type=Path, required=True)
    ap.add_argument("--in-matrix", type=Path, required=True, help="real strict matrix (geometry)")
    ap.add_argument("--in-grouping", type=Path, required=True, help="real strict grouping (K, per-col N)")
    ap.add_argument("--in-structural", type=Path, required=True, help="real strict off-diag concordance")
    ap.add_argument("--out-report", type=Path, required=True)
    ap.add_argument("--out-sentinel", type=Path, required=True)
    args = ap.parse_args()

    cfg = yaml.safe_load(args.config.read_text())
    cal = cfg["calibration_3c"]
    seeds = cfg["determinism"]["seeds"]
    quantile = cfg["rank_battery"]["parallel_analysis"]["quantile"]
    n_perm = int(cfg["rank_battery"]["parallel_analysis"]["n_perm"])

    grouping = json.loads(args.in_grouping.read_text())
    colmeta = grouping["columns"]
    struct = json.loads(args.in_structural.read_text())

    df = pd.read_csv(args.in_matrix, sep="\t", index_col=0)
    P = int(df.notna().all(axis=1).sum())            # complete-case rows the SVD sees
    N_per_col = [int(c.get("n_case_units") or 0) + int(c.get("n_control_units") or 0)
                 for c in colmeta]
    K = len(N_per_col)
    n_triggers = len({c["trigger"] for c in colmeta})
    real_rho = struct["mean"]
    if real_rho is None:
        raise SystemExit("[calibration_3c] real matrix off-diagonal concordance is undefined (K<=2)")
    floor = 1.0 / np.sqrt(max(P - 1, 1))             # concordance sampling floor 1/sqrt(P-1)

    rng = np.random.default_rng(seeds["calibration_gen"])

    # ARM 0 — estimator self-check: a CLEAN rank-R signal with NO arm bias (alpha=0) at
    # strong concordance. Separates "the estimator itself cannot resolve rank R from K
    # columns" (a structural limit of the corpus width) from "arm bias swamps the
    # sub-dominant shared axes" (a signal-to-nuisance limit). Not a gate — a diagnosis.
    cal_nobias = dict(cal); cal_nobias["arm_bias"] = 0.0
    selfcheck = run_arm(rng, "selfcheck", float(cal["reference_concordance"]),
                        P, N_per_col, K, cal_nobias, seeds, quantile, n_perm, floor)
    # ARM 1 — positive control (strong shared signal at the t116 arm-bias level): does the
    # battery RECOVER an identifiable R when signal exists at the operating bias?
    reference = run_arm(rng, "reference", float(cal["reference_concordance"]),
                        P, N_per_col, K, cal, seeds, quantile, n_perm, floor)
    # ARM 2 — corpus operating point (matched to the real off-diagonal concordance).
    matched = run_arm(rng, "matched", float(real_rho),
                      P, N_per_col, K, cal, seeds, quantile, n_perm, floor)

    estimator_correct = bool(selfcheck["identifiable_R_recovered"])
    band_ok = reference["structural_band_monotone"] or not cal["regime_band_must_match"]
    battery_validated = bool(reference["identifiable_R_recovered"] and band_ok)
    corpus_identifiable = bool(matched["identifiable_R_recovered"])
    signal_at_floor = any(r["signal_at_floor"] for r in matched["per_injected_R"])

    # grid gate: place R on the grid ONLY if the battery is validated AND the corpus can
    # identify a rank at its operating concordance (plan:0010 Stage 3c / Finding B).
    passed = bool(battery_validated and corpus_identifiable)

    def per_R_recovery_phrase(arm):
        """Precise, DATA-DRIVEN per-R recovery summary (not a coarse 'R~1-2'): recovery
        (|R_hat_med - R| <= tol) and CI coverage are reported separately, so a rank that
        is weakly recovered but under-covered is not conflated with an outright miss."""
        parts = []
        for r in arm["per_injected_R"]:
            R, med, cov = r["injected_R"], r["R_hat_median"], r["ci_coverage"]
            if not r["identifiable_at_corpus_K"]:
                parts.append(f"R={R} non-identifiable (R>=K)")
            elif r["recovered"] and r["coverage_ok"]:
                parts.append(f"R={R} recovered (R_hat_med={med:.1f}, coverage {cov:.2f})")
            elif r["recovered"]:
                parts.append(f"R={R} only weakly recovered (R_hat_med={med:.1f} within +-tol) "
                             f"but UNDER-COVERED (CI coverage {cov:.2f} < target)")
            else:
                parts.append(f"R={R} NOT recovered (R_hat_med={med:.1f})")
        return "; ".join(parts)

    # Reasons are ADDITIVE and INDEPENDENT: each failure mode that holds is recorded, so a
    # sentinel that fails for two independent reasons (estimator-width limit AND corpus at
    # the concordance floor) says so — "both independently mean no grid" (review Finding 1).
    reasons = []
    if not estimator_correct:
        reasons.append(
            "ESTIMATOR-vs-CORPUS-WIDTH LIMIT: on a CLEAN rank-R signal (no arm bias) at strong "
            f"concordance the battery does not cleanly recover the injected rank at K={K} columns "
            f"[{per_R_recovery_phrase(selfcheck)}] — a rotation-invariant SVD rank estimator "
            "cannot resolve the sub-dominant shared axes of a t116 nonneg-loading repertoire at "
            f"this corpus WIDTH. The SVD-rank -> t116-grid substitution (Finding B) is NOT "
            f"licensed at K={K}.")
    elif not battery_validated:
        reasons.append("ARM-BIAS SWAMPS SUB-DOMINANT AXES: the estimator recovers R on a clean "
                       f"signal but not at the t116 arm-bias level ({cal['arm_bias']}) "
                       f"[{per_R_recovery_phrase(reference)}] — independent per-arm bias masks all "
                       "but the leading shared axis at this K.")
    if not corpus_identifiable:
        reasons.append(
            f"CORPUS AT ITS OPERATING POINT DOES NOT IDENTIFY A RANK: the real matrix's "
            f"off-diagonal concordance ({real_rho:.3f}) is "
            + (f"at/below the sampling floor (1/sqrt(P-1)={floor:.3f}), so a t116 shared-axis "
               "structure injected at the matched concordance is negligible (kappa->0)"
               if signal_at_floor else "too low for the injected rank to be recovered")
            + f" [{per_R_recovery_phrase(matched)}] -> the corpus cannot identify a cross-PAIS "
              "rank at its signal level. This is an INDEPENDENT ground for no grid verdict (holds "
              "regardless of the estimator-width limit above) — the plan's low-power ceiling, "
              "DEMONSTRATED (review Finding A/B). No grid verdict is emitted (fail-closed).")

    if passed:
        interp = (f"Battery validated (recovers R up to {reference['max_identifiable_recovered_R']} "
                  f"at the reference concordance); corpus identifies R up to "
                  f"{matched['max_identifiable_recovered_R']} at its operating concordance. A "
                  "real-data R may be placed on the t116 grid up to that ceiling.")
    else:
        interp = "; ".join(reasons)

    report = {
        "stage": "3c", "grounding": "interpretation:0037 (t116 generative model)",
        "design": ("two-arm: a strong-signal POSITIVE CONTROL (reference_concordance) that "
                   "validates the battery, and the corpus OPERATING-POINT arm matched to the "
                   "real off-diagonal concordance — so a non-recovery is attributable to the "
                   "corpus's signal level, not a broken estimator."),
        "corpus_geometry": {"K_columns": K, "n_triggers": n_triggers, "P_complete_case": P,
                            "per_column_N": N_per_col,
                            "real_mean_offdiag_concordance": round(real_rho, 4),
                            "concordance_sampling_floor_1_over_sqrt_P_minus_1": round(floor, 4)},
        "generative_model": {"alpha_arm_bias": float(cal["arm_bias"]), "sigma0": float(cal["sigma0"]),
                             "note": ("P x K t116 model; shared = kappa * Z @ g (rank R, NONNEG "
                                      "loadings) + alpha*bias + per-column-N noise. LIMITATION: the "
                                      "t116 shared axis produces POSITIVE mean concordance only; the "
                                      "real matrix's ~0 mean with high off-diagonal SD (heterogeneous "
                                      "+/- pairs) is a finite-repertoire-like structure the caricature "
                                      "does not reproduce — see the structural co-primary.")},
        "criteria": {"recovery_tol": int(cal["recovery_tol"]),
                     "min_recovery_rate": float(cal["min_recovery_rate"]),
                     "ci_coverage_target": float(cal["ci_coverage_target"]),
                     "regime_band_must_match": bool(cal["regime_band_must_match"])},
        "selfcheck_arm_no_bias": selfcheck,
        "reference_arm_positive_control": reference,
        "matched_arm_operating_point": matched,
        "estimator_correct_clean_signal": estimator_correct,
        "battery_validated": battery_validated,
        "corpus_identifiable_at_operating_point": corpus_identifiable,
        "signal_at_floor": signal_at_floor,
        "max_identifiable_recovered_R": matched["max_identifiable_recovered_R"],
        "pass": passed,
        "fail_reasons": reasons,
        "interpretation": interp,
    }
    args.out_report.parent.mkdir(parents=True, exist_ok=True)
    args.out_report.write_text(json.dumps(report, indent=2))

    # sentinel carries the verdict; WP6 grid_placement is fail-closed on pass==true
    args.out_sentinel.write_text(json.dumps(
        {"pass": passed, "estimator_correct_clean_signal": estimator_correct,
         "battery_validated": battery_validated,
         "corpus_identifiable_at_operating_point": corpus_identifiable,
         "signal_at_floor": signal_at_floor,
         "max_identifiable_recovered_R": matched["max_identifiable_recovered_R"],
         "reasons": reasons}, indent=2))

    print(f"[calibration_3c] K={K} triggers={n_triggers} P={P} real_rho={real_rho:.4f} "
          f"floor={floor:.4f}")
    for arm_name, arm in [("SELFCHECK(a=0)", selfcheck), ("REFERENCE", reference),
                          ("MATCHED", matched)]:
        print(f"  --- {arm_name} arm (target rho={arm['target_concordance']}) ---")
        for r in arm["per_injected_R"]:
            print(f"    R={r['injected_R']} ident={r['identifiable_at_corpus_K']} "
                  f"kappa={r['kappa']} rho={r['achieved_mean_rho']} floor={r['signal_at_floor']} "
                  f"R_hat_med={r['R_hat_median']:.1f} rec={r['recovery_rate']:.2f} "
                  f"cov={r['ci_coverage']:.2f} sd={r['structural_sd_median']:.3f} "
                  f"recovered={r['recovered']}")
    print(f"[calibration_3c] battery_validated={battery_validated} "
          f"corpus_identifiable={corpus_identifiable} PASS={passed}")


if __name__ == "__main__":
    main()
