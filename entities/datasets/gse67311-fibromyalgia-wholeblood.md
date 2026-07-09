---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse67311-fibromyalgia-wholeblood
kind: dataset
title: GSE67311 — Fibromyalgia whole-blood transcriptome (non-infectious specificity, WP4b queued)
status: candidate
created: '2026-07-09'
updated: '2026-07-09'
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
  last_reviewed: "2026-07-09"
  verified_by: "agent (t117 WP4b sweep)"
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE67311
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: "GEO series matrix + processed data public; whole-blood Affymetrix HuGene 1.1 ST. Staging/parse DEFERRED (queued replication, not build_now) — needs the hugene11sttranscriptcluster.db probe->gene annotation add (microarray prebuilt chain), analogous to the GSE16059 GPL570 add."
accessions:
- GSE67311
ontology_terms:
- fibromyalgia
- non-infectious
- whole-blood
- microarray
- specificity-control
provided_capabilities:
  - modality: transcriptomics
    assay: microarray
    trigger: non-infectious-fibromyalgia
    cohort_design: case-control
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0017-deflationary-alternatives-vs-shared-pathophysiology
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE67311 — Fibromyalgia whole-blood transcriptome (non-infectious specificity, WP4b queued)

**Candidate dataset for `task:t117`** (`status: candidate`, WP4b **queued replication**). Record-verified
against the public GEO record on 2026-07-09 (t117 WP4b discovery sweep).

## What it is

The reference **fibromyalgia whole-blood** bulk gene-expression set: "Peripheral Blood Gene Expression in
Fibromyalgia Patients…" — **70 FM vs 70 healthy controls**, PAXgene whole blood, Affymetrix Human Gene 1.1
ST array (GPL11532). Non-infectious (idiopathic) trigger; ACR-criteria FM (exact 1990/2010 version to be
read from the sample metadata at parse time).

## Corpus role (t117 WP4b)

`matrix: specificity` — **queued replication** for the flagship
[[gse221921-fibromyalgia-pbmc]]. Its value is orthogonal axes: **independent whole-blood** (vs the
flagship's PBMC) **and independent microarray platform** (vs NovaSeq RNA-seq) — the cross-compartment +
cross-platform robustness check on the FM subspace-recovery reading. Held to the same admissibility gates
and run through the same uniform DE→enrichment when built. **Not built this pass** (needs the
`hugene11sttranscriptcluster.db` annotation add to the microarray prebuilt chain).
