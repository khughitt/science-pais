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
license: restricted
access:
  level: controlled
  availability: available
  verified: false
  source_url: "https://www.immport.org/shared/study/SDY1760"
accessions: [SDY1760, phs002686]
ontology_terms: [long-covid, sars-cov-2, multiomics, sex-differences, patient-reported-outcomes]
related:
  - task:t013
  - question:0007-mechanism-of-female-predominance-in-pais
  - paper:Ozonoff2024
  - paper:Gabernet2025
---

# IMPACC — Immunophenotyping Assessment in a COVID-19 Cohort

**Candidate dataset for `task:t013`.** `status: candidate`, `tier: evaluate-next` — controlled-access,
analyzable via secondary use; no local `datapackage` built.

## What it is

n≈1,164 hospitalized COVID-19 survivors (20 US hospitals, 2020–21; convalescent multiomics subset
n=513, ~41% female). Plasma metabolomics, PBMC transcriptomics, Olink proteomics, CyTOF, plus PROMIS
patient-reported outcomes. Anchor papers already in-corpus: `paper:Ozonoff2024` (PRO phenotype
clusters), `paper:Gabernet2025` (SPEAR recovery factor; androgen/mediator signal).

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
