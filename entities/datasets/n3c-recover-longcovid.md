---
id: dataset:n3c-recover-longcovid
type: dataset
title: "N3C — National COVID Cohort Collaborative (+ RECOVER-EHR)"
status: candidate
created: "2026-06-21"
updated: "2026-07-01"
origin: external
source_class: observational
tier: evaluate-next
license: proprietary
access:
  level: mixed
  availability: available
  verified: false
  source_url: "https://covid.cd2h.org/dashboard/recover"
accessions: []
ontology_terms: [long-covid, sars-cov-2, ehr, computable-phenotype, sex-differences]
related:
  - task:t013
  - task:t079
  - plan:0005-autoimmune-diathesis-sex-modifier-pais-analysis-plan
  - interpretation:0031-t079-n3c-vs-opensafely-vehicle-decision
  - dataset:opensafely-longcovid
  - question:0007-mechanism-of-female-predominance-in-pais
  - question:0003-acute-severity-threshold-for-self-sustaining-pais
consumed_by:
  - plan:0006-n3c-synthetic-prototype-autoimmune-sex-pais-pipeline
  - task:t079
siblings:
  - dataset:n3c-recover-longcovid-synthetic
---

# N3C — National COVID Cohort Collaborative (+ RECOVER-EHR)

**Candidate dataset for `task:t013`.** `status: candidate`, `tier: evaluate-next` — **open synthetic
tier** lets you build the pipeline now; real data is enclave-gated.

## What it is

Multi-site federated EHR (millions of patients) with a computable long-COVID phenotype. Tiered access:
Synthetic (open) → De-identified → Limited (DUA + institutional approval, enclave-only compute).

## Why it fits t013

EHR scale enables **sex-stratified acute-severity-vs-persistence odds ratios** and a built-in
**dissociation proxy**: psychiatric ICD codes vs fatigue codes. Prototype on the synthetic tier, then
apply for real data.

| Acute severity | Post-acute persistence | Neuropsychiatric | Somatic fatigue | Sex-stratified |
|---|---|---|---|---|
| yes (hospitalization) | yes (computable phenotype) | yes (ICD) | yes (ICD) | yes |

## Access / caveats

Enclave-only (no extraction). EHR-coded long COVID is **noisy / under-coded** (vendor-dependent);
no patient-reported fatigue severity. Single trigger.

## Access verification log

- 2026-07-01 (agent): consumed by `plan:0006-n3c-synthetic-prototype-autoimmune-sex-pais-pipeline`
  (t079/BC-2) — **open synthetic slice only**; the de-identified/Limited enclave siblings remain
  out of scope pending DUA. Locked as primary vehicle by `interpretation:0031`.
