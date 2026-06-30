---
id: interpretation:0001-cross-trigger-pathway-overlap-reanalysis-t035-null-nonarbitrating
type: interpretation
title: 'Cross-trigger pathway-overlap reanalysis (t035): null_nonarbitrating'
status: active
source_refs: &id001
- results/verdict.json
- results/run_metadata.json
related:
- hypothesis:0001-shared-dysregulated-attractor
- question:0017-deflationary-alternatives-vs-shared-pathophysiology
- question:0001-shared-molecular-signature-across-triggers
- pre-registration:0002-cross-trigger-pathway-overlap
- task:t035
created: '2026-06-21'
updated: '2026-06-21'
input: *id001
workflow_run: 0003-cross-trigger-pathway-overlap-pipeline
prior_interpretations: []
relations: []
---

# Interpretation: Cross-trigger pathway-overlap reanalysis (t035): null_nonarbitrating

## Verdict

**Verdict:** [?] Inconclusive — `null_nonarbitrating`: the C1 confirmatory NES rank-concordance (PI-CFS-vs-HC × QFS-vs-HC, pinned Hallmark) is anti-concordant (`rho = -0.563`) and sits deep in the left tail of a well-formed sample-label permutation null (`one-sided p_perm = 0.949 >= alpha = 0.05`), so the locked resolution order halts at step 2. Per `pre-registration:0002` this means **the test was inadequate, not that `hypothesis:0001` is wrong**; it is recorded as weighted-low evidence and is **explicitly not** support for the `question:0017` coincidence null.

This moves the pre-reg's standing verdict **off** `[?] inconclusive-for-coverage` (no qualifying vehicle) to `[?] inconclusive — power/bias ceiling` (an admissible vehicle, GSE14577 + GSE130353, cleared G1–G4 and the analysis ran). The token stays `[?]`, but the basis changed from "no evidence yet" to "evidence obtained, non-arbitrating at this n."

## Findings Summary

The verdict is a pure mechanical function of the pre-committed signals (`verdict.py`, WP8; byte-reproducible, KD10). Main results:

- **C1 confirmatory (null).** Primary × Hallmark: ρ_obs (multilevel) = **−0.562737**; ρ (permutation-internal, fgseaSimple) = −0.557167; **p_perm = 0.949** (B = 2000) vs α = 0.05. Evidence type: `empirical_data_evidence` / `negative_result`. Signal strength: **null**.
- **Sensitivity surface — all six pair × DB cells anti-concordant (null).** Every ρ is negative (−0.32 to −0.65) and every p_perm ∈ [0.8995, 0.9835] sits far above α. The null is uniform across DBs (Hallmark/Reactome/GO-BP) and across both fatigue contrasts (primary QFS-vs-HC and the S4 idiopathic CFS-vs-HC). Strength: **null**, and consistently so (no DB-dependent flip).
- **Admissibility passed on the assessable leg (methodological).** limma diagnostics are full-rank across all five contrasts (residual_df 13–18, 18.3–23.5k genes tested). The PCA-batch leg is **not assessable** (no batch covariate in either deposit) and is recorded as `batch_assessable: false`, non-firing, per the locked 2026-06-21 clarifying note — so step 1 does not fire and the verdict is set cleanly at step 2.
- **Descriptive specificity/theme surface (non-arbitrating, but directionally notable).** Because the primary test halts at step 2, steps 3–7 are **not reached**. Reported for interpretability only: the only concordance-carrying mitochondrial/OXPHOS sets that survive on Reactome/GO-BP classify as **`exposure_sequela`** (S2-positive in QS-vs-HC), and there are **no** fatigue-specific themes in any DB (`theme_sets.fatigue_specific_any_db = []`, `exposure_sequela_any_db = ["mitochondrial/OXPHOS"]`). This is consistent with the pre-registered competing account (Raijmakers2019: the Q-fever mito signal tracks past-*Coxiella* exposure, not fatigue) — but it is **descriptive only**; the non-arbitrating null caps any such read.

## Evidence Quality

