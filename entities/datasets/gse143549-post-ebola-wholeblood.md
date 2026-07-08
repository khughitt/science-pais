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
  verified: true
  verification_method: landing-confirmed
  last_reviewed: "2026-07-08"
  verified_by: "agent (t117 WP1)"
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE143549
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: "Per-sample normalized matrix GSE143549_Normalized_counts_CPM+0.0001_59_samples.txt.gz (all 59 samples) plus GSE143549_DEG_Total_GSA_EBOV_S_vs_HD_1024_genes.txt.gz and series matrix; staging to disk deferred to workflow execution."
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

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: evaluate-next`). Record-verified against the public GEO record on 2026-07-08 (t117 WP1).

## What it is

Post-Ebola survivors, **whole-blood bulk RNA-seq** (Illumina HiSeq 2500, GPL16791) — confirmed. Design confirmed: **26 Guinean EVD survivors vs 33 healthy donors** from the same region (59 samples total). Sampling window confirmed: a **median of 23 months after discharge** from the Ebola treatment centre. Source: Vetter/Wiedemann et al., "Long-lasting severe immune dysfunction in Ebola virus disease survivors," *Nat Commun* 2020, PMID 32709840. Case-vs-control (survivor vs healthy donor) contrast is usable (26 vs 33).

Per-sample matrix is downloadable: `GSE143549_Normalized_counts_CPM+0.0001_59_samples.txt.gz` (per-sample CPM for all 59 samples), plus a DEG table (`GSE143549_DEG_Total_GSA_EBOV_S_vs_HD_1024_genes.txt.gz`) and the series matrix.

## Corpus role (t117)

- **Matrix:** strict-primary
- **onset_certainty:** documented
- **Conditional/LOO flag:** rare trigger, single-platform contrast — non-arbitrating for platform-independent biology (rank conclusion must survive dropping it).

## Access / caveats

Public accession (`GSE143549`), per-sample normalized matrix confirmed downloadable (`GSE143549_Normalized_counts_CPM+0.0001_59_samples.txt.gz`, all 59 samples) plus series matrix (t117 WP1, record-checked 2026-07-08). Caveat carried from Corpus role: rare trigger, single-platform contrast — non-arbitrating for platform-independent biology.
