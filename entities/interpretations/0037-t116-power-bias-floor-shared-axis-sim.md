---
id: interpretation:0037-t116-power-bias-floor-shared-axis-sim
kind: interpretation
title: "t116/Q-A: the harmonized shared-axis test is arbitrating only structurally (K>=3) and only with a high-resolution feature universe — per-arm N is not the binding lever; any 2-arm design and the t035 mean-concordance statistic are non-arbitrating at any N"
status: active
source_refs:
  - results/t116-power-bias-floor-sim/surface.json
  - results/t116-power-bias-floor-sim/run_metadata.json
related:
  - task:t116
  - question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
  - question:0017-deflationary-alternatives-vs-shared-pathophysiology
  - question:0001-shared-molecular-signature-across-triggers
  - hypothesis:0001-shared-dysregulated-attractor
  - interpretation:0001-cross-trigger-pathway-overlap-reanalysis-t035-null-nonarbitrating
  - interpretation:0036-t103-cross-pathogen-co-enrollment-feasibility
  - pre-registration:0002-cross-trigger-pathway-overlap
created: "2026-07-07"
updated: "2026-07-07"
input: "In-silico power/bias-floor simulation (code/scripts/t116_power_bias_sim.py; numpy-only, deterministic seed 1729, 8000 reps/cell) seeded with the t035 observed concordance dispersion. Answers the Q-A gate raised in interpretation:0001 and upgrades the 'plausibly estimand-aligned / worth simulating' power claim in interpretation:0036. No participant data; this is a design-power simulation, not an empirical test of hypothesis:0001."
workflow_run: "t116-power-bias-floor-sim"
prior_interpretations:
  - interpretation:0001-cross-trigger-pathway-overlap-reanalysis-t035-null-nonarbitrating
  - interpretation:0036-t103-cross-pathogen-co-enrollment-feasibility
relations:
  - predicate: "sci:amends"
    target: "interpretation:0001-cross-trigger-pathway-overlap-reanalysis-t035-null-nonarbitrating"
  - predicate: "sci:amends"
    target: "interpretation:0036-t103-cross-pathogen-co-enrollment-feasibility"
---

<!-- Mode: DESIGN-POWER SIMULATION (t116, deliverable for the interp-0001 Q-A gate on q0050).
No participant-level data and no cohort in hand: this interprets a synthetic-data power surface,
not an empirical result about nature. Belief updates about hypothesis:0001 / question:0017 are
about the DEMONSTRABILITY PATH (what design can adjudicate them), not about their truth. -->

# Interpretation: t116 — power/bias-floor of the harmonized ≥3-trigger shared-axis test

## Verdict

**Verdict:** [~] Conditional — the harmonized shared-axis test **can** be arbitrating, but only along axes the project had not been costing: it requires a **structural** (single-shared-axis homogeneity) statistic run across **K ≥ 3 arms** on a **high-resolution feature universe (~1000 sets)**. Any **2-arm** design (the t035 route) and the **mean-concordance statistic itself** are **non-arbitrating at any per-arm N** — mean concordance is *blind by construction* to the `question:0017` finite-repertoire null (power ≈ 0.00 against a strength-matched null) while trivially clearing the Monte-Carlo bar (power = 1.00). Per-arm N (tens, MELLOW-scale) is **adequate and not the binding constraint**; **arm count and feature-space resolution are**.

## Findings Summary

Simulation (deterministic, seed 1729, 8000 reps/cell; `code/scripts/t116_power_bias_sim.py`). A generative model puts, on each arm's per-pathway effect vector, a shared component (`hypothesis:0001`: one global attractor axis through all arms // `question:0017`: R generic "finite-repertoire" axes with random per-arm loadings), plus arm-specific systematic bias (does **not** shrink with N) and within-arm sampling noise (shrinks as `sigma0/sqrt(N)`). The `question:0017` null is **concordance-matched** to `hypothesis:0001` per cell — the adversarial case of *identical average cross-arm overlap, different rank*.

