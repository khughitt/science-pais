---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse45924-primary-ebv-longitudinal
kind: dataset
title: GSE45924 — Peripheral blood gene expression during primary EBV infection (seronegative / acute IM / latent)
status: candidate
provided_capabilities:
- data_product: data-product:gene-expression-microarray
  qualifiers:
    cohort_design: prospective-longitudinal
    trigger: ebv
created: "2026-07-17"
updated: "2026-07-17"
origin: external
dataset_class: deposit
source_class: observational
tier: evaluate-next
license: unknown
access:
  level: public
  availability: available
  verified: true
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE45924
  verification_method: landing-confirmed
  last_reviewed: '2026-07-17'
  verified_by: agent (verify-access)
accessions: []
ontology_terms:
- infectious-mononucleosis
- ebv
- pre-infection-baseline
- microarray
related:
- question:0051-prior-symptomatic-ebv-mononucleosis-as-pais-risk-amplifier
identity_context:
  taxon: 9606
  assembly:
    label: UNKNOWN
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# GSE45924 — Peripheral blood gene expression during primary EBV infection (seronegative / acute IM / latent)

**Candidate dataset.** `status: candidate` — catalogued but not yet acquired.

## What it is

SuperSeries (sub-series GSE45918 / GSE45919) of peripheral blood gene expression across
**primary EBV infection**: 40 samples spanning **seronegative (pre-infection)**, acute infectious
mononucleosis, and latent EBV timepoints. Illumina HumanRef-8 v3.0 + HumanHT-12 V4.0.

## Why it fits

The one deposit that directly tests `question:0051`'s **imprint premise** — the same subjects
sampled *before* EBV acquisition, during IM, and in latency.

**It should be confronted, not cited selectively:** the source study reports **no lasting expression
changes in latency**, i.e. published **disconfirming evidence** for a durable transcriptomic imprint
from primary EBV infection. `question:0051` should engage this directly rather than route around it.

## Access / caveats

**Public.** GEO landing page confirmed 2026-07-17; `GSE45924_RAW.tar` (30.1 Mb).

**Caveats.**
- Stratifies **EBV state** (seronegative / acute / latent), **not IM-history-as-exposure with a PAIS
  outcome** — so it makes no `stratification: im-history` claim and does not satisfy
  `question:0051`.
- **No asymptomatic-seroconverter arm** — the exact comparator q0051 needs is absent.
- No fatigue or PAIS follow-up; small n; bulk microarray, so a null at this resolution is weak
  evidence of absence.

## Access verification log

- 2026-07-17 (agent (verify-access)): GEO landing page confirmed public 2026-07-17: SuperSeries (sub GSE45918 Ref8 / GSE45919 HT12), 40 samples, GPL6883+GPL10558, GSE45924_RAW.tar 30.1Mb downloadable. Confirmed to carry seronegative(pre-infection) / acute IM / latent EBV timepoints. Source paper reports NO lasting expression change in latency -- i.e. published DISCONFIRMING evidence for a durable transcriptomic imprint; no asymptomatic-seroconverter arm.
