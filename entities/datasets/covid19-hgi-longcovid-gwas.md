---
schema_profile: science-entity-base/1.0+dataset/1.0
id: dataset:covid19-hgi-longcovid-gwas
kind: dataset
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
  verified: true
  source_url: https://www.ebi.ac.uk/gwas/studies/GCST90454541
  verification_method: metadata-confirmed
  last_reviewed: '2026-07-04'
  verified_by: agent (plan:0007 run)
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: "Public GWAS summary statistics: downloadable harmonised flat files on the GWAS Catalog FTP (fullPvalueSet=true), re-poolable/re-analyzable locally at the summary grain — third-party-reproducible. Not individual-level genotypes (a scientific-strength limit, not an access one)."
accessions:
- GWAS_Catalog:GCST90454543
- GWAS_Catalog:GCST90454540
- GWAS_Catalog:GCST90454541
- GWAS_Catalog:GCST90454542
- PMID:40399555
- DOI:10.1038/s41588-025-02100-w
ontology_terms:
- long-covid
- post-acute-covid-19
- gwas
- summary-statistics
- homo-sapiens
- mr-outcome
provided_capabilities:
- modality: genetics
  assay: gwas-sumstats
  cohort_design: summary-stats
  trigger: sars-cov-2
  analysis_role: mr_outcome
  trait: long-covid
consumed_by:
- plan:0007-wave1-mr-autoimmune-longcovid-pilot
- plan:0008-wave1-mr-autoimmune-hormone-longcovid-design
- plan:0009-wave1-mr-hormone-pilot
- task:t089
related:
- question:0007-mechanism-of-female-predominance-in-pais
- hypothesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune
- question:0022-immune-state-displacement-mediator-vs-co-traveler
identity_context:
  taxon: 9606
  assembly:
    label: GRCh38
    registry: dataset:assembly-registry
    resolution_status: declared_unresolved
---

# COVID-19 Host Genetics Initiative — long-COVID GWAS summary statistics (2025 release)

**Candidate dataset.** `status: candidate` — **acquired + checksummed** (the
broad/population stratum GCST90454541) for `plan:0007` and re-staged for
`plan:0009` Task 1 (see the verification log); status stays `candidate` until a
result promotes the line.

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

## Bridge note (Task 8)

Linked as the **`mr_outcome` (`trait: long-covid`)** side of the Wave-1 two-sample-MR
estimand (`~/d/health/processes/post-acute-infection/doc/plans/2026-07-03-wave1-gwas-mr-estimand.md`
§a). Co-linked as the shared outcome GWAS to the causal targets `hypothesis:0005`
and `hypothesis:0007`, and independently satisfies `question:0022`
(immune-state-displacement mediator-vs-co-traveler) via
`{analysis_role: mr_outcome, trait: long-covid}` — the reverse-causation / mediation
direction the estimand §b(1) names. `hypothesis:0009`'s post-infectious latent→overt
*conversion* arrow is **not** identifiable by MR on this outcome (`plan:0008` KD6);
where reverse-direction MR uses long-COVID liability as the exposure it bears on
`question:0022` as shared-liability / directionality context, not h0009 conversion
evidence. This MR vehicle is the **sanctioned, reproducible
open substitute** described in the estimand note; it is **not** a re-opening of the
gated, non-reproducible N3C/OpenSAFELY EHR estimand shelved under **D-004** — that
population-scale, ascertainment-structured interaction stays with `hypothesis:0008`.

