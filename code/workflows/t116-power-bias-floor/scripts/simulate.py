# science:code
# status: workflow-owned
# task_ids: [t116]
# science:end

#!/usr/bin/env python3
"""t116: Power / bias-floor simulation for the harmonized >=3-trigger shared-axis test.

Worker for code/workflows/t116-power-bias-floor/Snakefile. ALL design parameters
are read from the workflow's config.yaml (--config); this script originates
nothing. It answers the Q-A gate raised in interpretation:0001 (t035 null) and
upgrades the "plausibly estimand-aligned / worth simulating" power claim in
interpretation:0036 (t103 conditional-GO staged design):

  At achievable dense-multi-omic per-arm N (tens, MELLOW-scale) across K harmonized
  trigger arms, does the shared-latent-axis test clear the ARBITRATING bar -- separating
  hypothesis:0001's coordinated shared attractor from the question:0017 finite-repertoire
  coincidence null -- not merely the Monte-Carlo (sampling-only) bar that the t035
  within-arm permutation test used?

Deliverable: a minimum arm-count (K) x per-arm-N surface of ARBITRATING power, across a
plausibility grid of how diffuse the finite-repertoire null is.

------------------------------------------------------------------------------------
The crux (why the t035 statistic is structurally blind)

Mean cross-arm pathway concordance CANNOT tell hypothesis:0001 apart from a
strength-matched question:0017 null: both are "a shared axis." A world with a genuine
coordinated attractor and a world where every trigger pair happens to share a slice of
the same finite sickness repertoire can produce IDENTICAL mean concordance. No per-arm N
and no arm count fixes a statistic that is blind by construction. (t035's permutation test
is exactly this statistic; it is why interp-0001 records the 2-cohort result as
non-arbitrating rather than as evidence against h0001.)

What DOES discriminate is STRUCTURE across arms:

  * h0001 (coordinated attractor): ONE global axis runs through ALL arms -> every
    trigger-pair is concordant to the SAME degree -> the K x K concordance matrix has
    HOMOGENEOUS off-diagonals (low off-diagonal SD; rank-1-plus-diagonal).
  * q0017 (finite-repertoire coincidence): different arm-pairs overlap on DIFFERENT
    generic axes -> pairwise concordances are HETEROGENEOUS (high off-diagonal SD; the
    shared structure is diffuse / higher-rank), even at the SAME mean concordance.

The discriminating statistic is therefore the SD of the off-diagonal pairwise
concordances (a single-shared-axis / homogeneity test). It is undefined for K = 2 (one
off-diagonal -> no variance) -> a 2-arm design is STRUCTURALLY non-arbitrating at ANY N.
This is the quantitative form of interp-0001's observation that "the effective
cross-trigger unit is the cohort, and there are only two."

Generative model (per pathway-set NES-like value; one length-P vector per arm k):

    x_k = shared_k + alpha * a_k + e_k
      shared_k : H1 -> lambda * s          (single global axis, all arms; homogeneous)
                 H0 -> kappa * sum_r Z_kr g_r  (R generic repertoire axes, nonneg random
                                                loadings Z_kr; diffuse; heterogeneous)
      alpha*a_k: arm-specific systematic bias (random direction; does NOT shrink with N)
      e_k      : within-arm sampling noise, sd = sigma0 / sqrt(N) (shrinks with N)

H0's kappa is CALIBRATED per (K, N) so its realized mean pairwise concordance MATCHES H1's
(the adversarial null: same average overlap, different rank). Because they are matched, the
mean-concordance test has ~5% power (non-arbitrating) BY CONSTRUCTION -- reported to show
the t035 statistic's blindness -- and all discriminating power comes from the off-diagonal
homogeneity statistic.

Two decision bars:
  * Monte-Carlo bar : reject the SAMPLING-ONLY null (no shared structure). Blind to the
                      finite-repertoire alternative; what a permutation test sees.
  * Arbitrating bar : classify H1 (homogeneous, single attractor) vs the concordance-
                      MATCHED q0017 finite-repertoire null, controlling the finite-
                      repertoire false-"it's-a-shared-attractor" rate at 5%.

    arbitrating_power(K,N) = P( offdiag_SD(H1) < q05( offdiag_SD | q0017 null ) )

Concordance-noise calibration (parameter-free): with P=50 Hallmark sets the sampling-null
SD of a single Spearman concordance ~= 1/sqrt(P-1) ~= 0.143, matching the t035 observed
rho spread (six cells, rho in [-0.65,-0.32], SD ~ 0.12-0.15) with no tuning.

Run (via the workflow):
    uv run --frozen snakemake -s code/workflows/t116-power-bias-floor/Snakefile -c1 all
Standalone (config required; hard-codes nothing):
    uv run --frozen python code/workflows/t116-power-bias-floor/scripts/simulate.py \
        --config code/workflows/t116-power-bias-floor/config.yaml \
        --out results/t116-power-bias-floor-sim
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import yaml

# --- design parameters: RESOLVED FROM config.yaml at runtime (see main) -------
# These module names are the single set of knobs the compute functions read.
# main() binds them from the workflow config; the script originates no value.
SEED: int = 0
P_HALLMARK: int = 0
LAM: float = 0.0
ALPHA: float = 0.0
SIGMA0: float = 0.0
K_GRID: list[int] = []
N_GRID: list[int] = []
M: int = 0
POWER_TARGET: float = 0.0
MATCH_TOL: float = 0.0

# kappa search bracket for the q0017 concordance-match (see _match_kappa). Named
# so the caller can detect a boundary pin (a failed match) — fail early, never
# consume a silently mis-matched null.
KAPPA_LO: float = 0.0
KAPPA_HI: float = 5.0


def _fixed_axes(rng: np.random.Generator, p: int, r: int):
    """One global axis s and R repertoire axes g (each mean 0, sd 1; mutually orthogonalized)."""
    A = rng.standard_normal((1 + r, p))
    A = A - A.mean(axis=1, keepdims=True)
    # Gram-Schmidt orthogonalization
    for i in range(A.shape[0]):
        for j in range(i):
            A[i] = A[i] - (A[i] @ A[j]) / (A[j] @ A[j]) * A[j]
        A[i] = A[i] / A[i].std()
    return A[0], A[1:]  # s (P,), g (R,P)


def _ranks(x: np.ndarray) -> np.ndarray:
    return np.argsort(np.argsort(x, axis=-1), axis=-1).astype(np.float64)


def _concord_matrix(x: np.ndarray) -> np.ndarray:
    """Spearman concordance matrices, one per replicate. x: (M,K,P) -> C: (M,K,K)."""
    r = _ranks(x)
    r = r - r.mean(axis=-1, keepdims=True)
    r = r / np.linalg.norm(r, axis=-1, keepdims=True)
    return np.einsum("mkp,mjp->mkj", r, r)


def _offdiag_mean_sd(C: np.ndarray, K: int):
    """Mean and SD of off-diagonal entries, per replicate."""
    iu = np.triu_indices(K, k=1)
    off = C[:, iu[0], iu[1]]  # (M, n_pairs)
    return off.mean(axis=1), (off.std(axis=1) if K > 2 else np.zeros(off.shape[0]))


def _gen(rng, kind, K, N, P, s, g, kappa, M):
    a = rng.standard_normal((M, K, P))
    a = a - a.mean(axis=-1, keepdims=True)
    a = a / a.std(axis=-1, keepdims=True)
    e = rng.standard_normal((M, K, P)) * (SIGMA0 / np.sqrt(N))
    if kind == "H1":
        shared = LAM * s  # broadcast (P,) -> (M,K,P)
    elif kind == "H0":
        R = g.shape[0]
        Z = np.abs(rng.standard_normal((M, K, R)))  # nonneg repertoire loadings
        shared = kappa * np.einsum("mkr,rp->mkp", Z, g)
    else:  # sampling-only null (no shared structure)
        shared = 0.0
    return shared + ALPHA * a + e


def _match_kappa(rng, K, N, P, s, g, target_rho, M_cal=2500):
    """Binary-search kappa so H0's realized mean concordance matches target_rho."""
    lo, hi = KAPPA_LO, KAPPA_HI
    for _ in range(16):
        mid = 0.5 * (lo + hi)
        C = _concord_matrix(_gen(rng, "H0", K, N, P, s, g, mid, M_cal))
        mrho, _ = _offdiag_mean_sd(C, K)
        if mrho.mean() < target_rho:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def _assert_matched(kappa, target, achieved, ctx):
    """Fail EARLY if the q0017 finite-repertoire null is not concordance-matched to
    H1 (pipeline-review finding #2). A binary search pinned to the KAPPA_HI boundary
    returns an unmatched null, which silently invalidates every power number for the
    cell. Explicit > defensive: raise, never emit a mis-matched surface that reads as
    'matched'. Returns the absolute match error for per-cell recording."""
    err = abs(float(achieved) - float(target))
    pinned = kappa >= KAPPA_HI - 1e-3
    if err > MATCH_TOL or pinned:
        raise RuntimeError(
            f"q0017 concordance-match FAILED at {ctx}: target mean rho {target:.4f}, "
            f"achieved {float(achieved):.4f} (|err|={err:.4f}, tol={MATCH_TOL}); "
            f"kappa={kappa:.4f}"
            + (f" pinned at the [{KAPPA_LO},{KAPPA_HI}] search boundary — widen the "
               f"bracket." if pinned else "")
            + " The null is not concordance-matched; power numbers would be invalid.")
    return round(err, 4)


