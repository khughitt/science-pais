---
id: dataset:slice-ptlds-aucott
type: dataset
title: "Johns Hopkins SLICE — Lyme / post-treatment Lyme disease syndrome"
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
  source_url: "https://www.frontiersin.org/articles/10.3389/fmed.2017.00224/full"
accessions: []
ontology_terms: [ptlds, lyme-disease, borrelia-burgdorferi, prospective-cohort, sex-differences]
related:
  - task:t013
  - question:0007-mechanism-of-female-predominance-in-pais
  - topic:shared-failure-mode-across-pais
---

# Johns Hopkins SLICE — Lyme / PTLDS

**Candidate dataset for `task:t013`.** `status: candidate`, `tier: track` — by-collaboration; no public
microdata located. The cleanest **non-COVID prospective acute→post-acute** design in the catalog.

## What it is

Johns Hopkins Lyme Disease Research Center prospective cohort following early Lyme (erythema migrans)
→ 6-month PTLDS, with **depression instruments measured at each visit** alongside fatigue/pain/cognition.

## Why it fits t013

A **bacterial trigger** with prospective acute→post-acute transition AND explicit separable
**neuropsychiatric vs somatic** outcomes — directly tests the dissociation hypothesis outside COVID.

| Acute severity | Post-acute persistence | Neuropsychiatric | Somatic fatigue | Sex-stratified |
|---|---|---|---|---|
| yes (early Lyme) | yes (6-mo PTLDS) | yes (depression) | yes (~50% severe) | sex recorded |

## Access / caveats

Private microdata (contact JH center); some omics substudies may be in GEO/dbGaP (unverified). Modest N
for sex-stratified PTLDS-incidence ORs. **Data-poor trigger** in our corpus — high marginal value.
