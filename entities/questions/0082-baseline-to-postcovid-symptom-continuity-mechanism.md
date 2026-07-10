---
id: question:0082-baseline-to-postcovid-symptom-continuity-mechanism
kind: question
title: Is the correlation between baseline and post-COVID symptoms in long illness
  explained by biological continuity or reporting behaviour?
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Sudre2024
related:
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- paper:Sudre2024
- question:0075-pre-covid-symptom-burden-vulnerability-vs
created: '2026-07-10'
updated: '2026-07-10'
---

# Is the correlation between baseline and post-COVID symptoms in long illness explained by biological continuity or reporting behaviour?

## Summary

In Sudre2024 (ZOE COVID Symptom Study, n=1350 long illness), nearly all post-COVID symptoms at 8–12
weeks were more likely to be present if the same symptom was reported in the pre-COVID baseline (4–8
weeks before infection), and baseline symptom burden linearly predicted post-COVID burden (+5.6% per
additional baseline symptom). This symptom concordance between baseline and post-COVID periods could
reflect: (a) biological continuity — pre-existing pathophysiology (e.g., atopic inflammation, autonomic
dysregulation, metabolic disorder) that persists through and is worsened or unmasked by COVID-19; or
(b) reporting-behavioural continuity — individuals who tend to notice and log symptoms pre-COVID
continue that behaviour post-COVID, inflating apparent post-COVID burden without indicating new
pathology. The paper cannot distinguish these because all data are self-reported and no objective
measurement or uninfected control group is included in the case-control arm.

## Why It Matters

- **Decision: interpretation of post-COVID symptom burden estimates.** If continuity is biological, the
  pre-COVID symptom profile is a valid risk stratifier for PAIS severity and informs subphenotyping.
  If it is behavioural, then cohort studies enriched for high baseline-symptom reporters will
  systematically overestimate PAIS symptom burden, and trials measuring self-reported outcomes in such
  cohorts will show apparent regression to mean rather than genuine treatment effects.
- **Decision: case definition discipline.** The "new or worsened symptoms" clause in OSC/PCS definitions
  (WHO 2021) is designed to exclude baseline-continuation; operationalising this clause requires knowing
  whether symptom continuity is pathological or behavioural.
- **Risk if unanswered:** Post-COVID clinical assessments treating all symptom continuity as pathological
  continuation of COVID-19 may misattribute pre-existing conditions as PAIS sequelae, leading to
  mismanagement and inflated healthcare burden estimates.

## Current Evidence

- **Sudre2024 (prospective self-report):** Baseline-to-post-COVID symptom concordance is strong in long
  illness for almost all symptoms, with one exception: anosmia/dysosmia is *less* likely post-COVID if
  present at baseline (OR 0.75). The exception may reflect that anosmia has a more specific infectious
  aetiology (COVID-19 olfactory nerve tropism), making post-COVID anosmia less tied to a pre-existing
  reporting pattern. The concordance pattern is consistent with either biological or behavioural
  continuity, or most plausibly a mixture.
- **Dutch Lifelines (Ballering 2022):** By including uninfected controls in a matched panel design,
  demonstrated that 21.4% of COVID-19 cases had substantial symptom increases at 90–150 days vs
  8.7% of controls — a design that can begin to separate attributable from background trajectories.
  However, this addresses attribution to infection, not the baseline-continuity mechanism within cases.
- **Walitt 2024 [@Walitt2024] (RECOVER ME/CFS):** In long COVID vs healthy controls, subjective
  cognitive complaint excess was not matched by objective neuropsychological test differences —
  directly demonstrating that some self-report excess reflects reporting behaviour, not objective
  biological change, in at least the cognitive domain.
- **No study within ZOE data** has yet paired the app-logged symptom trajectories with objective
  biomarkers or clinical records to test which symptom domains show biological versus pure reporting
  continuity.

## Thoughts

- **Best current interpretation:** Continuity is likely both components operating simultaneously, with
  relative contributions varying by symptom domain. Somatic pain, fatigue, and mood symptoms are
  plausibly more reporting-sensitive; anosmia/dysosmia and objective cardiorespiratory symptoms may
  have more biological continuity. The anosmia exception in Sudre2024 is a test-case for this
  domain-specificity hypothesis.
- **Major uncertainty:** Without an uninfected control group in the case-control arm, or objective
  measurement for even a subset of symptoms, Sudre2024 cannot separate pathophysiological persistence
  from reporting persistence. Adding an objective endpoint stratum (e.g., spirometry, CPET, autonomic
  testing) to an app-linked substudy would be the most efficient discriminating design.

## Connections to Project

- Related hypotheses: `hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent`
  (M1 channel-direction regularity: self-report continuity as a candidate reporting-channel artifact);
  `hypothesis:0020-host-immune-baseline-reserve-gate` (biological continuity interpretation);
  `hypothesis:0001-shared-dysregulated-attractor` (attractor persistence would produce biological
  symptom continuity even after apparent recovery).
- Required data or analyses: objective symptom endpoint substudy paired with ZOE app data; matched
  uninfected control arm in the long-illness case-control; Mendelian randomisation of symptom reporting
  propensity; symptom-specific domain analysis separating objective-correlatable from self-report-only
  symptoms.
- Priority level: Medium — subsidiary to `question:0075` (the mechanism question), but important for
  interpreting PAIS symptom-burden estimates and for designing clinical endpoints in treatment trials.

## Related

- Topic notes: `topic:measurement-ascertainment-artifacts-in-pais`; `topic:pais-case-definition-heterogeneity`
- Article notes: `paper:Sudre2024` (source); Ballering 2022 (uninfected-control design comparator);
  Walitt 2024 [@Walitt2024] (objective vs subjective dissociation anchor)
- Methods/Datasets: ZOE COVID Symptom Study (UK SAIL/HDRUK platform); RECOVER-LC cohort (if symptom
  trajectory data linked to objective endpoints are available)