def run_surface(rng, regime, k_grid, n_grid, P, M):
    s, g = _fixed_axes(rng, P, regime["R"])
    cells = []
    for K in k_grid:
        for N in n_grid:
            # H1: single global attractor axis
            C_h1 = _concord_matrix(_gen(rng, "H1", K, N, P, s, g, 0.0, M))
            mrho_h1, sd_h1 = _offdiag_mean_sd(C_h1, K)
            target = float(mrho_h1.mean())

            # Sampling-only null (for the Monte-Carlo bar)
            C_samp = _concord_matrix(_gen(rng, "H0", K, N, P, s, g, 0.0, M))  # kappa 0 -> no shared
            mrho_samp, _ = _offdiag_mean_sd(C_samp, K)
            q95_mc = float(np.quantile(mrho_samp, 0.95))
            power_mc = float(np.mean(mrho_h1 > q95_mc))  # mean-concordance vs sampling null

            # q0017 finite-repertoire null, concordance-MATCHED to H1
            kappa = _match_kappa(rng, K, N, P, s, g, target)
            C_h0 = _concord_matrix(_gen(rng, "H0", K, N, P, s, g, kappa, M))
            mrho_h0, sd_h0 = _offdiag_mean_sd(C_h0, K)
            match_err = _assert_matched(
                kappa, target, mrho_h0.mean(),
                f"K={K},N={N},P={P},R={regime['R']} ({regime['key']})")

            if K < 3:
                # Structural test undefined (one off-diagonal); non-arbitrating by construction.
                power_arb = 0.0
                power_meanconc_vs_q0017 = float(np.mean(
                    mrho_h1 > np.quantile(mrho_h0, 0.95)))
                q_crit = None
            else:
                # Arbitrating: classify H1 (homogeneous) vs q0017 (heterogeneous) off-diag SD,
                # controlling the finite-repertoire false-positive at 5%.
                q_crit = float(np.quantile(sd_h0, 0.05))
                power_arb = float(np.mean(sd_h1 < q_crit))
                power_meanconc_vs_q0017 = float(np.mean(
                    mrho_h1 > np.quantile(mrho_h0, 0.95)))

            cells.append({
                "K": K, "N": N,
                "power_arbitrating_structural": round(power_arb, 4),
                "arbitrating": (K >= 3) and (power_arb >= POWER_TARGET),
                "power_meanconc_vs_sampling": round(power_mc, 4),   # Monte-Carlo bar
                "power_meanconc_vs_q0017": round(power_meanconc_vs_q0017, 4),  # ~0.05: blind
                "matched_mean_rho": round(target, 4),
                "matched_mean_rho_achieved": round(float(mrho_h0.mean()), 4),
                "match_abs_err": match_err,   # asserted < MATCH_TOL (fail-early check)
                "offdiag_sd_H1": round(float(sd_h1.mean()), 4),
                "offdiag_sd_q0017": round(float(sd_h0.mean()), 4),
                "q05_offdiag_sd_q0017": (round(q_crit, 4) if q_crit is not None else None),
            })
    return cells


