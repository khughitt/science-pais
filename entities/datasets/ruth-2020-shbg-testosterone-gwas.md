---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:ruth-2020-shbg-testosterone-gwas
type: dataset
title: Ruth 2020 SHBG and testosterone GWAS summary statistics (sex-specific, European
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
  source_url: https://www.ebi.ac.uk/gwas/studies/GCST90012109
accessions: [GWAS_Catalog:GCST90012109, GWAS_Catalog:GCST90012107, GWAS_Catalog:GCST90012111, GWAS_Catalog:GCST90012113, GWAS_Catalog:GCST90012112, GWAS_Catalog:GCST90012114, GWAS_Catalog:GCST90012103, GWAS_Catalog:GCST90012102, GWAS_Catalog:GCST90012104, PMID:32042192, DOI:10.1038/s41591-020-0751-5]
ontology_terms: [sex-hormone-binding-globulin, testosterone, sex-hormone-biomarker, gwas, summary-statistics, sex-stratified, homo-sapiens, mr-exposure]
related:
- question:0007-mechanism-of-female-predominance-in-pais
- question:0013-reproductive-stage-failed-immune-recovery-after-infection
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
identity_context:
  taxon: 9606
  assembly:
    label: UNKNOWN
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# Ruth 2020 SHBG and testosterone GWAS summary statistics (sex-specific, European ancestry)

**Candidate dataset.** `status: candidate` — catalogued but not yet acquired.

## What it is

Genome-wide association summary statistics for **sex-hormone-binding globulin
(SHBG)** and **testosterone (bioavailable and total)** from Ruth et al., *Nature
Medicine* 2020 (PMID 32042192; DOI 10.1038/s41591-020-0751-5), "Using human
genetics to understand the disease impacts of testosterone in men and women"
(UK Biobank, European ancestry). The defining feature for this project is that the
release is **sex-specific**: the GWAS Catalog hosts separate male-only,
female-only, and sex-combined strata for each trait. Deposited accessions include:

- **SHBG:** GCST90012109 (men, n≈180,726), GCST90012107 (women, n≈189,473),
  GCST90012111 (sex-combined, n≈370,125); plus BMI-adjusted variants
  (GCST90012108 men, GCST90012106 women, GCST90012110 combined).
- **Total testosterone:** GCST90012113 (men, n≈194,453), GCST90012112 (women,
  n≈230,454), GCST90012114 (sex-combined, n≈425,097).
- **Bioavailable testosterone:** GCST90012103 (men), GCST90012102 (women),
  GCST90012104 (sex-combined). **Estradiol:** GCST90012105 (men).

## Why it fits

Serves the Wave-1 estimand's **`mr_exposure` (`trait: sex-hormone-biomarker`)**
role (`doc/plans/2026-07-03-wave1-gwas-mr-estimand.md` §a). Uniquely among the
three Wave-1 candidates, it **satisfies the discovery-filter sex-stratification
gate**: male-only and female-only sumstats are published, so genotype-effect
sex-modification of a hormone exposure on a PAIS outcome is estimable (subject to a
sex-stratified outcome GWAS also existing). This is the hinge candidate for
question:0007 (female predominance), question:0013 (reproductive-stage failed
recovery), and hypothesis:0005 (reproductive-stage immune-homeostatic margin).

## Access / caveats

- **Openly downloadable.** Every listed accession is flagged `fullPvalueSet=true`
  on the GWAS Catalog — harmonised genome-wide summary statistics on the GWAS
  Catalog FTP, no registration or gating. Third-party-reproducible.
- **GENUINELY sex-stratified (evidence-backed).** Male-only and female-only
  sumstats are separate deposited studies (see accession list). Task 8 **may**
  annotate `stratification: sex` for the sex-modification MR target — this is a
  true claim here, unlike the long-COVID outcome and SLE exposure candidates.
- Note (bridge assumption d for hormones): SHBG/testosterone genetic architecture
  is itself partly sex-specific; use the matching sex stratum on each side.
- **Assembly:** UK Biobank imputation → native GRCh37; GWAS Catalog also serves
  harmonised GRCh38. Recorded UNKNOWN pending Task-8 file confirmation.
- Ancestry: European only — flag cross-ancestry MR (bridge assumption 4, estimand §d).
- Sample-overlap risk (bridge assumption 3, estimand §d): UK Biobank contributes to both this exposure GWAS and
  the HGI long-COVID outcome — overlap must be quantified/corrected in Task 8.
