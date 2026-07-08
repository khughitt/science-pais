---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse16059-mecfs-twins-pbl
kind: dataset
title: GSE16059 — ME/CFS discordant-twin blood-leukocyte microarray
status: candidate
created: '2026-07-07'
updated: '2026-07-07'
origin: external
dataset_class: deposit
source_class: observational
tier: track
license: unknown
access:
  level: public
  availability: available
  verified: false
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE16059
accessions:
- GSE16059
ontology_terms:
- me-cfs
- pbl
- microarray
provided_capabilities:
  - modality: transcriptomics
    assay: microarray
    trigger: mixed
    cohort_design: case-control
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0001-shared-molecular-signature-across-triggers
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE16059 — ME/CFS discordant-twin blood-leukocyte microarray

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: track`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

ME/CFS discordant monozygotic twins, peripheral-blood-leukocyte microarray [UNVERIFIED]. Paired within-twin-pair design.

## Corpus role (t117)

- **Matrix:** ME/CFS-sensitivity
- **onset_certainty:** unknown-per-subject
- **Conditional/LOO flag:** enters ONLY the ME/CFS sensitivity matrix; discordant-twin (paired) design + microarray platform — handle pairing in WP2.

## Access / caveats

Public accession (`GSE16059`); per-sample expression matrix downloadability **not yet confirmed** — verification is t117 WP1.