def p_sensitivity(rng, k_grid, N, P_grid, R, M):
    """How the pathway-universe size P (Hallmark 50 -> Reactome/GO-BP ~1000) moves the
    minimum arbitrating arm count. Larger P lowers the concordance sampling floor
    (~1/sqrt(P-1)), sharpening the structural homogeneity test."""
    rows = []
    for P in P_grid:
        s, g = _fixed_axes(rng, P, R)
        for K in k_grid:
            C_h1 = _concord_matrix(_gen(rng, "H1", K, N, P, s, g, 0.0, M))
            mrho_h1, sd_h1 = _offdiag_mean_sd(C_h1, K)
            if K < 3:
                rows.append({"P": P, "K": K, "N": N, "power_arbitrating_structural": 0.0})
                continue
            target = float(mrho_h1.mean())
            kappa = _match_kappa(rng, K, N, P, s, g, target)
            C_h0 = _concord_matrix(_gen(rng, "H0", K, N, P, s, g, kappa, M))
            mrho_h0, sd_h0 = _offdiag_mean_sd(C_h0, K)
            _assert_matched(kappa, target, mrho_h0.mean(),
                            f"P-sensitivity P={P},K={K},N={N},R={R}")
            power = float(np.mean(sd_h1 < np.quantile(sd_h0, 0.05)))
            rows.append({"P": P, "K": K, "N": N,
                         "power_arbitrating_structural": round(power, 4),
                         "sampling_floor_1_over_sqrt_P_minus_1": round(1/np.sqrt(P-1), 4)})
    # minimum arbitrating K per P
    min_k = {}
    for P in P_grid:
        ok = [r for r in rows if r["P"] == P and r["K"] >= 3
              and r["power_arbitrating_structural"] >= POWER_TARGET]
        min_k[P] = (min(r["K"] for r in ok) if ok else None)
    return {"R": R, "N": N, "P_grid": P_grid, "min_arbitrating_K_by_P": min_k, "rows": rows}


