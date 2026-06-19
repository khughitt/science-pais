---
id: paper:Costeira2021
type: paper
title: Estrogen and COVID-19 symptoms
status: active
ontology_terms:
  - estrogen
  - menopause
  - hormone replacement therapy
  - acute COVID-19
  - COVID Symptom Study
dataset_usage: []
datasets: []
source_refs:
  - cite:Costeira2021
related:
  - question:0007-mechanism-of-female-predominance-in-pais
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - topic:menopause-sex-hormones-and-pais-risk
created: '2026-06-19'
updated: '2026-06-19'
---
# Estrogen and COVID-19 symptoms

- **Authors:** Ricardo Costeira, Karla A. Lee, Benjamin Murray, Colette Christiansen, Juan Castillo-Fernandez, Mary Ni Lochlainn, Joan Capdevila Pujol, Heather Macfarlane, Louise C. Kenny, Iain Buchan, Jonathan Wolf, Janice Rymer, Sebastien Ourselin, Claire J. Steves, Timothy D. Spector, Louise R. Newson, Jordana T. Bell
- **Year:** 2021
- **Journal:** PLOS ONE
- **DOI:** 10.1371/journal.pone.0257051
- **BibTeX key:** Costeira2021
- **Source:** PDF: `~/d/health/processes/post-acute-infection/papers/pdfs/2021_Costeira_Estrogen-and-COVID-19-symptoms-Associations-in-women-from-the-COVID-Symptom-Study.pdf`

## Key Contribution

Costeira et al. use large-scale UK COVID Symptom Study app data to test associations between estrogen exposure proxies and predicted or tested COVID-19 outcomes in women.
The paper provides population-scale acute-COVID evidence relevant to, but not directly measuring, long-COVID risk.

## Methods

The study analyzed self-reported app data collected from 7 May to 15 June 2020.
Analyses included 152,637 women for menopausal status, 295,689 women for combined oral contraceptive pill use, and 151,193 menopausal women for hormone replacement therapy use.
Models adjusted for age, BMI, and smoking, with age-bin sensitivity analyses and validation of menopausal self-report in a TwinsUK subset.
The main outcome was predicted COVID-19 based on a symptom model because testing was limited.

## Key Findings

Menopausal women aged 40-60 years had higher predicted COVID-19 (OR 1.22; 95% CI 1.07-1.39), with the signal strongest in the 45-50 age group.
COCP users had lower predicted COVID-19 (OR 0.87; 95% CI 0.81-0.93) and lower hospitalization (OR 0.79; 95% CI 0.64-0.97).
HRT use was associated with higher predicted COVID-19 (OR 1.32; 95% CI 1.16-1.49), but not higher hospitalization, and respiratory support and tested positivity trended negative but were not significant.
The authors caution that HRT type, route, dose, duration, and indication were unavailable.

## Relevance

This paper supports estrogen biology as a plausible acute-COVID modifier, but it does not answer whether estrogen exposure reduces or increases long-COVID risk.
For the PAIS project, its most important lesson is methodological: symptom-predicted infection can be distorted by menopause symptoms, hormone therapy selection, age, BMI, and testing scarcity.

## Project Framework Mapping

| Paper Concept | Project Concept | Notes |
|---|---|---|
| Menopausal status | endocrine covariate / symptom-overlap risk | Associated with predicted COVID, not confirmed infection. |
| COCP use | exogenous estrogen proxy | Possibly protective in acute infection; confounded by health selection. |
| HRT use | hormone therapy exposure | Direction differs from simple estrogen-protection story. |
| Predicted COVID outcome | measurement artifact risk | Relevant to long-COVID ascertainment concerns. |

## Limitations

The main outcome is predicted COVID-19, not uniformly tested infection.
All exposure data are self-reported, and hormone therapy details are missing.
The study is app-based and may underrepresent older, severely ill, or less digitally connected people.
It is acute-COVID focused and not a PAIS outcome study.

## Model / Tool Availability

Purpose-built quality-control scripts are referenced, and anonymized app data were available through HDR UK procedures.
No project-local reusable dataset is available.

## Follow-up

Do not use HRT status as a simple estrogen-dose variable.
Future long-COVID analyses should distinguish endogenous hormone status, therapy route, therapy indication, and symptom-based outcome definitions.
