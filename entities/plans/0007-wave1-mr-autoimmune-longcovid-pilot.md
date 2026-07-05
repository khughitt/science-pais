---
id: "plan:0007-wave1-mr-autoimmune-longcovid-pilot"
kind: "plan"
plan_kind: "pipeline"
title: "Wave-1 MR pilot: autoimmune liability → long-COVID (mechanics derisk)"
status: "active"
created: "2026-07-04"
updated: "2026-07-04"
related:
  - "hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate"
  - "question:0022-immune-state-displacement-mediator-vs-co-traveler"
  - "task:t089"
  - "dataset:bentham-2015-sle-gwas"
  - "dataset:covid19-hgi-longcovid-gwas"
  - "dataset:1000g-eur-ld-panel"
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

**Direction.** This pilot tests **autoimmune liability → long-COVID** (SLE
germline liability as exposure, long-COVID liability as outcome). That is the
forward direction of `hypothesis:0007` (autoimmune diathesis as a PAIS substrate)
and bears on `question:0022`. It is **not** a test of
`hypothesis:0009` (post-infectious immune set-point shift → *later* autoimmune
conversion), whose causal arrow runs PAIS → autoimmune — the opposite direction.
h0009 is kept as **background only** here; it would require a reverse-direction
(or bidirectional) MR, which this pilot does not run (see Out of scope).

**Pair + stratum choice.** Exposure `bentham-2015-sle-gwas` (GCST003156) is a
largely **non-UK-Biobank** European SLE case-control scan, so this pair sidesteps
the Ruth↔HGI UK-Biobank sample-overlap problem (handoff §3.3) and all
sex-stratification machinery, isolating pure MR mechanics. Outcome =
`covid19-hgi-longcovid-gwas` **GCST90454541** — the **broad-cases vs
population-controls** stratum (FTP metadata: "Broad case definition" /
"Broad control definition (population control)"). Population controls give a
general-population liability contrast comparable to Bentham's population
case-control design and avoid the collider/selection bias of conditioning on
prior infection. **This corrects the handoff §1 stratum label**, which named
GCST90454543 as broad/population: 543 is in fact broad-cases vs **strict**
controls ("had SARS-CoV-2 but did not develop Long COVID"), a *different,
within-infected estimand* — it is demoted to a design-phase sensitivity, not the
pilot primary.

**Ancestry caveat (load-bearing for the GO gate).** The GCST90454541 harmonised
file is a **European-dominant multi-ancestry meta-analysis** (European
n≈1,090,649 of ≈1,100,645 total, ~99%); the GWAS Catalog does **not** serve a
separate European-only file for this accession. A cleanly ancestry-matched
outcome therefore cannot be assembled from this file alone, so the pilot's MR
estimate is **mechanics-only** — see the ancestry hard-stop in Decision criteria.

## Approach

Two-sample MR with the standard `TwoSampleMR` R toolchain (cross-checked against
the `MendelianRandomization` package where estimators overlap). Instrument =
genome-wide-significant SLE variants, **extended-MHC-excluded** (chr6:25–34 Mb,
pre-committed per estimand §d.5 / handoff §3.4 — HLA-inclusive is a design-phase
sensitivity, not run here), LD-clumped against a **local, staged** 1000 Genomes
European reference panel (not the remote IEU clumping API — local clumping keeps
the step third-party-reproducible; see Inputs for its staging contract).
Estimators: **IVW primary**, MR-Egger and weighted-median as the minimum
robustness bar (handoff §3.2). Report per-instrument and mean F-statistic
(handoff §3.1). Clumping thresholds (r² < 0.001, 10 Mb) and `harmonise_data`
`action = 2` are the **TwoSampleMR `clump_data`/`harmonise_data` defaults**,
recorded as such in the run manifest. **Reproducibility:** IVW and MR-Egger are
closed-form, but the weighted-median SE is bootstrapped — set and record a
**fixed RNG seed** for it (and any bootstrapped diagnostic), and pin the
toolchain with **conda-lock**, matching the project's Snakemake `--use-conda`
convention (as in `plan:0003`) — not `renv`. All payloads gitignored under
`data/`; all outputs and a run manifest under `results/`.

## Reproducible execution harness

