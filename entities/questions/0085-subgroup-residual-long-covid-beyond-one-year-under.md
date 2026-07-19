---
id: question:0085-subgroup-residual-long-covid-beyond-one-year-under
kind: question
title: Which subgroups retain attributable long COVID effects beyond one year under
  ascertainment-corrected study designs?
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Nilforoshan2026
related:
- hypothesis:0004-acute-severity-threshold
- hypothesis:0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- interpretation:0043-t127-nilforoshan-recover-design-sensitivity-reconciliation
- paper:Thaweethai2023
- paper:Cai2024
created: '2026-07-10'
updated: '2026-07-19'
---

# Which subgroups retain attributable long COVID effects beyond one year under ascertainment-corrected study designs?

## Summary

Nilforoshan2026 finds zero attributable long COVID outcomes at 360–720 days (days 12–24 months post-infection) under their test-based prospective design across 244.7 million patients. However, this is a **population average** with a conservative RR ≥ 1.1 detection threshold and known ~10–20% negative bias. The null finding could mask genuine persistent effects in specific subgroups: hospitalized / severely ill patients, immunocompromised individuals, those with specific comorbidities, unvaccinated patients, or those with early-wave (Delta / pre-Omicron) infections. The question asks: when the ascertainment-correction logic of Nilforoshan2026 is applied within specific strata, which subgroups retain statistically and clinically meaningful attributable effects beyond one year?

## Why It Matters

- Directly determines the validity of hypothesis:0004 (acute severity threshold predicts self-sustaining PAIS): if the population mean recovers by 1 year but hospitalized patients do not, the threshold model is supported.
- Determines whether hypothesis:0010 (slow recovery gradient) describes the entire population or only a majority, with a small tail that is truly chronic.
- High clinical stakes: if no subgroup retains measurable effects beyond 1 year even under corrected designs, the policy case for long-term care programs for >1-year long COVID is weakened. If a severe-acute-illness subgroup retains effects, it targets intervention.
- The question also addresses the interpretation of RECOVER and other clinical cohort findings that find persistent effects in selected patients beyond 1 year — are those samples enriched for the subgroup that escapes population-average recovery?

## Current Evidence

- Nilforoshan2026: zero ICD outcomes clearing the compound RR ≥ 1.1 + Bonferroni threshold at 360–720 days (the authors gloss this as population health "returning to baseline"). Run on the **test-based analytic cohort — a subset** of the 244.7M-patient Komodo database (individuals enrolled at their first PCR test), not all 244.7M. Conservative threshold and ~10–20% author-estimated attenuation acknowledged; no subgroup stratification reported.
- Cai2024 (Xie, Topol, Al-Aly, Nature Medicine): three-year outcomes from VA cohort (predominantly male, older, comorbid) showing persistent multi-system effects at 3 years under conventional design. Not ascertainment-controlled; population is severity-enriched relative to Nilforoshan2026.
- RECOVER adult cohort (Thaweethai2023): clinical cohort with diverse enrollment and prospective symptom capture; finds persistent symptom clusters at 6–12 months. Not ascertainment-controlled in the same way, but prospectively enrolled with broad symptom capture.
- Hypothesis:0010 (from RECOVER trajectory data): 5% of participants in persistently high symptom stratum at 15 months; 36% near-minimal by 15 months; heterogeneous recovery trajectories at the individual level.
- **Cross-design reconciliation (`interpretation:0043` / t127, 2026-07-19):** placing Nilforoshan2026, RECOVER (`paper:Thaweethai2023`; trajectory classes from `cite:Thaweethai2025`), and the severity-enriched VA 3-year cohort (`paper:Cai2024`) side by side **does not adjudicate** the residual tail — the three differ simultaneously in estimand, measurement channel, ascertainment control, variant era, and severity mix. Nilforoshan's zero-outcome result is **uninformative about** (not a refutation of, and not proven blind to) a small subjective-symptom subgroup: claims capture the PRO fatigue/PEM/cognitive construct with **low, unquantified sensitivity**, dilution pushes any single-code RR toward the 1.1 floor, and no power/mixture-sensitivity analysis establishes invisibility. RECOVER's ~5% persistent-high class is PRO-defined and channel-mismatched to claims; Cai2024's severity-concentrated persistence (hospitalized: 29% elevated year-3 death risk) is **not** ascertainment-controlled. The three are mutually **compatible** with a severity-threshold reading (`hypothesis:0004`) but the inference is **ecological and underidentified** (between-study confounding). The discriminating design is unchanged and unmet: the test-based logic run **within acute-severity strata**.

## Thoughts

- The population-average null at 360–720 days is most plausibly correct for the broad PCR-tested population, which includes many mild cases. This is not inconsistent with a small (<5%) subgroup of severe-acute-illness patients who remain symptomatic at 1–2 years — this tail is invisible in population-level estimates but clinically significant.
- The most actionable stratum is hospitalization status: if the test-based design shows no effects at 360–720 days even in patients who were hospitalized during the acute phase, then "genuine chronic long COVID" is rare even among the severely ill. If hospitalized patients retain effects, the threshold model gains direct support.
- The ~10–20% conservative bias in Nilforoshan2026 means that an effect of RR 1.05–1.1 in the full population could be real but missed. In a severity-enriched subgroup (higher baseline rate of the outcome), the same absolute excess would manifest as a higher RR that crosses the detection threshold.
- Major uncertainty: Komodo Health may not capture hospitalization severity well enough for meaningful stratification; also, the most severely ill patients (ICU) may be harder to match to test-negative controls with comparable acute severity.

## Connections to Project

- Related hypotheses: hypothesis:0004 (acute severity threshold — the key question is whether the threshold prediction holds under the corrected design in severity strata); hypothesis:0010 (recovery gradient — whether a truly chronic 5% tail exists vs slow converging mean); hypothesis:0008 (methodological control — whether ascertainment bias accounts for virtually all apparent >1-year effects even in severe subgroups).
- Required datasets: Komodo Health or equivalent claims data with hospitalization-severity stratification + test-based design; RECOVER IPD for severity-stratified trajectory analysis.
- Required analyses: Re-run Nilforoshan2026 test-based design restricted to hospitalized acute cases (ICU / non-ICU) vs never-hospitalized PCR-positive cases; compare 360–720 day outcome counts.
- Priority level: high — this is the central interpretive gap in Nilforoshan2026 and determines whether hypothesis:0004 is supported or undermined by this study.

## Related

- Topic notes: `topic:shared-failure-mode-across-pais`; `topic:population-boundary-conditions-and-effect-modifiers-in-pais`
- Article notes: `paper:Nilforoshan2026`; `paper:Cai2024` (if present); RECOVER (Thaweethai2023)
- Methods/Datasets: Komodo Health (Nilforoshan2026 dataset); VA CDW (Al-Aly studies); RECOVER IPD
