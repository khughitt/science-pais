---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse217906-pics-pbmc-scrna
kind: dataset
title: GSE217906 — Immune-cell signatures of persistent inflammation-immunosuppression
  and catabolism syndrome (PICS)
status: candidate
provided_capabilities:
  - modality: transcriptomics
    assay: scrna
    trigger: sepsis
    cohort_design: case-control
created: '2026-07-17'
updated: '2026-07-17'
origin: external
dataset_class: deposit
source_class: observational
tier: evaluate-next
license: unknown
access:
  level: public
  availability: available
  verified: true
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE217906
  verification_method: landing-confirmed
  last_reviewed: '2026-07-17'
  verified_by: agent (verify-access)
accessions: []
ontology_terms:
- pics
- post-sepsis
- failed-recovery
- scrna-seq
related:
- question:0033-frailty-and-pre-frailty-as-an-independent-pais-boundary-condition-with
identity_context:
  taxon: 9606
  assembly:
    label: UNKNOWN
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# GSE217906 — Immune-cell signatures of persistent inflammation-immunosuppression and catabolism syndrome (PICS)

**Candidate dataset.** `status: candidate` — catalogued but not yet acquired.

## What it is

PBMC scRNA-seq profiling **persistent inflammation–immunosuppression and catabolism
syndrome (PICS)**: 16 samples — 4 PICS patients, 2 acute sepsis, 3 healthy controls. NovaSeq 6000.

## Why it fits

The only public omics deposit located that profiles **PICS itself** — the failed-recovery
phenotype after sepsis. It is a direct read-across to the project's core "failed recovery of
homeostasis after an acute insult" frame (`hypothesis:0001`), from a non-viral trigger.

## Access / caveats

**Public.** GEO landing page confirmed 2026-07-17; `GSE217906_RAW.tar` (663 Mb, MTX/TSV)
plus SRA.

**Caveats.**
- **n=4 PICS.**
- **Frailty is not measured** per-sample, so any frailty coupling is inferential. This is why the
  entity makes **no `stratification` claim** and does not satisfy `question:0033` — the deposit
  characterises failed recovery, but cannot test frailty as the modifier.

## Access verification log

- 2026-07-17 (agent (verify-access)): GEO landing page confirmed public 2026-07-17: 16 samples (4 PICS, 2 acute sepsis, 3 HC), NovaSeq 6000, GSE217906_RAW.tar 663Mb (MTX/TSV) downloadable + SRA. Frailty is NOT measured per-sample; frailty coupling is inferential.
