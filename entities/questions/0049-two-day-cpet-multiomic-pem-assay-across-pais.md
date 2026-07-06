---
id: question:0049-two-day-cpet-multiomic-pem-assay-across-pais
kind: question
title: Standardized 2-day CPET with concurrent multi-omic sampling as mechanistic
  PEM assay across PAIS
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Gattoni2025
- cite:Appelman2024
origins:
- type: assistant
  ref: explore-ideas-methodology
related:
- question:0028-ambulatory-within-person-wearable-ema-protocol-for-pem-phenotyping
- question:0011-mitochondrial-basis-of-pem
- question:0015-does-pem-requirement-improve-cross-study-comparability
- hypothesis:0017-pem-overdiagnosed-via-self-report-nonspecific
created: '2026-07-06'
updated: '2026-07-06'
added_by: explore-ideas:claude-opus-4-8:cand-methodology-cpet-multiomics-pem
lens_views:
- lens: methodology
  rationale: Existing 2-day CPET studies conflict on whether physiological variables
    change between days, partly because protocols vary and most capture only functional
    measurements without concurrent molecular sampling. Adding standardized multi-omic
    time points to the exercise challenge could reveal immune/metabolic perturbations
    even when ventilatory parameters are preserved, and would enable cross-PAIS syndrome
    comparison for the first time. This is distinct from the project's question:0028,
    which deliberately phenotypes PEM ambulatorily *without* exercise challenge; here
    the challenge is the instrument. Appelman 2024's exercise-challenge muscle multi-omics
    shows the design already yields mechanistic signal that pure CPET physiology misses.
  origin_ref: explore-ideas-methodology
---
# Standardized 2-day CPET with concurrent multi-omic sampling as mechanistic PEM assay across PAIS

## Summary

Would a harmonized 2-day cardiopulmonary exercise test (CPET) protocol with paired multi-omic blood
sampling (immune phenotyping, proteomics, metabolomics) at fixed pre-, during-, and 24-hour
post-challenge time points yield **reproducible, diagnostically discriminant PEM signatures** — and do
those signatures differ between long COVID, ME/CFS, and PTLDS versus non-PAIS fatigue controls? The
motivating premise is that PEM is the field's most-cited discriminating feature yet is largely
self-reported; a *molecular-plus-physiology* provocation assay could make it objectively measurable and
testable for cross-trigger convergence.

## Why It Matters

- **Decision it affects:** whether the project (and the field) should invest in a molecular-plus-physiology
  PEM assay rather than physiology-only 2-day CPET, and whether PEM biology is shared across triggers or
  trigger-specific. A validated objective assay would also give `question:0015` (does a PEM requirement
  improve cross-study comparability) an operational endpoint.
- **Risk if unanswered:** PEM remains defined by questionnaire, keeping cohorts cross-study incomparable
  and case definitions unstable; and 2-day CPET *alone* appears underpowered to capture PEM biology, so
  physiology-only replication may keep returning nulls that are mistaken for "no PEM."

## Current Evidence

- **Supporting:** Appelman2024 shows exercise-challenge muscle biopsy plus multi-omics reveals
  mitochondrial/metabolic abnormalities after PEM that are invisible to functional CPET — direct
  motivation for pairing molecular sampling with the physiological challenge. Keller2014 anchors the
  reproducible 2-day-CPET workload/VO₂ decrement in ME/CFS, establishing that a provocation paradigm can
  elicit an objective signal.
- **Conflicting / limiting:** Gattoni2025 found *no* significant day-2 functional-CPET decrement in a
  small (n≈15), PEM-enriched long-COVID cohort — i.e. standard physiological variables may not
  differentiate PEM, which is precisely why concurrent molecular readouts are proposed. Exercise
  provocation also carries real harms in severe PEM patients (an ethical and recruitment constraint), and
  reproducibility/diagnostic-discriminance of any candidate signature is unproven.

## Thoughts

- **Best current interpretation:** the Appelman-vs-Gattoni contrast suggests the PEM signal is molecular
  before it is reliably physiological; a paired multi-omic protocol is the most promising route to an
  objective, transferable PEM endpoint.
- **Major uncertainty:** whether such signatures are reproducible across sites and *discriminant* between
  PAIS and non-PAIS fatigue — and whether they converge or diverge across triggers (the cross-trigger
  question this project cares about most).

## Connections to Project

- Related hypotheses: complements `question:0011-mitochondrial-basis-of-pem` and the deconditioning/nocebo
  rivals in `question:0017`; provides the objective assay `hypothesis:0017` (PEM overdiagnosed via
  self-report) could be tested against.
- Required datasets: a new prospective 2-day-CPET + paired multi-omic cohort spanning ≥2 triggers with
  non-PAIS fatigue controls (`source_refs` anchor the physiological/biopsy precedent).
- Required analyses: harmonized multi-omic PEM-signature discovery; test–retest reproducibility;
  cross-trigger and case-vs-control discrimination.
- Priority level: P2 — high-value objective endpoint, but resource-intensive and requiring careful
  harms mitigation.

## Related

- Topic notes: `topic:biomarkers-and-objective-endpoints`, `topic:mecfs-long-covid-convergence`.
- Article notes: Gattoni2025 (2-day CPET null in long COVID), Appelman2024 (post-PEM muscle multi-omics),
  Keller2014 (ME/CFS 2-day-CPET decrement).
- Methods/Datasets: complements the ambulatory wearable/EMA PEM protocol in
  `question:0028-ambulatory-within-person-wearable-ema-protocol-for-pem-phenotyping`.

## Notes

- 2026-07-06: Complementary temporal readout: alongside the discriminant multi-omic signature, quantify the recovery trajectory after provocation (time and shape of return to pre-challenge mitochondrial, immune, and functional-capacity levels over 24-96h) as a longitudinal severity biomarker and objective trial endpoint. (explore-ideas 2026-07-06 · cand-temporal-pem-recovery-kinetics-biomarker; anchors in meta:explore-2026-07-06)