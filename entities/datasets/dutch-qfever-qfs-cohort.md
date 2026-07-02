---
id: dataset:dutch-qfever-qfs-cohort
type: dataset
title: "Dutch Q-fever fatigue syndrome cohorts (Nijmegen/Radboud)"
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
  source_url: "https://link.springer.com/article/10.1186/s12967-020-02585-5"
  reproducibility:
    obtainability: named-collaboration
    execution: custodian-run
    extractability: none
    notes: "Clinical microdata private (Nijmegen/Radboud investigators); reproducible only by direct collaboration, no standardized third-party export -> insider-only. A separate omics slice IS deposited as dataset:gse130353-qfs-cfs-monocytes (independently third-party-reproducible); this entity is the clinical cohort, not that slice."
accessions: []
ontology_terms: [post-q-fever-fatigue, q-fever, coxiella-burnetii, prospective-cohort, sex-differences]
related:
  - task:t013
  - question:0007-mechanism-of-female-predominance-in-pais
  - paper:Raijmakers2019
  - question:0003-acute-severity-threshold-for-self-sustaining-pais
  - question:0017-deflationary-alternatives-vs-shared-pathophysiology
---

# Dutch Q-fever fatigue syndrome cohorts (Nijmegen/Radboud)

**Candidate dataset for `task:t013`.** `status: candidate`, `tier: track` — clinical microdata gated;
some omics in GEO (`dataset:gse130353-qfs-cfs-monocytes`).

## What it is

Clinical + multi-omics cohorts from the Dutch Q-fever epidemic (Keijmel, Raijmakers; Qure trial,
cytokine/IFN-γ studies). QFS follows ~20% of acute Q fever; cohorts in the low hundreds with fatigue
(CIS) and some psychological measures [@Keijmel2016; @Raijmakers2019].

## Why it fits t013 (sharpest natural experiment)

Acute Q fever is **male-skewed** (occupational/farming exposure), yet fatigue persistence is not — so
this is the cleanest test of hypothesis (a): does female excess **emerge in the post-acute phase even
when acute infection is male-dominated?**

| Acute severity | Post-acute persistence | Neuropsychiatric | Somatic fatigue | Sex-stratified |
|---|---|---|---|---|
| yes (acute Q fever) | yes (QFS) | partial | yes (CIS) | sex recorded |

## Access / caveats

Microdata private (collaboration). Acute male-skew is **exposure-driven** (confounds biological-sex
inference) — a strength for the natural experiment but must be modeled explicitly.
