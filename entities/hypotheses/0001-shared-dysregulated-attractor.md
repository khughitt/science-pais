---
id: hypothesis:0001-shared-dysregulated-attractor
type: hypothesis
title: Post-acute infection syndromes are a shared dysregulated attractor reachable
  from many triggers, not merely a shared symptom repertoire
status: proposed
phase: active
source_refs:
- cite:Komaroff2023
- cite:Trautmann2025
- cite:Komaroff2025
- cite:Bai2023
- cite:Gattoni2025
- cite:Keller2014
- cite:Appelman2024
- cite:Liu2022
- cite:Guo2023
related:
- topic:shared-failure-mode-across-pais
- topic:mecfs-long-covid-convergence
- topic:gut-microbiome-barrier-axis
- question:0001-shared-molecular-signature-across-triggers
- question:0008-formalize-vicious-cycle-attractor-model
- immunity:research-question:immune-homeostasis-and-dysregulation
- pre-registration:0002-cross-trigger-pathway-overlap
- interpretation:0001-cross-trigger-pathway-overlap-reanalysis-t035-null-nonarbitrating
- interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation
- interpretation:0023-t007-microbiome-gut-brain-axis
- proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode
- proposition:0031-pais-gut-dysbiosis-scfa-depletion
created: '2026-06-11'
updated: '2026-06-22'
---
# Hypothesis: Post-acute infection syndromes are a shared dysregulated attractor reachable from many triggers, not merely a shared symptom repertoire

## Organizing Conjecture

Post-acute infection syndromes (long COVID, ME/CFS, PTLDS, post-dengue/Q-fever fatigue, post-SARS, "long flu") are not merely a coincidental sharing of a finite symptom repertoire; they are a single, *stable dysregulated attractor* in the space of immune-autonomic-metabolic physiology, reachable from many different infectious triggers. Above some perturbation, a susceptible host's recovery dynamics fall into a self-sustaining basin maintained by mutually reinforcing feedback loops (chronic immune activation, autonomic dysregulation, reduced cerebral perfusion, mitochondrial/energetic impairment, neuroinflammation) rather than progressive tissue damage. The trigger seeds the basin; the loops keep the system there even after the trigger is cleared. This predicts genuine *biological* (not just symptomatic) convergence across triggers and explains the field's signature feature — resistance to single-target therapy.

## Proposition Bundle

### Core Propositions

- The post-infectious chronic state is *stable and self-sustaining* (a dynamical attractor), not slowly progressive damage; it persists after the trigger is cleared (Komaroff2023, Komaroff2025).
- Distinct triggers (SARS-CoV-2, Borrelia, EBV/enterovirus, dengue, Coxiella, influenza) can converge on this same state, producing overlapping biology beyond overlapping symptoms (Komaroff2023, Bai2023).
- The state is maintained by *multiple mutually reinforcing loops*, such that no single-node intervention reliably restores homeostasis (Komaroff2025, Trautmann2025).

### Supporting Or Auxiliary Propositions

- Patients with more co-active loops are more severe and more treatment-refractory (Trautmann2025).
- Host predisposition (sex, genetics, prior immunity) sets the basin depth/threshold, partly explaining why only ~10-20% of infected individuals enter it (Bai2023, Kalimuddin2022, Morroy2016).
- The shared comorbidity cluster (POTS, MCAS, EDS, ADD) reflects a predisposing background that lowers the threshold for attractor entry (Komaroff2025).

## Current Uncertainty

- The strongest support is from narrative/synthesis reviews (Komaroff2023, Komaroff2025, Trautmann2025) and symptom-overlap comparisons (Bai2023); a *molecular* signature that is both shared across triggers and PAIS-specific has not been demonstrated (see `question:0001-shared-molecular-signature-across-triggers`).
- The "attractor" claim is currently qualitative — the dynamical hallmarks (bistability, hysteresis, critical slowing) have not been tested against longitudinal data (see `question:0008-formalize-vicious-cycle-attractor-model`).
- A serious rival reading is that convergence is only symptomatic: a small repertoire of organ-system failures reached by *distinct* mechanisms (Hanson2023, and the within-trigger divergence in Cruz2025).

