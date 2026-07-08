---
id: dataset:gse14577-pi-cfs-pbmc-microarray
kind: dataset
title: "GSE14577 — PI-CFS PBMC microarray"
status: candidate
created: "2026-06-26"
updated: "2026-06-26"
consumed_by:
- plan:0010-crosspais-pathway-response-rank-estimation
origin: external
dataset_class: deposit
source_class: observational
tier: evaluate-next
license: unknown
update_cadence: static
access:
  level: public
  availability: available
  verified: true
  verification_method: retrieved
  last_reviewed: "2026-06-26"
  verified_by: "agent (t065)"
  source_url: "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE14577"
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: "Open GEO series (GSE14577) — depositor intensity tables download without credentials and rerun locally. Third-party-reproducible."
accessions: [GSE14577]
ontology_terms: [post-infectious-cfs, me-cfs, pbmc, microarray, transcriptomics]
provided_capabilities:
  - modality: transcriptomics
    assay: microarray
    trigger: mixed
    cohort_design: case-control
source_refs:
  - cite:Gow2009
related:
  - task:t035
  - task:t065
  - question:0001-shared-molecular-signature-across-triggers
  - paper:Gow2009
  - hypothesis:0001-shared-dysregulated-attractor
---

# GSE14577 — PI-CFS PBMC microarray

## Summary

Public GEO source dataset for `paper:Gow2009`: Affymetrix U133A/U133B PBMC
microarrays from 8 male post-infectious CFS cases and 7 male healthy controls.
The project uses this source only through the derived clean-base entity
`dataset:gse14577-pi-cfs-prepared-gene-matrix`.

## Access verification log

- 2026-06-26 (agent t065): GEO accession and local acquired SOFT payload verified from the
  t035 acquisition manifest; license remains unknown.

## Connections to Project

This is the viral/post-infectious fatigue arm for the t035 cross-trigger
pathway-overlap reanalysis. Raw/source access is public, but the source itself
is small, male-only, microarray-based, and not directly merged with RNA-seq.

## Related

- Clean-base derivative: `dataset:gse14577-pi-cfs-prepared-gene-matrix`.
- Registry note: `doc/datasets/2026-06-20-public-cross-trigger-geo-sets.md`.
