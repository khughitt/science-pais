---
id: dataset:impacc-immunophenotyping-covid
type: dataset
title: "IMPACC — Immunophenotyping Assessment in a COVID-19 Cohort"
status: candidate
created: "2026-06-21"
updated: "2026-06-21"
origin: external
source_class: observational
tier: evaluate-next
license: proprietary
access:
  level: controlled
  availability: available
  verified: false
  source_url: "https://www.immport.org/shared/study/SDY1760"
accessions: [SDY1760, phs002686]
ontology_terms: [long-covid, sars-cov-2, multiomics, sex-differences, patient-reported-outcomes]
related:
  - task:t013
  - task:t061
  - question:0007-mechanism-of-female-predominance-in-pais
  - question:0015-does-pem-requirement-improve-cross-study-comparability
  - paper:Ozonoff2024
  - paper:Gabernet2025
  - question:0003-acute-severity-threshold-for-self-sustaining-pais
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
  - interpretation:0027-t061-severity-adjusted-pem-vehicle-triage
---

# IMPACC — Immunophenotyping Assessment in a COVID-19 Cohort

**Candidate dataset for `task:t013`.** `status: candidate`, `tier: evaluate-next` — controlled-access,
analyzable via secondary use; no local `datapackage` built.

## What it is

n≈1,164 hospitalized COVID-19 survivors (20 US hospitals, 2020–21; convalescent multiomics subset
n=513, ~41% female). Plasma metabolomics, PBMC transcriptomics, Olink proteomics, CyTOF, plus PROMIS
patient-reported outcomes. Anchor papers already in-corpus: `paper:Ozonoff2024` (PRO phenotype
clusters), `paper:Gabernet2025` (SPEAR recovery factor; androgen/mediator signal) [@Ozonoff2024; @Gabernet2025].

## Why it fits t013

Captures **acute severity** (ICU/ventilation/SOFA) **and post-acute** 12-month phenotype clusters,
**sex-stratified**: female sex is a consistent low-recovery risk factor; the **PHY (fatigue)** and
**COG (cognitive/mood)** clusters are *separate* — a built-in neuropsychiatric-vs-somatic dissociation
handle.

| Acute severity | Post-acute persistence | Neuropsychiatric | Somatic fatigue | Sex-stratified |
|---|---|---|---|---|
| yes | yes (4 clusters) | yes (COG) | yes (PHY) | yes |

## Access / caveats

Controlled (ImmPort SDY1760 / dbGaP phs002686); processed data obtainable without new assays.
**Hospitalized-only** (acute-severity HPG suppression confound, per `report:0005`); no menopausal
staging; no pre-infection baseline.

**t061/q0015 vehicle triage (2026-06-26):** not an admissible substitute for the decisive
severity-adjusted PEM molecular contrast on the documented public phenotype surface. It has post-acute
PRO clusters and multi-omics, but not a validated PEM-positive vs PEM-negative design with severity-matched
arms; use it for adjacent severity/phenotype-cluster questions unless controlled metadata reveals a true
PEM item.