def shared_bias_probe(rng, R, K, N, P, beta_grid, M):
    """False-arbitration rate under a SHARED / correlated arm-bias world (pipeline-
    review finding #1). The main surface models arm bias as INDEPENDENT per arm --
    the error harmonization REDUCES. But one harmonized protocol can INTRODUCE bias
    correlated ACROSS arms (a common platform / pipeline / reference-set axis on every
    arm). Such a shared axis HOMOGENIZES the off-diagonal concordances -> mimics
    hypothesis:0001 (one shared attractor). The structural test's null is the
    HETEROGENEOUS question:0017 repertoire; it has NO protection against a homogeneous
    shared artifact.

    Model (NO genuine attractor; LAM axis absent) — the shared artifact is applied
    IDENTICALLY to every arm, exactly as H1 applies its genuine attractor axis
    (shared = LAM * s). This is the point: to this SD-of-off-diagonals statistic a
    perfectly shared artifact is STRUCTURALLY IDENTICAL to a genuine attractor, so the
    test cannot separate them.
        x_k = beta * c + alpha * a_k + e_k
      c        : one shared artifact axis, IDENTICAL on every arm (fixed direction+loading)
      alpha*a_k, e_k : the usual independent arm bias + sampling noise
    beta is swept as a fraction of the true signal LAM; at beta=LAM the artifact matches
    the true attractor's strength (false rate should approach the true-attractor power).
    beta=0 is the pure-independent-bias baseline (no shared axis). Reported at a cell that
    DOES arbitrate against q0017 (the test's best case), so a rising false rate is a genuine
    vulnerability, not a weak-cell artifact.

    false_arbitration_rate = P( offdiag_SD(shared-bias world) < q05(offdiag_SD | q0017) )
    """
    s, g = _fixed_axes(rng, P, R)
    # Reconstruct this cell's q0017 arbitrating threshold (same construction as the surface).
    C_h1 = _concord_matrix(_gen(rng, "H1", K, N, P, s, g, 0.0, M))
    mrho_h1, sd_h1 = _offdiag_mean_sd(C_h1, K)
    target = float(mrho_h1.mean())
    kappa = _match_kappa(rng, K, N, P, s, g, target)
    C_h0 = _concord_matrix(_gen(rng, "H0", K, N, P, s, g, kappa, M))
    mrho_h0, sd_h0 = _offdiag_mean_sd(C_h0, K)
    _assert_matched(kappa, target, mrho_h0.mean(), f"shared-bias probe cell K={K},N={N},P={P},R={R}")
    q_crit = float(np.quantile(sd_h0, 0.05))
    true_attractor_power = float(np.mean(sd_h1 < q_crit))  # H1's arbitrating power here

    # one shared artifact axis, standardized (fresh; direction-agnostic — the test only sees SD)
    c = rng.standard_normal(P)
    c = (c - c.mean()) / c.std()
    rows = []
    for frac in beta_grid:
        beta = frac * LAM
        a = rng.standard_normal((M, K, P))
        a = a - a.mean(axis=-1, keepdims=True)
        a = a / a.std(axis=-1, keepdims=True)
        e = rng.standard_normal((M, K, P)) * (SIGMA0 / np.sqrt(N))
        x = beta * c + ALPHA * a + e          # IDENTICAL shared axis on every arm; NO attractor
        _, sd_sb = _offdiag_mean_sd(_concord_matrix(x), K)
        rows.append({
            "beta_frac_of_signal": frac,
            "beta": round(beta, 4),
            "offdiag_sd_shared_bias": round(float(sd_sb.mean()), 4),
            "false_arbitration_rate": round(float(np.mean(sd_sb < q_crit)), 4),
        })
    return {
        "R": R, "K": K, "N": N, "P": P,
        "q05_offdiag_sd_q0017": round(q_crit, 4),
        "true_attractor_arbitrating_power": round(true_attractor_power, 4),
        "note": ("false_arbitration_rate = P(shared-bias-world off-diagonal concordance SD < the "
                 "q0017 5% arbitrating threshold); beta scaled as a fraction of the true attractor "
                 "loading LAM. beta=0 recovers the test's proper size (independent bias only). A "
                 "rising rate shows harmonization must control CORRELATED bias, not just its magnitude."),
        "rows": rows,
    }


