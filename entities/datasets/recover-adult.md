---
id: dataset:recover-adult
kind: dataset
title: RECOVER-Adult (Researching COVID to Enhance Recovery)
status: candidate
created: "2026-06-21"
updated: "2026-06-26"
origin: external
source_class: observational
dataset_class: deposit
tier: track
license: proprietary
access:
  level: controlled
  availability: available
  verified: true
  source_url: https://recovercovid.org/data
  reproducibility:
    obtainability: approved-researcher
    execution: local
    extractability: full-dataset
    notes: 'Released via dbGaP / NHLBI BioData Catalyst (phs003463.v6.p5): a qualified researcher submits a standard Data Access Request, is approved, and downloads the individual-level release to their own environment to rerun — credentialed-reproducible. approved-researcher (standard DAR is broadly available to qualified third parties), NOT approved-project. The molecular-module gap noted in the body is a plan-feasibility issue, not an access-reproducibility one.'
accessions:
- phs003463.v6.p5
ontology_terms:
- long-covid
- sars-cov-2
- prospective-cohort
- biospecimens
- sex-differences
- pem
- ehr
- wearables
provided_capabilities: []
related:
- task:t013
- task:t040
- task:t061
- task:t070
- question:0007-mechanism-of-female-predominance-in-pais
- question:0015-does-pem-requirement-improve-cross-study-comparability
- question:0013-reproductive-stage-failed-immune-recovery-after-infection
- interpretation:0027-t061-severity-adjusted-pem-vehicle-triage
- interpretation:0030-t070-recover-adult-q0015-controlled-access-gate
---

# RECOVER-Adult

**Candidate dataset for `task:t013`.** `status: candidate`, `tier: track` — controlled, application-gated;
the eventual primary-positive-test vehicle for the menopause→PAIS line (`task:t040`).

## What it is

Largest US natural-history long COVID cohort (83 sites, ≥3 mo post-infection enrollment). EHR +
wearables + clinical assessments + **banked biospecimens** (serum/plasma/PBMC). Validated PASC index
(PEM-weighted); AMH already measured (unique); full E2/T/FSH/LH/SHBG panel **assayable de novo** but
not yet run. Released via NHLBI BioData Catalyst / dbGaP as `phs003463.v6.p5`.

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

**t061/q0015 vehicle triage (2026-06-26):** best controlled-access route for a severity-adjusted
PEM-positive vs PEM-negative molecular contrast, but not publicly/local-computable. Requires dbGaP/BioData
Catalyst access plus confirmation that the needed omics module and non-PEM severity covariates are
available in the same participants.

**t070/q0015 controlled-access gate (2026-06-26):** phenotype gates clear, molecular gate does not. The
current public Adult/Pregnancy release (`phs003463.v6.p5`; data through 2025-12-05, released 2026-05-13)
has participant-level controlled access, repeated PASC Symptoms variables, DePaul-style PEM
bother/frequency/severity fields, acute-severity/treatment items, EHR records for a subset, biospecimen
inventory, and raw wearable data. The public dbGaP page exposes phenotype datasets and variables but not
selectable molecular datasets, and the March 2026 release notes do not identify released proteomics,
metabolomics, transcriptomics, or immune-profiling matrices joinable to the symptom rows. Therefore this
dataset is still a DAR/scoping route for q0015, not a runnable molecular analysis vehicle.
