---
title: 'Wave-1 GWAS/MR ingestion + analysis handoff (front→back boundary)'
status: active
created: '2026-07-03'
see_also:
- doc:2026-07-03-wave1-gwas-mr-estimand
- doc:2026-07-03-wave1-checkpoint
- doc:2026-07-03-capability-vocabulary
- decision:D-004
- task:t088
---

<!-- Non-entity handoff doc under doc/plans/. No `type:` field, so `science
     validate` does not treat it as a mis-homed plan entity, consistent with the
     design doc's convention. -->

# Wave-1 GWAS/MR ingestion + analysis handoff

This is the design's §4a "candidate handoff contract" made concrete for the three
Wave-1 GWAS candidates. It is the **front→back boundary**: everything below is
catalog/handoff work, already done in `entities/datasets/`; **it does not run any
analysis**. Running MR on this data is **gated by `task:t088`** (the open
third-party-reproducible analysis scope decision) and, once t088 clears, the next
step is **`/science:plan-pipeline`**, not this document. The follow-up execution
task is filed as **`task:t089`** (blocked-by `task:t088`; see §6).

## 1. Per-candidate accession/URL + files to stage

### `dataset:covid19-hgi-longcovid-gwas` — mr_outcome (trait: long-covid)

> **Correction (2026-07-04, supersedes the stratum labels in this subsection).**
> The original text misidentified **GCST90454543** as broad-cases /
> **population**-controls. Per the GWAS Catalog harmonised `*-meta.yaml` files,
> **GCST90454541** is broad-cases / **population**-controls, and **GCST90454543** is
> broad-cases / **strict** controls (had SARS-CoV-2 but did not develop long COVID) —
> a different, within-infected estimand. `plan:0007` is authoritative: **primary MR
> outcome = GCST90454541**; 543 (broad/strict) and the strict-**case** strata are
> sensitivities. Both harmonised files are European-dominant *multi-ancestry* metas
> (no EUR-only sibling), constraining ancestry-matched MR — see `plan:0007`'s
> ancestry hard-stop.

- **Landing page:** https://www.ebi.ac.uk/gwas/studies/GCST90454541 (GWAS Catalog);
  initiative page https://www.covid19hg.org/results/
- **Accessions (GWAS Catalog):** GCST90454541 (primary — broad/population, see the
  correction above and the stratum note below), GCST90454543 (broad/strict —
  sensitivity), GCST90454540, GCST90454542
- **Citation:** Lammi et al., *Nature Genetics* 2025; PMID 40399555;
  DOI 10.1038/s41588-025-02100-w
- **Files to stage:** the harmonised full-summary-statistics flat file
  (`fullPvalueSet=true`) for **GCST90454541** (primary; plus GCST90454543 for the
  strict-control sensitivity) from the GWAS Catalog FTP
  (`ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/`, harmonised subfolder for
  this accession). Stage build/assembly alongside the file (the release ships both
  GRCh37 and GRCh38 — record whichever harmonised file is pulled; do not leave
  `identity_context.assembly.label: UNKNOWN` past ingestion).
- **Case-definition stratum decision (corrected 2026-07-04; see banner):** primary
  MR-outcome stratum is **GCST90454541** — the **broad** case definition (long COVID
  after *any* SARS-CoV-2 infection) with **population controls**. **GCST90454543**
  (broad cases / **strict** infected-but-no-long-COVID controls) and the
  strict-**case** strata (GCST90454540/542) are retained as **pre-committed
  case-/control-definition sensitivity analyses**, per bridge assumption 6 in the
  estimand note (§d below). Do not choose the stratum post-hoc from which gives a
  cleaner result.
- **Known limitation to carry into staging:** mixed-sex only; no sex-stratified or
  sex-interaction sumstats are published for this outcome. Out of scope for the
  sex-modification targets (question:0007/0013/0019–0022) as an outcome; in scope
  for the sex-agnostic estimand and the reverse-causation direction.

### `dataset:bentham-2015-sle-gwas` — mr_exposure (trait: autoimmune-disease)

- **Landing page:** https://www.ebi.ac.uk/gwas/studies/GCST003156
- **Accession:** GCST003156
- **Citation:** Bentham et al., *Nature Genetics* 2015; PMID 26502338;
  DOI 10.1038/ng.3434
- **Files to stage:** the harmonised full-summary-statistics flat file
  (`fullPvalueSet=true`) for GCST003156 from the GWAS Catalog FTP. Native build is
  GRCh37; a harmonised GRCh38 file is also served — record which is pulled.
- **Known limitations to carry into staging:** mixed-sex only (no sex-stratified
  sumstats — do not use as a sex-modification exposure); European-ancestry only
  (5,201 cases / 9,066 controls, the summary-stat-bearing scan); HLA-dense signal
  (chr6p21) requiring the a-priori HLA include/exclude decision below.

