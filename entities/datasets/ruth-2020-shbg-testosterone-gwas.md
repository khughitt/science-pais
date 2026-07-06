---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:ruth-2020-shbg-testosterone-gwas
kind: dataset
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
  verified: true
  source_url: https://www.ebi.ac.uk/gwas/studies/GCST90012109
  verification_method: metadata-confirmed
  last_reviewed: '2026-07-04'
  verified_by: agent (plan:0009 Task 1)
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: "Public GWAS summary statistics: downloadable harmonised flat files on the GWAS Catalog FTP for male-only, female-only, and sex-combined strata (fullPvalueSet=true), re-poolable/re-analyzable locally at the summary grain — third-party-reproducible. Not individual-level genotypes (a scientific-strength limit, not an access one)."
accessions:
- GWAS_Catalog:GCST90012109
- GWAS_Catalog:GCST90012107
- GWAS_Catalog:GCST90012111
- GWAS_Catalog:GCST90012113
- GWAS_Catalog:GCST90012112
- GWAS_Catalog:GCST90012114
- GWAS_Catalog:GCST90012103
- GWAS_Catalog:GCST90012102
- GWAS_Catalog:GCST90012104
- PMID:32042192
- DOI:10.1038/s41591-020-0751-5
ontology_terms:
- sex-hormone-binding-globulin
- testosterone
- sex-hormone-biomarker
- gwas
- summary-statistics
- sex-stratified
- homo-sapiens
- mr-exposure
provided_capabilities:
- modality: genetics
  assay: gwas-sumstats
  cohort_design: summary-stats
  analysis_role: mr_exposure
  trait: sex-hormone-biomarker
  outcome: sex-hormone-level
  stratification: sex
consumed_by:
- plan:0008-wave1-mr-autoimmune-hormone-longcovid-design
- plan:0009-wave1-mr-hormone-pilot
- task:t089
related:
- question:0007-mechanism-of-female-predominance-in-pais
- question:0013-reproductive-stage-failed-immune-recovery-after-infection
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
identity_context:
  taxon: 9606
  assembly:
    label: GRCh38
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# Ruth 2020 SHBG and testosterone GWAS summary statistics (sex-specific, European ancestry)

**Candidate dataset.** `status: candidate` — the six MR-exposure strata (SHBG +
total testosterone × combined/male/female) are **acquired + checksummed** for
`plan:0009` (see the verification log); status stays `candidate` until a result
promotes the line.

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
gate**: male-only and female-only sumstats are published, enabling **sex-specific
exposure instruments**. **Note (`plan:0008` KD3):** with the current long-COVID
outcome mixed-sex, this supports only a **bounded exposure-architecture** probe
(concordance/discordance of sex-specific hormone predictors against a common
outcome) — a genotype-effect sex-modification *test* would require a sex-stratified
outcome GWAS, which does not exist for long-COVID. This is the hinge candidate for
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
  harmonised GRCh38. **Resolved GRCh38** (plan:0009 Task 1 used the harmonised
  `fullPvalueSet` files); reconciled with the GRCh37 LD/LDSC references by rsID.
- Ancestry: European only — flag cross-ancestry MR (bridge assumption 4, estimand §d).
- Sample-overlap risk (bridge assumption 3, estimand §d): UK Biobank contributes to both this exposure GWAS and
  the HGI long-COVID outcome — overlap must be quantified/corrected in Task 8.

## Bridge note (Task 8)

