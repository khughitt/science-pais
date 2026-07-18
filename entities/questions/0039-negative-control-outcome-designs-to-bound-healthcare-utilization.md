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
pre-existing multimorbidity rather than genuine pathophysiology. This **extends** the numerical
bounding of `hypothesis:0008` that Nilforoshan2026 has already begun for long COVID (test-based
prospective design + NC-outcome bias benchmarking) toward a cross-trigger, DiD-based, reproducible
form.

## Why It Matters

- **Decision it affects:** how much of cross-study PAIS burden and group differences to attribute to
  biology vs measurement — the core of `hypothesis:0008` and of the measurement-ascertainment topic.
- **Risk if unanswered:** the project (and field) keep comparing incidence estimates that bake in
  uncorrected ascertainment bias, undermining every cross-cohort comparison.

## Current Evidence

- **The method is mature and directly applicable.** Yang2024 provides a taxonomy of negative-control
  exposure/outcome/population designs for bounding unmeasured confounding; Zhang2025 gives an
  NC-calibrated DiD estimator applicable to infected-vs-uninfected PAIS incidence comparisons.
- **Formal NCs have already been deployed for long COVID — h0008 is partly bounded, not unbounded.**
  Hua2024's umbrella review (2024 cutoff) noted the field had *not yet* deployed formal negative
  controls; but Nilforoshan2026 (already project-held) subsequently did, at 245M-patient claims scale:
  49 negative-control outcomes (e.g. firearm injury, lightning/drowning) benchmark bias, showing the
  **conventional design falsely detects 53.1% of NC outcomes as significant** while a test-based
  prospective design drops this to 4.1% — and correcting the long-COVID attributable burden downward by
  roughly an order of magnitude. So the ascertainment-inflation that `hypothesis:0008` predicts is
  already empirically demonstrated for long COVID.
- **The remaining gap is narrower** than "no NCs anywhere": (a) no PAIS-specific NC-*calibrated DiD*
  (Zhang2025's estimator, distinct from Nilforoshan's test-based / synthetic-control design); (b) no
  cross-trigger implementation (post-Lyme / post-sepsis / post-dengue); (c) no **open,
  third-party-reproducible** data vehicle — Nilforoshan used proprietary Komodo claims.

## Thoughts

- **Best current interpretation:** unlike `question:0030`'s TTE, an NC-DiD can *in principle* run on a
  downloadable claims/EHR sample, making it the most *admissible* of the ascertainment-bounding
  vehicles. Its value now is not to establish that ascertainment inflation exists (Nilforoshan2026
  already showed that for long COVID) but to **refine and generalize** that bound — a complementary
  DiD estimator, cross-trigger, on an open vehicle.
- **Major remaining uncertainty:** choice of valid negative-control outcomes (they must share the
  confounder structure without post-infectious biology — a domain-judgment, falsification-checked step);
  and — the binding constraint — whether a transparent, third-party-reproducible cohort with the needed
  exposure/outcome structure exists at all, since Nilforoshan's own demonstration ran on proprietary
  data (the open-vehicle gap, not the method, is what blocks this within D-004).
- **Priority:** P2 — high-leverage and the most-admissible bias-bounding design; it refines rather than
  originates the numerical bound on `hypothesis:0008`.

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