- **Confirmatory, not exploratory.** C1 is the single pre-registered confirmatory test; significance comes from the locked sample-label permutation null (B = 2000), which preserves gene-set correlation structure and tested-set size — the calibration the pre-reg chose over Fisher's exact.
- **Power/bias posture is the dominant caveat.** 2 cohorts; n = 7–10/group; cross-platform (U133A/B microarray vs MMSEQ RNA-seq); cross-compartment (PBMC vs isolated monocytes); sex unmatched (GSE14577 male-only, GSE130353 sex unreported). The effective cross-trigger unit is the **cohort, and there are only two** — the verdict ceiling was *suggestive* even on a clean positive, and most residual error here is **bias**, which the permutation budget does not shrink. A null under these conditions cannot exclude a real shared signature.
- **Independence relative to prior evidence.** This is the project's **first** empirical (non-literature) test bearing on hypothesis:0001 and question:0017. It does not collapse into an existing independence group — it adds a new, weak, `empirical_data_evidence` line where the prior evidence base was narrative/synthesis (Komaroff2023/2025, Trautmann2025) and molecular-literature (Galbraith2011, Raijmakers2021/2025). Weight is **low** by design (pilot-grade), not by redundancy.
- **No "too good to be true" risk.** The pre-reg's suspicious-result plan targets an implausibly *strong* positive; the observed result is a uniform null, so the leak/confound checks (compartment, exposure, single-set dominance) are moot for acceptance — they would have gated a positive, not this null.

## Data Quality Checks

- **Control uniqueness:** controls are distinct per contrast (HC, QS are separate sample groups; permutation pools are contrast-local, never jointly relabeled across the four GSE130353 groups). No shared-sample leakage across the two arms of any contrast.
- **Sample counts:** match the metadata-confirmed design — GSE14577 PI-CFS-vs-HC 8 vs 7; GSE130353 QFS-vs-HC / QFS-vs-QS / QS-vs-HC / CFS-vs-HC 10 vs 10. Genes tested per contrast (18.3–23.5k) are consistent with the harmonized universe.
- **Dimensionality/universe:** the pinned Hallmark universe carries 50 sets (n_shared = 50 in both primary and S4 Hallmark cells), Reactome ~1.08k, GO-BP ~4.0k — as expected for MSigDB 2024.1.Hs with the 15 ≤ |set| ≤ 500 filter.
- **Anomalies:** none identified. Determinism independently re-confirmed (two heavy-null cells regenerated to identical p_perm). **No data quality concerns identified.**

## Proposition-Level Updates

The pre-reg is **epistemic** with an operational sub-portion. The operational portion (did the locked procedure run as committed?) is **satisfied** — the analysis ran per the locked resolution order with the batch-leg clarifying note as the only operational annotation, and that note loosened no threshold. No `amendments:` deviation is owed. The epistemic portion produces a single weighted-low update, exactly as the locked Decision-Criteria table licenses for `null_nonarbitrating`:

- **hypothesis:0001 (shared dysregulated attractor) — `disputes` stance, strength `weak`, weighted-low.** Frame as a weighted update, **not** a verdict: a non-arbitrating null at this power floor is a small downward nudge on the *demonstrability-so-far* of a shared pathway signature, but per the pre-committed asymmetry it **cannot** exclude a real shared signature. The core Organizing Conjecture is intact; uncertainty in the prediction "harmonized cross-trigger data will reveal a shared pathway signature" is *increased only marginally*, because this 2-cohort probe was never powered to confirm or refute it. Net: minimal durable movement.
- **question:0017 (deflationary alternatives) — NO update.** Pre-committed asymmetry: absence of detectable concordance here is **not** evidence *for* the finite-repertoire-coincidence null. The result enters q0017's evidence base only as *"existing public data cannot adjudicate"* — it neither strengthens nor weakens the deflationary bundle. The descriptive `exposure_sequela` lean of the surviving mito sets is consistent with the exposure-confounding account but is non-arbitrating and is **not** recorded as support (steps 4–6 were never reached).
- **question:0001 (shared molecular signature across triggers) — navigation only, no `bears_on`.** This 2-cohort probe is a step toward, but explicitly not, the decisive ≥3-trigger harmonized test q0001 demands. No edge is claimed (as locked in the pre-reg `commits_to:` scoping).