Linked as the **`mr_exposure` (`trait: sex-hormone-biomarker`)** genetic instrument for
the sex-hormone arm of the Wave-1 MR estimand
(`~/d/health/processes/post-acute-infection/doc/plans/2026-07-03-wave1-gwas-mr-estimand.md`
§a). Serves the causal target `hypothesis:0005` (reproductive-stage immune-homeostatic
margin), which declares the matching required set
`{analysis_role: mr_exposure, trait: sex-hormone-biomarker}`. Uniquely among the three
Wave-1 GWAS this candidate carries a **truthful `stratification: sex`** (male-only /
female-only deposited sumstats), so it supplies genuine **sex-specific exposure
instruments** (estimand §b.2). But a sex-effect-modification *test* is **not
closeable** against the current mixed-sex HGI long-COVID outcome (no sex-stratified
outcome GWAS exists); per `plan:0008` KD3 this candidate therefore supports only a
**bounded exposure-architecture** probe, not a sex-modification claim. Reproducible germline-liability estimand, adjacent to but not a re-opening of the
D-004-shelved EHR line. MR reading gated on estimand §d bridge assumptions (note the
sample-overlap gate: UK Biobank contributes to both this exposure GWAS and the HGI
outcome — quantify/correct).

## Access verification log

- 2026-07-03 (agent (verify-access)): Ruth 2020 [@Ruth2020] SHBG/testosterone GWAS: fullPvalueSet=true harmonised genome-wide summary statistics on the GWAS Catalog FTP for male-only, female-only, and sex-combined strata, no registration/gating; landing page + downloadable files confirmed.
- 2026-07-04 (agent, plan:0009 Task 1 staging run): **retrieved + SHA-256-recorded** via the reproducible Snakemake workflow `code/workflows/wave1-mr-hormone/` (rule `acquire_sumstats`). All six harmonised `fullPvalueSet` strata pulled from the GWAS Catalog FTP, **build GRCh38** (assembly label resolved from UNKNOWN), file name form `32042192-<GCST>-<EFO>.h.tsv.gz` (EFO_0004696 = SHBG, EFO_0004908 = total testosterone). SHA-256 / rows: SHBG combined GCST90012111 `27c911dd…d703274d` (16,322,241); SHBG male GCST90012109 `4b71db9a…9ee5b8b7` (16,321,912); SHBG female GCST90012107 `39cb79e5…d5bf9709` (16,325,146); testosterone combined GCST90012114 `5b74d4ed…e9664b5fc` (16,317,870); testosterone male GCST90012113 `39d1648c…75b115072` (16,316,685); testosterone female GCST90012112 `193d0dc2…99b8e4e4a` (16,320,220). Payloads staged off-Dropbox at `/data/proj/post-acute-infection/raw/gwas/hormone-pilot/` (repo `data/raw` symlink); recorded in the run's `acquire_manifest.json`.
- 2026-07-04 (agent, plan:0009 Task 2 instrument-construction run): **six MR exposure instruments built** via `code/workflows/wave1-mr-hormone/` (rule `build_instrument`, `r-mr` conda env; TwoSampleMR 0.7.9 / ieugwasr 1.1.0 / R 4.5.3, version-assert passed). Per stratum: p < 5×10⁻⁸ → local LD-clump vs the staged 1000G-EUR panel (by rsID, r² < 0.001 / 10 Mb, **no MHC exclusion**) → F = (β/se)². **All six eligible** (mean F > 10 **and** ≥ 3 independent instruments), none quarantined: SHBG combined 353 instruments (mean F 155.2), SHBG male 213 (150.5), SHBG female 201 (120.5), testosterone combined 160 (89.7), testosterone male 159 (94.7), testosterone female 192 (91.8); every stratum's minimum single-instrument F > 22. **Panel-coverage caveat (recorded in each sidecar's `attrition.n_absent_in_panel`):** ~81–87% of each stratum's genome-wide-significant SNPs are absent from the 1000G-EUR reference panel (the Ruth sumstats carry ~16.3M variants vs the panel's ~1.84M), so LD-clumping — and thus instrument selection — operates only on the panel-covered subset; the surviving instrument sets are nonetheless well-powered. Peak RSS ≈ 8.6 GB/stratum, ~15 min total (`-c1`). Outputs (instrument TSVs + per-stratum JSON sidecars + `results/wave1-mr-hormone-pilot/instruments_manifest.json`) are gitignored, regenerable from the pinned config; the instrument-eligibility table is the pre-result checkpoint before any outcome-facing MR estimate (Task 3).
