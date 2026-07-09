---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:emexp2069-gulf-war-illness-pbmc
kind: dataset
title: E-MEXP-2069 — Gulf War Illness PBMC transcriptome (non-infectious specificity, WP4b queued)
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
  source_url: https://www.ebi.ac.uk/biostudies/arrayexpress/studies/E-MEXP-2069
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: "60 raw Affymetrix .CEL files + MAGE-TAB (.idf/.sdrf) public on BioStudies. Staging/parse DEFERRED (queued replication) — needs RMA/normalization + the hgu133plus2.db probe->gene chain (already pinned for GSE16059); use the baseline (pre-exercise) timepoint as the case-vs-control arm."
accessions:
- E-MEXP-2069
ontology_terms:
- gulf-war-illness
- non-infectious
- pbmc
- microarray
- specificity-control
provided_capabilities:
  - modality: transcriptomics
    assay: microarray
    trigger: non-infectious-gulf-war-illness
    cohort_design: case-control
related:
- task:t117
- question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
- question:0017-deflationary-alternatives-vs-shared-pathophysiology
- hypothesis:0001-shared-dysregulated-attractor
---

# E-MEXP-2069 — Gulf War Illness PBMC transcriptome (non-infectious specificity, WP4b queued)

**Candidate dataset for `task:t117`** (`status: candidate`, WP4b **queued replication**). Record-verified
against the ArrayExpress/BioStudies record on 2026-07-09 (t117 WP4b discovery sweep).

## What it is

Whistler et al. 2009 "Impaired immune function in Gulf War Illness" (BMC Med Genomics 2:12) — **9 GWI vs
11 Gulf-War-era control veterans**, PBMC, Affymetrix HG-U133 Plus 2.0, at three exercise timepoints (60
raw `.CEL` files); the baseline timepoint is a genuine case-vs-control arm. **Gulf War Illness is a
non-infectious (organophosphate/toxic-chemical) trigger** — a DIFFERENT non-infectious axis than
fibromyalgia, so it tests trigger-generality of any generic-sickness reading.

## Corpus role (t117 WP4b)

`matrix: specificity` — **queued replication** for the flagship [[gse221921-fibromyalgia-pbmc]]. This is
the **independent non-infectious TRIGGER** (chemical vs idiopathic) and an **independent microarray
platform**; the smallest N in the panel (9 vs 11). Same admissibility gates + uniform DE→enrichment when
built. **Not built this pass** (needs RMA + the hgu133plus2.db prebuilt chain + baseline-arm selection).
The whole-genome human GWI blood universe is effectively one US lab lineage (this + GSE286345/GSE168409,
all Klimas/Broderick), so cross-dataset GWI robustness is limited by design.
