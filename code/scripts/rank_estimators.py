# science:code
# status: workflow-owned
# task_ids: [t117]
# science:end

#!/usr/bin/env python3
"""rank_estimators.py — shared rotation-invariant effective-rank primitives (task:t117, WP3).

SINGLE source of the rank-estimation battery used by BOTH the real-data estimator
(`rank_battery.py`) and the t116-generative calibration (`calibration_3c.py`). They
MUST share these functions verbatim: Stage-3c (plan:0010 review Finding B) calibrates
the battery against a known generative rank, so the calibrated procedure and the
applied procedure have to be the identical code path — importing the same module is
what guarantees that (composition, not a re-implementation that could drift).

The analysis object is a pathway x contrast matrix X (rows = gene sets, cols =
case-vs-control contrasts). "Effective rank R" = the number of significant directions
of the SHARED column subspace — the contrasts covarying across pathways. Estimators
operate on the column-standardized complete-case matrix Z (each contrast centered to
mean 0, scaled to unit SD), so R is the rank of the contrast-correlation structure and
no single high-variance contrast dominates. Column-centering is deliberate: it does NOT
remove a shared cross-contrast axis (that axis lives in the covariance among columns),
only the per-contrast grand mean.

Estimators (all rotation-invariant — R must not depend on a factor rotation):
  * parallel_analysis  — Horn: observed singular values vs a per-column-permuted null.
  * bicv_svd           — Owen-Perry bi-cross-validation: rank minimizing held-out error.
  * split_half         — right-singular-subspace principal-angle agreement across random
                         halves of the pathway rows (subspace-stability -> R).
  * bootstrap_pa_rank  — row-bootstrap distribution of the parallel-analysis R (the CI).

Structural co-primary (plan:0010 Finding B; this is the statistic interpretation:0037
actually characterized, NOT the SVD rank):
  * spearman_offdiag   — SD (and mean) of the off-diagonal pairwise Spearman concordances
                         between contrast columns. Undefined for K<=2 (one off-diagonal).

No workflow I/O here — pure numeric functions taking a numpy matrix + an RNG.
"""
from __future__ import annotations

import numpy as np
from scipy.linalg import subspace_angles
from scipy.stats import spearmanr


# ---------------------------------------------------------------- preprocessing
def complete_case(X: np.ndarray):
    """Drop pathway rows carrying any NaN (a gene set not testable in some contrast).
    Returns (X_cc, n_dropped, kept_mask). SVD needs a dense matrix; the pairwise
    structural statistic uses its own pairwise-complete rule instead."""
    mask = ~np.isnan(X).any(axis=1)
    return X[mask], int((~mask).sum()), mask


def standardize_columns(X: np.ndarray) -> np.ndarray:
    """Center each contrast to mean 0 and scale to unit SD (correlation basis).
    A zero-variance column (degenerate contrast) is left centered (scale 1) rather
    than producing inf — fail-loud is the caller's job via the estimable checks."""
    mu = X.mean(axis=0, keepdims=True)
    sd = X.std(axis=0, ddof=1, keepdims=True)
    sd = np.where(sd < 1e-12, 1.0, sd)
    return (X - mu) / sd


def _singular_values(Z: np.ndarray) -> np.ndarray:
    """Economy singular values of Z (length min(P,K) = K for our tall matrices)."""
    return np.linalg.svd(Z, compute_uv=False)


# ---------------------------------------------------------- parallel analysis
def parallel_analysis(Z: np.ndarray, n_perm: int, quantile: float,
                      rng: np.random.Generator, band: np.ndarray | None = None):
    """Horn parallel analysis. Observed singular values vs a null that permutes each
    column independently (destroys cross-contrast structure, PRESERVES each contrast's
    marginal NES distribution). R = # observed SVs exceeding the null `quantile` band.

    `band` (precomputed null quantiles, length K) lets the caller reuse a shape-null
    across many observed draws (calibration): if given, no permutation is run here.
    Otherwise the null is computed from `n_perm` per-column permutations of Z itself
    (the real-data path)."""
    sv_obs = _singular_values(Z)
    K = Z.shape[1]
    if band is None:
        null = np.empty((n_perm, K))
        for i in range(n_perm):
            Zp = rng.permuted(Z, axis=0)      # each column shuffled independently
            null[i] = _singular_values(Zp)
        band = np.quantile(null, quantile, axis=0)
    passed = sv_obs > band
    # retained components are the leading contiguous run above the band (a trailing
    # SV crossing the band by chance does not add a component — standard Horn reading)
    R = 0
    for p in passed:
        if p:
            R += 1
        else:
            break
    return {
        "R": int(R),
        "singular_values": [float(v) for v in sv_obs],
        "null_band": [float(v) for v in band],
        "passed": [bool(v) for v in passed],
    }


