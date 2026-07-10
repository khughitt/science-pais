---
id: question:0079-ascertainment-controlled-designs-for-non-covid
kind: question
title: Can test-based prospective designs for ascertainment control be adapted to
  non-COVID PAIS triggers?
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Nilforoshan2026
related:
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- question:0039-negative-control-outcome-designs-to-bound-healthcare-utilization
created: '2026-07-10'
updated: '2026-07-10'
---

# Can test-based prospective designs for ascertainment control be adapted to non-COVID PAIS triggers?

## Summary

Nilforoshan2026 demonstrates that a **test-based prospective design** — enrolling individuals at the moment of their first COVID-19 PCR test and comparing positive to negative testers — dramatically reduces selection bias in long COVID estimates (false-positive rate on negative controls: 53.1% → 4.1%). This design exploits pandemic-era mass PCR testing infrastructure: nearly everyone who visited a healthcare center for COVID-related reasons received a PCR test, providing a natural matched-exposure design. The question is whether an equivalent ascertainment-controlled design can be constructed for other PAIS triggers (EBV/mononucleosis, Lyme disease, dengue, Q fever, post-influenza fatigue) where systematic same-healthcare-visit test-negative controls do not exist.

## Why It Matters

- Determines whether the large ascertainment-bias correction demonstrated by Nilforoshan2026 is a COVID-specific methodological windfall or can be generalized to cross-trigger PAIS comparisons in this project.
- If the test-based approach cannot be replicated for non-COVID triggers, cross-trigger prevalence estimates remain on unequal methodological footing, making hypothesis:0001 (shared PAIS attractor) and cross-trigger comparisons structurally confounded.
- Without ascertainment-controlled designs for non-COVID triggers, apparent differences in PAIS incidence across triggers may primarily reflect testing and care-seeking differences rather than true biological differences — undermining the project's cross-trigger comparative framework.

## Current Evidence

- Nilforoshan2026 demonstrates the design at scale for COVID-19 (n = 244.7M patients; false-positive correction from 53.1% to 4.1% on 49 negative controls; RR collapse at 360–720 days to zero attributable outcomes).
- Systematic PCR testing of matched healthcare visitors is unique to COVID-19 pandemic infrastructure. No equivalent universal test-negative comparator exists for EBV, Lyme, dengue, or influenza in routine clinical care.
- Test-negative designs have been used in influenza vaccine effectiveness studies (comparing vaccinated PCR+ flu to vaccinated PCR− flu patients seeking care with ILI), providing a partial precedent for the test-negative denominator approach.
- Ballering2022 (the Lifelines cohort) and the RECOVER study use symptom-matched or community controls with varying ascertainment, demonstrating that the methodological gap is recognized but not resolved for most triggers.

## Thoughts

- The key structural feature of the COVID-19 test-based design is that PCR testing was routinely applied to all healthcare visitors at a healthcare encounter, not just those with COVID-specific suspicion. This created a natural denominator of "visited healthcare + received test." This feature likely cannot be retroactively replicated for EBV or Lyme, where serological testing is selectively ordered based on clinical suspicion.
- A practical approximation: for Lyme disease, comparing patients in endemic regions who received serological testing and tested positive vs negative for B. burgdorferi — restricting to those tested for the same presenting reason — might approximate the COVID design, but clinical indications for testing are more heterogeneous.
- The major uncertainty is whether the magnitude of ascertainment bias in non-COVID PAIS studies is similar to (53% false positive) or substantially different from the COVID case. If non-COVID triggers involve less selective testing pressure, conventional designs may be less biased.

## Connections to Project

- Related hypotheses: hypothesis:0008 (the foundational methodological claim that ascertainment bias drives apparent PAIS group differences); hypothesis:0001 (cross-trigger shared attractor requires comparable ascertainment-controlled estimates to be credible).
- Required datasets: trigger-specific clinical datasets with matched test-negative controls or population-representative exposure + outcome data.
- Required analyses: design simulation comparing (a) clinically suspected + tested positive vs (b) clinically suspected + tested negative for EBV, Lyme, or influenza using existing cohorts.
- Priority level: medium — foundational for cross-trigger comparative work but requires specialized datasets not currently in the project.

## Related

- Topic notes: `topic:measurement-ascertainment-artifacts-in-pais`; `topic:pais-case-definition-heterogeneity`
- Article notes: `paper:Nilforoshan2026`; `question:0039-negative-control-outcome-designs-to-bound-healthcare-utilization`
- Methods/Datasets: Test-negative design literature from influenza VE studies; RECOVER cohort design (Thaweethai2023)
