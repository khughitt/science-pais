---
id: paper:Thompson2022
kind: paper
title: "Long COVID burden and risk factors in 10 UK longitudinal studies and electronic health records"
status: active
ontology_terms:
  - long COVID
  - longitudinal cohorts
  - OpenSAFELY
  - pre-pandemic risk factors
  - population studies
  - electronic health records
dataset_usage: []
datasets: []
source_refs:
  - cite:Thompson2022
related:
  - task:t008
  - topic:pais-case-definition-heterogeneity
  - question:0017-deflationary-alternatives-vs-shared-pathophysiology
created: "2026-06-25"
updated: "2026-06-25"
---

# Long COVID burden and risk factors in 10 UK longitudinal studies and electronic health records

- **Authors:** Ellen J. Thompson, Dylan M. Williams, Alex J. Walker, and colleagues
- **Year:** 2022
- **Journal:** Nature Communications
- **DOI:** 10.1038/s41467-022-30836-0
- **PMID:** 35764621
- **PMCID:** PMC9240035
- **BibTeX key:** Thompson2022

## Key Contribution

This paper coordinates long-COVID analyses across 10 UK longitudinal study samples
plus OpenSAFELY electronic health records. It estimates long-COVID burden and evaluates
pre-pandemic risk factors in community-based individuals, giving the project a broad
population-level triangulation design rather than another clinic-enriched series.

## Methods

**Design:** Harmonized analysis of survey data from 10 UK longitudinal study samples,
combined with a large primary-care EHR analysis.

**Scale:** The longitudinal-study arm includes thousands of self-reported COVID-19 cases;
the EHR arm includes roughly 1.1 million individuals with COVID-19 diagnostic codes.

**Baseline controls:** The major design advantage is pre-pandemic covariate measurement
across established longitudinal cohorts. Risk-factor ordering is therefore cleaner than
in post-hoc long-COVID surveys.

**Risk factors:** Age, sex, ethnicity, socioeconomic variables, pre-pandemic general
health, mental health, overweight/obesity, and asthma are among the reported factors.

## Key Findings

Across the longitudinal-study samples, long-COVID frequency varied by operational
definition and cohort, but several risk-factor patterns recurred: female sex, poorer
pre-pandemic general and mental health, overweight/obesity, and asthma were associated
with higher long-COVID risk. The EHR analysis added scale and a different ascertainment
channel, reinforcing that population-level estimates depend strongly on measurement
route and case definition.

## Relevance

For `task:t008`, this is the strongest broad **risk-factor triangulation** paper:
population cohorts supply pre-pandemic predictors, while EHR supplies scale and a
different ascertainment channel. It is useful for bounding reverse causation in
demographic and general-health risk factors.

It is not a deep mechanism vehicle. Its long-COVID definitions and measurement channels
vary by cohort, and the EHR arm inherits coding and care-seeking biases.

## Limitations

1. Long-COVID phenotype harmonization is imperfect across the 10 cohorts.
2. EHR-coded long COVID is vulnerable to healthcare-access and coding artifacts.
3. Pre-pandemic general health is valuable for temporal ordering but does not substitute
   for pre-infection molecular or physiological baseline data.

## Follow-up

Use this paper as the population-level comparator when evaluating clinic-biased PAIS
risk-factor claims. Effects that reverse or disappear in Thompson-style designs should
be treated as likely ascertainment- or selection-sensitive.
