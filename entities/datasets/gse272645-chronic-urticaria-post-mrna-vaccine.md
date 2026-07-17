---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse272645-chronic-urticaria-post-mrna-vaccine
kind: dataset
title: GSE272645 — Chronic urticaria after COVID-19 mRNA vaccine, real-life cohort
  (blood RNA-seq)
status: candidate
provided_capabilities:
  - modality: transcriptomics
    assay: bulk-rna
    trigger: non-infectious-vaccine-challenge
    cohort_design: case-control
    stratification: mast-cell-activation
created: '2026-07-17'
updated: '2026-07-17'
origin: external
dataset_class: deposit
source_class: observational
tier: track
license: unknown
access:
  level: public
  availability: available
  verified: true
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE272645
  verification_method: landing-confirmed
  last_reviewed: '2026-07-17'
  verified_by: agent (verify-access)
accessions: []
ontology_terms:
- mast-cell-activation
- chronic-urticaria
- pacvs
- boundary-monitor
- rna-seq
related:
- question:0034-pre-existing-atopic-and-mast-cell-activation-disorders-as-a
identity_context:
  taxon: 9606
  assembly:
    label: UNKNOWN
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# GSE272645 — Chronic urticaria after COVID-19 mRNA vaccine, real-life cohort (blood RNA-seq)

**Candidate dataset.** `status: candidate` — catalogued but not yet acquired.

## What it is

Whole-blood RNA-seq (PAXgene) from a real-life cohort of **chronic urticaria arising after
COVID-19 mRNA vaccination** versus healthy controls: 32 samples, HiSeq 4000. In the source cohort
~53% remained active into 2023.

## Why it fits

The closest public deposit located to persistent mast-cell-mediated disease following a
SARS-CoV-2-related exposure, and therefore the only mast-cell read-across available to
`question:0034`.

## Access / caveats

**Public.** GEO landing page confirmed 2026-07-17; raw counts downloadable.

**Scope — D-003 boundary-monitor only.** The **trigger is mRNA vaccination, not acute infection**.
Under D-003 this is PACVS-adjacent: it is held as **boundary-monitor / read-across** and
- must **never** be counted as a PAIS case,
- must **never** be used as independent cross-trigger support for `hypothesis:0001`,
- and any convergence claim drawn from it must be labelled a **non-infectious read-across**.

Its capability is recorded as `stratification: mast-cell-activation`, which deliberately does *not*
satisfy `question:0034`'s `atopy` requirement — chronic urticaria is not atopy, and conflating them
would manufacture false coverage.

**Caveats.** n=32; urticaria is a clinical phenotype with heterogeneous mechanism.

## Access verification log

- 2026-07-17 (agent (verify-access)): GEO landing page confirmed public 2026-07-17: 32 samples, PAXgene blood RNA-seq, HiSeq 4000, raw counts downloadable. D-003 BOUNDARY-MONITOR ONLY: trigger is mRNA vaccination, not acute infection -- PACVS-adjacent. Never counts as a PAIS case set or as cross-trigger support for hypothesis:0001.