def min_arbitrating(cells):
    ok = [c for c in cells if c["arbitrating"]]
    if not ok:
        return None
    ok.sort(key=lambda c: (c["K"], c["N"]))
    return {"K": ok[0]["K"], "N": ok[0]["N"],
            "power_arbitrating_structural": ok[0]["power_arbitrating_structural"]}


def calibration_check(rng, P, M):
    s, g = _fixed_axes(rng, P, 2)
    C = _concord_matrix(_gen(rng, "H0", 2, 8, P, s, g, 0.0, M))  # sampling-only
    mrho, _ = _offdiag_mean_sd(C, 2)
    return {
        "P": P, "K": 2, "N": 8,
        "sd_rho_sampling_null": round(float(mrho.std()), 4),
        "analytic_1_over_sqrt_P_minus_1": round(1.0 / np.sqrt(P - 1), 4),
        "t035_observed_rho_range": [-0.6535, -0.3209],
        "t035_observed_rho_sd_across_6_cells": 0.124,
    }


def _git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:  # noqa: BLE001
        return "unknown"


def _sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _emit_datapackage(outdir: Path, resources_meta, config_source: str):
    """Frictionless-style datapackage.json for manifest parity with the rest of
    results/ (pipeline-review finding #3). Lists the run's output resources with
    sizes + sha256, and cross-references the deliverable interpretation, workflow,
    and config as sources. Regenerable; results/* is gitignored."""
    resources = []
    for name, rel, mediatype, group in resources_meta:
        p = outdir / rel
        resources.append({
            "name": name, "path": str(p), "title": str(p),
            "bytes": p.stat().st_size, "hash": _sha256(p),
            "mediatype": mediatype, "group": group,
        })
    pkg_id = "sha256:" + hashlib.sha256(
        "".join(sorted(r["hash"] for r in resources)).encode()).hexdigest()
    pkg = {
        "name": "t116-power-bias-floor-sim-results",
        "title": "t116 power/bias-floor shared-axis simulation result bundle",
        "description": ("Deterministic manifest for the t116 design-power simulation outputs "
                        "(ARBITRATING-power surface, human tables, shared-bias probe, run "
                        "provenance). Regenerable; results/* is gitignored."),
        "profile": "data-package",
        "id": pkg_id,
        "sources": [
            {"title": "interpretation:0037-t116-power-bias-floor-shared-axis-sim",
             "path": "entities/interpretations/0037-t116-power-bias-floor-shared-axis-sim.md"},
            {"title": "workflow", "path": "code/workflows/t116-power-bias-floor/Snakefile"},
            {"title": "config", "path": config_source},
        ],
        "resources": resources,
    }
    (outdir / "datapackage.json").write_text(json.dumps(pkg, indent=2))
    return pkg


