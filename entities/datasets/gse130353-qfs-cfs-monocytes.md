---
id: dataset:gse130353-qfs-cfs-monocytes
type: dataset
title: "GSE130353 — QFS / CFS circulating-monocyte transcriptome"
status: candidate
created: "2026-06-21"
updated: "2026-06-26"
origin: external
dataset_class: deposit
source_class: observational
tier: evaluate-next
license: unknown
access:
  level: public
  availability: available
  verified: true
  verification_method: retrieved
  last_reviewed: "2026-06-26"
  verified_by: "agent (t065)"
  source_url: "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE130353"
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: "Open GEO series (GSE130353) — raw/processed matrices download without credentials and rerun locally (already retrieved to gitignored data/raw/). Third-party-reproducible."
accessions: [GSE130353]
ontology_terms: [post-q-fever-fatigue, q-fever, me-cfs, rna-seq, monocytes]
related:
  - task:t013
  - task:t035
  - question:0001-shared-molecular-signature-across-triggers
  - paper:Raijmakers2019
  - hypothesis:0001-shared-dysregulated-attractor
  - question:0017-deflationary-alternatives-vs-shared-pathophysiology
---

# GSE130353 — QFS / CFS circulating-monocyte transcriptome

**Candidate dataset for `task:t013`.** `status: candidate`, `tier: evaluate-next` — **public and
downloadable** (already provisioned for `task:t035`; see the legacy multi-set note
`2026-06-20-public-cross-trigger-geo-sets.md`). This entity splits it out as its own catalog record.

## What it is

40-sample monocyte RNA-seq: QFS=10, CFS=10, Q-fever-seropositive-recovered=10, healthy=10;
age- and sex-matched (`paper:Raijmakers2019`). MMSEQ `log_mu` expression, Ensembl rel-68.

## Why it fits t013 (with a caveat)

Puts a **bacterial trigger** (Q fever) beside ME/CFS with a built-in recovered-control — a molecular
acute-vs-post-acute persistence contrast for a data-poor trigger. **But** it is **sex-matched by
design**, so it cannot estimate female-excess *magnitude*; its t013 value is the persistence contrast,
not the sex contrast. (Primary relevance is to `task:t035` cross-trigger pathway overlap.)

| Acute severity | Post-acute persistence | Neuropsychiatric | Somatic fatigue | Sex-stratified |
|---|---|---|---|---|
| no | yes (QFS vs recovered) | no | molecular only | sex-matched (balanced) |

## Access / caveats

N=40; molecular only (no psychometrics); shared mitochondrial-peptide signal is **not fatigue-specific**
(asymptomatic seropositive controls share it). Sex labels: confirm per-sample in the series matrix.

## Access verification log

- 2026-06-26 (agent t065): GEO accession and local raw tar/SOFT payloads verified from the
  t035 acquisition manifest; license remains unknown. The project clean-base derivative is
  `dataset:gse130353-qfs-cfs-prepared-gene-matrix`.
