---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse128078-mecfs-wholeblood
kind: dataset
title: GSE128078 — ME/CFS whole-blood transcriptome (PEM)
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
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE128078
accessions:
- GSE128078
ontology_terms:
- me-cfs
- whole-blood
- rna-seq
provided_capabilities:
  - modality: transcriptomics
    assay: bulk-rna
    trigger: mixed
    cohort_design: case-control
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0001-shared-molecular-signature-across-triggers
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE128078 — ME/CFS whole-blood transcriptome (PEM)

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: evaluate-next`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

ME/CFS with post-exertional-malaise characterisation, whole-blood bulk RNA-seq, ≈14 vs 11 [UNVERIFIED]. No per-subject documented infectious onset.

## Corpus role (t117)

- **Matrix:** ME/CFS-sensitivity
- **onset_certainty:** unknown-per-subject
- **Conditional/LOO flag:** enters ONLY the ME/CFS sensitivity matrix, never the strict-primary verdict.

## Access / caveats

Public accession (`GSE128078`); per-sample expression matrix downloadability **not yet confirmed** — verification is t117 WP1.
