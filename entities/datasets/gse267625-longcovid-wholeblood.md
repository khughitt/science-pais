---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse267625-longcovid-wholeblood
kind: dataset
title: GSE267625 — Long COVID whole-blood longitudinal (P4O2)
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
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE267625
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: 'Per-sample matrix downloadable: GSE267625_P4O2_COVID_blood_transcriptome.csv.gz (4.8 Mb, CSV, 111 samples). Staging to disk deferred to workflow execution. CAVEAT — cohort is COVID-survivors-only (no external control arm); usable contrast must be defined within-cohort (long-COVID status / lung-function stratum) in WP2, not case-vs-healthy-control.'
accessions:
- GSE267625
source_refs:
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE267625
ontology_terms:
- long-covid
- sars-cov-2
- whole-blood
- rna-seq
provided_capabilities:
- data_product: data-product:gene-expression-bulk-rna
  qualifiers:
    cohort_design: case-control
    trigger: sars-cov-2
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0001-shared-molecular-signature-across-triggers
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE267625 — Long COVID whole-blood longitudinal (P4O2)

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: evaluate-next`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Whole-blood bulk RNA-seq from the **P4O2 post-hospitalised COVID cohort**: **95 COVID survivors sampled longitudinally at two timepoints (3–6 mo and 12–15 mo post-infection) → 111 GSMs total** (confirmed). Assay confirmed bulk RNA-seq on Illumina NovaSeq 6000 (GPL24676). Publication PMID 38830512 ("Whole blood transcriptome in long-COVID patients reveals association with lung function and immune response").

**FLAG — no classic case-vs-control design (t117 WP1, 2026-07-08).** The cohort is **COVID-survivors-only**; there is **no external healthy/uninfected control arm**. The record describes unsupervised clustering to associate transcriptome with lung function / long-COVID status. So a usable contrast exists only **within the cohort** (long-COVID vs recovered, or by lung-function stratum), and it is entangled with the longitudinal (within-subject, two-timepoint) structure. The claimed `cohort_design: case-control` is therefore **only conditionally true** — one contrast + timepoint policy must be defined in WP2.

## Corpus role (t117)

- **Matrix:** strict-primary
- **onset_certainty:** documented
- **Conditional/LOO flag:** longitudinal design — one contrast must be defined per subject/timepoint policy in WP2.

## Access / caveats

Verified: per-sample matrix `GSE267625_P4O2_COVID_blood_transcriptome.csv.gz` (4.8 Mb file, 111 samples) is publicly downloadable → `verified: true`. **Caveat carried forward:** COVID-survivors-only cohort + longitudinal within-subject structure means the case-vs-control contrast is not clean and must be constructed in WP2.
