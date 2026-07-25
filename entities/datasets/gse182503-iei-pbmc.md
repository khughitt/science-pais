---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse182503-iei-pbmc
kind: dataset
title: GSE182503 — Idiopathic environmental intolerance PBMC transcriptome (non-infectious specificity, WP4b queued)
status: candidate
created: "2026-07-09"
updated: "2026-07-09"
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
  last_reviewed: '2026-07-09'
  verified_by: agent (t117 WP4b sweep)
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE182503
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: GEO series matrix + raw TAR public (subseries of SuperSeries GSE182798); Agilent 8x60K one-colour microarray. Staging/parse DEFERRED (queued replication) — needs an Agilent probe->gene chain; EXCLUDE the co-deposited adult-onset-asthma arm, keep the 17 IEI vs 21 healthy contrast.
accessions:
- GSE182503
ontology_terms:
- idiopathic-environmental-intolerance
- non-infectious
- pbmc
- microarray
- specificity-control
provided_capabilities:
- data_product: data-product:gene-expression-microarray
  qualifiers:
    cohort_design: case-control
    trigger: non-infectious-environmental-intolerance
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0017-deflationary-alternatives-vs-shared-pathophysiology
- hypothesis:0001-shared-dysregulated-attractor
---

# GSE182503 — Idiopathic environmental intolerance PBMC transcriptome (non-infectious specificity, WP4b queued)

**Candidate dataset for `task:t117`** (`status: candidate`, WP4b **queued replication**). Record-verified
against the public GEO record on 2026-07-09 (t117 WP4b discovery sweep).

## What it is

Idiopathic environmental intolerance (IEI — the medically-unexplained chemical-intolerance umbrella;
MCS-adjacent), Finnish Institute of Occupational Health, 2021. **17 IEI vs 21 healthy controls**, PBMC,
Agilent-072363 SurePrint G3 Human GE v3 8x60K (subseries of GSE182798, which also profiles 50 damp-building
adult-onset asthma — a separable arm to exclude). **Trigger = environmental/chemical (non-infectious).**

## Corpus role (t117 WP4b)

`matrix: specificity` — **queued replication** for the flagship [[gse221921-fibromyalgia-pbmc]]. Its value is
a **THIRD independent non-infectious trigger class** (environmental, distinct from fibromyalgia's idiopathic
and GWI's chemical), broadening the trigger-generality test of any generic-sickness reading. Small N (17 vs
21). Same admissibility gates + uniform DE→enrichment when built. **Not built this pass** (needs an Agilent
probe→gene chain + exclusion of the asthma arm).