def surface_markdown(regime, cells, mn):
    lines = [f"### {regime['label']}  (`{regime['key']}`)", "",
             f"Finite-repertoire null spread over R = {regime['R']} generic axes. "
             f"{regime['note']}", ""]
    if mn:
        lines.append(f"**Minimum arbitrating footprint:** K = {mn['K']} arms x N = "
                     f"{mn['N']}/arm (structural arbitrating power "
                     f"{mn['power_arbitrating_structural']:.2f}).")
    else:
        lines.append(f"**No (K, N) in the grid reaches structural arbitrating power >= "
                     f"{POWER_TARGET:.2f}.**")
    lines += ["", "Structural arbitrating power (mean-concordance-vs-sampling / "
              "Monte-Carlo power in parentheses); **bold** = arbitrating "
              f">= {POWER_TARGET:.2f}:", ""]
    ns = sorted({c["N"] for c in cells})
    ks = sorted({c["K"] for c in cells})
    lines += ["| K \\ N/arm | " + " | ".join(str(n) for n in ns) + " |",
              "|" + "---|" * (len(ns) + 1)]
    grid = {(c["K"], c["N"]): c for c in cells}
    for K in ks:
        row = [f"| **{K}**"]
        for N in ns:
            c = grid[(K, N)]
            cell = (f"{c['power_arbitrating_structural']:.2f} "
                    f"({c['power_meanconc_vs_sampling']:.2f})")
            if c["arbitrating"]:
                cell = f"**{cell}**"
            row.append(cell)
        lines.append(" | ".join(row) + " |")
    lines.append("")
    return "\n".join(lines)