### `dataset:ruth-2020-shbg-testosterone-gwas` — mr_exposure (trait: sex-hormone-biomarker)

- **Landing page:** https://www.ebi.ac.uk/gwas/studies/GCST90012109 (SHBG, men);
  see full accession set below for the other strata
- **Accessions to stage (sex-stratified — the load-bearing feature of this
  candidate):**
  - SHBG: GCST90012109 (men, n≈180,726), GCST90012107 (women, n≈189,473),
    GCST90012111 (sex-combined, n≈370,125); BMI-adjusted variants GCST90012108
    (men), GCST90012106 (women), GCST90012110 (combined)
  - Total testosterone: GCST90012113 (men, n≈194,453), GCST90012112 (women,
    n≈230,454), GCST90012114 (sex-combined, n≈425,097)
  - Bioavailable testosterone: GCST90012103 (men), GCST90012102 (women),
    GCST90012104 (sex-combined)
  - Estradiol: GCST90012105 (men only — no female-stratum estradiol accession is
    deposited here; do not assume symmetry)
- **Citation:** Ruth et al., *Nature Medicine* 2020; PMID 32042192;
  DOI 10.1038/s41591-020-0751-5 (UK Biobank, European ancestry)
- **Files to stage:** the harmonised full-summary-statistics flat files for
  **whichever sex-matched strata the target analysis needs** (do not stage only
  the sex-combined file — the sex-stratified files are the reason this candidate
  clears the discovery-filter gate in the estimand note, §"Discovery filter").
  UK Biobank imputation → native GRCh37; a harmonised GRCh38 file is also served.
- **Known limitation to carry into staging:** UK Biobank is a contributing cohort
  to both this exposure GWAS and the HGI long-COVID outcome (GCST90454543 and
  siblings) — see the sample-overlap sensitivity requirement below; this is the
  single most concrete overlap risk of the three candidates.

## 2. The MR estimand + bridge assumptions

**Not re-derived here** — cite directly:
`~/d/health/processes/post-acute-infection/doc/plans/2026-07-03-wave1-gwas-mr-estimand.md`.

In brief (see the note for the full statement): two-sample MR of (i) genetic
liability to autoimmune disease and (ii) a sex-hormone biomarker, each on a PAIS
outcome (long-COVID liability), estimated by inverse-variance-weighted (IVW) MR as
primary, interpreted as a **germline-liability IV effect** — not the effect of
diagnosis, treatment, or age of acquisition, and explicitly **not** a reconstitution
of the D-004-shelved individual-level EHR autoimmune×sex×PASC estimand (estimand
note §c). Any result read as evidence toward `hypothesis:0005`,
`hypothesis:0007`, `hypothesis:0009`, or `question:0007`/`0013`/`0019`–`0022`
must satisfy every bridge assumption in the estimand note's §d — each is a gate,
not a caveat.

> **Narrowed by `plan:0008` KD6 (2026-07-04).** `hypothesis:0009`'s post-infectious
> latent→overt *conversion* arrow is not identifiable by germline-liability MR (in
> either direction); for the Wave-1 design it is shared-liability / directionality
> context only, not an admissible MR-evidence target. This applies equally to the
> h0009 mention in the §4 acceptance list below. h0005/h0007 unaffected.

## 3. Sensitivity analyses required (per estimand §d, restated as an execution checklist)

1. **Instrument relevance (IV1).** Report per-instrument and mean F-statistic for
   every exposure instrument; flag and report variance explained where available.
   Weak instruments bias two-sample MR toward the null.
2. **MR-Egger + weighted-median (IV2/pleiotropy).** Run both as sensitivity to
   IVW. MR-Egger intercept tests directional pleiotropy; its slope is a
   pleiotropy-robust point estimate. Weighted-median is consistent if <50% of
   instrument weight is invalid. Concordance across IVW/Egger/weighted-median is
   the minimum robustness bar; report discordance, do not suppress it.
3. **Sample-overlap check — UK Biobank, Ruth↔HGI specifically.** Quantify the
   overlap between the Ruth 2020 SHBG/testosterone GWAS (UK Biobank) and the
   COVID-19 HGI long-COVID outcome GWAS (which pools multiple biobanks, including
   UK Biobank contributions). Overlap biases two-sample MR toward the confounded
   observational association; if overlap cannot be reduced by cohort exclusion,
   apply an overlap-correction method (e.g. correction terms in the MR
   variance/estimate, or a non-overlapping sensitivity outcome GWAS if one exists).
   Also check Bentham SLE (largely non-UKB cohorts) against the HGI outcome for
   any shared contributing cohort.
