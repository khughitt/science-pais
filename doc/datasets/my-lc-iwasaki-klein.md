---
id: dataset:my-lc-iwasaki-klein
type: dataset
title: "MY-LC — Mount Sinai–Yale Long COVID immune/sex cohort"
status: candidate
created: "2026-06-21"
updated: "2026-06-21"
origin: external
source_class: observational
tier: evaluate-next
license: unknown
access:
  level: mixed
  availability: available
  verified: false
  source_url: "https://www.biorxiv.org/content/10.1101/2024.06.18.599612"
accessions: []
ontology_terms: [long-covid, sars-cov-2, immune-profiling, sex-hormones, sex-differences]
related:
  - task:t013
  - question:0007-mechanism-of-female-predominance-in-pais
  - paper:Silva2024
  - paper:Shahbaz2025
---

# MY-LC — Mount Sinai–Yale Long COVID immune/sex cohort

**Candidate dataset for `task:t013`.** `status: candidate`, `tier: evaluate-next` — published
sex-stratified estimates usable now; participant-level data controlled, some processed data in
supplements/GEO.

## What it is

Deep immune/hormonal case-control (order hundreds), explicitly **sex-stratified** (the study's focus):
flow/immune profiling, SERA epitope reactivity, Olink proteomics. Low testosterone predicts symptom
burden across sexes; female LC shows higher EBV/CMV/HSV-2 reactivity; male LC a TGF-β signature.

## Why it fits t013

Provides **published sex-stratified effect sizes** and a mechanistic sex axis (HPG suppression) that
bear directly on interpreting female excess.

| Acute severity | Post-acute persistence | Neuropsychiatric | Somatic fatigue | Sex-stratified |
|---|---|---|---|---|
| no | yes (>6 wk LC) | partial (neuro subset) | yes | yes |

## Access / caveats

Cross-sectional persistence focus, **no acute-severity arm**. Single-center; participant-level data
gated. Use published sex-stratified estimates + GEO/supplement processed data.
