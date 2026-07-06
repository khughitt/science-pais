---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:bentham-2015-sle-gwas
kind: dataset
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
  verified: true
  source_url: https://www.ebi.ac.uk/gwas/studies/GCST003156
  verification_method: metadata-confirmed
  last_reviewed: '2026-07-04'
  verified_by: agent (plan:0007 run)
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: "Public GWAS summary statistics: downloadable harmonised flat files on the GWAS Catalog FTP (GCST003156, fullPvalueSet=true), re-poolable/re-analyzable locally at the summary grain — third-party-reproducible. Not individual-level genotypes (a scientific-strength limit, not an access one)."
accessions:
- GWAS_Catalog:GCST003156
- PMID:26502338
- DOI:10.1038/ng.3434
ontology_terms:
- systemic-lupus-erythematosus
- autoimmune-disease
- gwas
- summary-statistics
- homo-sapiens
- mr-exposure
provided_capabilities:
- modality: genetics
  assay: gwas-sumstats
  cohort_design: summary-stats
  analysis_role: mr_exposure
  trait: autoimmune-disease
consumed_by:
- plan:0007-wave1-mr-autoimmune-longcovid-pilot
- plan:0008-wave1-mr-autoimmune-hormone-longcovid-design
- task:t089
related:
- question:0007-mechanism-of-female-predominance-in-pais
- hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate
- hypothesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune
identity_context:
  taxon: 9606
  assembly:
    label: GRCh38
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
(autoimmune small-fiber-neuropathy substrate) — the autoimmune-liability→PAIS
direction this exposure actually instruments. `hypothesis:0009` (post-infectious
immune set-point shift → *later* autoimmune conversion) runs the **opposite**,
acquired-state direction and is **not** tested by this exposure — shared-liability
context only (`plan:0008` KD6).

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

## Bridge note (Task 8)

Linked as the **`mr_exposure` (`trait: autoimmune-disease`)** genetic instrument for the
autoimmune→PAIS arm of the Wave-1 MR estimand
(`~/d/health/processes/post-acute-infection/doc/plans/2026-07-03-wave1-gwas-mr-estimand.md`
§a). Serves the causal target `hypothesis:0007` (autoimmune small-fiber-neuropathy
substrate — the autoimmune-liability→PAIS arm), which declares the matching required
set `{analysis_role: mr_exposure, trait: autoimmune-disease}`, satisfied by this
GWAS's `provided_capabilities` under exact-match. `hypothesis:0009` (post-infectious
immune-set-point shift → *later* autoimmune conversion) is the reverse,
acquired-state arrow and is **not identifiable** by this germline-liability
instrument in either MR direction (`plan:0008` KD6) — shared-liability context only,
not conversion evidence. This link is the **sanctioned open-MR
substitute** for one facet of the D-004-shelved autoimmune × sex × PASC line — a
narrower, reproducible germline-liability estimand, **not** a re-opening of the gated
EHR vehicle (which stays shelved with `hypothesis:0008`). The MR reading is gated on the
bridge assumptions in estimand §d — in particular the **a-priori HLA include/exclude
decision** (assumption 5), since the SLE signal is MHC-dense.

## Access verification log

- 2026-07-03 (agent (verify-access)): Bentham 2015 [@Bentham2015] SLE GWAS (GCST003156): fullPvalueSet=true harmonised genome-wide summary statistics on the GWAS Catalog FTP, no registration/gating; landing page + downloadable files confirmed.
- 2026-07-04 (agent): consumed by plan:0007-wave1-mr-autoimmune-longcovid-pilot (Wave-1 MR pilot; exposure GWAS).
- 2026-07-04 (agent, plan:0007 run): **retrieved + verified**. Harmonised fullPvalueSet file `26502338-GCST003156-EFO_0002690.h.tsv.gz` pulled from the GWAS Catalog FTP; SHA-256 `4480ff36…c02bd6583`, 7,914,824 rows, build GRCh38 (assembly label resolved). Used as the MR exposure (32 clumped instruments, mean F=76.4).