4. **A priori HLA include/exclude — the Bentham SLE instrument.** Before seeing any
   outcome-side result, fix and record whether the primary analysis excludes the
   extended MHC (chr6:25–34 Mb) from the SLE instrument, with an HLA-inclusive run
   reported only as sensitivity. Post-hoc HLA handling is disallowed (estimand §d.5).
5. **Ancestry-matched panels.** All three candidates are European-ancestry
   (Bentham: European case-control; Ruth: UK Biobank European subset; HGI: use the
   European-ancestry stratum of the multi-ancestry meta-analysis, or flag and treat
   as sensitivity if a matched European outcome stratum is unavailable). Any
   cross-ancestry combination is flagged and not treated as primary. Record the LD
   reference panel ancestry used for clumping/pruning.
6. **PAIS case-definition comparability.** Record and carry forward the corrected
   HGI stratum decision from §1 (primary = broad/population **GCST90454541**;
   sensitivities = broad/strict **GCST90454543** and the strict-case strata
   GCST90454540/542) through every downstream reported estimate; do not silently
   mix strata across sensitivity runs.

## 4. Acceptance check

An MR result may be reported as evidence toward `hypothesis:0005`/`0007`/`0009` or
`question:0007`/`0013`/`0019`–`0022` only if **all** of the following hold:

- [ ] Every dataset entity's handoff fields are complete per the design's §4a
      contract (`entities/datasets/{covid19-hgi-longcovid-gwas,
      bentham-2015-sle-gwas, ruth-2020-shbg-testosterone-gwas}.md`): access
      `verified: true`, dated `last_reviewed`, resolvable accession/URL,
      reproducibility class recorded (`third-party-reproducible`, not
      `unknown`/`below-bar`), `provided_capabilities` declared, target
      `required_capabilities` declared, `related:` edge wired, fit/limitation note
      present (all already true as of this handoff — see the entity files).
- [ ] Instrument F-statistics reported and no exposure relies solely on
      weak instruments (§3.1).
- [ ] IVW, MR-Egger, and weighted-median all run and concordance/discordance
      reported explicitly (§3.2).
- [ ] Sample overlap (especially Ruth↔HGI, both via UK Biobank) quantified and,
      if present and material, corrected (§3.3).
- [ ] The a-priori HLA include/exclude decision for the Bentham SLE instrument was
      fixed before outcome results were seen, and is stated in the write-up (§3.4).
- [ ] All instrument, exposure, and outcome panels are ancestry-matched (or the
      mismatch is flagged and the result is not treated as primary) (§3.5).
- [ ] The HGI case-definition stratum used (broad primary / strict sensitivity)
      is stated for every reported estimate (§3.6).
- [ ] The result is stated as a germline-liability IV effect and explicitly not
      as evidence about diagnosis/treatment/ascertainment-structured effects
      (estimand note §c) — i.e. it is not represented as closing the D-004-shelved
      gap, only as an adjacent, narrower, reproducible finding.
- [ ] For any sex-effect-modification claim specifically: only the
      `ruth-2020-shbg-testosterone-gwas` sex-stratified strata are used on the
      exposure side, and the claim is scoped to what a mixed-sex HGI outcome can
      support (a sex-stratified *outcome* is not currently available — see the
      dataset entity's bridge note) — do not assert sex-modification beyond what
      the actually-run sumstats support.

If any box cannot be checked, the result is not reportable as hypothesis/question
evidence until it is — this list is the acceptance gate, not a post-hoc checklist.

## 5. Scope: this plan does not run MR

**Running MR, ingesting the sumstats files above, and any pipeline code is gated by
`task:t088`** (open third-party-reproducible computational analysis scope
decision, referencing `specs/scope-boundaries.md`). This document is catalog/handoff
work only — the dataset entities exist, are `related:`-linked, and carry
`provided_capabilities`; no sumstats file has been downloaded, no MR estimator has
been run, and no code has been written. Gate-0 and dataset cataloging/discovery are
explicitly *not* gated by t088 (per t088's own scope note); only execution is.

**Once t088 resolves in favor of proceeding**, the next step is **`/science:plan-pipeline`**
against this handoff (not a continuation of this document) — it will turn the
per-candidate staging list, estimand, and sensitivity checklist above into concrete
pipeline steps, tool choices (e.g. `TwoSampleMR`/`MendelianRandomization` R
packages), configs, and validation criteria.

## 6. Follow-up task filed

**`task:t089`** — "Wave-1: run open GWAS/MR analysis for sex×autoimmune PAIS
questions" — priority P3, `blocked-by: [task:t088]`, `related: [task:t088]`,
status `proposed`. Description points back at this document as the handoff to
execute once unblocked. See `tasks/active.md`.
