---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse226260-longcovid-pbmc
kind: dataset
title: GSE226260 — Long COVID PBMC transcriptome (>6 mo)
status: candidate
created: '2026-07-07'
updated: '2026-07-07'
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
  last_reviewed: "2026-07-08"
  verified_by: "agent (t117 WP1)"
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE226260
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: "GEO series matrix + supplementary per-sample CSVs (raw counts and log-normalized counts) publicly downloadable via FTP/HTTP; staging to disk deferred to workflow execution"
accessions:
- GSE226260
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

# GSE226260 — Long COVID PBMC transcriptome (>6 mo)

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: evaluate-next`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Long COVID PBMC **bulk total RNA-seq** (record title: "Long COVID involves activation of proinflammatory and immune exhaustion pathways"). Confirmed against the GEO record (2026-07-08): tissue is **PBMC**; assay is **bulk RNA-seq** on **GPL24676 (Illumina NovaSeq 6000)** and **GPL34284 (Illumina NovaSeq X Plus)**. Design spans two cohorts with **≈46 long-COVID** (28 in cohort 1 + 18 in cohort 2) versus a rich control set of **convalescent/recovered controls (≈44: 24 + 20)** plus **uninfected controls (≈35)** and **acutely infected (≈54)** — i.e. controls include both infected-recovered and healthy-naive; the "178 control" figure reflects the total non-Long-COVID blood samples. Long-COVID group sampled **>180 d after initial infection** (confirmed). Case-vs-control contrast is well-powered (LC vs convalescent controls, both n in the mid-40s). Flagged in the discovery sweep as one of the best-designed long-COVID blood-bulk sets.

## Corpus role (t117)

- **Matrix:** strict-primary
- **onset_certainty:** documented
- **Conditional/LOO flag:** none

## Access / caveats

Public accession (`GSE226260`); per-sample expression matrix **confirmed downloadable** (GEO series matrix + supplementary CSVs of raw counts and log-normalized counts) — verified in t117 WP1 (2026-07-08).
