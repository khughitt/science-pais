---
id: dataset:all-of-us-covid
kind: dataset
title: All of Us Research Program — COVID / long COVID
status: candidate
created: "2026-06-21"
updated: "2026-06-21"
origin: external
source_class: observational
tier: track
license: proprietary
access:
  level: registration
  availability: available
  verified: false
  source_url: https://www.researchallofus.org/
  reproducibility:
    obtainability: registration
    execution: trusted-environment
    extractability: aggregate-reviewed
    notes: 'All of Us Researcher Workbench is a no-extraction TRE: registered/controlled-tier access + DURA, compute stays in the workbench, only disclosure-reviewed aggregates export. Registration does NOT rescue reproducibility because execution is enclave-bound -> trust-based-output, below the third-party bar.'
accessions: []
ontology_terms:
- long-covid
- sars-cov-2
- ehr
- diverse-cohort
- sex-differences
provided_capabilities: []
capability_scope: clinical-outcome
related:
- task:t013
- task:t039
- question:0007-mechanism-of-female-predominance-in-pais
- question:0013-reproductive-stage-failed-immune-recovery-after-infection
- question:0003-acute-severity-threshold-for-self-sustaining-pais
---

# All of Us Research Program — COVID / long COVID

**Candidate dataset for `task:t013`.** `status: candidate`, `tier: track` — Researcher-Workbench-gated;
also the hormone-coverage-query vehicle for `task:t039`.

## What it is

Large US-diverse cohort (hundreds of thousands) with EHR + surveys + omics + Fitbit; intentional
demographic diversity that offsets UK Biobank's skew. Opportunistic EHR hormone labs (uncensored,
pre-pandemic enrollment) — the only candidate that could break reverse-causation.

## Why it fits t013

Lets you test female excess across a **more representative population** (acute severity + long-COVID
codes + mental-health surveys + fatigue items, all sex-stratifiable).

| Acute severity | Post-acute persistence | Neuropsychiatric | Somatic fatigue | Sex-stratified |
|---|---|---|---|---|
| yes (EHR) | yes (codes/surveys) | yes (surveys) | yes (items) | yes |

## Access / caveats

Workbench-only compute (no extraction); DURA + controlled-tier access. Long-COVID phenotyping less
mature than RECOVER. Hormone-coverage adequacy in peri/post-menopausal long-COVID women is the
make-or-break unknown (`task:t039`).