- **Parameter-free calibration holds.** Sampling-null concordance SD at Hallmark P=50, K=2, N=8 = **0.1432**, matching the analytic 1/√(P−1) = 0.1429 and the **t035 observed ρ spread** (six cells ρ∈[−0.65,−0.32], SD ≈ 0.124). The concordance-noise scale is anchored to the real t035 run with **no tuning**. *(methodological, strong)*

- **The t035 statistic is structurally blind.** Mean cross-arm concordance vs the concordance-matched `question:0017` null: power ≈ **0.00** at every (K,N) — it *cannot* exceed a finite-repertoire null of equal strength. Against the **sampling-only** null (what a within-arm permutation test sees) the *same* statistic scores power = **1.00** everywhere. A study using mean concordance would look emphatically significant while adjudicating nothing — the exact "clears the Monte-Carlo floor, not the bias floor" trap `interpretation:0001` Q-A named. *(null / methodological)*

- **K = 2 is structurally non-arbitrating at any N.** The discriminating statistic (SD of the off-diagonal pairwise concordances — a single-shared-axis homogeneity test) is **undefined for two arms** (one off-diagonal → no variance). No per-arm N repairs it. This is the mechanized form of `interpretation:0001`'s "the effective cross-trigger unit is the cohort, and there are only two." *(strong, discriminating)*

- **Arm count is the dominant lever; per-arm N is secondary and saturating.** At Hallmark P=50 against a lumpy (R=2) null, N=30: structural power rises K3→K6 = 0.17 → 0.91; whereas at fixed K=5 across N=10→100 it moves only 0.64 → 0.78. Adding an arm buys far more than 10× the per-arm N. *(strong)*

- **Minimum arbitrating footprint depends on how lumpy the finite-repertoire null is** (Hallmark P=50): lumpy R=2 → **K=6 × N=10** (power 0.82); moderate R=4 → **K=6 × N=30** (0.85); high-rank R=8 and R=16 → **no (K,N) ≤ 6 arms** reaches 0.80. A finite repertoire spread over *many* axes makes pairwise overlaps concentrate (CLT) toward a homogeneous value that *mimics one global axis* — the harder null. *(discriminating; model-dependent thresholds)*

- **Feature-space resolution is a lever co-equal with arm count.** Moderate (R=4) null, N=30, minimum arbitrating K by pathway-universe size P: **P=50 → ≥6 arms (borderline)**, **P=200 → K=4** (power 0.97), **P=1000 → K=3** (power 0.95). The concordance sampling floor is 1/√(P−1) = 0.143 → 0.071 → 0.032; a richer feature universe sharpens the structural test enough to **drop the required arm count from >6 to 3**. *(strong, decision-relevant)*

## Evidence Quality

- **Design-power simulation, not empirical evidence.** Every number here is about *which design can adjudicate* `hypothesis:0001` vs `question:0017`, not about which is true. It carries **no** weight on the truth of the attractor conjecture and is explicitly **not** support for either.
- **Seed fidelity is the main strength.** The concordance-noise scale is not free-tuned: it falls out of the pathway-set count P and matches the t035 run. The qualitative conclusions (mean-concordance blindness; K=2 undefined; K ≫ N as the lever; P as a co-lever) are **structural** — they follow from the statistic's algebra and the CLT, not from the specific loading magnitudes.
- **The absolute K thresholds are model-dependent.** "K=6 at Hallmark-50 for a lumpy null" moves with the true-axis loading, arm-bias magnitude, the matched concordance level (~0.5 here), and the finite-repertoire rank R — none of which are known for real PAIS data. Treat the *trend and ordering* of levers as robust and the *specific cell counts* as illustrative. (A single boundary cell — R=4, P=50, K=6, N=30 — reads 0.85 in the M=8000 main surface and 0.76 in the M=6000 P-sensitivity pass: Monte-Carlo scatter at the 0.80 line, not a contradiction.)
- **Confirmatory vs exploratory:** this is a pre-data methodological result. It sets an admissibility floor for any future vehicle under `pre-registration:0002`'s data-gated gate; it does not itself test anything.

## Data Quality Checks