Runs under the project's established convention (`plan:0003`): a **Snakemake**
DAG with **per-rule `conda:` envs**, invoked `uv run snakemake --use-conda`. The
MR pilot is an **isolated** pipeline under `code/workflows/wave1-mr/` (its own
`Snakefile` + `config.yaml`), not folded into the 0003 gene-set Snakefile.

- **Env:** `code/workflows/wave1-mr/envs/r-mr.yaml` → byte-level
  `r-mr.conda-lock.yml`. Conda-available deps are locked there (`r-base`,
  `r-remotes`, `r-data.table`, `r-mendelianrandomization`, `plink` from bioconda,
  …).
- **TwoSampleMR is not on conda.** It is installed from a **pinned GitHub tag**
  (`remotes::install_github("MRCIEU/TwoSampleMR@<tag>")`, `upgrade = "never"`)
  by a dedicated setup rule that writes a sentinel and **records the resolved
  version** into `run_metadata.json`. `<tag>` is a locked `config.yaml` value.
- **Params are locked in `config.yaml`** (accessions/URLs, p-threshold, clump
  r²/kb, MHC window, weighted-median seed, TwoSampleMR tag, paths) — the runtime
  reads them; nothing is hard-coded in rules (0003 KD4 pattern).
- **Invocation-independent:** `workdir` pinned to repo root so `data/` and
  `results/` resolve to one tree regardless of where `snakemake` is invoked.

## Inputs

- **Exposure** — `dataset:bentham-2015-sle-gwas`, GCST003156, harmonised
  `fullPvalueSet=true` flat file (European case-control; binary trait, effects on
  the **log-OR** scale; native GRCh37, harmonised GRCh38 also served).
- **Outcome** — `dataset:covid19-hgi-longcovid-gwas`, **GCST90454541**
  (broad cases / population controls; binary trait, **log-OR**; harmonised
  GRCh38). European-dominant multi-ancestry meta (see ancestry caveat); no
  EUR-only file exists for this accession.
- **LD reference panel** — `dataset:1000g-eur-ld-panel` (1000 Genomes Phase 3
  **EUR** subset; plink1 `.bed/.bim/.fam` bfile; native GRCh37). A load-bearing,
  now first-class tracked input (it determines the surviving instrument set).
  Stage under `data/raw/ld/1000g-eur-phase3/` (gitignored), recording in the run
  manifest / datapackage: **source URL**, **release/version**, **genome build**,
  per-file **SHA-256**, and local path. Its build **must be reconciled with the
  GRCh38 harmonised sumstats** — either a GRCh38-lifted panel, or rsID-based
  matching via the harmonised `hm_rsid` column; a build mismatch resolved by
  neither is a **hard stop** (Task 2).
- Estimand + bridge assumptions: `doc/plans/2026-07-03-wave1-gwas-mr-estimand.md`.
- Staging + acceptance contract: `doc/plans/2026-07-03-gwas-mr-ingestion-handoff.md`.
- `TwoSampleMR` (R), `MendelianRandomization` (R), and a local `plink` (1.9+) for
  clumping.

## Approach detail: GWAS-SSF → TwoSampleMR schema boundary

Both inputs are GWAS Catalog harmonised summary-statistics-format (SSF) files.
Pin the ingestion contract before code:

- **Column mapping** (harmonised `hm_*` columns → TwoSampleMR fields):
  `hm_rsid`→SNP, `hm_chrom`→chr, `hm_pos`→pos, `hm_effect_allele`→effect_allele,
  `hm_other_allele`→other_allele, `hm_beta`→beta, `standard_error`→se,
  `effect_allele_frequency` (or `hm_effect_allele_frequency` where present)→eaf,
  `p_value`→pval. Fail loud on any missing required column rather than defaulting.
- **Effect scale.** Both traits are binary → `hm_beta` is a **log-OR**; carry it
  as `beta` with its `se` unchanged (no exp/logit transform). The MR estimate is
  the effect of a unit change in log-odds of SLE liability on the log-odds of
  long-COVID; report on that scale and label it as such.
- **EAF / palindromic policy.** Use `harmonise_data(action = 2)` — infer strand
  for palindromic SNPs from EAF and **drop palindromic SNPs whose EAF is
  ambiguous (≈0.5)** or whose EAF is missing. Do not fall back to `action = 1`
  (assume-all-forward) or `action = 3` (drop-all-palindromic) without recording
  the reason.
