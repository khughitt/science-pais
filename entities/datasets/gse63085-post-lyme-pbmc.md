---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse63085-post-lyme-pbmc
kind: dataset
title: GSE63085 — Post-treatment Lyme PBMC transcriptome
status: candidate
created: "2026-07-07"
updated: "2026-07-07"
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
  verified: true
  verification_method: landing-confirmed
  last_reviewed: '2026-07-08'
  verified_by: agent (t117 WP1)
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE63085
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: GEO Series Matrix (TXT) + GSE63085_RAW.tar (75.6 MB, per-sample TXT files); staging to disk deferred to workflow execution.
accessions:
- GSE63085
source_refs:
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE63085
ontology_terms:
- post-lyme
- ptlds
- lyme-disease
- pbmc
- rna-seq
provided_capabilities:
- data_product: data-product:gene-expression-bulk-rna
  qualifiers:
    cohort_design: case-control
    trigger: lyme-disease
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0001-shared-molecular-signature-across-triggers
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE63085 — Post-treatment Lyme PBMC transcriptome

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: evaluate-next`). Design specifics below are WP1-verified against the GEO record (2026-07-08).

## What it is

Acute-through-post-treatment Lyme disease PBMC **bulk RNA-seq** (GPL11154, Illumina HiSeq 2000; 97 samples total). 29 Lyme patients sampled at 3 timepoints — **V1** (acute, pre-treatment), **V2** ("3 weeks later, immediately following completion of a standard course of antibiotics"), and **V5** ("6 months following treatment completion") — plus 13 healthy controls sampled once (a few patient-timepoints missing, hence 97 not 100). Cases are an **unselected Lyme timecourse, NOT selected for persistent (PTLDS) symptoms**. A post-acute/convalescent contrast **is** available at V5 (6 months post-treatment), well above the ≥4-week post-acute floor; V2 (~3 wk, immediately post-antibiotics) sits at the floor. Per-sample matrix downloadable (GEO Series Matrix TXT + `GSE63085_RAW.tar` of per-sample TXT files). Note: the parent study is framed as **acute-Lyme** diagnostic-signature discovery — title "Identification of a Molecular Signature for Acute Lyme Disease by Human Transcriptome Profiling" — so the "post-treatment Lyme" entity label captures only the V2/V5 arms of an acute→post-treatment timecourse.

## Corpus role (t117)

- **Matrix:** strict-primary
- **onset_certainty:** documented (Lyme trigger)
- **Conditional/LOO flag:** not PTLDS-symptom-selected — represents post-Lyme, not necessarily symptomatic PTLDS; LOO-drop candidate.

## Access / caveats

Public accession (`GSE63085`); per-sample expression matrix confirmed downloadable (WP1, 2026-07-08): GEO Series Matrix (TXT) + `GSE63085_RAW.tar` (75.6 MB archive of per-sample TXT files). Bulk RNA-seq assay confirmed (GPL11154).
