---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:prjna1001790-post-chikv-wholeblood
kind: dataset
title: PRJNA1001790 — Post-chikungunya whole-blood transcriptome
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
  source_url: https://www.ncbi.nlm.nih.gov/bioproject/PRJNA1001790
accessions:
- PRJNA1001790
ontology_terms:
- post-chikungunya
- chikungunya
- whole-blood
- rna-seq
provided_capabilities:
  - modality: transcriptomics
    assay: bulk-rna
    trigger: chikungunya
    cohort_design: case-control
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0001-shared-molecular-signature-across-triggers
- hypothesis:0001-shared-dysregulated-attractor
---

# PRJNA1001790 — Post-chikungunya whole-blood transcriptome

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: track`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Post-chikungunya whole-blood bulk RNA-seq, ≈29 vs 25 [UNVERIFIED], sampled ≤ day 21 [UNVERIFIED] (early window).

## Corpus role (t117)

- **Matrix:** strict-primary **(PROVISIONAL — floor-gated)**. Sampled ~day 21 — *inside* the plan's ≥4 wk post-acute floor — so this deposit is **NOT counted in the strict trigger/K total**. `matrix: strict-primary` stands only as a *target* pending the WP1 timepoint check.
- **onset_certainty:** documented
- **WP1 resolution:** promote into the strict count **only if** later post-acute *symptomatic* samples are verified; otherwise **demote** to the early-convalescent decoy/specificity layer. Additionally SRA-only → the pinned raw-read quantification path must be verified (G4) before staging.
- **Conditional/LOO flag (if promoted):** SRA-only platform axis — LOO-drop candidate; feeds the platform-LOO artifact control.

## Access / caveats

Public accession (`PRJNA1001790`); per-sample expression matrix downloadability **not yet confirmed** — verification is t117 WP1. SRA/BioProject deposit only — may require raw-read quantification in WP1.