- **Instrument strength.** Per-SNP F = (beta / se)² (Wald statistic; needs no N).
  Report per-instrument F and mean F. Where an R²-based check is wanted, use the
  binary-trait **effective N** = 4 / (1/N_case + 1/N_control) with the standard
  log-OR variance-explained approximation; record N_case/N_control per dataset.

## Tasks

1. **Retrieve + register the two sumstats.** Pull GCST003156 and **GCST90454541**
   harmonised `fullPvalueSet` flat files from the GWAS Catalog FTP
   (`ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/`, harmonised subfolder)
   into `data/raw/gwas/` (gitignored). Record SHA-256, the actual assembly build
   pulled, and row counts in the run manifest. Then upgrade each dataset entity's
   access to a retrieval-grade `verification_method` and set
   `identity_context.assembly.label` (both harmonised files are GRCh38) — it must
   not remain UNKNOWN past ingestion (handoff §1).
2. **Stage + reconcile the LD panel; build the SLE instrument.** Stage the
   1000G-EUR panel per the Inputs contract (source/version/build/SHA-256/path).
   **Hard stop** if its build cannot be reconciled with the GRCh38 harmonised
   inputs (accept a GRCh38 panel, or rsID-match via `hm_rsid`; otherwise stop).
   Then filter Bentham to p < 5×10⁻⁸, **drop the extended MHC window
   chr6:25–34 Mb**, LD-clump locally (r² < 0.001, 10 Mb, 1000G-EUR panel), and
   compute per-instrument + mean F = (beta/se)². Halt loud if mean F < 10 or if
   any surviving instrument lies in the excluded MHC window.
3. **Harmonize exposure ↔ outcome.** Run `harmonise_data(action = 2)` per the SSF
   contract above: align effect alleles, infer/drop palindromic SNPs by EAF,
   extract outcome effects for the instrument SNPs (proxy lookup for missing SNPs
   is optional and, if skipped, logged as a limitation). **Scale discipline:** the
   GCST90454541 harmonised full-p-value file is multi-GB (N≈1.1M, tens of millions
   of variants) — extract the instrument SNPs by **streaming / selective read keyed
   on `hm_rsid`, not a full in-memory load** — and record **peak memory +
   wall-clock** for the extraction in `qa_report`. Log every dropped SNP with its
   reason; **no silent drops**.
4. **Estimate + diagnostics + reproducible output bundle.** Run IVW (primary),
   MR-Egger, and weighted-median; report point estimates, SEs, the MR-Egger
   intercept (directional-pleiotropy test), and explicit IVW/Egger/weighted-median
   concordance-or-discordance. Write the full output bundle under
   `results/wave1-mr-pilot/` (see Outputs contract).
5. **Probe write-up + go/no-go.** One short results note recording the mechanics
   outcome against the Decision criteria below. State plainly that the pilot
   estimate's sign/significance is **not** interpreted as evidence for or against
   `hypothesis:0007` or `question:0022` — that requires the full acceptance gate
   (handoff §4), which this probe does not attempt; and that the **ancestry
   hard-stop** independently bars this pilot from yielding a valid primary
   estimate. Recommend whether to proceed to the full `design` plan (prospective
   `plan:0008`).

## Outputs contract (Task 4)

`results/wave1-mr-pilot/` must contain, for the run to count as complete:

- **`datapackage.json`** — Frictionless descriptor listing every input and output
  resource with SHA-256 and source (the two sumstats + the LD panel), plus
  **entity cross-references** (`dataset:bentham-2015-sle-gwas`,
  `dataset:covid19-hgi-longcovid-gwas`, `dataset:1000g-eur-ld-panel`,
  `plan:0007`) and a **provenance DAG** linking each output back to its inputs.
- **`qa_report.json` + `qa_report.md`** — structural checks with explicit
  pass/fail: required-column presence, row counts, allele-coding sanity,
  instrument count, mean F, palindromic-drop count, the ancestry/build
  reconciliation result, and the **peak-memory + wall-clock** of the outcome
  extraction. Any failed **structural hard-stop** aborts the run.
- **Instrument table + MR results** — the clumped instrument set (with per-SNP F)
  and the IVW/Egger/weighted-median estimates + Egger intercept.
