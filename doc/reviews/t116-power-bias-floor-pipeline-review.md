---
reviews:
  - interpretation:0037-t116-power-bias-floor-shared-axis-sim
  - code/workflows/t116-power-bias-floor/Snakefile
date: "2026-07-07"
overall: WARN
---

# Pipeline Review: t116 power/bias-floor shared-axis simulation

- **Reviews:** `interpretation:0037-t116-power-bias-floor-shared-axis-sim` + the Snakemake workflow `code/workflows/t116-power-bias-floor/` that produces it
- **Date:** 2026-07-07
- **Status:** RESOLVED 2026-07-07 (see *Resolution* below)
- **Overall:** WARN

## Summary

The t116 pipeline is a self-contained, deterministic design-power simulation — not a data-analysis plan — so several rubric dimensions (data availability, some integration boundaries) apply only in an internal sense. On its own terms it is **strong on reproducibility and unusually honest about its own limits**: the deliverable (`interpretation:0037`) already discloses the model-dependence of its quantitative thresholds, the assumed matched-concordance level, the identifiability ceiling, and the fixed arm-bias magnitude. The review confirms those, and surfaces **three actionable gaps the interpretation does *not* flag** — a code-level silent fallback in the null-matching step, an unmodeled *correlated* arm-bias failure mode that is the most dangerous confound for the harmonized design the sim is meant to de-risk, and a missing datapackage manifest. None invalidate the qualitative conclusions (which are structural), but all three should be closed before the surface is cited as an admissibility floor for `question:0050`.

## Rubric Results

| Dimension | Score | Issues |
|---|---|---|
| Evidence coverage | WARN | Noise *scale* calibrated parameter-free (1/√(P−1) ↔ t035); signal (λ), bias (α), noise (σ₀) magnitudes chosen, not sourced — disclosed in interp-0037 |
| Assumption audit | WARN | Arm bias modeled as **independent** per arm; correlated/shared bias (the harmonization confound) unmodeled. Repertoire axes forced exactly orthogonal |
| Data availability | PASS (note) | No external data consumed; only input is the t035 concordance dispersion (results/verdict.json / interp-0001), used for calibration |
| Identifiability | PASS | Surface reachable from params; the R→∞ non-identifiability the sim *reports* is a finding, not a defect (routed to Q-D) |
| Reproducibility | WARN | Seed 1729 + PCG64 + config-pinned + byte-identical regen verified; but `numpy>=2` (not ==) and default_rng value-stability is version-sensitive |
| Validation criteria | WARN | Excellent internal checks (calibration; matched-null power≈0.05); but `_match_kappa` has no convergence assertion → silent fallback; no test file |
| Scope check | PASS | Squarely PAIS design methodology; feeds q0050 |
| Integration boundaries | PASS (note) | Sim levers (K, P, R) map to design knobs; but R is not a design choice — correctly routed to Q-C/t117 |
| Manifest completeness | WARN | Emits surface.json + surface.md + run_metadata.json (provenance), but no `datapackage.json` (the t035 pipeline emits one) |

## Detailed Findings

### Assumption audit — the correlated-bias failure mode (most important)

The generative model puts an arm-specific systematic bias `alpha * a_k` with `a_k` drawn **independently per arm** (random direction, mean-0, unit variance, N-invariant). This correctly captures *independent* batch/site error that harmonization reduces. But it structurally **cannot represent the failure mode that most threatens a harmonized multi-arm study**: bias that is **correlated *across* arms** — a common platform, processing pipeline, normalization, or reference-set artifact shared by every arm because they run the *same* protocol. Such shared bias adds a genuine common axis to every arm's vector, **inflating off-diagonal concordance homogeneity** — i.e. it mimics `hypothesis:0001` (a single shared attractor) and would drive a **false-positive "it's an attractor" verdict**, the exact error the arbitrating bar is meant to control.

This matters because it points the opposite way from interp-0037's framing: the interpretation treats arm bias only as a *magnitude to be lowered* ("harmonization should lower it"), but harmonization **reduces independent bias while potentially introducing shared bias**. The structural test's null is calibrated against a *heterogeneous* finite-repertoire alternative; it has no protection against a *homogeneous* shared-artifact alternative. **Recommendation:** add a third arm — a "shared-bias" regime (`beta * c`, one common axis across all arms) — and report the false-arbitration rate. This is the single most decision-relevant extension for q0050, above the already-listed Q-E full-recovery-control sweep.

### Validation criteria — silent fallback in `_match_kappa` (violates project rule)

`scripts/simulate.py::_match_kappa` binary-searches `kappa ∈ [0, 5]` over 16 iterations to match the finite-repertoire null's mean concordance to the shared-axis alternative's target, then returns the midpoint **with no check that the achieved concordance is actually within tolerance of the target**. If a cell's target mean concordance is unreachable at `kappa ≤ 5` (e.g. high K, high N, low-rank regime), the search silently pins to the boundary and returns a **mis-matched null** — yielding a wrong `power_meanconc_vs_q0017` and a mis-calibrated structural threshold, with no error raised. This directly violates the project's "fail early / avoid silent fallbacks" rule (CLAUDE.md). The reported `power_meanconc_vs_q0017 ≈ 0.05` across cells is *evidence* the match usually succeeded, but it is not asserted per cell. **Recommendation:** after the search, assert `|achieved_rho − target| < tol` (and that the bracket did not terminate at a boundary); raise on failure, or record a per-cell `match_ok` flag in surface.json.

