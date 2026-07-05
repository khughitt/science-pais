---
id: paper:Esseffar2025
kind: paper
title: Menopause-Associated Comorbidities and Their Impact on COVID-19 Severity
status: active
ontology_terms:
  - menopause
  - acute COVID-19
  - comorbidity
  - cardiovascular disease
  - diabetes
dataset_usage: []
datasets: []
source_refs:
  - cite:Esseffar2025
related:
  - question:0007-mechanism-of-female-predominance-in-pais
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - topic:menopause-sex-hormones-and-pais-risk
created: '2026-06-19'
updated: '2026-06-19'
---
# Menopause-Associated Comorbidities and Their Impact on COVID-19 Severity

- **Authors:** Sara Esseffar, Said Bellahcen, Ghizlane Azizi, Hamza Ngadi, Abdelmajid Moumen
- **Year:** 2025
- **Journal:** E3S Web of Conferences
- **DOI:** 10.1051/e3sconf/202563201026
- **BibTeX key:** Esseffar2025
- **Source:** PDF: `~/d/health/processes/post-acute-infection/papers/pdfs/2025_Esseffar_Menopause-Associated-Comorbidities-and-Their-Impact-on-COVID-19-Severity.pdf`

## Key Contribution

Esseffar et al. examine whether comorbidities common after menopause are associated with acute COVID-19 symptom intensity and recovery duration.
The paper is most useful as a confounding reminder: menopause-associated cardiovascular disease, diabetes, hypertension, and obesity can drive severity signals that might otherwise be attributed to menopause itself.

## Methods

The authors conducted a retrospective interview-based study of 50 menopausal women in Nador, Morocco, who reported COVID-19.
They collected socioeconomic, health-status, and comorbidity data through structured face-to-face questionnaires.
Associations between comorbidities and symptom intensity were tested with chi-square/Fisher tests, and recovery duration was compared with t-tests.

## Key Findings

The sample had a mean age of 56.06 +/- 5.58 years and mean menopause age of 50.84 +/- 3.30 years.
Chronic disease was common; cardiovascular disease occurred in 40%, diabetes in 38%, mental illness in 38%, obesity in 36%, and hypertension in 34%.
Cardiovascular disease was strongly associated with intense COVID-19 symptoms (OR 16.0; 95% CI 3.9-65.8), diabetes was also associated (OR 8.1; 95% CI 2.2-29.5), and hypertension showed a smaller significant association (OR 3.7; 95% CI 1.1-12.5).
Cardiovascular disease was associated with longer recovery time (18.2 +/- 4.2 vs 9.3 +/- 3.8 days).

## Relevance

For PAIS, this paper does not directly address long COVID, but it matters for causal interpretation.
Menopause-related comorbidities are plausible confounders or mediators between age/hormonal transition and post-infectious severity or delayed recovery.
It supports treating cardiovascular and metabolic disease as separate covariates rather than folding them into a broad menopause effect.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Cardiovascular disease | vascular vulnerability / confounder | Could amplify acute severity and post-acute symptoms. |
| Diabetes | metabolic comorbidity | Important PAIS risk covariate. |
| Recovery duration | early post-acute outcome | Short duration, not long-COVID case definition. |
| Menopause-associated comorbidities | age/hormonal-state confounding | Key for DAG design. |

## Limitations

The sample is small, single-region, retrospective, and interview-based.
It includes only menopausal women, so it cannot estimate menopause effects relative to premenopausal women or men.
COVID-19 severity is symptom-intensity based and not equivalent to PAIS or long-COVID outcomes.

## Model / Tool Availability

No model, tool, or dataset was released.

## Follow-up

Use this paper in synthesis as evidence that comorbidity pathways must be separated from hormonal mechanisms.
Future PAIS analyses should model cardiovascular disease, diabetes, obesity, and hypertension explicitly.
