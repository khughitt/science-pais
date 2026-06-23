---
id: proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment
type: proposition
title: The PAIS vascular-thromboinflammatory hard-endpoint domain is male-biased and
  the reversal survives acute-severity adjustment
status: active
claim_layer: empirical_regularity
identification_strength: observational
proxy_directness: direct
supports_scope: hypothesis_bundle
discusses:
- frame: hypothesis:0004-acute-severity-threshold
  role: background
related:
- question:0007-mechanism-of-female-predominance-in-pais
- interpretation:0003-t018-subphenotype-sex-reproductive-stage
- proposition:0007-vascular-autonomic-pathways-contribute-to-the-stage-pais-link
- proposition:0008-female-excess-concentrates-in-post-acute-persistence
- proposition:0009-dysautonomia-female-skew-is-baseline-carried-not-pais-amplified
- hypothesis:0004-acute-severity-threshold
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- task:t042
source_refs:
- paper:Xie2022
- paper:Kopp2024
- paper:Abubasheer2025
- paper:Ambrosino2021
created: '2026-06-23'
updated: '2026-06-23'
---
# Proposition: The PAIS vascular-thromboinflammatory hard-endpoint domain is male-biased and the reversal survives acute-severity adjustment

## Claim

Across **hard thrombotic and cardiovascular endpoints** after SARS-CoV-2 infection — venous thromboembolism (VTE) and cardiovascular mortality — the post-acute risk is **male-biased**, the reverse of the overall female PAIS skew, and this male excess **persists within acute-severity strata and after multivariable adjustment**, so it is a **genuine domain reversal**, not merely acute-severity carryover. The decisive discriminator is that the male VTE excess is present in **ambulatory (non-hospitalized = lowest-severity) patients** (Xie2022 adjusted HR 1.69), not only in hospitalized cohorts; and that the male cardiovascular-mortality excess persists **within a hospitalized-restricted (severity-controlled) cohort** (Kopp2024 Delta-wave HR 1.68). This is an `empirical_regularity` about the **sex direction** of one subphenotype domain; it is deliberately agnostic about mechanism and does not claim the male excess is COVID-*specific* amplification (see Caveats).

## Evidence Summary

All `literature_evidence`. The claim has two sub-parts — (A) the domain is male-biased, (B) the bias survives severity adjustment — bracketed by evidence in **both** severity strata:

- **Low-severity stratum (the decisive test)** — Xie2022 (UKBB population cohort, 18,818 ambulatory COVID-19 outpatients vs 93,179 propensity-matched uninfected; hospitalized-at-test excluded) finds **male sex an independent risk factor for incident VTE, adjusted HR 1.69 (95% CI 1.30–2.19)** after adjustment for age, obesity, vaccination, cancer, and comorbidity count. Male excess in the *lowest* acute-severity stratum directly refutes a pure acute-severity-carryover reading. See `evidence-line:0029`.
- **High-severity stratum (severity-restricted)** — Kopp2024 (4,509 patients **all hospitalized** with moderate-to-severe COVID-19 pneumonia) finds higher 18-month CV mortality in men (Delta wave 6.13% vs 3.62%, p=0.017; combined CV endpoint 16.87% vs 12.61%), with **male sex an independent predictor in multivariable Cox, HR 1.68 (1.005–2.796), p=0.048** — i.e. the male excess holds *within* a hospitalized (high-severity) population. Wave-heterogeneous: significant in Delta only. See `evidence-line:0030`.
- **Cross-study breadth (direction)** — Abubasheer2025 meta-analysis pools a male excess across hard endpoints (VTE RR 1.43 [1.19–1.71]; MI RR 1.24; plus ischemic stroke, mortality, major bleeding RR 1.22). Establishes the male *direction* is reproducible across cohorts; severity adjustment is **not** established at the meta level (the pooled studies are mostly hospitalized and not severity-stratified), so this line supports sub-claim (A), not (B). See `evidence-line:0031`.
- **Endothelial-function leg (direction only, severity-confounded)** — Ambrosino2021 (case-control, FMD) finds endothelial dysfunction concentrated in males (male convalescent FMD 2.5%±1.9 vs female 6.1%±2.9, p<0.001; female cases vs female controls null, p=0.362). But FMD **correlates with pulmonary-impairment severity** (FEV1% rho=0.436; FVC% rho=0.406; PaO2 rho=0.247) and the sex contrast was not severity-adjusted, so this leg supports the male *direction* but **cannot** discriminate a sex effect from acute-severity confounding. Carried as a **weak, direction-only** line (`evidence-line:0032`), explicitly excluded from the severity-discriminating set (sub-claim B rests on `evidence-line:0029` + `0030`).

## Caveats

`empirical_regularity` / `background` role for `hypothesis:0004`: this characterises *where and how strongly the female PAIS skew reverses*, and it constrains a pure acute-severity-threshold reading of the vascular signal (the effect is present below the hospitalization threshold). Bounding conditions:

1. **Mechanism unresolved — possible baseline-rate carryover.** VTE and arterial cardiovascular disease are male-predominant at baseline in older populations (the Xie2022 cohort mean age ~64), so the male excess may partly be **carried-through baseline male vascular risk** rather than a COVID-*specific* sex amplification — the mirror-image of the POTS baseline-carried structure (`proposition:0009`), in the opposite sex direction. The matched-vs-uninfected designs (Xie2022; the Alberta cohort) give *some* evidence of a COVID-associated component, but no study reports a formal infection×sex interaction term, so a COVID-specific amplification can be neither confirmed nor excluded.
2. **The FMD/endothelial leg is severity-confounded** (above) and does not independently establish the reversal; the thrombotic/CV-mortality lines carry sub-claim (B).
3. **Wave heterogeneity** — the CV-mortality signal (Kopp2024) is significant in Delta only; Alpha and Omicron are null.
4. **Within-stratum residual severity** — Kopp2024 did not adjust for ICU-vs-floor within the hospitalized cohort; Xie2022 carries a published correction (JAMA Intern Med 2022;182(11):1234) that should be confirmed not to alter the sex HR before any quantitative reuse.
5. **Ascertainment asymmetry** — hard endpoints (VTE, CV death) are far less ascertainment-sensitive than the self-report channels that carry the female-biased domains, which is itself the point: the reversal is concentrated exactly where measurement is objective (`proposition:0010`, the measurement-channel structure in `interpretation:0003`).
