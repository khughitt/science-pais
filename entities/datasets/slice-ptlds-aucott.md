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
license: proprietary
access:
  level: controlled
  availability: available
  verified: false
  source_url: "https://www.frontiersin.org/articles/10.3389/fmed.2017.00224/full"
  reproducibility:
    obtainability: named-collaboration
    execution: custodian-run
    extractability: none
    notes: "Individual-level SLICE clinical cohort private (contact Johns Hopkins Lyme Disease Research Center); reproducible only by direct collaboration, no standardized third-party export -> insider-only. Some omics substudies MAY be deposited in GEO/dbGaP (UNVERIFIED); if confirmed, register those as separate third-party-reproducible slices."
accessions: []
ontology_terms: [ptlds, lyme-disease, borrelia-burgdorferi, prospective-cohort, sex-differences]
provided_capabilities:
  - modality: epidemiology
    trigger: lyme-disease
    cohort_design: prospective-longitudinal
    outcome: fatigue
related:
  - task:t013
  - question:0007-mechanism-of-female-predominance-in-pais
  - topic:shared-failure-mode-across-pais
  - question:0003-acute-severity-threshold-for-self-sustaining-pais
  - question:0017-deflationary-alternatives-vs-shared-pathophysiology
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
