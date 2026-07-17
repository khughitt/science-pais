---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:gse196793-frailty-influenza-vaccine-pbmc
kind: dataset
title: GSE196793 — Physical frailty and response to inactivated influenza vaccine
  in older adults (PBMC RNA-seq)
status: candidate
provided_capabilities:
  - modality: transcriptomics
    assay: bulk-rna
    trigger: non-infectious-vaccine-challenge
    cohort_design: prospective-longitudinal
    stratification: frailty
created: '2026-07-17'
updated: '2026-07-17'
origin: external
dataset_class: deposit
source_class: observational
tier: evaluate-next
license: unknown
access:
  level: public
  availability: available
  verified: true
  source_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE196793
  verification_method: landing-confirmed
  last_reviewed: '2026-07-17'
  verified_by: agent (verify-access)
accessions: []
ontology_terms:
- frailty
- inflammaging
- immune-challenge
- influenza-vaccine
- rna-seq
related:
- question:0033-frailty-and-pre-frailty-as-an-independent-pais-boundary-condition-with
identity_context:
  taxon: 9606
  assembly:
    label: UNKNOWN
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# GSE196793 — Physical frailty and response to inactivated influenza vaccine in older adults (PBMC RNA-seq)

**Candidate dataset.** `status: candidate` — catalogued but not yet acquired.

## What it is

PBMC bulk RNA-seq from 28 older adults (84 samples) profiled before inactivated influenza
vaccination and at day 3 and day 7 after, with participants characterised by the **Fried 5-item
physical frailty phenotype**. Illumina NextSeq 500.

## Why it fits

The best-in-stratum public vehicle for `question:0033`. It is the only deposit found that
pairs a **measured frailty index** with a **timed immune challenge and longitudinal response** —
i.e. it can speak to frailty as a modifier of *response trajectory*, which is the structure the
frailty-as-boundary-condition claim requires.

## Access / caveats

**Public.** GEO landing page confirmed 2026-07-17; htseq counts (3.5 Mb) downloadable.

**Caveats.**
- **Raw FASTQ deliberately withheld** by the authors on privacy grounds — processed counts only,
  so reprocessing choices are fixed upstream.
- **Vaccine challenge is not infection**, and there is no post-acute outcome: this constrains
  frailty × *immune response*, not frailty × *PAIS*. Under D-003 a vaccine challenge is not an
  acute-infection trigger, so this cannot count as a PAIS case set — hence
  `trigger: non-infectious-vaccine-challenge`.
- n=28, single site.

## Access verification log

- 2026-07-17 (agent (verify-access)): GEO landing page confirmed public 2026-07-17: 84 samples / 28 subjects, pre-vaccination plus day 3 and day 7 post inactivated influenza vaccine, NextSeq 500. htseq counts (3.5Mb) downloadable; raw FASTQ deliberately withheld by authors for privacy -- processed layer only.
