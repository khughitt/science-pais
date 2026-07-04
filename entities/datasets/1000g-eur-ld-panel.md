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
  source_url: https://doi.org/10.5281/zenodo.6614170
  verification_method: metadata-confirmed
  last_reviewed: '2026-07-04'
  verified_by: agent (plan:0007 run)
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: "1000 Genomes Phase 3 EUR plink reference for local LD clumping, sourced from Zenodo 6614170 (DOI 10.5281/zenodo.6614170, CC-BY-4.0) over https — a DOI-archival, checksummed source chosen over the plain-http MRC-IEU `1kg.v3` fileserve (plan:0007 pipeline-review Dim 3 hardening). Published per-file md5 is verified on download; SHA-256 recorded at retrieval. Third-party-reproducible (top class)."
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
- plan:0008-wave1-mr-autoimmune-hormone-longcovid-design
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

- **Openly downloadable over https from a DOI-archival source** — Zenodo 6614170
  (DOI 10.5281/zenodo.6614170, CC-BY-4.0), no credentials/gating →
  third-party-reproducible (top class; clears the `science.yaml`
  `third-party-reproducible` bar). Chosen over the plain-http, single-host
  MRC-IEU `1kg.v3` fileserve source for transport security + archival permanence
  (plan:0007 pipeline-review Dim 3). Published per-file md5 (bed/bim/fam) is
  verified on download.
- **Build = GRCh37 (native).** The Phase 3 call set is GRCh37/hg19. The
  `plan:0007` harmonised sumstats are GRCh38, so the panel's build must be
  reconciled with them — either a GRCh38-lifted panel or **rsID-based matching**
  via the harmonised `hm_rsid` column. `plan:0007` Task 2 makes this a **hard
  stop** if neither reconciliation holds. `identity_context.assembly` records the
  build label but is left `declared_unresolved` (no seqcol digest pinned yet).
- **EUR superpopulation only** — matched to the European exposure/outcome strata;
  do not use for non-European ancestry MR without an ancestry-matched panel.
- **Per-file md5 pinned; SHA-256 recorded on download.** md5s
  (bed `a163c74e…`, bim `81b1ee40…`, fam `669a4260…`) are pinned in the pipeline
  `config.yaml` and verified by `stage_ld.py`; SHA-256 recorded into the run
  manifest at retrieval.

## Access verification log

- 2026-07-04 (agent, plan:0007 review): registered as the tracked LD reference
  for the Wave-1 MR pilot (pipeline-review Dim-3 finding). Initially pointed at the
  1000G portal.
- 2026-07-04 (agent, plan:0007 run-prep): **source hardened** to Zenodo 6614170
  (https, DOI 10.5281/zenodo.6614170, CC-BY-4.0) after the plain-http MRC-IEU
  fileserve source proved unreachable/insecure; per-file md5 pinned in
  `config.yaml`. Build reconciliation = rsID (GRCh37 panel vs GRCh38 sumstats).
- 2026-07-04 (agent, plan:0007 run): **retrieved + md5-verified**. 1000G_EUR
  bed/bim/fam downloaded from Zenodo, md5s matched; SHA-256 bed
  `96da3683…f53a2463`, bim `0375fd02…1478653e`, fam `ccc5f199…c9c5edc8`
  (503 EUR samples, 1,836,406 variants). Used as the local plink LD-clumping panel.