## Hypothesis-Level Implications

`hypothesis:0001` status remains **`proposed`** — no mechanical status flip. The attractor conjecture rests on narrative/synthesis support plus symptom-overlap; this first empirical probe was, by pre-registered design, incapable of confirming or refuting it. The honest position is unchanged from the `question:0017` "best current interpretation": cross-trigger convergence is supported at the *pathway/physiology* level but not at shared molecules, consistent with **both** a real shared attractor and a coincidence-of-repertoire null. What this run adds is a concrete, reproducible demonstration that **public `2`-cohort, cross-platform, cross-compartment data cannot adjudicate** — which sharpens the case that the discriminating test must be the harmonized `>=3`-trigger, full-recovery-controlled, definition-held-constant design, not another opportunistic public-data pairing.

## Evidence vs. Open Questions

- **question:0001 — unchanged.** The decisive ≥3-trigger harmonized test still does not exist; this probe was navigation context for it. What is now *empirically* (not just argumentatively) established: a 2-trigger pathway-rank-concordance route over heterogeneous public deposits is underpowered to the point of non-arbitration — a design lesson that raises the priority of a purpose-built harmonized cohort over further public-data mining.
- **question:0017 — unchanged standing, now with one recorded non-arbitrating empirical line.** The deflationary bundle's competitiveness is neither strengthened nor weakened. The sub-question that becomes more important: can *any* assemblable public cohort set clear the power/bias floor, or is the coincidence-vs-attractor question structurally unanswerable without prospective harmonized sampling?
- **question:0014 / question:0015 (case-definition coherence, PEM stratification) — untouched** by this run, but remain upstream of any future harmonized design.

## New Questions Raised

- **Q-A (methodological, P2):** What is the minimum cohort count / per-group n at which a cross-trigger pathway-rank-concordance test becomes arbitrating (clears the bias floor, not just the Monte-Carlo floor)? Most efficient evidence: a power/bias simulation seeded with the observed NES dispersion from this run — cheap, and it would set an admissibility floor for future vehicles under the pre-reg's data-gated gate.
- **Q-B (empirical, P3):** Does the descriptive `exposure_sequela` lean of the mitochondrial/OXPHOS sets (S2-positive in QS-vs-HC) replicate in any independent Q-fever-exposed-vs-recovered comparison? This would test the Raijmakers2019 exposure-confounding account directly, *outside* the non-arbitrating concordance frame where it is currently only descriptive.

## Limitations & Residual Uncertainty

- The verdict is **non-arbitrating by construction at this n** — it is a statement about the *vehicle*, not about nature. The anti-concordant sign (all six ρ < 0) is *not* interpretable as evidence against a shared signature: at this power/bias level the point estimate's sign carries little information, and the pre-registered reading is "inadequate test."
- Steps 3–7 of the resolution order were **not reached**, so the specificity/compartment/DB-robustness machinery is unexercised here — the `exposure_sequela` mito observation is descriptive and must not be cited as an adjudicated finding.
- Cross-platform (microarray vs MMSEQ) and cross-compartment (PBMC vs monocytes) heterogeneity, plus unadjustable sex confounding, remain the dominant un-shrinkable error sources. These are properties of the only public data that exists for this trigger pair.

## Updated Priorities

- **Record the two weighted updates** (hypothesis:0001 weak-`disputes`/weighted-low; question:0017 no-update) — done in this interpretation; the standing verdict moves off `[?] inconclusive-for-coverage` to `[?] inconclusive — power/bias ceiling`.
- **Close t035** — its definition-of-done ("flips to `done` once an admissible vehicle clears G1–G4 and the analysis runs") is now satisfied.
- **Do not re-run on more public pairings** before a power/bias floor exists (Q-A). The evidence gap worth targeting is a purpose-built harmonized ≥3-trigger design, not another opportunistic public dataset — this run is the empirical argument for that reprioritization.
- **Hold hypothesis:0001 promotion** against the q0017 bundle, exactly as before; this run does not license promotion and does not license demotion.