### Reproducibility — env pin and RNG version-stability

The env declares `numpy>=2`. NumPy's `default_rng`/PCG64 bit-stream is stable, but value-level reproducibility of downstream ops across major versions is **not universally guaranteed**, and the surface's headline cell already sits within Monte-Carlo scatter of the 0.80 line (0.85 vs 0.76 across M=8000/6000). For a result intended as a citable admissibility floor, pin `numpy==<current>` in `envs/py.yaml` (and optionally raise M or report a bootstrap CI on boundary cells). **Minor** — determinism *within* a fixed environment is already verified byte-identical.

### Manifest completeness

The workflow writes `run_metadata.json` (task, answers, git_commit, seed, params, config_source, per-regime minima) — good provenance, but not the repo-standard `datapackage.json` the t035 pipeline emits (resources + entity cross-refs + provenance DAG). **Recommendation:** emit a `datapackage.json` listing the three outputs as resources and cross-referencing `interpretation:0037` / `task:t116`, so the sim's outputs are discoverable by the same tooling as the rest of `results/`.

### Evidence coverage — what is and isn't anchored

Credit where due: the concordance-noise **scale** is genuinely parameter-free (falls out of P via 1/√(P−1) and matches the t035 run). But the **signal:bias:noise ratio** (λ=0.70 / α=0.60 / σ₀=1.5) — which sets *where* the K-threshold lands and underwrites the load-bearing "per-arm N in the tens is adequate" claim — is chosen, not sourced. interp-0037 discloses this (Evidence Quality, Limitations 1–2, 4). The qualitative lever ordering (K=2 undefined; mean-concordance blindness; K and P as the levers, not N) is **structural** and robust to these; the specific cell counts are illustrative. No change needed to the write-up — the hedging is already correct — but the dependence should be remembered when the surface is quoted.

## Recommendations

1. **Add a correlated/shared-bias regime** to the generative model and report the false-arbitration rate — the harmonized q0050 design's most dangerous confound, currently invisible to the sim.
2. **Close the `_match_kappa` silent fallback** with a convergence/tolerance assertion (or per-cell `match_ok` flag) — a fail-early fix, cheap and mandated by project rules.
3. **Emit `datapackage.json`** from the workflow for manifest parity with the rest of `results/`.
4. **Pin `numpy==`** in `envs/py.yaml`; optionally report a bootstrap CI on boundary cells (R=4/P=50/K=6/N=30).
5. When citing the surface for q0050, carry the caveat that absolute K/N thresholds are conditional on the (unmeasured) signal:bias:noise ratio and the finite-repertoire rank — the latter is exactly what **t117 (Q-C)** is meant to measure.

## Strengths

- **Reproducibility is exemplary for a simulation:** single seed, PCG64, all design parameters externalized to `config.yaml`, deterministic, and regeneration verified byte-identical to commit cd6c428 after the workflow refactor.
- **Two strong built-in validations:** the parameter-free calibration (concordance SD vs 1/√(P−1)) and the by-construction `power_meanconc_vs_q0017 ≈ 0.05` sanity check that the adversarial null is truly concordance-matched.
- **Intellectual honesty:** the deliverable does not oversell. It explicitly labels itself design-power (not evidence for/against h0001), flags its quantitative thresholds as illustrative, and surfaces its own identifiability ceiling as a new conceptual question (Q-D) rather than burying it.
- **The core results are structural, not tuned:** mean-concordance blindness and the K=2-undefined result follow from the statistic's algebra and the CLT, so they survive the model-dependence caveats above.

## Resolution (2026-07-07)

All three findings + the reproducibility nit were implemented in the workflow and folded into `interpretation:0037`. The pre-existing power surface, calibration, and P-sensitivity numbers are **byte-identical** after the changes (verified) — the additions are strictly additive, so the reviewed result stands unchanged.

1. **Correlated/shared arm-bias regime (finding #1)** — added `shared_bias_probe` to `simulate.py` (config: `shared_bias_probe`). It adds one shared artifact axis *identical* on every arm (no genuine attractor) at the R=2/K=6/N=30 cell that *does* arbitrate (true-attractor power 0.89). As the artifact grows to signal strength (β=0→λ) the false-"attractor" rate climbs **0.13 → 0.30 → 0.62 → 0.92** and off-diagonal SD collapses 0.136 → 0.082 — confirming the structural test cannot separate a fully shared artifact from a genuine attractor. Result carried into interp-0037 Findings and a fifth condition on `question:0050`.
2. **kappa-match silent fallback (finding #2)** — added `_assert_matched`: a per-cell fail-early assertion (tolerance `match_tol=0.03`, plus a boundary-pin check) in both `run_surface` and `p_sensitivity`. Observed max match error **0.0048**; per-cell `matched_mean_rho_achieved` + `match_abs_err` now recorded in `surface.json`.
3. **Manifest (finding #3)** — the workflow now emits `datapackage.json` (Frictionless-style: resources with sizes + sha256, entity/workflow/config sources, deterministic id).
4. **Reproducibility nit** — `envs/py.yaml` pins `numpy=2.4.6` (was `>=2`).

The shared-bias probe also caught a **modeling bug in the first implementation**: an initial per-arm *random* loading on the shared axis made it heterogeneous (mimicking the q0017 repertoire, not an attractor), inverting the curve; corrected to an identical-per-arm loading matching how H1 builds the genuine attractor.
