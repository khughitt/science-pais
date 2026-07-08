---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse226260-longcovid-pbmc
kind: dataset
title: GSE226260 — Long COVID PBMC transcriptome (>6 mo)
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
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE226260
accessions:
- GSE226260
ontology_terms:
- long-covid
- sars-cov-2
- pbmc
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

# GSE226260 — Long COVID PBMC transcriptome (>6 mo)

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: evaluate-next`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Long COVID PBMC bulk RNA-seq, ≈46 long-COVID vs 178 control (recovered + healthy) [UNVERIFIED], sampled >180 d post-infection [UNVERIFIED]. Flagged in the discovery sweep as one of the best-designed long-COVID blood-bulk sets.

## Corpus role (t117)

- **Matrix:** strict-primary
- **onset_certainty:** documented
- **Conditional/LOO flag:** none

## Access / caveats

Public accession (`GSE226260`); per-sample expression matrix downloadability **not yet confirmed** — verification is t117 WP1.
