---
id: dataset:uk-biobank-covid
type: dataset
title: "UK Biobank — COVID-19 / long COVID"
status: candidate
created: "2026-06-21"
updated: "2026-06-21"
origin: external
source_class: observational
tier: track
license: proprietary
access:
  level: commercial
  availability: available
  verified: false
  source_url: "https://www.ukbiobank.ac.uk/"
accessions: []
ontology_terms: [long-covid, sars-cov-2, prospective-cohort, mental-health-linkage, sex-differences]
related:
  - task:t013
  - question:0007-mechanism-of-female-predominance-in-pais
  - paper:AlcaldeHerraiz2025
  - question:0003-acute-severity-threshold-for-self-sustaining-pais
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
---

# UK Biobank — COVID-19 / long COVID

**Candidate dataset for `task:t013`.** `status: candidate`, `tier: track` — controlled + paid
application; already the planned vehicle for the menopause→PAIS UKB analysis (`paper:AlcaldeHerraiz2025`).

## What it is

~500k base cohort with pre-infection biomarkers (SHBG measured), linked EHR, and COVID test/outcome
data. Mental-health questionnaire (MHQ) at baseline + linked depression/anxiety coding.

## Why it fits t013

Enables **sex-stratified acute-severity** analysis (test-positivity, hospitalization) **plus
mental-health linkage** to test the neuropsychiatric-vs-somatic dissociation, with deep covariate
adjustment and a rare **pre-infection baseline**.

| Acute severity | Post-acute persistence | Neuropsychiatric | Somatic fatigue | Sex-stratified |
|---|---|---|---|---|
| yes | yes (reported + coded PACS) | yes (MHQ + linkage) | limited | yes |

## Access / caveats

Approved application + access fee. **Healthy-volunteer & older-age skew** limits acute-COVID
generalizability; fatigue not as cleanly measured as in PAIS-specific cohorts; pre-infection hormone
panel limited to SHBG (E2 floor-censored).
