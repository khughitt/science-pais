---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:prjna1184005-longcovid-pbmc
kind: dataset
title: PRJNA1184005 — Long COVID PBMC (pilot, n=7/7)
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
  source_url: https://www.ncbi.nlm.nih.gov/bioproject/PRJNA1184005
accessions:
- PRJNA1184005
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

# PRJNA1184005 — Long COVID PBMC (pilot, n=7/7)

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: track`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Long COVID PBMC bulk RNA-seq, ≈7 vs 7 [UNVERIFIED] (very small pilot).

## Corpus role (t117)

- **Matrix:** strict-primary
- **onset_certainty:** documented
- **Conditional/LOO flag:** very small N — LOO-drop candidate; SRA-only (may need raw-read quantification in WP1).

## Access / caveats

Public accession (`PRJNA1184005`); per-sample expression matrix downloadability **not yet confirmed** — verification is t117 WP1. SRA/BioProject deposit only — may require raw-read quantification in WP1.
