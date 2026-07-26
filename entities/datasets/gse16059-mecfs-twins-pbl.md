---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse16059-mecfs-twins-pbl
kind: dataset
title: GSE16059 — ME/CFS discordant-twin blood-leukocyte microarray
status: candidate
created: "2026-07-07"
updated: "2026-07-07"
consumed_by:
- plan:0010-crosspais-pathway-response-rank-estimation
origin: external
dataset_class: deposit
source_class: observational
tier: track
license: unknown
access:
  level: public
  availability: available
  verified: true
  verification_method: landing-confirmed
  last_reviewed: '2026-07-08'
  verified_by: agent (t117 WP1)
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE16059
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: Series matrix (TXT, per-sample) public; raw CEL files as GSE16059_RAW.tar (393.9 MB, Affymetrix CEL) for re-normalization. 88 samples = 44 discordant MZ twin pairs. Staging to disk deferred to workflow execution.
accessions:
- GSE16059
source_refs:
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE16059
ontology_terms:
- me-cfs
- pbl
- microarray
provided_capabilities:
- data_product: data-product:gene-expression-microarray
  qualifiers:
    cohort_design: case-control
    trigger: mixed
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0001-shared-molecular-signature-across-triggers
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE16059 — ME/CFS discordant-twin blood-leukocyte microarray

**Candidate dataset for `task:t117`** (`status: candidate`, `tier: track`). Catalogued but not yet acquired; design specifics below are from a discovery sweep and are `[UNVERIFIED]` pending WP1.

## What it is

Peripheral-blood-leukocyte (PBL) microarray of monozygotic twins **discordant for chronic fatigue** — cases meeting international CFS/idiopathic-chronic-fatigue criteria vs their never-fatigued co-twins. **44 twin pairs → 88 samples (44 cases / 44 controls, control = healthy co-twin)** (confirmed against GEO record). Assay: Affymetrix microarray, **GPL570 (Human Genome U133 Plus 2.0)** — bulk, not single-cell (confirmed). Tissue: PBL (confirmed). Paired within-twin-pair design (handle pairing in WP2). **Not infection-anchored** — no per-subject infectious onset in record; sampling window not stated. Case-vs-control contrast usable (44 vs 44, paired). Linked publication PMID 19503787 (no biomarker identified). Onset certainty remains unknown-per-subject.

## Corpus role (t117)

- **Matrix:** ME/CFS-sensitivity
- **onset_certainty:** unknown-per-subject
- **Conditional/LOO flag:** enters ONLY the ME/CFS sensitivity matrix; discordant-twin (paired) design + microarray platform — handle pairing in WP2.

## Access / caveats

Verified public (record-checked 2026-07-08, t117 WP1). Per-sample series matrix (TXT) downloadable; raw `GSE16059_RAW.tar` (393.9 MB archive, Affymetrix CEL) available for re-normalization. Paired discordant-twin design (44 pairs) — WP2 must model within-pair pairing rather than treating the 88 samples as independent.
