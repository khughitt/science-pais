---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse267625-longcovid-wholeblood
kind: dataset
title: GSE267625 — Long COVID whole-blood longitudinal (P4O2)
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
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE267625
accessions:
- GSE267625
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

# GSE267625 — Long COVID whole-blood longitudinal (P4O2)

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: evaluate-next`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Long COVID whole-blood bulk RNA-seq, ≈95 subjects [UNVERIFIED], longitudinal, drawn from the P4O2 post-hospitalised COVID cohort.

## Corpus role (t117)

- **Matrix:** strict-primary
- **onset_certainty:** documented
- **Conditional/LOO flag:** longitudinal design — one contrast must be defined per subject/timepoint policy in WP2.

## Access / caveats

Public accession (`GSE267625`); per-sample expression matrix downloadability **not yet confirmed** — verification is t117 WP1.
