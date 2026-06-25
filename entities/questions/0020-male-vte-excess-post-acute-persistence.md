---
id: question:0020-male-vte-excess-post-acute-persistence
type: question
title: Does the male-biased VTE excess in ambulatory COVID-19 persist into the post-acute
  phase or resolve after the 30-day acute window?
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Xie2022
- paper:Spetz2025
related:
- hypothesis:0004-acute-severity-threshold
- question:0019-male-biased-vascular-signal-pasc-persistence
- proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment
- interpretation:0005-t042-vascular-male-reversal-survives-severity-adjustment
- interpretation:0018-t048-vascular-sex-baseline-carryover-audit
- task:t048
created: '2026-06-22'
updated: '2026-06-25'
---

# Does the male-biased VTE excess in ambulatory COVID-19 persist into the post-acute phase or resolve after the 30-day acute window?

## Summary

> **Partially addressed (2026-06-23, t042 → `proposition:0012`, `interpretation:0005`); narrowed,
> not closed.** t042 established that the male-biased hard-vascular direction survives the coarse
> hospitalized-vs-ambulatory acute-severity boundary, including an 18-month male CV-mortality excess
> (Kopp2024) and a 30-day male VTE excess in ambulatory patients (Xie2022). But Kopp2024 is *CV
> mortality*, not late VTE, and Xie2022 is only the 30-day acute window: the specific question here
> — sex-stratified VTE incidence in the **31–180-day** post-acute window in ambulatory cohorts —
> remains an open gap. Kept as the narrower VTE-temporal companion to the substantially resolved
> CV question `question:0019`.
>
> **t048 update (2026-06-25): partial positive, not closed.** Spetz2025 shows DVT and PE risk remain
> elevated in the 91-180 day window overall (DVT HR 1.20; PE HR 1.29) and that mild/non-hospitalized
> COVID-19 carries elevated DVT/PE risk overall (DVT HR 1.41; PE HR 1.78). However, the paper does not
> report the sex-stratified 31-180 day estimate within the non-hospitalized stratum, so the exact
> late-ambulatory male-VTE persistence question remains open.

Xie2022 demonstrates that male sex is an independent VTE risk factor within ambulatory (non-hospitalized) COVID-19 patients (aHR 1.69, 95% CI 1.30–2.19), with the 30-day acute window as the observation period. The question is whether this male-biased thrombotic excess is strictly an acute-phase phenomenon that resolves once the infection clears, or whether it seeds downstream post-acute thromboinflammatory pathology — microclots, small-fiber neuropathy, cardiovascular sequelae — that persists into long COVID.

## Why It Matters

- Determines whether the male-biased acute VTE excess (Xie2022) is mechanistically upstream of the male-biased cardiovascular PASC phenotype, or whether the two are independent processes.
- If the acute VTE signal persists post-acutely, male sex becomes a priority stratification variable for thromboprophylaxis trials in PAIS and for identifying post-acute thromboinflammatory endophenotypes.
- Unanswered, this leaves open whether the acute-phase thromboinflammation mechanism (microclots, endothelial activation) is the same biological process running at lower amplitude in the post-acute phase, or a distinct acute-only insult.

## Current Evidence

- **Supporting persistence:** The acute thromboinflammatory mechanism (platelet activation, endothelial injury, fibrin microclots) is not acutely self-limited — microclot evidence in PASC patients (CerviaHasler2024) suggests ongoing coagulation dysregulation well beyond 30 days. Male sex is associated with greater platelet reactivity and endothelial dysfunction at baseline, which may not fully normalize post-infection.
- **Supporting persistence:** Spetz2025 adds population-register evidence that DVT and PE remain elevated in the 91-180 day window overall, and that mild/non-hospitalized infection has elevated DVT/PE risk overall.
- **Against persistence / uncertainty:** Xie2022 only measured 30-day VTE; no post-acute follow-up data available from this cohort. The VA cohort studies of post-acute cardiovascular outcomes (e.g. Xie2024 / Al-Aly data) use administrative codes and do not stratify acute-phase VTE risk by sex at the ambulatory level.
- **Gap:** No ambulatory-only sex-stratified study of long-COVID thromboinflammatory sequelae (DVT/PE at 31-180 days, microclot burden, or cardiovascular PASC by sex) was found in the current literature batch; Spetz2025 reports the needed dimensions separately but not crossed.

## Thoughts

- The best current interpretation is that post-acute DVT/PE persistence is real at the population level through at least 91-180 days, but the sex-specific ambulatory component remains unidentified.
- The major uncertainty is the joint estimator: sex-stratified ambulatory VTE or thromboinflammatory biomarker follow-up beyond 30 days post-COVID-19.

## Connections to Project

- Related hypotheses: `hypothesis:0004-acute-severity-threshold` (this question probes whether thromboinflammatory risk factors operate independently of severity-gating); implicitly also relevant to the shared-failure-mode attractor (hypothesis:0001) if thromboinflammation is a persistent mechanism.
- Required data or analyses: Sex-stratified longitudinal VTE incidence beyond 30 days in ambulatory COVID-19 cohorts; or sex-stratified microclot / endothelial biomarker follow-up at 3, 6, 12 months in PASC cohorts.
- Priority level: P2 — important for mechanism framing but not blocking current analyses.

## Related

- Topic notes: Thromboinflammation as a PAIS mechanism (no dedicated topic entity yet).
- Article notes: `paper:Xie2022` (the seed study), `paper:CerviaHasler2024` (microclots in PASC).
- Methods/Datasets: UK Biobank extended follow-up; Al-Aly/VA post-acute cardiovascular outcomes datasets (sex-stratified analysis needed).
