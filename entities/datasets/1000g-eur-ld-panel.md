---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:1000g-eur-ld-panel
type: dataset
title: 1000 Genomes Phase 3 European (EUR) LD reference panel
status: candidate
created: '2026-07-04'
updated: '2026-07-04'
origin: external
dataset_class: reference
source_class: reference
tier: use-now
license: custom
update_cadence: static
access:
  level: public
  availability: available
  verified: true
  source_url: https://www.internationalgenome.org/data
  verification_method: landing-confirmed
  last_reviewed: '2026-07-04'
  verified_by: agent (plan:0007 review)
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: "Open, unrestricted 1000 Genomes Phase 3 genotypes (Fort Lauderdale / no data-use restriction), downloadable without credentials and usable locally as a plink LD reference. Third-party-reproducible. The de-facto ready-to-use plink bundle for two-sample-MR clumping is the MRC-IEU `1kg.v3` EUR subset; exact bundle + per-file SHA-256 are pinned at retrieval (plan:0007 Task 1/2)."
accessions:
- PMID:26432245
- DOI:10.1038/nature15393
- IGSR:1000G-phase3
ontology_terms:
- 1000-genomes
- ld-reference-panel
- european-ancestry
- homo-sapiens
consumed_by:
- plan:0007-wave1-mr-autoimmune-longcovid-pilot
- task:t089
related:
- plan:0007-wave1-mr-autoimmune-longcovid-pilot
- task:t089
identity_context:
  taxon: 9606
  assembly:
    label: GRCh37
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# 1000 Genomes Phase 3 European (EUR) LD reference panel

## Summary

Population LD reference panel (European / EUR superpopulation) from the 1000
Genomes Project Phase 3 release (1000 Genomes Project Consortium, *Nature* 2015;
PMID 26432245; DOI 10.1038/nature15393). Used **only** as the linkage-
disequilibrium reference for local plink LD-clumping of exposure instruments in
`plan:0007` — not as a measured-phenotype dataset. It satisfies no
question/hypothesis capability target; it is analysis infrastructure.

## Why it fits

`plan:0007` clumps the Bentham SLE exposure instrument **locally** (r² < 0.001,
10 Mb) rather than via the remote IEU clumping API, to keep the step
third-party-reproducible. That requires a pinned, checksummed local LD reference
— this entity. Because the LD panel determines which SNPs survive clumping (hence
the instrument set, hence the MR estimate), it is a load-bearing input and is
tracked as a first-class dataset per the project's reproducibility standard
(pipeline-review Dim 3).

## Access / caveats

- **Openly downloadable**, no credentials/gating → third-party-reproducible (top
  class; clears the `science.yaml` `third-party-reproducible` bar).
- **Build = GRCh37 (native).** The Phase 3 call set is GRCh37/hg19. The
  `plan:0007` harmonised sumstats are GRCh38, so the panel's build must be
  reconciled with them — either a GRCh38-lifted panel or **rsID-based matching**
  via the harmonised `hm_rsid` column. `plan:0007` Task 2 makes this a **hard
  stop** if neither reconciliation holds. `identity_context.assembly` records the
  build label but is left `declared_unresolved` (no seqcol digest pinned yet).
- **EUR superpopulation only** — matched to the European exposure/outcome strata;
  do not use for non-European ancestry MR without an ancestry-matched panel.
- **Exact bundle + SHA-256 pending retrieval.** Recorded at `plan:0007` Task 1/2
  (mirrors the sumstats: landing-confirmed now, checksums on download).

## Access verification log

- 2026-07-04 (agent, plan:0007 review): registered as the tracked LD reference
  for the Wave-1 MR pilot (pipeline-review Dim-3 finding). Open 1000G Phase 3 EUR
  genotypes; landing confirmed. File retrieval, exact bundle/version, per-file
  SHA-256, and build reconciliation pending per plan:0007 Task 1/2.
