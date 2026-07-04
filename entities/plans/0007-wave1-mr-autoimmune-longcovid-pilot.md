---
id: "plan:0007-wave1-mr-autoimmune-longcovid-pilot"
type: "plan"
plan_kind: "pipeline"
title: "Wave-1 MR pilot: autoimmune liability → long-COVID (mechanics derisk)"
status: "active"
created: "2026-07-04"
updated: "2026-07-04"
related:
  - "hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate"
  - "hypothesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune"
  - "question:0022-immune-state-displacement-mediator-vs-co-traveler"
  - "task:t089"
  - "dataset:bentham-2015-sle-gwas"
  - "dataset:covid19-hgi-longcovid-gwas"
---

# Wave-1 MR pilot: autoimmune liability → long-COVID (mechanics derisk)

## Goal

Run one two-sample Mendelian randomization (MR) pair — genetic liability to
systemic lupus erythematosus (SLE) as the autoimmune exposure, long-COVID
liability as the outcome — **end to end**, from GWAS Catalog FTP files to an
IVW/Egger/weighted-median estimate with diagnostics, to derisk the pipeline
mechanics before a full `design` plan commits the three-candidate sensitivity
matrix. This is a **plumbing test, not a scientific verdict.**

## Background

D-005 authorized the fully-open, third-party-reproducible Wave-1 GWAS/MR pilot
as a narrow, reproducible substitute for the D-004-shelved gated-EHR
autoimmune × sex × PASC line — a **germline-liability IV effect**, explicitly not
a reconstruction of the shelved individual-level estimand. The estimand, bridge
assumptions, and required sensitivity analyses are already settled in
`~/d/health/processes/post-acute-infection/doc/plans/2026-07-03-wave1-gwas-mr-estimand.md`
and the per-candidate staging/acceptance contract in
`doc/plans/2026-07-03-gwas-mr-ingestion-handoff.md`; this plan does not
re-decide them. Three candidate datasets are catalogued, access-verified
(`landing-confirmed`), and classed third-party-reproducible. What is untested is
the **execution path**: FTP retrieval of the harmonised flat files, allele
harmonization, MHC-aware instrument construction, and the estimators. This probe
runs the single cleanest pair to prove that path works and to surface the
harmonization gotchas cheaply.

Pair choice — `bentham-2015-sle-gwas` (GCST003156) → `covid19-hgi-longcovid-gwas`
(GCST90454543, broad stratum): Bentham is a largely **non-UK-Biobank**
European case-control scan, so this pair sidesteps the Ruth↔HGI UK-Biobank
sample-overlap problem (handoff §3.3) and all sex-stratification machinery for
the pilot, isolating pure MR mechanics. It bears directly on
`hypothesis:0007`/`hypothesis:0009` (post-infectious autoimmunity) and, via the
outcome, `question:0022`.

## Approach

Two-sample MR with the standard `TwoSampleMR` R toolchain (cross-checked against
the `MendelianRandomization` package where estimators overlap). Instrument =
genome-wide-significant SLE variants, **extended-MHC-excluded** (chr6:25–34 Mb,
pre-committed per estimand §d.5 / handoff §3.4 — HLA-inclusive is a design-phase
sensitivity, not run here), LD-clumped against a **local** 1000 Genomes European
reference panel (not the remote IEU clumping API — local clumping keeps the step
third-party-reproducible). Both sides restricted to **European-ancestry** strata
(handoff §3.5). Estimators: **IVW primary**, MR-Egger and weighted-median as the
minimum robustness bar (handoff §3.2). Report per-instrument and mean
F-statistic (handoff §3.1). All payloads gitignored under `data/`; all outputs
and a run manifest under `results/`.

## Inputs

- `dataset:bentham-2015-sle-gwas` — GCST003156, harmonised `fullPvalueSet=true`
  flat file (European case-control; native GRCh37, harmonised GRCh38 also served).
- `dataset:covid19-hgi-longcovid-gwas` — GCST90454543 (broad long-COVID stratum),
  harmonised `fullPvalueSet=true`; **European-ancestry stratum** of the
  multi-ancestry meta-analysis (flag and treat as sensitivity if only the
  all-ancestry file is retrievable).
- Estimand + bridge assumptions: `doc/plans/2026-07-03-wave1-gwas-mr-estimand.md`.
- Staging + acceptance contract: `doc/plans/2026-07-03-gwas-mr-ingestion-handoff.md`.
- `TwoSampleMR` (R) + a local 1000G-EUR plink reference for clumping.

## Tasks

