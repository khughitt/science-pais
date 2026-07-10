---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse224615-longcovid-wholeblood
kind: dataset
title: GSE224615 — Long COVID whole-blood transcriptome (8 mo)
status: candidate
created: '2026-07-07'
updated: '2026-07-10'
consumed_by:
- plan:0010-crosspais-pathway-response-rank-estimation
origin: external
dataset_class: deposit
source_class: observational
tier: evaluate-next
license: unknown
access:
  level: public
  availability: available
  verified: false
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE224615
  reproducibility:
    obtainability: public
    execution: local
    extractability: none
    notes: BLOCKER — no per-sample expression matrix on GEO. The only series-level
      supplementary is GSE224615_DEGs.xlsx (a differential-expression summary table,
      not per-sample counts). Per-sample expression is only obtainable from SRA raw
      reads (GPL20301) requiring a re-alignment/quantification pipeline; series-matrix
      TXT carries metadata only. Not usable as a drop-in count matrix for t117.
  verification_method: ''
  exception:
    mode: scope-reduced
    decision_date: '2026-07-10'
    rationale: 'Evaluated by plan:0010 (t117) and DEMOTED (G4): accession is public
      but no downloadable per-sample expression matrix (DEG summary only, GSE224615_DEGs.xlsx);
      RNA-seq control arm n~9. Usable at most for DEG-level triangulation, not the
      per-sample rank matrix. Role reduced accordingly; not in the delivered t117
      matrix.'
accessions:
- GSE224615
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

# GSE224615 — Long COVID whole-blood transcriptome (8 mo)

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: evaluate-next`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Long COVID blood bulk RNA-seq from the San Francisco LIINC cohort, **8 months post-infection** (confirmed). Assay confirmed bulk RNA-seq on Illumina HiSeq 4000 (GPL20301). Control arm is **infected-recovered** (non-PASC), a design strength.

**Record-checked corrections (t117 WP1, 2026-07-08):**
- The RNA-seq series holds **36 GSMs = 27 PASC (Long COVID) vs 9 non-PASC controls** — NOT 27 vs 16. The "16 non-LC" figure is the whole-study (multi-omic: CyTOF/RNAseq/Olink) participant count; the RNA-seq control arm is only **n = 9**. Corrected here.
- Tissue is recorded only as "blood specimens" — **whole blood vs PBMC not stated in record** (the multi-omic study drew PBMCs for CyTOF). Whole-blood claim is unconfirmed.
- **No per-sample count matrix is publicly downloadable** — see access block. This is the load-bearing blocker: only a DEGs summary table (`GSE224615_DEGs.xlsx`) is posted; per-sample expression requires SRA re-alignment.
- Publication: Nat Immunol 2024, PMID 38212464 / DOI 10.1038/s41590-023-01724-6.

## Corpus role (t117)

- **Matrix:** **DEMOTED from strict-primary (WP1 2026-07-08).** Fails **G4**: no downloadable per-sample expression matrix (only a DEG-summary `.xlsx`; per-sample counts need SRA re-alignment), and the RNA-seq control arm is only n≈9 (the "16" was the whole-study multi-omic count). Retained only as possible **DEG-level triangulation**, not the primary rank matrix.
- **onset_certainty:** documented
- **Conditional/LOO flag:** out of primary matrix (G4 failure).

## Access / caveats

Accession resolves and is public, but **per-sample expression is NOT directly downloadable** (only `GSE224615_DEGs.xlsx`, a DEG summary; per-sample counts require SRA re-alignment). Combined with the small control arm (n = 9) and unconfirmed whole-blood tissue, this is a **DEMOTION candidate** for the t117 strict-primary matrix. `verified: false`.

## Access verification log

- 2026-07-10 (keith@2026-07-10): scope-reduced — Evaluated by plan:0010 (t117) and DEMOTED (G4): accession is public but no downloadable per-sample expression matrix (DEG summary only, GSE224615_DEGs.xlsx); RNA-seq control arm n~9. Usable at most for DEG-level triangulation, not the per-sample rank matrix. Role reduced accordingly; not in the delivered t117 matrix.
