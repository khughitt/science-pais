---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse251849-longcovid-pbmc-cognitive
kind: dataset
title: GSE251849 — Long COVID PBMC (cognitive phenotype)
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
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE251849
accessions:
- GSE251849
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

# GSE251849 — Long COVID PBMC (cognitive phenotype)

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: evaluate-next`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Long COVID with a cognitive/brain-fog phenotype, PBMC bulk RNA-seq, ≈11 vs 12 [UNVERIFIED] (small).

## Corpus role (t117)

- **Matrix:** strict-primary
- **onset_certainty:** documented
- **Conditional/LOO flag:** small N — LOO-drop candidate.

## Access / caveats

Public accession (`GSE251849`); per-sample expression matrix downloadability **not yet confirmed** — verification is t117 WP1.