- **Command/run log** — the commands executed and their stdout/stderr.
- **`r-mr.conda-lock.yml`** (byte-level conda-lock env) + the recorded pinned
  TwoSampleMR tag/version — the reconstructable toolchain.
- **`run_metadata.json`** — tool + R-package versions (`sessionInfo()` /
  package versions), all parameters (clump thresholds, MHC window,
  `harmonise_data` action, **weighted-median RNG seed**), input accessions +
  SHA-256s, retrieval date, and the producing git commit — full provenance to
  re-run.

## Decision criteria

The probe concerns **mechanics**, not the scientific result. **GO** to the full
`design` plan if all hold:

- Both harmonised files retrieve, parse, and yield sane row counts and a recorded
  GRCh38 build.
- The LD panel stages and its build reconciles with the inputs (else hard stop).
- The clumped, MHC-excluded SLE instrument retains a workable set of independent
  variants (target ≳ 10) with **mean F-statistic > 10**.
- Harmonization completes under `action = 2` with palindromic/ambiguous SNPs
  resolved or logged, and outcome effects extracted for the instruments.
- IVW, MR-Egger, and weighted-median all return finite, sane-magnitude estimates,
  and the Egger intercept is computable — i.e. the estimator layer works and
  concordance is reportable.

**Ancestry hard-stop.** Because the only retrievable outcome file is a
European-dominant *multi-ancestry* meta (no EUR-only sibling), this pilot **cannot
produce a valid ancestry-matched primary estimate**. Any estimate it yields is
**mechanics-only** and must be labelled as such; escalation to a reportable
primary is blocked until the design plan obtains a European outcome stratum (or
formally justifies the European-dominant approximation with an ancestry
sensitivity). If no EUR-only outcome can be sourced, `plan:0008` demotes this
line to mechanics/robustness-only rather than a primary MR claim.

**NO-GO / fix-first** if the LD build cannot be reconciled, the instrument
collapses below the weak-instrument floor, harmonization cannot resolve allele
coding, or an estimator fails — surface the blocker and repair the mechanics
before the design plan.

## Validation

- Retrieved-file SHA-256s and GRCh38 build recorded in the run manifest; row
  counts within expected order of magnitude for genome-wide harmonised sumstats.
- LD panel staged with source/version/build/SHA-256; build reconciliation result
  recorded (hard-stop on failure).
- Every instrument SNP has p < 5×10⁻⁸ in the exposure and **none** falls in
  chr6:25–34 Mb.
- Palindromic/ambiguous-SNP handling under `action = 2` is logged; harmonization
  drop-log is present and non-silent.
- Per-instrument and mean F-statistics are reported.
- The weighted-median RNG seed and the committed conda-lock env
  (`r-mr.conda-lock.yml`) + recorded TwoSampleMR tag are present;
  outcome-extraction peak-memory + wall-clock are recorded in `qa_report`.
- The full output bundle (datapackage.json **with entity cross-refs**,
  qa_report.{json,md}, logs, r-mr.conda-lock.yml, run_metadata.json) is present;
  the ancestry/mechanics-only label is stated.
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
- **Strict-control HGI stratum** (GCST90454543, broad cases vs infected-no-long-COVID
  controls) — a *different, within-infected estimand*, retained as a design-phase
  sensitivity/estimand-comparison, not the pilot primary (handoff §3.6, §1). The
  intermediate strata GCST90454540/542 likewise deferred.
- **A EUR-only / ancestry-matched outcome** — required for any reportable primary
  estimate; sourcing or approximating it is a `plan:0008` obligation.
- **HLA-inclusive** sensitivity run (primary excludes the extended MHC; the
  inclusive comparison is design-phase, per the pre-commitment).
- **Reverse-causation / bidirectional MR** (long-COVID liability → autoimmune) —
  the direction that would bear on `hypothesis:0009`; not run here.
- **Reporting as hypothesis/question evidence** — gated by the full acceptance
  checklist (handoff §4) and, ideally, a prior `/science:pre-register`.

## Notes on plan scope

This is deliberately a one-pair `probe`, not the full three-candidate design: the
point is to derisk retrieval + harmonization + estimator mechanics on the single
cleanest pair before committing the multi-candidate sensitivity matrix. Over-
specifying the full pipeline before a single MR has run end-to-end is the
documented failure mode this size guards against; grow to `plan:0008` only after
the Decision criteria clear.
