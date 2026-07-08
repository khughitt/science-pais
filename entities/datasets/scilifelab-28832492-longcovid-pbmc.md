---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:scilifelab-28832492-longcovid-pbmc
kind: dataset
title: SciLifeLab 28832492 — Long COVID PBMC (28 mo)
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
  source_url: https://doi.org/10.17044/scilifelab.28832492
accessions: []
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

# SciLifeLab 28832492 — Long COVID PBMC (28 mo)

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: evaluate-next`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Long COVID PBMC bulk RNA-seq, ≈60 long-COVID vs 50 control [UNVERIFIED], sampled ≈28 months post-infection [UNVERIFIED] (long follow-up). Deposited on SciLifeLab FigShare (DOI `10.17044/scilifelab.28832492`); no GEO accession.

## Corpus role (t117)

- **Matrix:** strict-primary
- **onset_certainty:** documented
- **Conditional/LOO flag:** non-GEO deposit — staging path differs (FigShare); confirm per-sample matrix format in WP1.

## Access / caveats

Public FigShare deposit (DOI `10.17044/scilifelab.28832492`, no GEO accession); per-sample expression matrix downloadability **not yet confirmed** — verification is t117 WP1. Non-GEO staging path (FigShare) — confirm per-sample matrix format in WP1.
