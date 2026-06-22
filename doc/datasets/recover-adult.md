---
id: dataset:recover-adult
type: dataset
title: "RECOVER-Adult (Researching COVID to Enhance Recovery)"
status: candidate
created: "2026-06-21"
updated: "2026-06-21"
origin: external
source_class: observational
tier: track
license: restricted
access:
  level: controlled
  availability: available
  verified: false
  source_url: "https://recovercovid.org/data"
accessions: []
ontology_terms: [long-covid, sars-cov-2, prospective-cohort, biospecimens, sex-differences]
related:
  - task:t013
  - task:t040
  - question:0007-mechanism-of-female-predominance-in-pais
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
---

# RECOVER-Adult

**Candidate dataset for `task:t013`.** `status: candidate`, `tier: track` — controlled, application-gated;
the eventual primary-positive-test vehicle for the menopause→PAIS line (`task:t040`).

## What it is

Largest US natural-history long COVID cohort (83 sites, ≥3 mo post-infection enrollment). EHR +
wearables + clinical assessments + **banked biospecimens** (serum/plasma/PBMC). Validated PASC index
(PEM-weighted); AMH already measured (unique); full E2/T/FSH/LH/SHBG panel **assayable de novo** but
not yet run. Released via NHLBI BioData Catalyst / dbGaP (specific accession to verify).

## Why it fits t013

Best-powered single-trigger resource for sex-stratified post-acute persistence with separable mood vs
fatigue domains.

| Acute severity | Post-acute persistence | Neuropsychiatric | Somatic fatigue | Sex-stratified |
|---|---|---|---|---|
| limited | yes (PASC index) | yes | yes (PEM-weighted) | yes |

## Access / caveats

NIH-gated (dbGaP DAR via BioData Catalyst). Single trigger (no cross-trigger contrast).
Enrollment ≥3 mo post-infection → **no within-person pre-infection baseline** (reverse-causation limit).
Biospecimen hormone assay is funding-gated, post-seed-stage (`task:t040`).
