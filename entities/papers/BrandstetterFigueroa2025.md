---
id: paper:BrandstetterFigueroa2025
kind: paper
title: Viral Burden and Illness Severity During Acute SARS-CoV-2 Infection Predict
  Persistent Long COVID Symptoms
status: active
ontology_terms:
- long COVID
- SARS-CoV-2 viral burden
- nucleocapsid antigen
- acute illness severity
- prospective cohort
dataset_usage: []
source_refs: []
related:
- hypothesis:0002-tissue-reservoir-antigen-fragment
- proposition:0024-retained-fragment-burden-predicts-chronicity-over-initial-load
- topic:antigen-pathogen-persistence
- task:t053
created: '2026-06-25'
updated: '2026-06-25'
---
# Viral Burden and Illness Severity During Acute SARS-CoV-2 Infection Predict Persistent Long COVID Symptoms

<!--
- Authors: Elisabeth Brandstetter Figueroa, Anne E. P. Frosch, Kristina S. Burrack, Gayathri Dileepan, Rachael Goldsmith, Morgan Harris, Nwando Ikeogu, Hodan Jibrell, Sangeitha Thayalan, Robin L. Dewar, Chetan Shenoy, Irini Sereti, Jason V. Baker
- Year: 2025
- Journal: Open Forum Infectious Diseases 12(2):ofaf048
- DOI: 10.1093/ofid/ofaf048
- PMID: 39917335
- PMCID: PMC11800476
-->

## Key Contribution

BrandstetterFigueroa2025 prospectively followed adults with acute COVID-19 from an urban safety-net
hospital/clinic cohort and tested whether baseline acute-illness characteristics predicted persistent
long-COVID symptoms at 9 months. Acute plasma SARS-CoV-2 nucleocapsid antigen (N Ag), measured by a
Quanterix microbead immunoassay, remained independently associated with persistent symptoms.

## Methods

- **Design:** prospective cohort of adults with symptomatic acute COVID-19, enrolled July 2020 to December
  2022.
- **Analysis set:** 162 participants with known 9-month recovery status from 222 enrolled.
- **Exposure:** acute plasma SARS-CoV-2 N Ag, detectable above 3 pg/mL.
- **Outcome:** persistent symptoms / not recovered at 9 months.
- **Models:** logistic regression with demographic, comorbidity, disease-severity, vaccination/variant, and
  laboratory covariates.

## Key Findings

- 41% of participants with known 9-month status reported persistent symptoms.
- Detectable acute N Ag was associated with persistent long-COVID symptoms at 9 months after adjustment
  for demographics, comorbidities, and disease severity (adjusted OR **3.0**, 95% CI **1.1-8.0**).
- Supplemental oxygen requirement also remained independently associated (adjusted OR **3.6**, 95% CI
  **1.2-11**).
- The authors interpret acute viral burden and acute illness severity as important predictors of long-COVID
  risk.

## Relevance

This paper is a useful **model-criticism** line for `proposition:0024`. The proposition predicts that
retained fragment burden/duration should out-predict initial pathogen load for chronicity. This study does
not measure retained post-clearance fragment burden, so it cannot adjudicate the full comparison, but it
shows that **acute** viral burden itself has independent predictive value. That narrows the room for a
strong "initial load is not the lever" version of h0002 and makes a retained-burden-vs-initial-load head
to head more necessary.

## Limitations

This is not a retained-fragment study: the N Ag exposure was measured during acute illness, not at
treatment completion or after pathogen clearance. It also uses a hospital/clinic cohort with substantial
acute-severity structure, so the result may partly index severity and systemic dissemination rather than
fragment-retention kinetics.
