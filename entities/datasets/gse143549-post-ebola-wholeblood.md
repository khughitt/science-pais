---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse143549-post-ebola-wholeblood
kind: dataset
title: GSE143549 — Post-Ebola whole-blood transcriptome (survivors)
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
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE143549
accessions:
- GSE143549
ontology_terms:
- post-ebola
- ebola
- whole-blood
- rna-seq
provided_capabilities:
  - modality: transcriptomics
    assay: bulk-rna
    trigger: ebola
    cohort_design: case-control
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0001-shared-molecular-signature-across-triggers
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE143549 — Post-Ebola whole-blood transcriptome (survivors)

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: evaluate-next`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Post-Ebola survivors, whole-blood bulk RNA-seq, ≈26 vs 33 [UNVERIFIED], sampled ≈23 months post-infection [UNVERIFIED].

## Corpus role (t117)

- **Matrix:** strict-primary
- **onset_certainty:** documented
- **Conditional/LOO flag:** rare trigger, single-platform contrast — non-arbitrating for platform-independent biology (rank conclusion must survive dropping it).

## Access / caveats

Public accession (`GSE143549`); per-sample expression matrix downloadability **not yet confirmed** — verification is t117 WP1.
