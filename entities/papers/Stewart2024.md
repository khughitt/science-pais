---
id: paper:Stewart2024
kind: paper
title: Menopause symptom prevalence in three post-COVID-19 syndrome clinics in England
status: active
ontology_terms:
  - long COVID
  - menopause
  - perimenopause
  - symptom overlap
  - women health
dataset_usage: []
datasets: []
source_refs:
  - cite:Stewart2024
related:
  - question:0007-mechanism-of-female-predominance-in-pais
  - topic:shared-failure-mode-across-pais
created: '2026-06-19'
updated: '2026-06-19'
---
# Menopause symptom prevalence in three post-COVID-19 syndrome clinics in England

- **Authors:** Stuart Stewart, Adrian Heald, Yvette Pyne, Nawar Diar Bakerly
- **Year:** 2024
- **Journal:** IJID Regions
- **DOI:** 10.1016/j.ijregi.2024.100405
- **BibTeX key:** Stewart2024
- **Source:** PDF: `~/d/health/processes/post-acute-infection/papers/pdfs/2024_Stewart_Menopause-symptom-prevalence-in-three-post-COVID-19-syndrome-clinics-in-England-A-cross-sectional-analysis.pdf`

## Key Contribution

Stewart et al. quantify menopause-symptom burden among women attending three NHS post-COVID syndrome clinics in Greater Manchester.
The key contribution is practical and epidemiologic: many symptoms used to recognize long COVID overlap with perimenopause and menopause, and the 40-54 year age group had the highest total menopause symptom questionnaire burden.

## Methods

The authors performed a cross-sectional service-improvement analysis of 122 completed women health questionnaires from new female patients aged 18-79 years in three post-COVID syndrome clinics between February and May 2023.
They used the Balance menopause symptom questionnaire, summarized symptom prevalence by age group, and modeled predictors of total MSQ score with multivariable linear regression.
The study used age groups rather than reproductive-status groups because COVID-associated menstrual disturbance could confound self-classification of perimenopause.

## Key Findings

Across the cohort, the most prevalent symptoms were fatigue or low energy (97.5%), muscle and joint pain (95.9%), memory problems (92.6%), difficulty concentrating (92.6%), and feeling tense or nervous (88.5%).
Women aged 40-54 years had the highest mean total MSQ score (36.4; CI 32.3-40.6), higher than both 18-39 years and 55-79 years.
Regression modeling found a positive parabolic relationship between age and total MSQ score, a higher score in the 40-54 year group than the 55-79 year group, lower scores with less deprivation, and higher scores with a gynecologic diagnosis.
Among patients who menstruated, 51% reported menstrual disturbance with COVID-19 infection and 21% with COVID-19 vaccination.

## Relevance

This paper is directly relevant to `question:0007-mechanism-of-female-predominance-in-pais`.
It does not show that menopause causes long COVID; instead, it shows that symptom overlap and reproductive-stage covariates are large enough to distort long-COVID ascertainment, phenotype assignment, and clinical management.
For the PAIS framework, it supports adding menopausal status, gynecologic diagnoses, and deprivation to sex-stratified long-COVID analyses.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Menopause symptom questionnaire | PAIS symptom-overlap measurement | Helps distinguish endocrine symptoms from post-infectious symptoms. |
| Age 40-54 symptom peak | sex and hormonal-state covariate | The high-risk long-COVID demographic overlaps with menopausal transition. |
| Menstrual disturbance after infection | endocrine/reproductive perturbation after infection | Plausible mediator or confounder, not causal proof. |
| Deprivation association | ascertainment and social-context modifier | Supports modeling care access and socioeconomic gradients. |

## Limitations

The cohort is clinic-referred, cross-sectional, and lacks a recovered-COVID or non-COVID control group.
The analysis cannot separate long-COVID symptoms from menopause symptoms at the individual level and cannot infer whether SARS-CoV-2 altered ovarian/endocrine physiology.
The study is also geographically localized to Greater Manchester and uses service-improvement data rather than a prespecified research cohort.

## Model / Tool Availability

No reusable computational model or dataset was released.
The questionnaire-based workflow is reusable as a clinic-screening approach.

## Follow-up

Use this paper when designing sex- and hormone-status-stratified PAIS cohorts.
The highest-priority follow-up is a longitudinal study that measures menstrual status, hormone therapy, inflammatory markers, and long-COVID trajectories from pre-infection or early post-infection baseline.