def _load_config(path: Path) -> dict:
    """Bind the module-level design knobs from config.yaml. The script hard-codes
    no design value; every knob originates here (fail early on a missing key)."""
    cfg = yaml.safe_load(path.read_text())
    global SEED, P_HALLMARK, LAM, ALPHA, SIGMA0, K_GRID, N_GRID, M, POWER_TARGET, MATCH_TOL
    det, mod, grid = cfg["determinism"], cfg["model"], cfg["grid"]
    SEED = int(det["seed"])
    M = int(det["replicates"])
    POWER_TARGET = float(det["power_target"])
    MATCH_TOL = float(det["match_tol"])
    P_HALLMARK = int(mod["p_hallmark"])
    LAM = float(mod["lam"])
    ALPHA = float(mod["alpha"])
    SIGMA0 = float(mod["sigma0"])
    K_GRID = list(grid["k_grid"])
    N_GRID = list(grid["n_grid"])
    return cfg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", type=Path, required=True,
                    help="Workflow config.yaml (single source of design parameters).")
    ap.add_argument("--out", type=Path, required=True,
                    help="Output directory (results/*, gitignored).")
    args = ap.parse_args()

    cfg = _load_config(args.config)
    ps_cfg = cfg["p_sensitivity"]
    regimes = cfg["regimes"]
    args.out.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(SEED)
    calib = calibration_check(rng, P_HALLMARK, M)

    surfaces = []
    for regime in regimes:
        cells = run_surface(rng, regime, K_GRID, N_GRID, P_HALLMARK, M)
        surfaces.append({"regime": regime, "min_arbitrating": min_arbitrating(cells),
                         "cells": cells})

    # Pathway-universe (P) sensitivity: does a higher-resolution feature space lower the
    # arm-count threshold? Run against the moderate-rank null at fixed N.
    psens = p_sensitivity(rng, K_GRID, int(ps_cfg["N"]), list(ps_cfg["p_grid"]),
                          R=int(ps_cfg["R"]), M=min(int(ps_cfg["replicates"]), M))

    # Correlated / shared arm-bias confound (pipeline-review finding #1): does the
    # arbitrating test false-positive on a homogeneous shared artifact? Runs AFTER the
    # surface + p_sensitivity so those draws (and their numbers) are unchanged.
    sb_cfg = cfg["shared_bias_probe"]
    shared_bias = shared_bias_probe(
        rng, R=int(sb_cfg["R"]), K=int(sb_cfg["K"]), N=int(sb_cfg["N"]),
        P=P_HALLMARK, beta_grid=list(sb_cfg["beta_grid"]),
        M=min(int(sb_cfg["replicates"]), M))

    out = {
        "determinism": {"seed": SEED, "rng": "PCG64 (numpy default_rng)", "replicates": M},
        "params": {"P_sets": P_HALLMARK, "lam": LAM, "alpha": ALPHA, "sigma0": SIGMA0,
                   "K_grid": K_GRID, "N_grid": N_GRID, "power_target": POWER_TARGET,
                   "match_tol": MATCH_TOL},
        "statistic": "off-diagonal pairwise-concordance SD (single-shared-axis homogeneity test)",
        "config_source": str(args.config),
        "calibration": calib,
        "surfaces": surfaces,
        "p_sensitivity": psens,
        "shared_bias_probe": shared_bias,
        "provenance": {"git_commit": _git_commit(),
                       "created_utc": datetime.now(timezone.utc).isoformat()},
    }
    (args.out / "surface.json").write_text(json.dumps(out, indent=2))

    md = ["# t116 -- Power / bias-floor surface for the harmonized >=3-trigger shared-axis test",
          "",
          "**Arbitrating** = the shared-axis test separates hypothesis:0001 (one coordinated "
          "attractor axis through all arms) from the concordance-MATCHED question:0017 "
          "finite-repertoire null, via off-diagonal concordance homogeneity. **Monte-Carlo** "
          "(parenthetical) = mean concordance beats the sampling-only null -- blind to q0017.",
          "",
          "Mean-concordance power against the matched q0017 null is ~0.05 at every cell (the "
          "t035 statistic is non-arbitrating by construction); all discrimination comes from "
          "the structural homogeneity statistic, which is undefined at K=2.",
          "",
          "## Calibration (parameter-free)", "",
          f"Sampling-null concordance SD at P={calib['P']}, K=2, N=8: "
          f"**{calib['sd_rho_sampling_null']}** vs analytic 1/sqrt(P-1) = "
          f"{calib['analytic_1_over_sqrt_P_minus_1']}; consistent with the t035 observed rho "
          f"spread (SD ~ {calib['t035_observed_rho_sd_across_6_cells']}).",
          "", "## Surfaces", ""]
    for surf in surfaces:
        md.append(surface_markdown(surf["regime"], surf["cells"], surf["min_arbitrating"]))
    md += ["## Pathway-universe (P) sensitivity",
           "",
           "Minimum arbitrating arm count K vs feature-space size P (moderate-rank R=4 null, "
           "N=30/arm). A higher-resolution pathway universe lowers the concordance sampling "
           "floor (~1/sqrt(P-1)) and sharpens the structural test:",
           "",
           "| P (sets) | sampling floor | min arbitrating K |",
           "|---|---|---|"]
    for P in psens["P_grid"]:
        mk = psens["min_arbitrating_K_by_P"][P]
        md.append(f"| {P} | {1/np.sqrt(P-1):.3f} | {mk if mk else '> 6 (none)'} |")
    sb = shared_bias
    md += ["",
           "## Correlated / shared arm-bias confound",
           "",
           f"The main surface models arm bias as **independent** per arm. This probe adds one "
           f"**shared** artifact axis to every arm (a common platform/pipeline/reference-set "
           f"effect — what a single harmonized protocol can *introduce*) with **no** genuine "
           f"attractor, at a cell that DOES arbitrate against the q0017 null (R={sb['R']}, "
           f"K={sb['K']}, N={sb['N']}, P={sb['P']}; true-attractor arbitrating power "
           f"{sb['true_attractor_arbitrating_power']:.2f}). A shared axis homogenizes the "
           f"off-diagonals and **mimics a single attractor**, so the structural test — whose "
           f"null is only the *heterogeneous* repertoire — false-positives:",
           "",
           "| shared-bias beta (frac of signal) | off-diag SD | false-arbitration rate |",
           "|---|---|---|"]
    for r in sb["rows"]:
        md.append(f"| {r['beta_frac_of_signal']:.2f} | {r['offdiag_sd_shared_bias']:.4f} | "
                  f"{r['false_arbitration_rate']:.2f} |")
    md += ["",
           "beta=0 is the pure-independent-bias baseline; as the shared artifact grows toward the "
           "true signal strength (beta -> LAM) the false-arbitration rate climbs toward the "
           f"true-attractor arbitrating power ({sb['true_attractor_arbitrating_power']:.2f}) — i.e. a "
           "perfectly shared artifact is, to this SD statistic, **indistinguishable from a genuine "
           "attractor**. This is review finding #1: **harmonization must control *correlated* bias, "
           "not just its magnitude** — full-recovery-control contrasts and shared-artifact "
           "diagnostics are load-bearing for question:0050, not optional.", ""]
    (args.out / "surface.md").write_text("\n".join(md))

    meta = {
        "task": "task:t116", "answers": ["interpretation:0001 (Q-A)", "interpretation:0036"],
        "workflow": "code/workflows/t116-power-bias-floor/Snakefile",
        "config_source": str(args.config),
        "git_commit": out["provenance"]["git_commit"],
        "created_utc": out["provenance"]["created_utc"],
        "determinism": out["determinism"], "params": out["params"],
        "statistic": out["statistic"],
        "min_arbitrating_by_regime": {s["regime"]["key"]: s["min_arbitrating"] for s in surfaces},
        "p_sensitivity_min_K": psens["min_arbitrating_K_by_P"],
        "shared_bias_false_arbitration": {r["beta_frac_of_signal"]: r["false_arbitration_rate"]
                                          for r in shared_bias["rows"]},
        "review_findings_resolved": [
            "#1 correlated/shared arm-bias regime (shared_bias_probe)",
            "#2 kappa-match convergence assertion (_assert_matched, fail-early)",
            "#3 datapackage.json manifest",
        ],
    }
    (args.out / "run_metadata.json").write_text(json.dumps(meta, indent=2))

    # Manifest (finding #3): emit AFTER the three outputs exist so hashes are final.
    _emit_datapackage(
        args.out,
        [("surface-json", "surface.json", "application/json", "terminal"),
         ("surface-md", "surface.md", "text/markdown", "terminal"),
         ("run-metadata-json", "run_metadata.json", "application/json", "provenance")],
        str(args.config))

    print("calibration:", json.dumps(calib))
    for s in surfaces:
        print(f"{s['regime']['key']:>16}: min_arbitrating = {s['min_arbitrating']}")
    print("p_sensitivity min K by P:", psens["min_arbitrating_K_by_P"])
    print("shared-bias false-arbitration by beta:",
          {r["beta_frac_of_signal"]: r["false_arbitration_rate"] for r in shared_bias["rows"]})
    print(f"wrote -> {args.out}/surface.json, surface.md, run_metadata.json, datapackage.json")


if __name__ == "__main__":
    main()
