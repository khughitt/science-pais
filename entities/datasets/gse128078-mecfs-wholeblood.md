---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse128078-mecfs-wholeblood
kind: dataset
title: GSE128078 — ME/CFS whole-blood transcriptome (PEM)
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
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE128078
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: "Per-sample processed expression matrix public as supplementary GSE128078_FES_isoforms_FPKM.txt.gz (isoform-level FPKM, 11.0 Mb); series matrix (TXT) carries sample metadata; raw reads via SRA SRP187984 for gene-level recount. Staging to disk deferred to workflow execution."
accessions:
- GSE128078
ontology_terms:
- me-cfs
- whole-blood
- rna-seq
provided_capabilities:
  - modality: transcriptomics
    assay: bulk-rna
    trigger: mixed
    cohort_design: case-control
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0001-shared-molecular-signature-across-triggers
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE128078 — ME/CFS whole-blood transcriptome (PEM)

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: evaluate-next`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Whole-blood bulk RNA-seq (Illumina HiSeq 2500, GPL16791) of ME/CFS patients vs sedentary controls, sampled around cardiopulmonary exercise testing to probe post-exertional-malaise (PEM) transcriptome/virome. **14 ME/CFS cases vs 11 controls** (confirmed against GEO record; 99 total samples reflect the longitudinal 2-exercise-day + 7-day follow-up sampling, i.e. multiple time points per subject). Tissue: whole blood (confirmed). Exercise-anchored, **not infection-anchored** — no per-subject documented infectious onset. Case-vs-control contrast is usable (n=14 vs 11 subjects). Linked publication PMID 30897114 (reported only 6 candidate DEGs, none immune-related). Onset certainty remains unknown-per-subject.

## Corpus role (t117)

- **Matrix:** ME/CFS-sensitivity
- **onset_certainty:** unknown-per-subject
- **Conditional/LOO flag:** enters ONLY the ME/CFS sensitivity matrix, never the strict-primary verdict.

## Access / caveats

Verified public (record-checked 2026-07-08, t117 WP1). Per-sample processed matrix downloadable as supplementary `GSE128078_FES_isoforms_FPKM.txt.gz` (isoform-level FPKM); gene-level counts require reprocessing raw reads from SRA `SRP187984`. Note the longitudinal design (multiple samples per subject across exercise days) — WP2 must collapse/select time points for a clean 14-vs-11 case-control contrast.