- **Determinism:** fixed seed 1729 (echoing the t035 determinism seed), numpy PCG64, 8000 reps/cell; re-running reproduces the surface.
- **Calibration anchor verified:** sampling-null concordance SD (0.1432) matches the closed-form 1/√(P−1) (0.1429) and the t035 empirical dispersion — the noise model is not mis-scaled.
- **Null construction verified:** the `question:0017` null is concordance-matched per cell by binary search on its loading scale; realized mean concordance tracks `hypothesis:0001`'s (~0.43–0.53), confirming the two hypotheses are separated *only* by structure, not by average overlap — as intended for an adversarial test.
- **Internal consistency:** mean-concordance-vs-matched-null power ≈ 0.00 across all cells, as required if the match is faithful. No anomalies. **No data quality concerns identified.**

## Proposition-Level Updates

- **`hypothesis:0001` (shared dysregulated attractor) — no update to belief; update to the demonstrability path.** The conjecture's truth is untouched by a synthetic power study. What changes is *how it can be shown*: the discriminating evidence must be **structural** (a single shared axis running through ≥3 arms), **not** the magnitude of cross-trigger concordance. A corollary the simulation surfaces: against a *sufficiently high-rank* finite repertoire, "one coordinated attractor" and "a universal low-dimensional generic-sickness manifold shared by all triggers" become **empirically indistinguishable** by this family of tests — a genuine identifiability boundary for `hypothesis:0001` as currently worded (see New Questions Q-D).
- **`question:0017` (deflationary alternatives) — no update to plausibility; sharpened adjudication requirement.** The finite-repertoire null is *not* refuted or weakened here. The result specifies what it would take to distinguish it: structural rank evidence at K≥3 on a rich feature space — and flags that the *lumpiness* (rank) of the real cross-PAIS repertoire is itself the pivotal unknown that decides whether adjudication is even possible.
- **`question:0001` (shared molecular signature across triggers) — the decisive test is now specced, not just named.** The ≥3-trigger harmonized test it demands acquires concrete admissibility conditions: (a) a structural/single-factor statistic, retiring mean concordance for the confirmatory contrast; (b) K ≥ 3 arms; (c) a ~1000-set feature universe; (d) full-recovery controls (from `interpretation:0036`).

## Hypothesis-Level Implications

`hypothesis:0001` status remains **`proposed`** — a design-power simulation licenses no status change. The load-bearing implication is for `interpretation:0036`'s staged-GO recommendation, which this interpretation **amends**:

- **Per-arm N is not the binding constraint.** `interpretation:0036` hedged that "achievable N is *plausibly aligned with* the shared pathway/latent-factor axis … 'adequately powered' not yet established." The simulation resolves the direction: **N in the tens (MELLOW-scale) is adequate**; it saturates quickly and is the *wrong* variable to optimize. The binding levers are **arm count (K≥3)** and **feature-space resolution (~1000 sets)**.
- **The Tier-1 triad (K=3) is viable — but conditionally.** COVID-19 + influenza + EBV can be structurally arbitrating **only if** paired with a high-resolution feature universe; at Hallmark-50 resolution K=3 is badly underpowered (~0.13). The analysis plan's feature-space choice is therefore **co-load-bearing** with the recruitment plan.
- **Opportunistic Tier-2/Tier-3 arms are promoted from "nice to have" to "power margin."** Because K is the dominant lever, each added arm (Lyme, Q-fever) materially raises structural power and widens the margin against harder (higher-rank) finite-repertoire nulls. They are how the design buys robustness to the unknown repertoire rank.
- **The t035 confirmatory statistic must be retired for this contrast.** Mean rank-concordance clears the Monte-Carlo bar trivially while being blind to `question:0017`; a successor pre-registration must commit to a structural single-factor-adequacy statistic.

## Evidence vs. Open Questions

- **`question:0050` feasibility gate — advanced from "worth simulating" to "specced, with the binding constraints identified."** The go/no-go moves feasible → *fundable-with-conditions*: fund only a design that commits to (K≥3, ~1000-set features, structural statistic, full-recovery controls). A 2-arm or Hallmark-resolution or mean-concordance design is a predictable non-arbitration and should not be funded.
- **`question:0017` — the pivotal empirical unknown is now named:** the *rank/lumpiness* of the real cross-PAIS pathway overlap (which R regime we are in). This is partially estimable from existing single-trigger multi-omics before any co-enrollment (Q-C).
- **`question:0001` / `pre-registration:0002` — unchanged standing, now with an admissibility floor.** The data-gated gate acquires a quantitative floor: no vehicle with K<3, low-resolution features, or a mean-concordance confirmatory statistic can clear it.

