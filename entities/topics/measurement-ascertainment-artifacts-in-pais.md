---
id: topic:measurement-ascertainment-artifacts-in-pais
kind: topic
title: Measurement-channel and ascertainment artifacts in PAIS
status: active
related:
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
- hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- topic:pais-case-definition-heterogeneity
- topic:biomarkers-and-objective-endpoints
- proposition:0010-cognitive-female-excess-is-self-report-only-absent-in-objective-testing
- proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode
- proposition:0009-dysautonomia-female-skew-is-baseline-carried-not-pais-amplified
- interpretation:0003-t018-subphenotype-sex-reproductive-stage
- interpretation:0014-sfn-prevalence-metric-harmonization-reanalysis
- proposition:0014-pais-small-fiber-structural-lesion-ienfd
- question:0004-convergent-small-fiber-neuropathy-substrate
- question:0014-which-pais-case-definition-is-most-biologically-coherent
- question:0015-does-pem-requirement-improve-cross-study-comparability
- paper:Novak2026
- paper:Oaklander2022
- paper:Joseph2021
- paper:Walitt2024
- proposition:0027-pais-group-differences-attenuate-under-objective-re-measurement
- proposition:0028-pais-heterogeneity-explained-by-ascertainment-and-scoring
- proposition:0029-pais-objective-correlate-is-endpoint-and-trigger-specific
source_refs: []
created: '2026-06-24'
updated: '2026-06-24'
---
# Measurement-channel and ascertainment artifacts in PAIS

## Summary

A recurring, cross-hypothesis finding in this project is that apparent PAIS biology is frequently
shaped — sometimes generated — by **how** a phenotype is measured and **who** gets ascertained, rather
than by underlying pathophysiology. The same signal can appear, vanish, or reverse depending on
whether the endpoint is self-reported or objectively measured, which case definition is applied, and
how the cohort was sampled. This topic collects that cross-cutting concern as a first-class
methodological axis so that future analyses pre-commit to distinguishing a measurement-channel
explanation from a biological one. It is the adjacency partner of
`topic:biomarkers-and-objective-endpoints` (which catalogs the objective endpoints themselves) and of
`topic:pais-case-definition-heterogeneity` (which catalogs the definitional variance); this topic is
specifically about the **artifact-vs-biology inference**.

## Key Concepts

- **Measurement-channel axis.** PAIS subphenotypes sort along a self-report ↔ objective-measurement
  axis. The crude female PAIS excess concentrates in self-report channels and is sex-null or reversed
  in objective/hard-endpoint channels (`interpretation:0003-t018-subphenotype-sex-reproductive-stage`).
- **Self-report-only effects.** The female cognitive excess is confined to subjective complaint and
  absent in objective neuropsychological testing
  (`proposition:0010-cognitive-female-excess-is-self-report-only-absent-in-objective-testing`).
- **Baseline-carried vs PAIS-amplified.** A sex/group skew can be inherited from a pre-existing
  baseline rather than created by PAIS — e.g. the dysautonomia female skew tracks the ~5:1 baseline
  POTS female predominance, not a PAIS-specific amplification
  (`proposition:0009-dysautonomia-female-skew-is-baseline-carried-not-pais-amplified`). The male
  vascular reversal raises the mirror-image version of this question (COVID-specific vs baseline
  carryover; see `question:0021`).
- **Endpoint-specificity masquerading as a shared mechanism.** PEM's objective correlates are
  trigger- and endpoint-specific, so choosing one endpoint (e.g. 2-day-CPET) can manufacture or hide
  a "shared failure mode"
  (`proposition:0011-objective-pem-correlates-are-trigger-and-endpoint-specific-not-one-shared-failure-mode`).
- **Case-definition selection.** Which long-COVID/ME-CFS definition is used selects different
  populations, so apparent molecular/mechanistic differences across studies may be definitional rather
  than biological (`question:0014`, `question:0015`, `topic:pais-case-definition-heterogeneity`).
