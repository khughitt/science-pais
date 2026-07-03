---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:bentham-2015-sle-gwas
type: dataset
title: Bentham 2015 systemic lupus erythematosus GWAS summary statistics (European
  ancestry)
status: candidate
created: '2026-07-03'
updated: '2026-07-03'
origin: external
dataset_class: reference
source_class: observational
tier: evaluate-next
license: unknown
access:
  level: public
  availability: available
  verified: false
  source_url: https://www.ebi.ac.uk/gwas/studies/GCST003156
accessions: [GWAS_Catalog:GCST003156, PMID:26502338, DOI:10.1038/ng.3434]
ontology_terms: [systemic-lupus-erythematosus, autoimmune-disease, gwas, summary-statistics, homo-sapiens, mr-exposure]
related:
- question:0007-mechanism-of-female-predominance-in-pais
- hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
- hypothesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune
identity_context:
  taxon: 9606
  assembly:
    label: UNKNOWN
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# Bentham 2015 systemic lupus erythematosus GWAS summary statistics (European ancestry)

**Candidate dataset.** `status: candidate` — catalogued but not yet acquired.

## What it is

Genome-wide association summary statistics for **systemic lupus erythematosus
(SLE)** from Bentham et al., *Nature Genetics* 2015 (PMID 26502338; DOI
10.1038/ng.3434), "Genetic association analyses implicate aberrant regulation of
innate and adaptive immunity genes in the pathogenesis of systemic lupus
erythematosus." GWAS Catalog study **GCST003156**: 5,201 European-ancestry cases
and 9,066 European-ancestry controls (the full published discovery/replication set
is ~7,219 cases / ~15,991 controls; GCST003156 is the summary-stat-bearing
European case-control scan). Identified 43 susceptibility loci including ten novel
associations. A well-established, widely re-used autoimmune GWAS.

## Why it fits

Serves the Wave-1 estimand's **`mr_exposure` (`trait: autoimmune-disease`)** role
(`doc/plans/2026-07-03-wave1-gwas-mr-estimand.md` §a): genetic liability to an
autoimmune disease, instrumented by genome-wide-significant SNPs, tested for a
causal effect on the long-COVID / PAIS outcome. SLE is female-predominant and a
canonical systemic-autoimmune exemplar, aligning with hypothesis:0007
(autoimmune small-fiber-neuropathy substrate) and hypothesis:0009 (post-infectious
immune set-point shift → autoimmune conversion).

## Access / caveats

- **Openly downloadable.** GCST003156 is flagged `fullPvalueSet=true` on the GWAS
  Catalog — harmonised genome-wide summary statistics available on the GWAS
  Catalog FTP without registration or gating. Third-party-reproducible.
- **NOT sex-stratified.** The deposited SLE sumstats are a mixed-sex case-control
  meta-analysis; no male-only / female-only sumstats are published. Usable for the
  sex-agnostic MR estimand but **out of scope as a sex-modification exposure** and
  must NOT be annotated `stratification: sex`.
- **HLA-dense signal (bridge assumption 5, estimand §d).** SLE associations include strong MHC
  (chr6p21) signal; the a-priori HLA include/exclude decision applies with force.
- **Assembly:** native build GRCh37; GWAS Catalog also serves a harmonised
  GRCh38 file. Recorded UNKNOWN pending Task-8 confirmation of the file used.
- Ancestry: European only — flag cross-ancestry MR against any non-European
  outcome stratum (bridge assumption 4, estimand §d).
