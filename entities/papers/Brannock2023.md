---
id: paper:Brannock2023
kind: paper
title: Long COVID risk and pre-COVID vaccination in an EHR-based cohort study from
  the RECOVER program
status: active
ontology_terms:
- long COVID
- vaccination
- electronic health records
- RECOVER
- N3C
dataset_usage: []
source_refs:
- cite:Brannock2023
related:
- task:t010
- question:0012-prevention-vaccination-antiviral-reduces-pais
- hypothesis:0004-acute-severity-threshold
created: '2026-06-25'
updated: '2026-06-25'
---

# Long COVID risk and pre-COVID vaccination in an EHR-based cohort study from the RECOVER program

- **Authors:** M. Daniel Brannock, Robert F. Chew, Alexander J. Preiss, Emily C. Hadley, Signe Redfield, Julie A. McMurry, Peter J. Leese, Andrew T. Girvin, Miles Crosskey, Andrea G. Zhou, Richard A. Moffitt, Michele Jonsson Funk, Emily R. Pfaff, Melissa A. Haendel, Christopher G. Chute, N3C and RECOVER Consortia
- **Year:** 2023
- **Journal:** Nature Communications
- **DOI:** 10.1038/s41467-023-38388-7
- **Article:** 14:2914
- **BibTeX key:** Brannock2023

## Key Contribution

Brannock2023 is a large RECOVER/N3C EHR study of pre-infection vaccination and later long-COVID
diagnosis. It is valuable because it tests the association in two outcome channels: a clinical diagnosis
cohort and a high-confidence computational phenotype cohort.

## Methods

- **Exposure:** completed COVID-19 vaccine series before SARS-CoV-2 infection.
- **Population:** adults with COVID-19 between 2021-08-01 and 2022-01-31.
- **Outcomes:** long-COVID clinical diagnosis in a clinic-based cohort (n=47,404) and a computational
  phenotype in a model-based cohort (n=198,514).
- **Adjustment:** inverse-probability weighting with demographic and medical-history covariates; both
  logistic and Cox/time-to-event models.

## Key Findings

Vaccination before infection was consistently associated with lower odds and rates of long-COVID
diagnosis across the clinical-diagnosis and computational-phenotype outcomes after adjustment.

## Relevance

This is a strong observational anchor for `question:0012` because it evaluates breakthrough infections:
the analysis conditions on having SARS-CoV-2 infection, so it speaks to reduced long-COVID risk beyond
vaccination's primary prevention of infection.

## Limitations

The authors do not interpret the results as causal because unmeasured confounding and latent variables
remain. EHR outcomes are vulnerable to healthcare-utilization bias, underdiagnosis, vaccination-record
misclassification, and symptom-channel incompleteness. The result supports prevention/modification, not
a specific antigen-burden mechanism.
