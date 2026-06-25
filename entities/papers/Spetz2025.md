---
id: paper:Spetz2025
type: paper
title: Covid-19 and cardiovascular disease in a total population-study of long-term effects, social factors and Covid-19-vaccination
status: active
ontology_terms:
- COVID-19
- cardiovascular disease
- thromboembolic disease
- venous thromboembolism
- sex stratification
- population registry
- post-acute cardiovascular outcomes
- SCIFI-PEARL
dataset_usage: []
datasets: []
source_refs: []
related:
- proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment
- question:0020-male-vte-excess-post-acute-persistence
- question:0021-male-vascular-reversal-covid-specific-vs-baseline-carryover
- hypothesis:0004-acute-severity-threshold
- topic:thromboinflammation-and-endothelial-dysfunction
- task:t048
created: '2026-06-25'
updated: '2026-06-25'
---
# Covid-19 and cardiovascular disease in a total population-study of long-term effects, social factors and Covid-19-vaccination

<!--
- Authors: Malin Spetz, Yvonne Natt och Dag, Huiqi Li, Fredrik Nyberg, Maria Rosvall
- Year: 2025
- Journal: Nature Communications 16:10115
- DOI: 10.1038/s41467-025-66270-1
- Type: nationwide population-register cohort
-->

## Key Contribution

Spetz2025 uses Swedish SCIFI-PEARL linked registers to estimate incident cardiovascular disease and
mortality after SARS-CoV-2 infection in the total Swedish population aged 40-75 years. The analysis is
useful for the PAIS vascular-sex question because it combines four features that were missing from the
project's t042 evidence base: an uninfected comparator, hospitalization-defined severity strata, explicit
post-infection risk windows, and sex-stratified cardiovascular estimates.

## Methods

- **Design:** nationwide observational cohort using linked Swedish population and health registers.
- **Population:** 4,095,414 residents aged 40-75 years followed from 2020-01-01 to 2021-12-31 after
  exclusion of individuals with prior outcome-specific cardiovascular events in the preceding five years.
- **Exposure:** SARS-CoV-2 infection as a time-varying exposure from first positive PCR test.
- **Comparator:** uninfected person-time in the same source population.
- **Severity:** severe COVID-19 defined by hospitalization due to COVID-19 within -2 to +14 days from
  first positive test; mild COVID-19 defined as no COVID-19 hospitalization.
- **Outcomes:** ischemic stroke, intracerebral hemorrhage, cerebrovascular disease, acute myocardial
  infarction, ischemic heart disease, cardiomyopathy, heart failure, deep venous thrombosis (DVT),
  pulmonary embolism (PE), thromboembolic disease (DVT or PE), and mortality outcomes.
- **Models:** Cox regression with adjustment for age, sex, country of birth, income, education,
  comorbidities, and vaccination; some stratified models omit the stratifying covariate.

## Key Findings

- Overall fully adjusted hazard ratios after COVID-19 were elevated across cardiovascular outcomes,
  including PE HR 4.31 and acute myocardial infarction HR 1.22.
- Mild/non-hospitalized COVID-19 still carried increased thromboembolic risk: DVT HR 1.41 and PE HR 1.78.
- In the 91-180 day post-infection window, risk remained slightly but significantly elevated for both
  thrombotic outcomes: DVT HR 1.20 and PE HR 1.29.
- The broader thromboembolic outcome (DVT or PE) was more strongly associated with COVID-19 in men than
  women. In the no-prior-comorbidity sensitivity table, relative to uninfected men, uninfected women had
  HR 0.78, COVID-infected men HR 3.64, and COVID-infected women HR 1.81. This implies an approximate
  infection-added male-vs-female ratio-of-ratios of 1.57: male infection HR 3.64 versus female infection
  HR 1.81 / 0.78 = 2.32.

## Relevance

This is the strongest current near-vehicle for task:t048. It does not provide the exact fully crossed
estimand requested there - sex x infection x 31-180-day window x non-hospitalized severity - but it
substantially narrows the previous baseline-carryover caveat. The male vascular/thromboembolic reversal
is not just a male baseline-rate fact: COVID-19 appears to add more thromboembolic relative risk in men
than in women, while post-acute DVT/PE risk persists into the 91-180 day window overall.

## Limitations

The decisive t048 cross-tab is not reported. Sex-stratified estimates are for three broad outcome groups
over follow-up, while risk-period estimates are sex-adjusted but not sex-stratified, and severity estimates
are not crossed with sex and risk period. Therefore the paper partly answers q0020/q0021 but does not
fully discharge the requested ambulatory 31-180 day infection x sex interaction.