1. **Retrieve + register the two sumstats.** Pull the GCST003156 and
   GCST90454543 harmonised `fullPvalueSet` flat files from the GWAS Catalog FTP
   (`ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/`, harmonised subfolder)
   into `data/raw/gwas/` (gitignored). Record SHA-256, the actual assembly build
   pulled, and row counts in a small manifest; select the HGI European-ancestry
   stratum (or flag if unavailable). Then upgrade each dataset entity's access to
   a retrieval-grade `verification_method` and set `identity_context.assembly.label`
   — it must not remain UNKNOWN past ingestion (handoff §1).
2. **Build the SLE exposure instrument.** Filter Bentham to p < 5×10⁻⁸, **drop
   the extended MHC window chr6:25–34 Mb**, LD-clump locally (r² < 0.001, 10 Mb,
   1000G-EUR reference), and compute per-instrument + mean F-statistic. Halt loud
   if mean F < 10 (weak-instrument floor) or if any surviving instrument lies in
   the excluded MHC window.
3. **Harmonize exposure ↔ outcome.** Align effect alleles across the two GWAS,
   resolve or drop palindromic/ambiguous SNPs via effect-allele frequency, and
   extract outcome effects for the instrument SNPs (proxy lookup for missing SNPs
   is optional and, if skipped, logged as a limitation). Log every dropped SNP
   with its reason; no silent drops.
4. **Estimate + diagnostics.** Run IVW (primary), MR-Egger, and weighted-median;
   report point estimates, SEs, the MR-Egger intercept (directional-pleiotropy
   test), and explicit IVW/Egger/weighted-median concordance-or-discordance. Write
   the instrument table, estimates, diagnostics, and a run manifest (input SHA-256s,
   tool versions, parameters) under `results/wave1-mr-pilot/`.
5. **Probe write-up + go/no-go.** One short results note recording the mechanics
   outcome against the Decision criteria below. State plainly that the pilot
   estimate's sign/significance is **not** interpreted as evidence for or against
   `hypothesis:0005`/`0007`/`0009` or `question:0022` — that requires the full
   acceptance gate (handoff §4), which this probe does not attempt. Recommend
   whether to proceed to the full `design` plan (prospective `plan:0008`).

## Decision criteria

The probe concerns **mechanics**, not the scientific result. **GO** to the full
`design` plan if all hold:

- Both harmonised files retrieve, parse, and yield sane row counts and a recorded
  build.
- The clumped, MHC-excluded SLE instrument retains a workable set of independent
  variants (target ≳ 10) with **mean F-statistic > 10**.
- Harmonization completes with palindromic/ambiguous SNPs resolved or logged, and
  outcome effects extracted for the instruments.
- IVW, MR-Egger, and weighted-median all return finite, sane-magnitude estimates,
  and the Egger intercept is computable — i.e. the estimator layer works and
  concordance is reportable.

**NO-GO / fix-first** if the instrument collapses below the weak-instrument floor,
harmonization cannot resolve allele coding, or an estimator fails — surface the
blocker and repair the mechanics before the design plan.

## Validation

- Retrieved-file SHA-256s and assembly build recorded in the run manifest; row
  counts within expected order of magnitude for genome-wide harmonised sumstats.
- Every instrument SNP has p < 5×10⁻⁸ in the exposure and **none** falls in
  chr6:25–34 Mb.
- Palindromic/ambiguous-SNP handling is logged; harmonization drop-log is present
  and non-silent.
- Per-instrument and mean F-statistics are reported.
- Outputs land under `results/wave1-mr-pilot/`; no data payload is committed
  (confirm `git status` shows nothing under `data/`).

## Out of scope

Deferred to the full `design` plan (prospective `plan:0008`), not attempted here:

- `dataset:ruth-2020-shbg-testosterone-gwas` and **every sex-effect-modification
  target** (`question:0007`/`0013`/`0019`–`0022` as sex-modifiers) — the pilot is
  sex-agnostic.
- **Sample-overlap correction** (Ruth↔HGI, both via UK Biobank; handoff §3.3). Not
  triggered by this largely-non-UKB pair; a formal Bentham↔HGI shared-cohort check
  is a design-phase item.
- **Strict-stratum HGI sensitivity** (GCST90454540–542) and the broad-vs-strict
  comparison (handoff §3.6, §1).
- **HLA-inclusive** sensitivity run (primary excludes the extended MHC; the
  inclusive comparison is design-phase, per the pre-commitment).
- **Reverse-causation** direction (long-COVID liability → autoimmune).
- **Reporting as hypothesis/question evidence** — gated by the full acceptance
  checklist (handoff §4) and, ideally, a prior `/science:pre-register`.

## Notes on plan scope

This is deliberately a one-pair `probe`, not the full three-candidate design: the
point is to derisk retrieval + harmonization + estimator mechanics on the single
cleanest pair before committing the multi-candidate sensitivity matrix. Over-
specifying the full pipeline before a single MR has run end-to-end is the
documented failure mode this size guards against; grow to `plan:0008` only after
the Decision criteria clear.