## New Questions Raised

- **Q-C (empirical, P2):** What is the effective **rank / diffuseness** of the real cross-PAIS pathway-response overlap — i.e., which finite-repertoire regime (lumpy low-rank vs homogeneous high-rank) are we actually in? This single unknown decides whether the ≥3-trigger test is arbitrating at achievable K, and it is partly estimable *now* from existing single-trigger multi-omic deposits (factor/rank analysis of per-condition pathway-effect vectors) without a new cohort. Most efficient next probe on the whole design question.
- **Q-D (conceptual, P2/P3):** Is the distinction "one coordinated attractor" vs "a universal low-dimensional generic-sickness manifold shared across triggers" **operationally meaningful**, given the simulation shows a high-rank shared repertoire is structurally indistinguishable from a single attractor? Either sharpen `hypothesis:0001` to embrace a shared low-dim manifold (rank-agnostic), or specify the extra evidence (e.g., trigger-specific perturbation/recovery dynamics, full-recovery-control specificity) that would separate them — otherwise the attractor claim has an identifiability ceiling independent of sample size.
- **Q-E (methodological, P3):** Does adding **full-recovery-control contrasts** (the `interpretation:0036` correction) raise structural power beyond raw case-only concordance — i.e., does specificity-to-the-nonrecovered-state add a discriminating dimension the current simulation omits? A worthwhile extension of this model.

## Limitations & Residual Uncertainty

- **Synthetic throughout.** The generative model is a deliberate caricature (one attractor axis; random-loading finite repertoire; Gaussian arm bias and sampling noise). Real multi-omic NES vectors have heavier tails, cross-omic block structure, and platform-specific artifact the model does not carry. The **qualitative** lever ordering is robust; the **quantitative** thresholds are illustrative.
- **The matched concordance level (~0.5) is assumed, not measured.** If the true cross-trigger shared signal is weaker, every threshold worsens; if stronger, they improve. Q-C is the way to replace this assumption with data.
- **Identifiability ceiling is real.** For high-rank finite-repertoire nulls (R≥8 here) no arm count ≤6 arbitrates. Whether that regime is a genuine "coincidence" or is itself a shared mechanism is the conceptual question Q-D — the simulation cannot resolve it, and neither can more N.
- **Arm-specific bias magnitude is fixed.** Harmonization + full-recovery controls should lower it; the simulation does not sweep it (a further extension), so the results assume a moderate, non-catastrophic residual arm bias — i.e., that harmonization *works* to the degree `interpretation:0036` requires.

## Updated Priorities

- **Amend `interpretation:0036`:** the staged-GO conditions gain two co-load-bearing analysis-plan requirements — a **~1000-set (Reactome/GO-BP-scale) feature universe** and a **structural single-factor-adequacy confirmatory statistic** — and the emphasis shifts from per-arm N (adequate at tens) to **arm count K≥3** with opportunistic arms as power margin. (Recorded in `question:0050` and here; the interp-0036 conclusion is revised via the `sci:amends` graph edge from this interpretation, per the project's amend-in-the-newer-doc convention.)
- **Retire mean cross-arm concordance** as a confirmatory statistic for the shared-vs-trigger-specific contrast; a successor pre-registration for `question:0050` must pre-commit to the structural statistic + K≥3 + high-resolution features + full-recovery controls.
- **Prioritize Q-C** (estimate the real repertoire rank from existing single-trigger multi-omics) as the cheapest thing that most changes the go/no-go — it converts the "which R regime" assumption into data before any cohort commitment.
- **Do not fund** a 2-arm, Hallmark-resolution, or mean-concordance design: each is a predictable non-arbitration. The t035 route stays closed.
- **`hypothesis:0001` promotion** remains held against the `question:0017` bundle; this simulation neither licenses nor blocks promotion — it defines the test that eventually could.
