---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse240694-omicron-ba2-6mo-china
kind: dataset
title: GSE240694 — Omicron BA.2 breakthrough infection, 6-month prospective scRNA-seq (China)
status: candidate
provided_capabilities:
- data_product: data-product:gene-expression-single-cell
  qualifiers:
    cohort_design: prospective-longitudinal
    trigger: sars-cov-2
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
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE240694
  verification_method: landing-confirmed
  last_reviewed: '2026-07-17'
  verified_by: agent (verify-access)
accessions: []
ontology_terms:
- long-covid
- sars-cov-2
- east-asian-ancestry
- scrna-seq
related:
- question:0032-pais-burden-phenotype-and-mechanism-in-lmic-and-ancestrally-diverse
identity_context:
  taxon: 9606
  assembly:
    label: UNKNOWN
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# GSE240694 — Omicron BA.2 breakthrough infection, 6-month prospective scRNA-seq (China)

**Candidate dataset.** `status: candidate` — catalogued but not yet acquired.

## What it is

Single-cell RNA-seq (plus proteomics in the source study) from a 6-month prospective
follow-up of Omicron BA.2 breakthrough infection in Beijing: 9 samples (5 convalescent, 4 healthy
controls), NovaSeq 6000. Reports persistent coagulation disorder and immunity–metabolism imbalance
at 6 months.

## Why it fits

An East-Asian cohort at a **true post-acute timepoint** for `question:0032`, touching the
thromboinflammation and metabolic/mitochondrial mechanism families directly.

## Access / caveats

**Processed layer public; raw layer gated.** GEO landing page confirmed 2026-07-17:
processed TAR (634.7 Mb archive) downloadable. **Raw reads are not in GEO** — they sit in China's Genome
Sequence Archive under **HRA004484**, a request-gated human-restricted tier. The processed layer
clears the D-004 bar; the raw layer does not.

**Caveats.**
- **n=9** — descriptive only.
- Single East-Asian population with **no ancestry contrast**, so it does not stratify ancestry and
  does not satisfy `question:0032`'s requirement. It contributes non-EUR *representation*, which is
  not the same thing as an ancestry effect-modification design.

## Access verification log

- 2026-07-17 (agent (verify-access)): GEO landing page confirmed public 2026-07-17: 9 samples (5 BA.2 convalescent, 4 HC), NovaSeq 6000, processed TAR 634.7Mb downloadable. Raw reads are NOT here: they sit in China GSA/HRA004484, a request-gated human-restricted tier (D-004 below-bar for the raw layer; processed layer clears).
