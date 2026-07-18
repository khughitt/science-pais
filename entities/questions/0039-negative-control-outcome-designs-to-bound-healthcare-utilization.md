---
id: question:0039-negative-control-outcome-designs-to-bound-healthcare-utilization
kind: question
title: Negative-control outcome designs to bound healthcare-utilization confounding
  in PAIS incidence estimates
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Nilforoshan2026
- cite:Yang2024
- cite:Hua2024
- cite:Zhang2025
origins:
- type: assistant
  ref: explore-ideas-methodology
related:
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- question:0030-target-trial-emulation-in-multi-trigger-ehr-cohorts-for-cross-pais
- topic:measurement-ascertainment-artifacts-in-pais
- theme:0003-demonstrability-ceiling-cross-pathogen-design
created: '2026-07-04'
updated: '2026-07-18'
added_by: explore-ideas:claude-opus-4-8:cand-methodology-negative-control-outcome-ascertainment-bias
lens_views:
- lens: methodology
  rationale: "hypothesis:0008 asserts measurement-channel and ascertainment bias predictably\
    \ shapes apparent PAIS group differences; this supplies the concrete design that\
    \ converts that qualitative claim into a numerical bound. NC-calibrated difference-in-differences\
    \ with biologically irrelevant outcomes quantifies health-seeking and multimorbidity\
    \ confounding \u2014 a reproducibility-enabling step for cross-study comparison.\n"
  origin_ref: explore-ideas-methodology
---
# Negative-control outcome designs to bound healthcare-utilization confounding in PAIS incidence estimates

## Summary

Negative-control-outcome (NCO) designs use outcomes that share PAIS's healthcare-utilization /
ascertainment / multimorbidity confounders but have **no plausible post-infectious biology** to
calibrate reported PAIS incidence and risk-factor associations in observational EHR/claims cohorts. A
negative-control-calibrated difference-in-differences (NC-DiD) estimator quantifies how much of the
reported excess PAIS burden is attributable to differential health-seeking, surveillance intensity, or
pre-existing multimorbidity rather than genuine pathophysiology. This is the concrete design that
converts `hypothesis:0008`'s qualitative ascertainment claim into a numerical bound.

## Why It Matters

- **Decision it affects:** how much of cross-study PAIS burden and group differences to attribute to
  biology vs measurement — the core of `hypothesis:0008` and of the measurement-ascertainment topic.
- **Risk if unanswered:** the project (and field) keep comparing incidence estimates that bake in
  uncorrected ascertainment bias, undermining every cross-cohort comparison.

## Current Evidence

- **The method is mature and directly applicable.** Yang2024 provides a taxonomy of negative-control
  exposure/outcome/population designs for bounding unmeasured confounding; Zhang2025 gives an
  NC-calibrated DiD estimator applicable to infected-vs-uninfected PAIS incidence comparisons.
- **The gap is documented and unfilled.** Hua2024's umbrella review of long-COVID observational studies
  catalogs ascertainment/utilization/self-report biases and notes that **no study has deployed formal
  negative-control outcomes** to bound them. Nilforoshan2026 (already project-held) is the adjacency
  anchor on the measurement axis.

## Thoughts

- **Best current interpretation:** unlike `question:0030`'s TTE, an NC-DiD can in principle run on a
  downloadable claims/EHR sample, making it the most *admissible* of the ascertainment-bounding vehicles
  — the concrete operationalization of `hypothesis:0008` rather than a new hypothesis.
- **Major remaining uncertainty:** choice of valid negative-control outcomes (they must share the
  confounder structure without post-infectious biology — a domain-judgment, falsification-checked step),
  and whether a transparent, third-party-reproducible cohort with the needed exposure/outcome structure
  is obtainable within D-004 (NC-DiD on a public claims sample is the target).
- **Priority:** P2 — highest-leverage, most-admissible bias-bounding design; it directly numeric-izes
  `hypothesis:0008`.

## Connections to Project

- Related hypotheses: `hypothesis:0008` (this design converts its qualitative claim into a bound).
- Related questions / topic / theme: `question:0030` (sibling EHR-design vehicle);
  `topic:measurement-ascertainment-artifacts-in-pais`; `theme:0003` (named vehicle).
- Required datasets: downloadable EHR/claims with infected/uninfected exposure + candidate NC outcomes.
- Required analyses: NC-DiD (Zhang2025); NC-outcome selection + falsification (Yang2024).
- Priority level: P2.

## Related

- Topic notes: `topic:measurement-ascertainment-artifacts-in-pais`;
  `theme:0003-demonstrability-ceiling-cross-pathogen-design`.
- Article notes: `cite:Yang2024`, `cite:Hua2024`, `cite:Zhang2025`, `cite:Nilforoshan2026`.
- Methods/Datasets: `question:0030` (companion target-trial-emulation vehicle).