- **Endpoint-breadth manufacturing prevalence (worked case: skin-biopsy SFN).** The single largest
  driver of a cross-study "prevalence" figure can be *what counts as a positive*. In Novak2026 the SFN
  rate climbs **48% → 67% → 91%** on the *identical* long-COVID patients purely by widening the
  abnormality definition from sensory ENFD only → any morphological (ENFD or sweat-gland SGNFD) →
  including functional ESC (`interpretation:0014`). Surprisingly, the percentile *cutoff* rule
  (QASAT > 0 vs ≤5th-percentile) is a *minor* driver: Novak's QASAT ENFD rate for ME/CFS (33.5%)
  nearly matches Joseph2021's strict ≤5th-percentile distal rate (31%). And once trigger is held fixed
  the corpus is concordant (LC ~50–67% across Oaklander + Novak; ME/CFS ~31–33% at the ENFD channel),
  so the apparent 0%→91% "heterogeneity" is partly an artifact of pooling triggers and abnormality
  definitions. Walitt2024 remains the important adjudicated, non-neuropathy-referred counterexample,
  preventing a universal-lesion reading. The lesson: an SFN-prevalence number is uninterpretable without
  stating *trigger + biopsy modality counted + site protocol + cutoff rule + referral stream*.

## Current State of Knowledge

### What the evidence supports

- The female PAIS excess is real but largely measurement-channeled, not uniformly biological
  (`interpretation:0003`, `proposition:0010`).
- Objective-endpoint choice materially changes conclusions about whether a mechanism is shared
  across triggers (`proposition:0011`).

### What is contested or unresolved

- How much of any given group difference is artifact vs biology in the **vascular** domain, where an
  uninfected comparator is missing (`question:0021`).
- Whether requiring PEM in case definitions improves cross-study comparability or just narrows the
  sampling frame (`question:0015`).

### Tensions between papers

- Self-report vs objective measures of the same construct (cognition, fatigue) routinely disagree in
  direction or sex-association, which is the core empirical engine of this topic.
- Skin-biopsy SFN prevalence across PAIS spans 0% (Walitt2024, ME/CFS, adjudicated non-neuropathy-
  referred cohort) to 91% (Novak2026, LC, broadest definition). `interpretation:0014` shows this
  tension is largely resolvable: it decomposes into modality breadth, trigger (LC>ME/CFS), and cohort
  referral-enrichment. Positive referral cohorts support a substantial lesion-positive subset, while
  Walitt's null shows the lesion is not universal and may be cohort-enrichment sensitive.

## Controversies and Open Questions

- Can a project-wide convention be set: every claimed group difference must state which measurement
  channel it lives in and whether a baseline-carryover or ascertainment explanation has been excluded?
- Does the measurement-channel axis itself have a biological correlate (e.g. interoception, illness
  behavior) or is it purely methodological?

## Relevance to This Project

This topic is a standing methodological check on `hypothesis:0001` (case-definition coherence),
`hypothesis:0005` (the sex-excess decomposition), and `hypothesis:0006` (PEM endpoint specificity).
It exists so the "is this artifact?" question is asked **before** a difference is read as mechanism —
the discipline the synthesis identified as recurring but previously un-housed.

## Key References

- Shah2025 (within-age-band menopause null), Aid2025 / Shahbaz2025 / Silva2024 (objective immune
  domain) via `interpretation:0006-t041-objective-female-biased-subphenotype-search`.
- Boneva2015 (ME/CFS early/surgical-menopause directionality) via `interpretation:0026`.
- Appelman2024 / Gattoni2025 (muscle vs whole-body PEM endpoints) via
  `interpretation:0004-t025-pem-stratified-molecular-gap-and-cross-trigger-cpet-dissociation`.
- Oaklander2022 / Joseph2021 / Walitt2024 / Novak2026 (skin-biopsy SFN prevalence harmonization) via
  `interpretation:0014-sfn-prevalence-metric-harmonization-reanalysis`.
