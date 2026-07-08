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
  reproducibility:
    obtainability: public
    execution: local
    extractability: none
    notes: "SRA raw reads only (14 RNA-seq runs, NovaSeq 6000, ~94 Gbases) — no processed per-sample expression matrix deposited; matrix requires pinned quantification (G4)"
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

Long COVID PBMC **bulk RNA-seq** (BioProject title: "Long COVID versus COVID recovered pilot study", submitted by La Trobe University, 2024-11-09). Confirmed against the BioProject/SRA record (2026-07-08): tissue **PBMC**; **14 BioSamples / 14 SRA RNA-seq runs** on **Illumina NovaSeq 6000** — bulk (not single-cell); ~94 Gbases total. Contrast is **Long COVID vs COVID-recovered** (infected-recovered controls). Per-run split consistent with the claimed **≈7 vs 7** (14 runs total) but the explicit case/control assignment is **[UNVERIFIED] — not shown in the SRA run table**. Time post-infection at sampling **[UNVERIFIED] — not stated in record**. **SRA raw reads only — no processed expression matrix deposited.**

## Corpus role (t117)

- **Matrix:** strict-primary **(DEFERRED, WP1 2026-07-08).** SRA raw-reads only — **no downloadable per-sample matrix** (G4 blocker), only 14 samples, and the case/control split + sampling window are unverifiable from the record. **Not in the matrix** until the pinned quantification path (G4) is implemented and the split confirmed; enters only if WP1-round-2 resolves both.
- **onset_certainty:** documented
- **Conditional/LOO flag:** very small N — LOO-drop candidate even if quantified.

## Access / caveats

Public accession (`PRJNA1184005`); **SRA raw reads only — no processed per-sample expression matrix deposited** (confirmed t117 WP1, 2026-07-08). Building a matrix requires pinned raw-read quantification (G4). `verified: false` retained: reads are public but a ready-to-use matrix is not.