def pa_null_band(Z: np.ndarray, n_perm: int, quantile: float,
                 rng: np.random.Generator) -> np.ndarray:
    """The per-column-permuted null singular-value quantile band for a matrix of Z's
    shape+marginals (length K). Reused across calibration replicates: the null depends
    on the shape and column marginals, not on the particular replicate's shared
    structure, so computing it once per shape is a faithful, standard shortcut."""
    K = Z.shape[1]
    null = np.empty((n_perm, K))
    for i in range(n_perm):
        null[i] = _singular_values(rng.permuted(Z, axis=0))
    return np.quantile(null, quantile, axis=0)


# ------------------------------------------------------ bi-cross-validation SVD
def bicv_svd(Z: np.ndarray, row_folds: int, col_folds: int,
             rng: np.random.Generator, max_rank: int | None = None):
    """Owen & Perry (2009) bi-cross-validation. Partition rows x cols into a
    row_folds x col_folds grid; for each held-out block A predict it from the three
    complementary blocks (A_hat = B D+_r C) using a rank-r SVD of the held-in corner
    D. R = the candidate rank minimizing total held-out squared error. Rotation-
    invariant and does not need a null. r=0 (no structure) competes so a matrix with
    no reproducible low-rank signal returns R=0."""
    P, K = Z.shape
    r_perm = rng.permutation(P)
    c_perm = rng.permutation(K)
    row_groups = np.array_split(r_perm, row_folds)
    col_groups = np.array_split(c_perm, col_folds)
    # feasible rank is bounded by the smallest held-in corner across folds
    min_D_cols = min(K - len(cg) for cg in col_groups)
    min_D_rows = min(P - len(rg) for rg in row_groups)
    feasible = max(0, min(min_D_cols, min_D_rows))
    top = feasible if max_rank is None else min(max_rank, feasible)
    ranks = list(range(0, top + 1))
    err = {r: 0.0 for r in ranks}
    for rg in row_groups:
        rmask = np.zeros(P, bool); rmask[rg] = True
        for cg in col_groups:
            cmask = np.zeros(K, bool); cmask[cg] = True
            A = Z[np.ix_(rmask, cmask)]
            B = Z[np.ix_(rmask, ~cmask)]
            C = Z[np.ix_(~rmask, cmask)]
            D = Z[np.ix_(~rmask, ~cmask)]
            U, s, Vt = np.linalg.svd(D, full_matrices=False)
            for r in ranks:
                if r == 0:
                    A_hat = np.zeros_like(A)
                else:
                    rr = min(r, len(s))
                    D_pinv = Vt[:rr].T @ np.diag(1.0 / s[:rr]) @ U[:, :rr].T
                    A_hat = B @ D_pinv @ C
                err[r] += float(np.sum((A - A_hat) ** 2))
    R = min(err.items(), key=lambda kv: kv[1])[0]
    # An argmin at the feasible ceiling means the held-out error never turned back up —
    # bicv found NO interior optimum (weak/diffuse signal, or true rank >= ceiling). Flag
    # it: such an R is a lower-ceiling artifact, not an identified rank (do not trust it
    # as the effective rank; the caller down-weights it in the consensus).
    informative = (R < top) if top >= 1 else False
    return {"R": int(R), "informative": bool(informative), "feasible_max_rank": int(top),
            "error_curve": {int(r): round(e, 4) for r, e in err.items()}}