## Predictions

**Strong / discriminating:**

- Harmonized multi-omics across ≥3 triggers (SARS-CoV-2, Borrelia, dengue/EBV) with full-recovery controls will reveal a shared *pathway-level* signature (e.g. mitochondrial/energy stress + innate non-resolution) present in cases of all triggers and absent in recovered controls.
- Longitudinal trajectories will show attractor signatures — bistability or hysteresis (recovery requires a larger push than the perturbation that induced illness) and critical slowing near transitions — rather than monotonic exponential decay.
- Combination interventions hitting ≥2 loop nodes will outperform the sum of single-target interventions; single-target trials will tend to fail or show small effects (consistent with the broad single-agent null/weak signals in Seo2025).

**Weaker / corollaries:**

- Loop-co-occurrence count (number of active loop axes measured in one cohort) will correlate with severity and treatment-refractoriness (Trautmann2025).
- The shared comorbidity cluster will appear across non-COVID PAIS (post-Lyme, post-Q-fever), not only ME/CFS and long COVID.

## Falsifiability

Confidence would be materially reduced if:

- Adequately powered cross-trigger multi-omics finds *no* shared PAIS-specific pathway signature — i.e. each trigger's chronic state is molecularly distinct despite symptom overlap (supporting Hanson2023's trigger-specific view).
- Longitudinal data show simple monotonic decay with no bistability/hysteresis/critical-slowing, and recovery probability depends only on time and initial severity (no separatrix).
- A single-target intervention (e.g. one cytokine blockade) reliably and durably resolves PAIS across patients, contradicting the multi-loop requirement.

## Supporting Evidence

- **Komaroff2023 (literature):** seven-domain ME/CFS ↔ long COVID overlap in symptoms and objective abnormalities; explicit stable-attractor/dauer framing.
- **Komaroff2025 (literature):** PAIS within IACIs; mutually reinforcing vicious cycles; no single-target sufficiency.
- **Trautmann2025 (literature):** self-sustained inflammatory loops + failed interoception; severity scales with loop co-occurrence.
- **Bai2023 (literature):** 26/29 canonical ME/CFS symptoms present in PTLDS — cross-trigger symptom convergence.
- Cross-pathogen anchors (Kalimuddin2022, Morroy2016, Zheng2026) show a consistent chronic fraction across triggers, consistent with a shared host-determined threshold.
- **t007 microbiome/gut-brain axis (2026-06-25; `proposition:0031`, `interpretation:0023`):** long
  COVID and ME/CFS both show gut dysbiosis with depleted SCFA/butyrate-producing capacity or related
  microbial-metabolite abnormalities (Liu2022/Su2023; Guo2023/Xiong2023), and a synbiotic perturbation
  trial in PACS weakly improves symptoms (Lau2024). This supports a plausible gut-immune-metabolic-neural
  loop node, but **does not promote this hypothesis**: the evidence is mostly observational, only mature
  for long COVID + ME/CFS, and Xiong2023 shows chronic symptoms can outlast overt microbiome-composition
  dysbiosis.

## Disputing Evidence

