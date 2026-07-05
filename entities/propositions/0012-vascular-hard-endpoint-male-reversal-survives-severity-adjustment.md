---
id: proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment
kind: proposition
title: The PAIS vascular-thromboinflammatory hard-endpoint domain is male-biased and
  the reversal survives coarse acute-severity restriction
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
- task:t048
source_refs:
- paper:Xie2022
- paper:Kopp2024
- paper:Abubasheer2025
- paper:Ambrosino2021
- paper:Spetz2025
created: '2026-06-23'
updated: '2026-06-25'
---
# Proposition: The PAIS vascular-thromboinflammatory hard-endpoint domain is male-biased and the reversal survives coarse acute-severity restriction

## Claim

Across **hard thrombotic and cardiovascular endpoints** after SARS-CoV-2 infection — acute ambulatory venous thromboembolism (VTE) and post-acute cardiovascular mortality — the vascular hard-endpoint direction is **male-biased**, the reverse of the overall female PAIS skew. This male excess is not explained by the coarse hospitalized-vs-ambulatory acute-severity boundary: it is present in **ambulatory (non-hospitalized = lowest-severity) patients** for 30-day VTE (Xie2022 adjusted HR 1.69) and in a **hospitalized-restricted cohort** for 18-month cardiovascular mortality (Kopp2024 Delta-wave HR 1.68) [@Xie2022; @Kopp2024]. This is an `empirical_regularity` about the **sex direction** of one hard-endpoint subphenotype domain and about its survival of coarse severity restriction. It does **not** establish post-acute VTE persistence specifically, full within-stratum severity independence, mechanism, or COVID-*specific* amplification (see Caveats).

## Evidence Summary

All `literature_evidence`. The claim has two sub-parts — (A) the hard vascular endpoint direction is male-biased, (B) the bias survives the coarse hospitalized-vs-ambulatory acute-severity boundary — bracketed by evidence in **both** severity strata:

- **Low-severity stratum (the decisive severity-boundary test, acute VTE)** — Xie2022 (UKBB population cohort, 18,818 ambulatory COVID-19 outpatients vs 93,179 propensity-matched uninfected; hospitalized-at-test excluded) finds **male sex an independent risk factor for 30-day incident VTE, adjusted HR 1.69 (95% CI 1.30–2.19)** after adjustment for age, obesity, vaccination, cancer, and comorbidity count. Male excess in the *lowest* acute-severity stratum directly refutes a pure hospitalization/ICU carryover reading for the vascular hard-endpoint direction, but it is not evidence that VTE persists into the 31-180-day post-acute window. See `evidence-line:0029` and `question:0020`.
- **High-severity stratum (severity-restricted)** — Kopp2024 (4,509 patients **all hospitalized** with moderate-to-severe COVID-19 pneumonia) finds higher 18-month CV mortality in men (Delta wave 6.13% vs 3.62%, p=0.017; combined CV endpoint 16.87% vs 12.61%), with **male sex an independent predictor in multivariable Cox, HR 1.68 (1.005–2.796), p=0.048** — i.e. the male excess holds *within* a hospitalized (high-severity) population. Wave-heterogeneous: significant in Delta only. See `evidence-line:0030`.
- **Cross-study breadth (direction)** — Abubasheer2025 meta-analysis pools a male excess across hard endpoints (VTE RR 1.43 [1.19–1.71]; MI RR 1.24; plus ischemic stroke, mortality, major bleeding RR 1.22). Establishes the male *direction* is reproducible across cohorts; severity adjustment is **not** established at the meta level (the pooled studies are mostly hospitalized and not severity-stratified), so this line supports sub-claim (A), not (B). See `evidence-line:0031`.
- **Endothelial-function leg (direction only, severity-confounded)** — Ambrosino2021 (case-control, FMD) finds endothelial dysfunction concentrated in males (male convalescent FMD 2.5%±1.9 vs female 6.1%±2.9, p<0.001; female cases vs female controls null, p=0.362). But FMD **correlates with pulmonary-impairment severity** (FEV1% rho=0.436; FVC% rho=0.406; PaO2 rho=0.247) and the sex contrast was not severity-adjusted, so this leg supports the male *direction* but **cannot** discriminate a sex effect from acute-severity confounding. Carried as a **weak, direction-only** line (`evidence-line:0032`), explicitly excluded from the severity-discriminating set (sub-claim B rests on `evidence-line:0029` + `0030`).
- **Baseline-carryover audit (COVID-added component)** — Spetz2025 (Swedish SCIFI-PEARL total-population cohort, ages 40-75, uninfected comparator) adds the missing comparator logic. In the no-prior-comorbidity sensitivity table, thromboembolic disease (DVT or PE) is HR 3.64 in COVID-infected men and HR 1.81 in COVID-infected women, with uninfected men as reference and uninfected women HR 0.78. The implied infection-added male-vs-female ratio-of-ratios is ~1.57. This supports a **COVID-added male thromboembolic increment beyond pure baseline carryover**, but does not fully discharge the exact ambulatory 31-180-day interaction because sex, time-window, and non-hospitalized strata are not crossed in one model. See `evidence-line:0074` and `interpretation:0018`.

## Caveats

`empirical_regularity` / `background` role for `hypothesis:0004`: this characterises *where and how strongly the female PAIS skew reverses*, and it constrains a pure acute-severity-threshold reading of the vascular signal (the effect is present below the hospitalization threshold). Bounding conditions:

1. **Mechanism partly narrowed — baseline-rate carryover is not enough.** VTE and arterial cardiovascular disease are male-predominant at baseline in older populations (the Xie2022 cohort mean age ~64), so part of the male excess may still be **carried-through baseline male vascular risk** — the mirror-image of the POTS baseline-carried structure (`proposition:0009`), in the opposite sex direction. But Spetz2025 weakens a *pure* baseline-carryover reading by showing that the COVID-associated thromboembolic increment is larger in men than women against an uninfected population baseline. Remaining gap: no study yet reports the exact sex×infection interaction restricted to non-hospitalized patients in the 31-180-day window, so attribution is partly but not fully identified.
2. **The FMD/endothelial leg is severity-confounded** (above) and does not independently establish the reversal; the thrombotic/CV-mortality lines carry sub-claim (B).
3. **Wave heterogeneity** — the CV-mortality signal (Kopp2024) is significant in Delta only; Alpha and Omicron are null.
4. **Temporal scope for VTE** — Xie2022 is a 30-day acute-window VTE study. It is load-bearing for the low-severity severity-boundary test, not for post-acute VTE persistence; the 31-180-day ambulatory VTE question remains open in `question:0020`.
5. **Within-stratum residual severity** — Kopp2024 did not adjust for ICU-vs-floor within the hospitalized cohort; Xie2022 carries a published correction (JAMA Intern Med 2022;182(11):1234) that affects the data-sharing statement rather than the reported estimates, but should still be checked before quantitative reuse.
6. **Ascertainment asymmetry** — hard endpoints (VTE, CV death) are far less ascertainment-sensitive than the self-report channels that carry the female-biased domains, which is itself the point: the reversal is concentrated exactly where measurement is objective (`proposition:0010`, the measurement-channel structure in `interpretation:0003`).
