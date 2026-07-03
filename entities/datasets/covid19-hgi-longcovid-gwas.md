---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:covid19-hgi-longcovid-gwas
type: dataset
title: COVID-19 Host Genetics Initiative — long-COVID GWAS summary statistics (2025
  release)
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
  source_url: https://www.ebi.ac.uk/gwas/studies/GCST90454543
accessions: [GWAS_Catalog:GCST90454543, GWAS_Catalog:GCST90454540, GWAS_Catalog:GCST90454541, GWAS_Catalog:GCST90454542, PMID:40399555, DOI:10.1038/s41588-025-02100-w]
ontology_terms: [long-covid, post-acute-covid-19, gwas, summary-statistics, homo-sapiens, mr-outcome]
related:
- question:0007-mechanism-of-female-predominance-in-pais
- hypothesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune
- question:0022-immune-state-displacement-mediator-vs-co-traveler
identity_context:
  taxon: 9606
  assembly:
    label: UNKNOWN
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# COVID-19 Host Genetics Initiative — long-COVID GWAS summary statistics (2025 release)

**Candidate dataset.** `status: candidate` — catalogued but not yet acquired.

## What it is

Genome-wide association summary statistics for **long COVID** from the COVID-19
Host Genetics Initiative (HGI) long-COVID working group (Lammi et al., *Nature
Genetics* 2025; PMID 40399555; DOI 10.1038/s41588-025-02100-w). The published
meta-analysis spans up to ~6,450 long-COVID cases and ~1.09M population controls
in the discovery freeze (24 cohorts, 16 countries), expanded in replication to
~15,950 cases / ~1.89M controls across 33 studies / 19 countries and six genetic
ancestries. Reports the FOXP4 (chr6) long-COVID risk locus, independent of the
severe-COVID association. Four multi-ancestry meta-analysis strata are deposited
on the GWAS Catalog, differing by case definition (strict = long COVID after
**test-verified** SARS-CoV-2 infection; broad = long COVID after **any**
SARS-CoV-2 infection) and control definition (strict = infected-but-no-long-COVID;
broad = population). Initiative landing page: https://www.covid19hg.org/results/.

## Why it fits

Serves the Wave-1 estimand's **`mr_outcome` (`trait: long-covid`)** role
(`doc/plans/2026-07-03-wave1-gwas-mr-estimand.md` §a): the PAIS-outcome GWAS
against which autoimmune-liability and sex-hormone-biomarker exposures are
two-sample-MR'd. Canonical open long-COVID GWAS. Case definition must be recorded
per bridge assumption 6 (estimand §d); the strict/broad split above is the material fact.

## Access / caveats

- **Openly downloadable.** All four deposited studies (GCST90454540–GCST90454543)
  are flagged `fullPvalueSet=true` on the GWAS Catalog, i.e. harmonised genome-wide
  summary statistics are on the GWAS Catalog FTP with no registration or gating.
  Third-party-reproducible (not an access-gated enclave class).
- **NOT sex-stratified.** The deposited long-COVID strata are mixed-sex
  meta-analyses; no male-only / female-only or genotype×sex interaction sumstats
  are published here. This candidate is therefore **out of scope for the
  sex-modification targets** (question:0007/0013/0019–0022) as an outcome, and
  must NOT be annotated `stratification: sex`. It serves the sex-agnostic MR
  estimand and the reverse-causation direction only.
- **Assembly:** the release ships both GRCh37 and GRCh38; recorded UNKNOWN here
  pending Task-8 verification of the exact file used (identity kept light).
- Sample-overlap check vs exposure GWAS (bridge assumption 3, estimand §d) is deferred to
  Task 8 — HGI shares biobanks (e.g. UK Biobank, FinnGen) that also contribute to
  autoimmune and hormone GWAS, so overlap is plausible and must be quantified.