**Case-definition stratum (Task-7 minor; corrected 2026-07-04).** The primary
MR-outcome stratum is **GCST90454541** — the **broad** case definition (long COVID
after *any* SARS-CoV-2 infection) with **population controls** (FTP metadata:
"Broad control definition (population control)"). *Correction: an earlier note named
GCST90454543 as the broad/population stratum. That is wrong — GCST90454543 is broad
cases vs **strict** controls (had SARS-CoV-2 but did not develop long COVID), a
different, within-infected estimand. Verified 2026-07-04 against the GWAS Catalog
harmonised `*-meta.yaml` files for GCST90454541 and GCST90454543.* GCST90454543
(broad/strict) and the strict-**case** strata (GCST90454540/542) are retained as
**pre-committed case-definition sensitivities** per bridge assumption 6 (estimand §d);
the case × control definition choice is a live methodological one, deliberately not
yet frozen. **Ancestry:** the harmonised files are European-dominant *multi-ancestry*
metas (no EUR-only sibling file), which constrains ancestry-matched MR — see
`plan:0007` Decision-criteria ancestry hard-stop. Sex-agnostic outcome only — this
GWAS is mixed-sex and carries no `stratification: sex`.

## Access verification log

- 2026-07-03 (agent (verify-access)): COVID-19 HGI long-COVID summary statistics: fullPvalueSet=true harmonised genome-wide flat files on the GWAS Catalog FTP (GCST90454540-543), no registration/gating; landing page + downloadable files confirmed.
- 2026-07-04 (agent): consumed by plan:0007-wave1-mr-autoimmune-longcovid-pilot (Wave-1 MR pilot; outcome GWAS, broad/population-controls stratum GCST90454541, European-dominant multi-ancestry, GRCh38).
- 2026-07-04 (agent, plan:0007 run): **retrieved + verified**. Harmonised fullPvalueSet file `GCST90454541.h.tsv.gz` pulled from the GWAS Catalog FTP; SHA-256 `bd7e0a06…bd00a6891`, 9,442,353 rows, build GRCh38 (assembly label resolved). Used as the MR outcome (streamed instrument-SNP extraction, mechanics-only).
- 2026-07-04 (agent, plan:0009 Task 1 staging run): **re-staged for the Arm-B hormone pilot** via `code/workflows/wave1-mr-hormone/` (rule `acquire_sumstats`). Same harmonised file `GCST90454541.h.tsv.gz`, SHA-256 `bd7e0a06…bd00a6891`, 9,442,353 rows, GRCh38 — **identical to the plan:0007 retrieval** (byte-stable). The sibling `*-meta.yaml` was also staged: the broad/population stratum aggregates **5 case-control cohorts, total N = 1,100,445** (≈ the published European n≈1,090,649 of ≈1,100,645) — this is the **total N** to inject for MRlap's observed-scale correction (plan:0009 KD-scale). Per-cohort case/control splits are not in the meta; if a case/control breakdown is later needed it must come from the HGI DF4 release notes. Payload off-Dropbox at `/data/proj/post-acute-infection/raw/gwas/hormone-pilot/` (repo `data/raw` symlink).
- 2026-07-04 (agent, plan:0008 WP1): **EUR-outcome sourcing — negative result (definitive).** The Lammi 2025 [@Lammi2025] *Nat Genet* Data Availability (nature.com/articles/s41588-025-02100-w) confirms the Long COVID HGI DF4 release deposited **only the four multi-ancestry (European-dominant, ~85–90% EUR) strata** to GWAS Catalog (GCST90454540–543) and LocusZoom; the paper's "European-ancestry only" analysis was an **internal sensitivity, not a deposited file** — no EUR-only summary-statistics file is publicly downloadable. Fallback checked and also negative: Nat Cardiovasc Res 2025 (DOI 10.1038/s44161-025-00749-4) does **not** deposit a EUR-only file — it reuses the multi-ancestry HGI LocusZoom N1 (`my.locuszoom.org/gwas/793752/`) meta-analysed with FinnGen r10. **So the `plan:0008` ancestry hard-stop cannot be lifted from a downloadable EUR-only HGI file;** the fork is primary-demotion (KD1) vs a FinnGen authorisation (D-006 held). Stratum→LocusZoom map recorded: broad/population **GCST90454541 = "W2" = LZ 826733** (MR primary); broad/strict 543 = W1 (LZ 91854); strict/population 540 = N2 (LZ 192226); strict/strict 542 = N1 (LZ 793752). Case-def letters: **N**=narrow/strict case (test-verified), **W**=wide/broad case; trailing **1**=strict control (infected, no long COVID), **2**=population control.
