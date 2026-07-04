---
id: "plan:0008-wave1-mr-autoimmune-hormone-longcovid-design"
type: "plan"
plan_kind: "pipeline"
title: "Wave-1 MR full design: autoimmune + sex-hormone liability → long-COVID (reportable-grade)"
status: "active"
created: "2026-07-04"
updated: "2026-07-04"
related:
  - "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
  - "hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate"
  - "hypothesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune"
  - "question:0007-mechanism-of-female-predominance-in-pais"
  - "question:0013-reproductive-stage-failed-immune-recovery-after-infection"
  - "question:0022-immune-state-displacement-mediator-vs-co-traveler"
  - "plan:0007-wave1-mr-autoimmune-longcovid-pilot"
  - "task:t089"
  - "dataset:bentham-2015-sle-gwas"
  - "dataset:covid19-hgi-longcovid-gwas"
  - "dataset:ruth-2020-shbg-testosterone-gwas"
  - "dataset:1000g-eur-ld-panel"
---

# Wave-1 MR full design: autoimmune + sex-hormone liability → long-COVID

## Purpose

`plan:0007` proved the two-sample-MR **mechanics** end to end (retrieval →
MHC-aware instrument → local reproducible clumping → streamed harmonisation →
seeded estimators → QA'd output bundle) on the single cleanest pair, and returned
**GO**. This plan is the full `design` it pointed to: the analysis that can produce
a **reportable-grade** MR estimate — one that clears the handoff §4 acceptance gate
and is admissible as evidence toward `hypothesis:0005`/`0007`/`0009` and
`question:0007`/`0013`/`0022`.

Guiding principle: the pilot was explicitly **mechanics-only**, blocked from a
scientific reading by two independent bars — the **ancestry hard-stop** (the only
retrievable outcome was a European-dominant *multi-ancestry* meta) and the unrun
**acceptance gate** (sample-overlap correction, HLA-inclusive and case-definition
sensitivities, and — for any sex claim — sex-stratified instruments). This design's
entire job is to retire both bars honestly, or to state precisely where they cannot
be retired and demote the affected claim accordingly. It does **not** re-decide the
estimand or bridge assumptions — those are fixed in
`~/d/health/processes/post-acute-infection/doc/plans/2026-07-03-wave1-gwas-mr-estimand.md`
and the execution checklist in `doc/plans/2026-07-03-gwas-mr-ingestion-handoff.md`.
It operates strictly within **D-005** (authorising only the open,
third-party-reproducible Wave-1 GWAS/MR line) and does **not** re-open the
**D-004**-shelved gated-EHR autoimmune × sex × PASC estimand — the germline-liability
IV effect is an *adjacent, narrower, reproducible* question, not a reconstruction of
the shelved one.

## Scope decomposition

**In scope (this plan):**

- **Arm A — autoimmune → long-COVID** (`bentham-2015-sle-gwas` → long-COVID),
  the pilot pair, promoted to reportable grade with the full sensitivity matrix.
- **Arm B — sex-hormone → long-COVID** (`ruth-2020-shbg-testosterone-gwas` SHBG /
  testosterone → long-COVID), the new arm, including **sex-specific exposure
  instruments** and **sample-overlap correction** (Ruth is 100% UK Biobank; HGI
  pools UKB).
- **A EUR-matched outcome** to lift the ancestry hard-stop (WP1), with an explicit
  sourcing ladder and a fail-closed fallback.
- **The full pre-committed sensitivity matrix:** broad/population (primary) +
  broad/strict + strict-case outcome strata; extended-MHC-excluded (primary) +
  HLA-inclusive exposure instruments; IVW + MR-Egger + weighted-median.
- **Reverse / bidirectional direction** (long-COVID liability → autoimmune/hormone),
  the arrow that bears on `hypothesis:0009` and `question:0022`.
- **The acceptance gate** (handoff §4) assembled per reported estimate, and a
  pre-registration of the frozen analysis matrix + HLA decision **before** any
  outcome-side result is read.

**Out of scope (deferred, with reason):**

- **A sex-stratified *outcome* GWAS.** None is published for long-COVID (handoff §1,
  Ruth entity bridge note). Arm B therefore runs sex-specific *exposure* instruments
  against a **mixed-sex** outcome — a **bounded** sex-modification probe, not a full
  genotype × sex interaction. The ceiling is a Key Decision below, not a bug to fix
  here.
- **Non-European ancestry MR.** All three exposures and the target outcome are
  European; cross-ancestry is a separate, later line.
- **New exposure traits** beyond SLE and SHBG/testosterone (e.g. RA, thyroid
  autoimmunity, estradiol-female). Additive; a Wave-2 concern once the two-arm
  template is proven reportable.
- **Individual-level / ascertainment-structured effects** — permanently with
  `hypothesis:0008` under D-004; MR cannot and does not address them.

## Architecture

Reuse the pilot's proven, isolated Snakemake+conda harness under
`code/workflows/wave1-mr/`. The design generalises the pilot's single hard-coded
pair into a **config-driven analysis matrix** (exposure × outcome-stratum ×
HLA-policy × direction), so no estimator logic is rewritten — only parametrised and
fanned out. New surface is the EUR-outcome acquisition, the Ruth arm, the MRlap
overlap correction (which needs genome-wide LDSC infrastructure), and the
matrix/aggregation layer.

```
code/workflows/wave1-mr/
├── Snakefile                         MODIFY  fan rules over config.matrix (was one pair)
├── config.yaml                       MODIFY  add: eur outcome ladder, ruth strata,
│                                              analysis matrix, mrlap/ldsc params,
│                                              hla-inclusive policy, direction flag
├── envs/
│   ├── r-mr.yaml                     MODIFY  add r-mrlap (+ its deps); keep pinned
│   ├── r-mr.conda-lock.yml           MODIFY  relock after env change
│   └── ldsc.yaml                     NEW     ldsc / munge infra env (python2 or
│                                              a maintained LDSC fork), conda-locked
├── scripts/
│   ├── acquire_sumstats.py           MODIFY  parametrise over accession list
│   ├── stage_ld.py                   UNCHANGED  1000G-EUR panel staging
│   ├── stage_ldsc_ref.py             NEW     stage eur_w_ld_chr LD scores (checksummed)
│   ├── setup_twosamplemr.R           UNCHANGED  pinned-tag install + version sentinel
│   ├── build_instrument.R            MODIFY  emit both MHC-excluded and HLA-inclusive
│   │                                          instrument sets; sex-stratum aware
│   ├── harmonize_estimate.R          MODIFY  loop the matrix; TwoSampleMR 3-estimator
│   ├── overlap_correct.R             NEW     MRlap (LDSC-intercept) correction, Arm B
│   ├── reverse_direction.R           NEW     long-COVID → exposure MR (bidirectional)
│   └── emit_datapackage_qa.py        MODIFY  matrix-aware manifest + acceptance-gate
│                                              checklist emission
code/workflows/wave1-mr/results → results/wave1-mr/   (gitignored payloads under data/)
entities/datasets/
├── covid19-hgi-longcovid-gwas.md     MODIFY  add EUR-stratum file (if HGI EUR deposit)
├── <eur-longcovid-outcome>.md        NEW?    only if the EUR outcome is a distinct
│                                              study (FinnGen / NatCardioVasc-2025)
└── <eur-ldsc-ld-scores>.md           NEW     reference dataset for MRlap/LDSC
doc/plans/
└── 2026-07-04-wave1-mr-pilot-result.md  UNCHANGED  pilot go/no-go of record
```

## Key decisions

### Key decision 1: source a EUR-matched outcome via an explicit ladder; fail closed to mechanics-only

- **Chosen approach:** WP1 sources a genuinely European-ancestry long-COVID outcome
  in priority order: **(1)** an HGI EUR-ancestry-specific long-COVID stratum if one
  is deposited (HGI serves ancestry-specific subpopulation files for the COVID
  phenotypes; verify a long-COVID EUR file exists on the Catalog/FTP or the
  covid19hg portal); **(2)** the **European-ancestry long-COVID GWAS** in Nature
  Cardiovascular Research 2025 (*"Human genetics implicate thromboembolism in the
  pathogenesis of long COVID in individuals of European ancestry"*,
  DOI 10.1038/s44161-025-00749-4) if its summary statistics are openly downloadable
  and third-party-reproducible; **(3)** a **FinnGen** long-COVID endpoint (European
  isolate — record the LD-panel caveat). Each rung must clear the same
  reproducibility bar (public, downloadable, checksummable) before use.
- **Rejected alternative:** keep the European-dominant multi-ancestry
  GCST90454541 as the *primary* outcome. Rejected because bridge assumption 4
  (ancestry-matched panels) makes an unmatched primary inadmissible; the pilot
  already banked this as the hard-stop.
- **Reason:** the acceptance gate's ancestry box cannot be checked without a
  matched European outcome; if **no** rung yields one, the primary claim is
  **demoted to mechanics/robustness-only** (per the pilot's stated fallback) and the
  European-dominant run is reported only with an explicit ancestry sensitivity — the
  line does not silently promote an unmatched estimate.

### Key decision 2: correct Ruth↔HGI sample overlap with MRlap (LDSC-intercept), not exclusion

- **Chosen approach:** for Arm B, quantify and **correct** the UK-Biobank overlap
  with **MRlap** (Mounier & Kutalik 2023), which jointly corrects sample overlap and
  weak-instrument bias from the cross-trait LDSC intercept; report the MRlap-corrected
  effect as primary for Arm B, with the naive TwoSampleMR IVW as the uncorrected
  comparator, and record the estimated overlap fraction.
- **Rejected alternative:** UK-Biobank *exclusion* (use a leave-UKB-out outcome
  meta). Rejected because no leave-UKB-out long-COVID meta is published; we cannot
  manufacture one from summary statistics.
- **Reason:** Ruth is 100% UKB and the HGI outcome pools UKB, so overlap is
  structural and material for Arm B (bridge assumption 3). MRlap is the reproducible,
  open, summary-statistics-only correction. **Cost carried forward:** MRlap needs
  *genome-wide* munged sumstats for both traits plus an EUR LD-score reference — not
  the instrument-only streaming the pilot used — so WP2 stages the LD scores and WP5
  budgets a genome-wide LDSC pass (a real resource step, validated on real data).
  Arm A (Bentham, largely non-UKB) still gets a shared-cohort check but is expected
  to need no correction.

### Key decision 3: Arm B is a bounded sex-modification probe, ceilinged by the mixed-sex outcome

- **Chosen approach:** run **male-only** and **female-only** Ruth exposure
  instruments (SHBG, testosterone) against the **mixed-sex** long-COVID outcome, and
  compare the two sex-specific effects. Report this as a **sex-specific-instrument**
  contrast — it captures sex-differences in the *exposure* genetic architecture
  propagated to a common outcome.
- **Rejected alternative:** claim full genotype × sex effect-modification of the
  exposure→outcome effect. Rejected because that requires a **sex-stratified
  outcome**, which does not exist for long-COVID (handoff §1; estimand §b.2).
- **Reason:** the acceptance gate (box 9) forbids asserting sex-modification beyond
  what the run sumstats support. The honest, estimable claim is bounded; the write-up
  must state that a difference between male- and female-instrument effects on a
  mixed-sex outcome is **necessary but not sufficient** for sex-modification of the
  causal effect, and cannot separate exposure-architecture differences from
  outcome-response differences.

### Key decision 4: generalise the pilot harness to a config matrix; do not fork a second workflow

- **Chosen approach:** extend `code/workflows/wave1-mr/` in place — the Snakefile
  fans its existing rules over a `config.matrix` of `(exposure, outcome_stratum,
  hla_policy, direction)` cells; estimators, harmonisation, and QA are the pilot's,
  parametrised.
- **Rejected alternative:** a fresh `wave1-mr-full/` workflow. Rejected — it would
  duplicate the proven, locked env and rule bodies and invite drift.
- **Reason:** the pilot's mechanics are the asset; the design's novelty is coverage,
  not plumbing. One workflow, one locked env, config-driven fan-out (the `plan:0003`
  KD4 "params live in config, not rules" pattern the pilot already follows).

### Key decision 5: pre-register the frozen matrix + HLA decision before any outcome result is read

- **Chosen approach:** WP7 opens with a `/science:pre-register`-style freeze of the
  full analysis matrix, the a-priori HLA include/exclude decision (primary =
  extended-MHC-excluded), the primary outcome stratum, and the overlap-correction
  plan — committed **before** WP4/WP5 estimates are unblinded.
- **Rejected alternative:** decide HLA / stratum / primary-vs-sensitivity after
  seeing which gives a cleaner result. Rejected outright — it is the
  researcher-degrees-of-freedom hole the estimand §d.5 and handoff §3.4 explicitly
  disallow.
- **Reason:** the acceptance gate is only credible if the choices it audits were
  fixed in advance; post-hoc selection voids the causal reading regardless of the
  numbers.

## Work packages

### WP1 — Source + stage the EUR-matched outcome (lifts the ancestry hard-stop)

- **Depends on:** `plan:0007` (harness) — done.
- **Entry point:** `scripts/acquire_sumstats.py` (parametrised), the KD1 ladder.
- **Definition of done:** a European-ancestry long-COVID outcome staged under
  `data/raw/gwas/` (gitignored) with source URL, build, per-file SHA-256, row count,
  and ancestry evidence recorded; the corresponding dataset entity created or
  extended (extend `covid19-hgi-longcovid-gwas` if it is an HGI EUR stratum; else a
  new entity via `/science:find-datasets`) with `access.verified: true`, enum-safe
  `verification_method`, dated `last_reviewed`, and reproducibility class
  `third-party-reproducible`; the **data-access + reproducibility gate rerun and
  passing** for this input. **Hard stop / fail-closed:** if no ladder rung yields a
  reproducible EUR outcome, record the negative result and invoke KD1's demotion —
  the design proceeds mechanics/robustness-only and says so, rather than promoting an
  unmatched outcome.

### WP2 — Stage the Ruth sex-stratified exposures + LDSC infrastructure

- **Depends on:** WP1 (parallel-safe; no data dependency).
- **Entry point:** `scripts/acquire_sumstats.py`, `scripts/stage_ldsc_ref.py`,
  `envs/ldsc.yaml`.
- **Definition of done:** the required Ruth strata staged — **male-only** and
  **female-only** SHBG (GCST90012109 / GCST90012107) and total testosterone
  (GCST90012113 / GCST90012112), plus the sex-combined siblings for cross-check —
  each with SHA-256/build/rows; `ruth-2020-shbg-testosterone-gwas` entity upgraded to
  a retrieval-grade `verification_method` and its `assembly.label` resolved
  (currently UNKNOWN). An **EUR LD-score reference** (`eur_w_ld_chr`) staged as a new
  tracked reference dataset (checksummed, openly downloadable) for MRlap/LDSC; a
  reproducible `ldsc.yaml` env locked. Gate rerun and passing for both inputs.

### WP3 — Generalise the harness to the analysis matrix

- **Depends on:** WP1, WP2 (needs the real staged inputs to validate fan-out).
- **Entry point:** `Snakefile`, `config.yaml`, `scripts/build_instrument.R`,
  `scripts/harmonize_estimate.R`, `scripts/emit_datapackage_qa.py`.
- **Definition of done:** `config.matrix` enumerates the pre-committed cells;
  `build_instrument.R` emits **both** an extended-MHC-excluded and an HLA-inclusive
  instrument set per exposure and is sex-stratum aware; `harmonize_estimate.R` loops
  the matrix producing per-cell IVW/Egger/weighted-median + Egger intercept + per/mean
  F; the QA emitter is matrix-aware (one datapackage, per-cell QA rows, structural
  hard-stops preserved). A **dry-run + one real cell** (the pilot pair, re-run
  through the generalised code) reproduces the pilot's numbers bit-for-bit —
  regression guard that the refactor changed no estimator behaviour.

### WP4 — Arm A: autoimmune → long-COVID, full sensitivity matrix

- **Depends on:** WP3, and WP1's EUR outcome (or its documented demotion).
- **Entry point:** the matrix cells for `exposure = bentham-sle`.
- **Definition of done:** primary = SLE (extended-MHC-excluded) → **EUR** broad/
  population long-COVID; sensitivities = HLA-inclusive instrument; broad/strict
  (GCST90454543) and strict-case (GCST90454540/542) outcome strata; the
  European-dominant multi-ancestry run reported *only* as an ancestry sensitivity if
  WP1 demoted. Bentham↔HGI shared-cohort check recorded (expected: negligible). Per
  cell: F-stats, three estimators + concordance/discordance stated, Egger intercept.
  No cell is read as evidence until WP7's gate is assembled for it.

### WP5 — Arm B: sex-hormone → long-COVID, overlap-corrected + sex-specific instruments

- **Depends on:** WP3, WP2 (LD scores), WP1's EUR outcome.
- **Entry point:** the matrix cells for `exposure = ruth-shbg / ruth-testosterone`,
  `scripts/overlap_correct.R`.
- **Definition of done:** sex-combined and **sex-specific** (male, female) instrument
  runs for SHBG and total testosterone → long-COVID; **MRlap** overlap+weak-instrument
  correction applied with the estimated UKB overlap fraction recorded, MRlap-corrected
  primary vs naive-IVW comparator both reported; the male-vs-female instrument-effect
  contrast reported strictly as the **bounded** probe of KD3 (no full-interaction
  claim). **Scale/resource validation on real data:** the genome-wide LDSC munge +
  MRlap pass is run on the full staged sumstats with **peak memory + wall-clock
  recorded** in `qa_report` — MRlap's genome-wide requirement is exactly the kind of
  real-input resource behaviour green fixtures do not prove.

### WP6 — Reverse / bidirectional direction

- **Depends on:** WP4, WP5 (reuses staged inputs + instruments).
- **Entry point:** `scripts/reverse_direction.R`.
- **Definition of done:** long-COVID liability → SLE and long-COVID liability →
  SHBG/testosterone MR run where the outcome-as-exposure instrument is adequately
  strong (report F; **halt-and-note** the direction if long-COVID yields too few
  strong instruments — a single-locus FOXP4-dominated long-COVID GWAS may not
  instrument well, which is itself the finding). This is the arrow that bears on
  `hypothesis:0009` (PAIS → later autoimmune conversion) and sharpens
  `question:0022` (mediator vs co-traveler); its interpretation is stated as
  directional evidence under the same bridge assumptions.

### WP7 — Acceptance-gate assembly, pre-registration, write-up

- **Depends on:** WP4, WP5, WP6.
- **Entry point:** `scripts/emit_datapackage_qa.py` (gate emission), a results note.
- **Definition of done:** the **pre-registration freeze** (KD5) is committed before
  any WP4/WP5 estimate is unblinded (temporally: this is authored at WP7's *open*,
  gating WP4–WP6 reads — listed last only because it closes the loop). Then, per
  reported estimate, the handoff §4 nine-box acceptance checklist is emitted into
  `qa_report` with each box explicitly checked or the estimate marked
  not-reportable; a results note records which arms/cells cleared the gate and are
  admissible as `hypothesis:0005`/`0007`/`0009` / `question:0007`/`0013`/`0022`
  evidence, which are mechanics/robustness-only, and the go/no-go for a Wave-2
  trait expansion.

## Open questions

1. **Does an HGI EUR-ancestry long-COVID stratum exist as a downloadable file?**
   WP1 rung 1. If not, rung 2 (NatCardioVasc-2025 EUR long-COVID) hinges on whether
   its summary statistics are openly deposited — to verify at WP1, not assumed here.
2. **Is the NatCardioVasc-2025 EUR long-COVID phenotype comparable** (case
   definition, bridge assumption 6) to the HGI broad/population definition, or does
   switching outcome studies change the estimand? If it changes it, record the
   case-definition delta and treat cross-study as its own sensitivity, not a
   drop-in.
3. **Will long-COVID instrument well enough for WP6's reverse direction?** The
   published long-COVID signal is FOXP4-dominated (few genome-wide-significant loci);
   the reverse MR may be underpowered — WP6 treats that as a reportable negative, not
   a failure.
4. **MRlap LD-score ancestry/build match** to the Ruth (GRCh37-native) and outcome
   sumstats — confirm the `eur_w_ld_chr` reference aligns (rsID-keyed) as WP2's DoD.

## Non-goals

- Reconstructing the D-004-shelved individual-level, ascertainment-structured
  autoimmune × sex × PASC interaction (stays with `hypothesis:0008`).
- Any non-European-ancestry MR.
- New exposure traits beyond SLE and SHBG/testosterone (Wave-2).
- A sex-stratified outcome analysis (no such long-COVID GWAS exists).
- Clinical, diagnostic, or treatment-effect interpretation — the estimate is a
  germline-liability IV effect only (estimand §c).

## Acceptance criteria

An MR estimate from this plan is reportable as evidence toward the target
hypotheses/questions **only if** its per-estimate `qa_report` checklist (handoff §4)
is fully checked:

- [ ] All consumed dataset entities complete + access-verified + reproducibility
      class recorded (§4 box 1); **ancestry-matched EUR outcome used**, or the
      mismatch flagged and the estimate **not** treated as primary (KD1 demotion).
- [ ] Instrument F-statistics reported; no exposure relies solely on weak
      instruments (§3.1).
- [ ] IVW + MR-Egger + weighted-median all run; concordance/discordance stated
      explicitly (§3.2).
- [ ] Sample overlap quantified; **Arm B MRlap-corrected** (Ruth↔HGI via UKB),
      Arm A shared-cohort check recorded (§3.3).
- [ ] A-priori HLA include/exclude decision fixed **before** outcome results seen
      and stated; HLA-inclusive reported as sensitivity (§3.4, KD5).
- [ ] All panels ancestry-matched, or mismatch flagged and not primary (§3.5).
- [ ] HGI case-definition stratum stated per estimate; broad/population primary,
      broad/strict + strict-case as sensitivities, never silently mixed (§3.6).
- [ ] Stated as a germline-liability IV effect, explicitly **not** as closing the
      D-004 gap (estimand §c).
- [ ] Any sex claim uses only Ruth sex-stratified exposure strata and is scoped to
      the **bounded** mixed-sex-outcome ceiling (§4 box 9, KD3).
- [ ] The pre-registration freeze predates every unblinded estimate (KD5).
- [ ] Full reproducible bundle present (matrix-aware `datapackage.json` with entity
      cross-refs + provenance DAG, per-cell `qa_report.{json,md}`, `run_metadata.json`
      with seeds/versions/SHA-256s, updated `r-mr.conda-lock.yml` + `ldsc.yaml` lock);
      no data payload committed.

If any box cannot be checked for a given estimate, that estimate is not reportable
as hypothesis/question evidence — this is the gate, not a post-hoc checklist.
