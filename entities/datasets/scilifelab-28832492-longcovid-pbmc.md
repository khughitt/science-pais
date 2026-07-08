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
  verified: true
  verification_method: landing-confirmed
  last_reviewed: "2026-07-08"
  verified_by: "agent (t117 WP1)"
  source_url: https://doi.org/10.17044/scilifelab.28832492
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: "FigShare deposit contains salmon.merged.gene_counts.tsv (22 MB, per-sample nf-core/rnaseq gene counts, all 110 samples) + SamplesPC.txt (sample info) + README/MANIFEST; publicly downloadable, staging to disk deferred to workflow execution"
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

Post-COVID PBMC **bulk RNA-seq** (polyA, nf-core/rnaseq → salmon gene counts). Confirmed against the FigShare deposit + linked paper (Fineschi, Klar et al., *Front. Immunol.* 2025; PMC12162955) on 2026-07-08: **60 post-COVID patients vs 50 controls**, tissue **PBMC**, assay **bulk RNA-seq**, sampled at a **median 28 months** after a mild SARS-CoV-2 infection. **Control type is infected-recovered** (controls contracted SARS-CoV-2 in the same period but recovered fully without long-term symptoms) — not healthy-naive. Case-vs-control contrast well-powered (60 vs 50). Deposited on SciLifeLab FigShare (DOI `10.17044/scilifelab.28832492`); no GEO accession.

## Corpus role (t117)

- **Matrix:** strict-primary
- **onset_certainty:** documented
- **Conditional/LOO flag:** non-GEO deposit — staging path differs (FigShare); confirm per-sample matrix format in WP1.

## Access / caveats

Public FigShare deposit (DOI `10.17044/scilifelab.28832492`, no GEO accession); per-sample expression matrix **confirmed downloadable** — `salmon.merged.gene_counts.tsv` (22 MB, all 110 samples) plus `SamplesPC.txt` sample sheet — verified in t117 WP1 (2026-07-08). Non-GEO staging path (FigShare API/DOI); note the FigShare web page returns HTTP 403 to unauthenticated fetch but the file list resolves via the FigShare API (`api.figshare.com/v2/articles/28832492`).