- **Hanson2023:** argues classical ME/CFS is enterovirus-specific and cautions against conflating it with post-COVID illness — favors trigger-specific mechanisms.
- **Cruz2025:** within a single trigger (SARS-CoV-2), pulmonary sequelae and systemic long COVID are biologically distinct — convergent symptoms need not imply convergent biology even within one pathogen.
- **Peppercorn2023:** direction-of-effect discordances (HLA-E, S100A4) between LC and ME/CFS caution against assuming molecular identity.
- **t025 / `proposition:0011` (functional/tissue; PEM endpoint localization):** the new constraint is the three-arm pattern, not the Gattoni2025 null alone. Keller2014 anchors the ME/CFS whole-body 2-day-CPET decrement; Gattoni2025 reports no significant day-2 GET/VO2peak/WRpeak decrement in a small PEM-enriched long-COVID cohort (n = 15; 80% PEM-positive by mDSQ); Appelman2024 shows long-COVID PEM still has objective peripheral-muscle OXPHOS pathology after provocation. This does not refute the attractor hypothesis, but it disputes a strong "single shared whole-body bioenergetic lesion" interpretation: if an attractor is shared, its objective bioenergetic expression is trigger- and endpoint-specific. Gattoni remains the weak/underpowered leg; Appelman prevents reading the update as "long-COVID PEM has no objective basis."
- **t035 cross-trigger pathway-overlap reanalysis (2026-06-21; `interpretation:0001-...`, `empirical_data_evidence`, weighted-low):** the first *empirical* test bearing on this hypothesis. NES rank-concordance between two distinct triggers (PI-CFS, GSE14577; Q-fever fatigue, GSE130353) was anti-concordant and non-arbitrating (`null_nonarbitrating`; C1 p_perm = 0.949 ≥ α; all six pair × DB cells null). Per `pre-registration:0002` the pre-committed reading is **the test was inadequate, not that this hypothesis is wrong** — 2 cohorts, n = 7–10/group, cross-platform, cross-compartment, sex-unmatched; a non-arbitrating null at this power/bias ceiling **cannot exclude a real shared signature**. Recorded as a marginal downward nudge on *demonstrability-so-far*, not on the conjecture; the Organizing Conjecture and predictions are intact.

## Evidence Needed To Shift Belief

- **Most efficient upward:** a harmonized, controlled cross-trigger multi-omics study demonstrating a shared PAIS-specific pathway signature (answers `question:0001`); plus longitudinal evidence of bistability/critical slowing (answers `question:0008`).
- **Most efficient downward:** the same cross-trigger study finding trigger-distinct signatures, or a durable single-target cure.
- **Also useful:** combination-vs-single-target intervention trials; loop-co-occurrence-vs-severity test in one richly phenotyped cohort.

## Related Work

- `topic:shared-failure-mode-across-pais` — the synthesis this hypothesis formalizes.
- `topic:mecfs-long-covid-convergence` — the strongest empirical test bed.
- `question:0001-shared-molecular-signature-across-triggers`, `question:0008-formalize-vicious-cycle-attractor-model` — the two decisive open tests.
- Sibling hypotheses 0002 (antigen-fragment seed), 0003 (exhaustion loop), 0004 (severity threshold) specify candidate seeding and maintenance mechanisms for this attractor.
- `immunity:research-question:immune-homeostasis-and-dysregulation` — peer mechanism owner.

## Notes

- 2026-06-20: Deflationary rival now tracked as question:0017 — the finite-organ-failure-repertoire coincidence account (convergence is symptomatic, not a shared attractor) plus ascertainment-artifact. These remain genuinely competitive with this hypothesis; head-to-head molecular designs still fail a shared positive signature and the >=3-trigger harmonized test does not exist. Score this hypothesis against q0017 before promotion.
- 2026-06-21: First empirical probe (t035, pre-registration:0002) ran and returned `null_nonarbitrating` — see `interpretation:0001-cross-trigger-pathway-overlap-reanalysis-t035-null-nonarbitrating`. Weighted-low, asymmetric: a marginal downward nudge on demonstrability, **not** support for the q0017 coincidence null (the absence of detectable concordance at this n cannot exclude a real shared signature). Status held at `proposed`; promotion still gated on the harmonized ≥3-trigger test. The run's concrete contribution is the empirical demonstration that public 2-cohort, cross-platform, cross-compartment data cannot adjudicate this question.
- 2026-06-25: t007 added `proposition:0031` as `supports_scope: local_proposition` rather than a core
  member of this hypothesis. Rationale: gut dysbiosis/SCFA depletion is a plausible reinforcing loop node,
  but current evidence cannot distinguish driver, consequence, baseline susceptibility, or disease-stage
  marker.
