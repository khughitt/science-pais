---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse224615-longcovid-wholeblood
kind: dataset
title: GSE224615 — Long COVID whole-blood transcriptome (8 mo)
status: candidate
created: '2026-07-07'
updated: '2026-07-07'
origin: external
dataset_class: deposit
source_class: observational
tier: evaluate-next
license: unknown
access:
  level: public
  availability: available
  verified: false
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE224615
accessions:
- GSE224615
ontology_terms:
- long-covid
- sars-cov-2
- whole-blood
- rna-seq
provided_capabilities:
  - modality: transcriptomics
    assay: bulk-rna
    trigger: sars-cov-2
    cohort_design: case-control
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0001-shared-molecular-signature-across-triggers
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE224615 — Long COVID whole-blood transcriptome (8 mo)

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: evaluate-next`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Long COVID whole-blood bulk RNA-seq, ≈27 long-COVID vs 16 recovered [UNVERIFIED], sampled ≈8 months post-infection [UNVERIFIED]. Recovered-control arm is a design strength (scored favourably).

## Corpus role (t117)

- **Matrix:** strict-primary
- **onset_certainty:** documented
- **Conditional/LOO flag:** none

## Access / caveats

Public accession (`GSE224615`); per-sample expression matrix downloadability **not yet confirmed** — verification is t117 WP1.
