---
id: dataset:mcam-mecfs
type: dataset
title: "MCAM — Multi-Site Clinical Assessment of ME/CFS (CDC)"
status: candidate
created: "2026-06-21"
updated: "2026-06-21"
origin: external
source_class: observational
tier: evaluate-next
license: restricted
access:
  level: registration
  availability: available
  verified: false
  source_url: "https://searchmecfs.org/Home/Studies"
accessions: []
ontology_terms: [me-cfs, post-infectious-fatigue, clinical-cohort, biospecimens, sex-differences]
related:
  - task:t013
  - question:0007-mechanism-of-female-predominance-in-pais
  - topic:shared-failure-mode-across-pais
---

# MCAM — Multi-Site Clinical Assessment of ME/CFS (CDC)

**Candidate dataset for `task:t013`.** `status: candidate`, `tier: evaluate-next` — biospecimens/data via
searchMECFS / MapMECFS application.

## What it is

Best-characterized US ME/CFS cohort (Stage 1 ~471 ME/CFS + matched controls) with standardized
**fatigue + mood instruments** and biospecimens. Strong female predominance (~3–4:1) typical of ME/CFS.
(The UK ME/CFS Biobank, LSHTM, is an analogous gated option for sex-rich omics.)

## Why it fits t013

Anchors the **established-PAIS** end of the spectrum with separable fatigue vs mood instruments —
useful as the persistence reference, and for testing whether female-predominant mechanisms are shared.

| Acute severity | Post-acute persistence | Neuropsychiatric | Somatic fatigue | Sex-stratified |
|---|---|---|---|---|
| no (prevalent cases) | yes (established ME/CFS) | yes (mood) | yes | yes |

## Access / caveats

**Prevalent cases → no acute→post-acute transition**; trigger often unconfirmed. Application/governance
overhead. Deliberate sex/age selection in some sub-studies limits sex-difference estimation.