# ------------------------------------------------------------------ split-half
def split_half(Z: np.ndarray, n_splits: int, angle_cutoff_deg: float,
               rng: np.random.Generator, max_rank: int | None = None):
    """Subspace stability: randomly halve the pathway rows, take each half's leading-r
    contrast-loading subspace, and measure the largest principal angle between them
    (rotation-invariant). R_sh = the largest r whose mean max-principal-angle stays
    below `angle_cutoff_deg` — how many contrast-loading directions reproduce on
    independent halves of the feature space. Reported as a per-r angle curve too."""
    P, K = Z.shape
    top = (K - 1) if max_rank is None else min(max_rank, K - 1)
    ranks = list(range(1, top + 1))
    acc = {r: [] for r in ranks}
    for _ in range(n_splits):
        perm = rng.permutation(P)
        h1, h2 = perm[: P // 2], perm[P // 2:]
        Z1, Z2 = Z[h1], Z[h2]
        _, _, Vt1 = np.linalg.svd(Z1, full_matrices=False)
        _, _, Vt2 = np.linalg.svd(Z2, full_matrices=False)
        for r in ranks:
            ang = np.degrees(subspace_angles(Vt1[:r].T, Vt2[:r].T))
            acc[r].append(float(ang.max()))
    mean_angle = {r: float(np.mean(v)) for r, v in acc.items()}
    # subspace stability is NESTED: the leading-r subspace can only be stable if every
    # smaller leading subspace is too. So R_sh = the longest CONTIGUOUS run from r=1
    # below the cutoff — not the largest r anywhere below it (which can catch a spurious
    # high-r dip while intermediate r's are unstable).
    R = 0
    for r in ranks:
        if mean_angle[r] <= angle_cutoff_deg:
            R = r
        else:
            break
    return {"R": int(R),
            "mean_max_principal_angle_deg": {int(r): round(a, 3) for r, a in mean_angle.items()},
            "angle_cutoff_deg": angle_cutoff_deg}


# ---------------------------------------------------------------- bootstrap CI
def bootstrap_pa_rank(Z: np.ndarray, n_boot: int, quantile: float,
                      band: np.ndarray, rng: np.random.Generator):
    """Row-bootstrap distribution of the parallel-analysis R, against a FIXED null
    `band` (the full-data band). Resampling the pathway rows perturbs the observed
    singular values; the spread of R over resamples is the estimator's sampling
    uncertainty -> a central-(quantile) CI on R."""
    P = Z.shape[0]
    rs = np.empty(n_boot, dtype=int)
    for b in range(n_boot):
        idx = rng.integers(0, P, size=P)
        rs[b] = parallel_analysis(Z[idx], 0, quantile, rng, band=band)["R"]
    lo = float(np.quantile(rs, (1 - quantile) / 2))
    hi = float(np.quantile(rs, 1 - (1 - quantile) / 2))
    return {"R_median": float(np.median(rs)), "R_ci_lo": lo, "R_ci_hi": hi,
            "R_distribution": {int(k): int(v) for k, v in
                               zip(*np.unique(rs, return_counts=True))}}


# ------------------------------------------------- structural co-primary (t116)
def spearman_offdiag(X: np.ndarray):
    """t116's discriminating statistic: mean and SD of the off-diagonal pairwise
    Spearman concordances between contrast columns. Pairwise-complete (a gene set
    enters a pair iff its NES is non-NA in BOTH columns — the pre-reg:0002 rule).
    SD is undefined for K<=2 (a single off-diagonal), the mechanized form of the
    K>=3 identifiability floor: returns sd=None there, never a fabricated 0."""
    K = X.shape[1]
    pairs = []
    for i in range(K):
        for j in range(i + 1, K):
            xi, xj = X[:, i], X[:, j]
            ok = ~(np.isnan(xi) | np.isnan(xj))
            if ok.sum() >= 3:
                rho = spearmanr(xi[ok], xj[ok]).statistic
                if np.isfinite(rho):
                    pairs.append(float(rho))
    pairs = np.array(pairs)
    if pairs.size == 0:
        return {"mean": None, "sd": None, "n_pairs": 0}
    return {
        "mean": float(pairs.mean()),
        "sd": (float(pairs.std(ddof=1)) if pairs.size >= 2 else None),
        "n_pairs": int(pairs.size),
        "pairs": [round(p, 4) for p in pairs],
    }


def participation_ratio(Z: np.ndarray) -> float:
    """Auxiliary continuous effective-rank scalar: (sum s^2)^2 / sum s^4 (the
    participation ratio of the eigenvalue spectrum). Reported alongside the integer
    R as a rotation-invariant, threshold-free effective-dimension summary."""
    ev = _singular_values(Z) ** 2
    return float((ev.sum() ** 2) / (ev ** 2).sum())
