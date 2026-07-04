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

> **Status update (2026-07-04) — reportable-primary execution DEFERRED; design banked.**
> WP1 established that **no matched EUR long-COVID outcome is publicly downloadable**
> (see the WP1 finding below + the `dataset:covid19-hgi-longcovid-gwas` verification
> log), so every estimate this design could produce is irreducibly
> **ancestry-flagged and non-primary** (estimand §d.5) — no reportable *primary*
> hypothesis evidence is achievable until a matched EUR long-COVID (or EUR PAIS —
> e.g. EUR ME/CFS/fatigue) GWAS is published. **Decision: defer the full
> reportable-primary design and bank it as-is**, and pursue the one novel,
> high-value line now as a scoped exploratory probe — **`plan:0009` (Arm-B
> sex-hormone pilot)**, the hormone analogue of `plan:0007`. This design remains the
> target to resume when a matched outcome exists.
> **Revisit trigger:** a matched EUR long-COVID / EUR PAIS GWAS becomes publicly
> downloadable → resume this design (Arm A sensitivity matrix, formal
> pre-registration, acceptance-gate-for-primary, bidirectional-as-evidence).
> **FinnGen remains held** (D-006).

## Purpose

`plan:0007` proved the two-sample-MR **mechanics** end to end (retrieval →
MHC-aware instrument → local reproducible clumping → streamed harmonisation →
seeded estimators → QA'd output bundle) on the single cleanest pair, and returned
**GO**. This plan is the full `design` it pointed to: the analysis that can produce
a **reportable-grade** MR estimate — one that clears the handoff §4 acceptance gate
and is admissible as evidence toward `hypothesis:0005`/`0007` and
`question:0007`/`0013`/`0022`. (`hypothesis:0009` is **contextual only** — its
post-infectious latent→overt *conversion* arrow is not MR-identifiable in this
design; see KD6.)

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
**Supersession (KD6):** where those two documents list `hypothesis:0009` as an
admissible MR-evidence target, this design **narrows** them — germline-liability MR,
in either direction, cannot identify h0009's acquired-state→later-conversion arrow,
so h0009 stands here as shared-liability context only. That narrowing governs this
plan; both upstream docs now carry a dated pointer to it.

**Authorisation scope (load-bearing, gated by WP0).** This plan operates within
**D-005**, which authorised the Wave-1 open GWAS/MR line over the **three cataloged
public GWAS-summary-statistic vehicles** named in the handoff
(`bentham-2015-sle-gwas`, `covid19-hgi-longcovid-gwas`,
`ruth-2020-shbg-testosterone-gwas`). Promoting the pilot to reportable grade needs a
**EUR-matched long-COVID outcome**, plus reference infrastructure (an EUR LD-score
panel, a HapMap3 SNP list) that D-005 did not enumerate. Two of those additions are
**still the authorised HGI vehicle** in a different distribution/freeze (see KD1);
the LD-score/HapMap3 references are analysis infrastructure, not new
measured-phenotype vehicles. Anything beyond that — notably a **FinnGen** outcome —
is a *distinct* vehicle not covered by D-005 as written. **WP0 is a scope gate that
must resolve before any WP1 acquisition code**: either confirm the new inputs are
in-authorisation (same HGI vehicle / pure infrastructure) or record a D-005
clarification, and hold FinnGen behind its own explicit authorisation +
reproducibility-class check. This plan does **not** re-open the **D-004**-shelved
gated-EHR autoimmune × sex × PASC estimand — the germline-liability IV effect is an
*adjacent, narrower, reproducible* question, not a reconstruction of the shelved one.

## Scope decomposition

**In scope (this plan):**

- **Arm A — autoimmune → long-COVID** (`bentham-2015-sle-gwas` → long-COVID),
  the pilot pair, promoted to reportable grade with the full sensitivity matrix.
- **Arm B — sex-hormone → long-COVID** (`ruth-2020-shbg-testosterone-gwas` SHBG /
  testosterone → long-COVID), the new arm, including **sex-specific exposure
  instruments** and **sample-overlap correction** (Ruth is 100% UK Biobank; HGI
  pools UKB).
- **A EUR-matched outcome** to lift the ancestry hard-stop (WP1), sourced within
  D-005 authorisation (WP0), with an explicit ladder and a fail-closed fallback.
- **The full pre-committed sensitivity matrix:** broad/population (primary) +
  broad/strict + strict-case outcome strata; extended-MHC-excluded (primary) +
  HLA-inclusive exposure instruments; IVW + MR-Egger + weighted-median.
- **Reverse / bidirectional direction** (long-COVID liability → autoimmune/hormone)
  as a **shared-liability / directionality** sensitivity for `question:0022` (see
  KD6 for why it does *not* identify `hypothesis:0009`'s conversion arrow).
- **The acceptance gate** (handoff §4) assembled per reported estimate, behind a
  **pre-registration freeze** (WP3.5) of the analysis matrix + HLA decision that
  temporally precedes every unblinded outcome-side result.

**Out of scope (deferred, with reason):**

- **A sex-stratified *outcome* GWAS.** None is published for long-COVID (handoff §1,
  Ruth entity bridge note). Arm B therefore runs sex-specific *exposure* instruments
  against a **mixed-sex** outcome — a **bounded, hypothesis-generating** probe of
  sex-specific exposure architecture, not any form of genotype × sex interaction
  (KD3).
- **Non-European ancestry MR.** All three exposures and the target outcome are
  European; cross-ancestry is a separate, later line.
- **New exposure traits** beyond SLE and SHBG/testosterone (e.g. RA, thyroid
  autoimmunity, estradiol-female). Additive; a Wave-2 concern once the two-arm
  template is proven reportable.
- **`hypothesis:0009`'s post-infectious latent→overt conversion arrow.** No MR
  design here can estimate an *acquired-state → later-disease* transition over a
  5–10-year horizon (KD6). h0009 is retained in `related:` only for the
  shared-liability context, with that limitation stated.
- **Individual-level / ascertainment-structured effects** — permanently with
  `hypothesis:0008` under D-004; MR cannot and does not address them.

## Architecture

Reuse the pilot's proven, isolated Snakemake+conda harness under
`code/workflows/wave1-mr/`. The design generalises the pilot's single hard-coded
pair into a **config-driven analysis matrix** (exposure × outcome-stratum ×
HLA-policy × direction), so no estimator logic is rewritten — only parametrised and
fanned out. New surface: the EUR-outcome acquisition, the Ruth arm, the **per-source
schema-adapter contract** (WP3, F7), the MRlap overlap correction with its own
genome-wide LDSC/HapMap3 infrastructure and scale contract (KD2/KD-scale), and the
matrix/aggregation + pre-registration/acceptance layer.

```
code/workflows/wave1-mr/
├── Snakefile                         MODIFY  fan rules over config.matrix (was one pair);
│                                              WP4-6 rules gated on prereg sentinel
├── config.yaml                       MODIFY  add: eur outcome ladder, ruth strata,
│                                              analysis matrix, mrlap/ldsc/hm3 params,
│                                              hla-inclusive policy, direction flag,
│                                              per-source schema-adapter map
├── envs/
│   ├── r-mr.yaml                     MODIFY  add r-mrlap (pinned commit) + deps
│   ├── r-mr.conda-lock.yml           MODIFY  relock after env change
│   └── ldsc.yaml                     NEW     LDSC / munge infra env, conda-locked
├── schemas/
│   └── source_adapters.yaml          NEW     per-source-family column/scale contract (F7)
├── scripts/
│   ├── acquire_sumstats.py           MODIFY  parametrise over accession/URL list + source family
│   ├── stage_ld.py                   UNCHANGED  1000G-EUR panel staging
│   ├── stage_ldsc_ref.py             NEW     stage eur_w_ld_chr LD scores + HapMap3 SNP list (checksummed)
│   ├── setup_twosamplemr.R           UNCHANGED  pinned-tag install + version sentinel
│   ├── adapt_sumstats.py             NEW     apply source_adapters.yaml → canonical schema; hard-stop on gaps
│   ├── build_instrument.R            MODIFY  emit MHC-excluded AND HLA-inclusive sets; sex-stratum aware
│   ├── prereg_freeze.R               NEW     write immutable prereg sentinel (matrix+HLA+primary, commit+ts)
│   ├── harmonize_estimate.R          MODIFY  loop the matrix; TwoSampleMR 3-estimator
│   ├── overlap_correct.R             NEW     MRlap (LDSC-intercept) correction, native-scale, Arm B
│   ├── reverse_direction.R           NEW     long-COVID → exposure MR (shared-liability sensitivity)
│   └── emit_datapackage_qa.py        MODIFY  matrix-aware manifest + acceptance-gate checklist;
│                                              HARD-STOP if any result artifact predates prereg sentinel
code/workflows/wave1-mr/results → results/wave1-mr/   (gitignored payloads under data/)
entities/datasets/
├── covid19-hgi-longcovid-gwas.md     MODIFY  add EUR-stratum file (LocusZoom Long COVID HGI DFx EUR)
├── ruth-2020-shbg-testosterone-gwas.md  MODIFY  consumed_by += plan:0008; resolve assembly at WP2
├── bentham-2015-sle-gwas.md          MODIFY  consumed_by += plan:0008
├── 1000g-eur-ld-panel.md             MODIFY  consumed_by += plan:0008
├── <finngen-longcovid>.md            NEW?    ONLY if WP0 authorises FinnGen rung 3
└── <eur-ldsc-hm3-reference>.md       NEW     eur_w_ld_chr LD scores + HapMap3 SNP list (MRlap infra)
doc/plans/
└── 2026-07-04-wave1-mr-pilot-result.md  UNCHANGED  pilot go/no-go of record
```

## Key decisions

### Key decision 1: source a EUR-matched outcome within D-005 authorisation, via an explicit ladder; fail closed to mechanics-only

- **Chosen approach:** prefer the **same HGI vehicle** in a EUR distribution before
  any new vehicle. Ladder: **(1)** the **Long COVID HGI** European-ancestry
  summary statistics as distributed via **LocusZoom** (e.g. the public
  "Long COVID HGI — DF4 N1" study download, build GRCh38) or the covid19hg portal /
  GWAS Catalog EUR stratum — this is the D-005-authorised HGI vehicle, just a
  different freeze/channel, so it stays in-authorisation; **(2)** the
  European-ancestry long-COVID analysis in Nature Cardiovascular Research 2025
  (DOI 10.1038/s44161-025-00749-4), **whose data-availability itself points to the
  Long COVID HGI LocusZoom study** — i.e. rung 2 largely resolves to rung 1's
  vehicle; **(3)** a **FinnGen** long-COVID endpoint — a *distinct* vehicle, allowed
  **only** if WP0 authorises it and its form/email-mediated access is confirmed to
  clear the project's third-party-reproducible bar (record the LD-panel isolate
  caveat).
- **Rejected alternative:** keep the European-dominant multi-ancestry
  GCST90454541 as the *primary* outcome. Rejected because bridge assumption 4
  (ancestry-matched panels) makes an unmatched primary inadmissible; the pilot
  already banked this as the hard-stop.
- **Reason:** the acceptance gate's ancestry box cannot be checked without a matched
  European outcome; the ladder retires the hard-stop while keeping the primary within
  the authorised HGI vehicle. If **no** rung yields a reproducible, authorised EUR
  outcome, the primary claim is **demoted to mechanics/robustness-only** (the pilot's
  stated fallback) and the European-dominant run is reported only with an explicit
  ancestry sensitivity — the line does not silently promote an unmatched or
  unauthorised estimate.

### Key decision 2: correct Ruth↔HGI sample overlap with MRlap; report it as a native-scale bias-correction sensitivity, not a drop-in primary

- **Chosen approach:** for Arm B, quantify and **correct** the UK-Biobank overlap
  with **MRlap** (Mounier & Kutalik 2023), which jointly corrects sample overlap,
  weak-instrument, and winner's-curse bias from the cross-trait LDSC intercept.
  MRlap operates on **standardised effects** and its own contract (KD-scale below);
  because that scale differs from the pilot's TwoSampleMR log-OR path, the
  MRlap-corrected effect is reported as a **bias-correction sensitivity in its native
  standardised/observed-scale units**, *beside* the naive TwoSampleMR log-OR IVW —
  the two are **not** presented as interchangeable point estimates, and the naive
  IVW remains the labelled log-OR primary unless a pre-specified, defensible scale
  conversion is registered at WP3.5.
- **Rejected alternative:** (a) UK-Biobank *exclusion* (leave-UKB-out outcome meta) —
  no such long-COVID meta is published; (b) treating MRlap-corrected and naive-IVW as
  one comparable primary-vs-comparator pair on a shared log-OR scale — a scale
  mismatch (KD-scale).
- **Reason:** Ruth is 100% UKB and the HGI outcome pools UKB, so overlap is
  structural and material for Arm B (bridge assumption 3). MRlap is the reproducible,
  open, summary-statistics-only correction, but honest reporting requires respecting
  its effect scale. **Cost carried forward:** MRlap needs *genome-wide* munged
  sumstats for both traits plus an EUR LD-score + HapMap3 reference — not the
  instrument-only streaming the pilot used — so WP2 stages that infrastructure and
  WP5 budgets a genome-wide LDSC pass (a real resource step, validated on real data).
  Arm A (Bentham, largely non-UKB) still gets a shared-cohort check but is expected
  to need no correction.

### KD-scale: MRlap interface + effect-scale contract (freeze before WP5)

- **Input contract:** MRlap consumes canonical-schema sumstats with `SNP` (rsID),
  effect/other alleles, `beta`/`SE` (or `Z`), `chr`/`pos`, and **total sample size
  `N`** (case-control uses **observed-scale analysis with total N**, *not* effective
  N), restricted to the HapMap3 SNP set, with the `eur_w_ld_chr` LD-score reference.
- **Effect scale:** the reportable MRlap effect is in **standardised/observed-scale**
  units; it is **not** relabelled as a log-OR. Any liability- or log-OR-scale
  conversion must be **pre-specified at WP3.5** with its formula and assumptions, or
  it is not done and the native scale stands. The `qa_report` states the scale of
  every Arm B estimate explicitly.
- **Reference + pinning:** LDSC reference = `eur_w_ld_chr`; SNP set = HapMap3
  (both new tracked references, WP2). **MRlap is pinned by git commit** (no tagged
  release exists) in `envs/r-mr.yaml` and recorded in `run_metadata.json`.

### Key decision 3: Arm B is a bounded exposure-architecture probe, not a sex-modification test

- **Chosen approach:** run **male-only** and **female-only** Ruth exposure
  instruments (SHBG, testosterone) against the **mixed-sex** long-COVID outcome, and
  report whether sex-specific genetic predictors of SHBG/testosterone show
  **concordant or discordant** associations with mixed-sex long-COVID liability.
- **Rejected alternative:** framing this as a genotype × sex effect-modification test
  — or even as a *necessary condition* for sex-modification. Rejected: sex
  modification of the exposure→outcome effect can exist even when sex-specific
  instrument estimates look similar after mixing the outcome, and divergent
  male/female estimates can reflect **exposure genetic architecture** rather than any
  effect modification. So the contrast is neither necessary nor sufficient for
  sex-modification.
- **Reason:** the acceptance gate (box 9) forbids asserting sex-modification beyond
  what the run sumstats support. With no sex-stratified outcome, the only honest,
  estimable, reportable claim is a **hypothesis-generating** concordance/discordance
  read on the exposure side.

### Key decision 4: generalise the pilot harness to a config matrix; do not fork a second workflow

- **Chosen approach:** extend `code/workflows/wave1-mr/` in place — the Snakefile
  fans its existing rules over a `config.matrix` of `(exposure, outcome_stratum,
  hla_policy, direction)` cells; estimators, harmonisation, and QA are the pilot's,
  parametrised. A **per-source schema-adapter** (`schemas/source_adapters.yaml`,
  applied by `adapt_sumstats.py`) normalises each source family to one canonical
  schema before harmonisation (F7).
- **Rejected alternative:** a fresh `wave1-mr-full/` workflow. Rejected — it would
  duplicate the proven, locked env and rule bodies and invite drift.
- **Reason:** the pilot's mechanics are the asset; the design's novelty is coverage,
  not plumbing. One workflow, one locked env, config-driven fan-out (the `plan:0003`
  KD4 "params live in config, not rules" pattern the pilot already follows).

### Key decision 5: pre-register the frozen matrix + HLA decision as its own gate that structurally precedes every estimate

- **Chosen approach:** a dedicated **WP3.5 pre-registration freeze** — depending only
  on WP1/WP2/WP3 (staging + matrix construction), **not** on any estimate — writes an
  immutable sentinel (`prereg_freeze.R`) recording the full analysis matrix, the
  a-priori HLA include/exclude decision (primary = extended-MHC-excluded), the primary
  outcome stratum, the overlap-correction plan, and any registered scale conversion,
  stamped with its git commit + timestamp. **WP4/WP5/WP6 rules are gated on this
  sentinel**, and `emit_datapackage_qa.py` **hard-stops if any result artifact
  predates the sentinel** (commit/timestamp check).
- **Rejected alternative:** rely on a parenthetical note that WP7 "opens" the
  pre-registration before unblinding. Rejected — work-package *dependency order* is
  what a scheduler or future agent follows; a note cannot prevent WP4/WP5 running
  first and back-dating the freeze (review F2).
- **Reason:** the acceptance gate is only credible if the choices it audits were
  fixed in advance and *provably* so; making the freeze a dependency and enforcing it
  in QA turns "we promise we pre-registered" into a machine-checked invariant.

### Key decision 6: reverse MR is a shared-liability / directionality sensitivity — it does NOT identify h0009's conversion arrow

- **Chosen approach:** WP6's long-COVID-liability → SLE and → SHBG/testosterone runs
  are reported as **shared-inherited-liability / liability-direction** sensitivities
  for `question:0022` (mediator vs co-traveler) and as context for the
  autoimmunity↔PAIS relationship — **not** as evidence for `hypothesis:0009`.
- **Rejected alternative:** reading reverse MR as directional evidence for h0009
  (the original draft's WP6 framing). Rejected: h0009 is a **post-infectious
  acquired-state → later overt autoimmune conversion** claim over a 5–10-year horizon;
  germline liability to long-COVID is fixed at conception, precedes infection and
  onset, and therefore **cannot** test whether the *acquired* post-infectious state
  causes later autoimmune disease. Reverse MR at best probes shared inherited
  liability and direction under strong assumptions.
- **Reason:** conflating the two would smuggle an unidentified longitudinal claim
  into an acceptance-gated estimate. h0009's conversion proposition needs a
  longitudinal/incident-disease design outside this plan; here it earns only a stated
  limitation.

## Work packages

### WP0 — D-005 authorisation scope gate (blocks all acquisition) — ✅ DISCHARGED by D-006 (2026-07-04)

- **Depends on:** `plan:0007` (done).
- **Entry point:** `core/decisions.md` (D-005), the handoff, this plan's KD1.
- **Outcome (D-006):** EUR outcome via the Long COVID HGI DF4 distribution (LocusZoom
  `gwas/793752`, GRCh38, public) = **same authorised HGI vehicle** → in-scope;
  `eur_w_ld_chr` + HapMap3 = **infrastructure** (like the pilot's 1000G-EUR panel) →
  in-scope; **FinnGen = held** (distinct vehicle, needs its own authorisation +
  reproducibility check). WP1/WP2 may proceed; FinnGen rung 3 is blocked pending a
  new decision. If WP1 finds no EUR-specific HGI stratum, KD1 demotion applies.
- **Definition of done:** each new input classified against D-005: **(a)** EUR
  long-COVID via the Long COVID HGI LocusZoom/portal distribution = the **authorised
  HGI vehicle** → in-scope, record the freeze/channel; **(b)** `eur_w_ld_chr` +
  HapMap3 = analysis **infrastructure**, not a measured-phenotype vehicle → in-scope;
  **(c)** FinnGen = **distinct vehicle** → held until an explicit authorisation
  (D-005 clarification or a new decision) **and** a reproducibility-class check of its
  form/email access are recorded. If any needed input is neither authorised HGI
  vehicle nor pure infrastructure and cannot be authorised, it is dropped and KD1's
  demotion applies. No WP1 acquisition code runs before WP0 is recorded.

### WP1 — Source + stage the EUR-matched outcome (lifts the ancestry hard-stop)

- **Depends on:** WP0.
- **Entry point:** `scripts/acquire_sumstats.py` (parametrised), the KD1 ladder.
- **Definition of done:** a European-ancestry long-COVID outcome staged under
  `data/raw/gwas/` (gitignored) with source URL, distribution/freeze, build, per-file
  SHA-256, row count, and ancestry evidence recorded; the corresponding dataset entity
  created or extended (extend `covid19-hgi-longcovid-gwas` for an HGI EUR
  distribution; a new entity via `/science:find-datasets` only if WP0 authorised a
  distinct vehicle) with `access.verified: true`, enum-safe `verification_method`,
  dated `last_reviewed`, reproducibility class `third-party-reproducible`, and
  `consumed_by += plan:0008`; the **data-access + reproducibility gate rerun and
  passing**. **Case-definition check:** record the EUR distribution's case definition
  and its comparability to the HGI broad/population definition (bridge assumption 6) —
  a study/freeze switch that changes the estimand is itself a sensitivity, not a
  drop-in. **Fail-closed:** if no authorised rung yields a reproducible EUR outcome,
  record the negative result and invoke KD1's demotion.
- **WP1 finding (2026-07-04) — ladder exhausted, NEGATIVE.** No EUR-only Long COVID
  summary-statistics file is publicly downloadable: the HGI DF4 release deposited
  only the four **multi-ancestry** (European-dominant ~85–90%) strata
  (GCST90454540–543 / LocusZoom N2·W2·N1·W1); the paper's European-ancestry analysis
  was an internal sensitivity, not a deposited file. The NatCardioVasc-2025 fallback
  deposits no EUR-only file either (it reuses the multi-ancestry HGI N1 + FinnGen r10).
  See the `covid19-hgi-longcovid-gwas` verification log (2026-07-04, plan:0008 WP1)
  for sources. **The ancestry hard-stop cannot be lifted from a downloadable EUR-only
  HGI file.** This triggers the KD1 fork — accept the demotion (European-dominant
  outcome, ancestry-flagged, non-primary per estimand §d.5) **or** open a new decision
  to authorise FinnGen r10 as a genuine (Finnish-isolate) European outcome. **Held for
  the user's governance choice before WP3+ proceeds.**

### WP2 — Stage Ruth sex-stratified exposures + LDSC/HapMap3 infrastructure

- **Depends on:** WP0 (parallel-safe with WP1).
- **Entry point:** `scripts/acquire_sumstats.py`, `scripts/stage_ldsc_ref.py`,
  `envs/ldsc.yaml`.
- **Definition of done:** required Ruth strata staged — **male-only** and
  **female-only** SHBG (GCST90012109 / GCST90012107) and total testosterone
  (GCST90012113 / GCST90012112), plus sex-combined siblings for cross-check — each
  with SHA-256/build/rows; `ruth-2020-shbg-testosterone-gwas` upgraded to a
  retrieval-grade `verification_method`, `assembly.label` resolved (currently
  UNKNOWN), and `consumed_by += plan:0008`. An **EUR LD-score reference**
  (`eur_w_ld_chr`) **and a HapMap3 SNP list** staged as a new tracked reference
  dataset (checksummed, openly downloadable, build/ancestry recorded, rsID-key policy
  confirmed against the GRCh37-native Ruth and the outcome sumstats); a reproducible
  `ldsc.yaml` env locked. Gate rerun and passing for all inputs.

### WP3 — Generalise the harness to the analysis matrix + per-source schema adapter

- **Depends on:** WP1, WP2 (needs real staged inputs to validate fan-out).
- **Entry point:** `Snakefile`, `config.yaml`, `schemas/source_adapters.yaml`,
  `scripts/adapt_sumstats.py`, `scripts/build_instrument.R`,
  `scripts/harmonize_estimate.R`, `scripts/emit_datapackage_qa.py`.
- **Definition of done:** `config.matrix` enumerates the pre-committed cells;
  `source_adapters.yaml` defines, **keyed by source family** (GWAS Catalog harmonised
  SSF; LocusZoom Long COVID HGI; FinnGen endpoint if authorised; Ruth strata;
  LDSC/HapMap3 reference), the column mapping, allele orientation, build/rsID policy,
  beta/log-OR/OR/Z handling, p-value handling, EAF/palindrome policy, case/control N,
  and **missing-column hard stops**; `adapt_sumstats.py` applies it to a canonical
  schema with a **real row-level smoke test per source family**. `build_instrument.R`
  emits **both** an extended-MHC-excluded and an HLA-inclusive instrument set per
  exposure and is sex-stratum aware; `harmonize_estimate.R` loops the matrix
  producing per-cell IVW/Egger/weighted-median + Egger intercept + per/mean F; the QA
  emitter is matrix-aware. A **dry-run + one real cell** (the pilot pair, re-run
  through the generalised code) reproduces the pilot's numbers bit-for-bit —
  regression guard that the refactor changed no estimator behaviour.

### WP3.5 — Pre-registration freeze (gates WP4–WP6)

- **Depends on:** WP1, WP2, WP3 (staging + matrix construction only — **no
  estimate**).
- **Entry point:** `scripts/prereg_freeze.R`.
- **Definition of done:** an immutable pre-registration sentinel committed —
  recording the full analysis matrix, the a-priori HLA include/exclude decision
  (primary = extended-MHC-excluded), the primary outcome stratum, the
  overlap-correction plan, and any registered MRlap scale conversion — stamped with
  git commit + timestamp. WP4/WP5/WP6 Snakemake rules take this sentinel as an input;
  the QA emitter later hard-stops if any result artifact predates it (KD5).

### WP4 — Arm A: autoimmune → long-COVID, full sensitivity matrix

- **Depends on:** WP3.5, and WP1's EUR outcome (or its documented demotion).
- **Entry point:** the matrix cells for `exposure = bentham-sle`.
- **Definition of done:** primary = SLE (extended-MHC-excluded) → **EUR** broad/
  population long-COVID; sensitivities = HLA-inclusive instrument; broad/strict
  (GCST90454543) and strict-case (GCST90454540/542) outcome strata; the
  European-dominant multi-ancestry run reported *only* as an ancestry sensitivity if
  WP1 demoted. Bentham↔HGI shared-cohort check recorded (expected: negligible). Per
  cell: F-stats, three estimators + concordance/discordance stated, Egger intercept.
  No cell is read as evidence until WP7's gate is assembled for it.

### WP5 — Arm B: sex-hormone → long-COVID, overlap-corrected + sex-specific instruments

- **Depends on:** WP3.5, WP2 (LD scores + HapMap3), WP1's EUR outcome.
- **Entry point:** the matrix cells for `exposure = ruth-shbg / ruth-testosterone`,
  `scripts/overlap_correct.R` (per KD-scale contract).
- **Definition of done:** sex-combined and **sex-specific** (male, female) instrument
  runs for SHBG and total testosterone → long-COVID; **MRlap** overlap+weak-instrument
  correction applied per the KD-scale contract, with the estimated UKB overlap fraction
  recorded and the MRlap effect reported in its **native scale** beside the naive-IVW
  log-OR (labelled, not merged); the male-vs-female instrument concordance/discordance
  reported strictly as the **bounded exposure-architecture** probe of KD3.
  **Scale/resource validation on real data:** the genome-wide LDSC munge + MRlap pass
  is run on the full staged sumstats with **peak memory + wall-clock recorded** in
  `qa_report` — MRlap's genome-wide requirement is exactly the kind of real-input
  resource behaviour green fixtures do not prove.

### WP6 — Reverse / bidirectional direction (shared-liability sensitivity)

- **Depends on:** WP3.5, WP4, WP5 (reuses staged inputs + instruments).
- **Entry point:** `scripts/reverse_direction.R`.
- **Definition of done:** long-COVID liability → SLE and → SHBG/testosterone MR run
  where the outcome-as-exposure instrument is adequately strong (report F;
  **halt-and-note** the direction if long-COVID yields too few strong instruments — a
  FOXP4-dominated long-COVID GWAS may not instrument well, which is itself the
  finding). Interpreted strictly as a **shared-liability / directionality** sensitivity
  for `question:0022` — **not** as evidence for `hypothesis:0009` (KD6), with that
  limitation stated in the write-up.

### WP7 — Acceptance-gate assembly + write-up

- **Depends on:** WP4, WP5, WP6.
- **Entry point:** `scripts/emit_datapackage_qa.py` (gate emission), a results note.
- **Definition of done:** per reported estimate, the handoff §4 nine-box acceptance
  checklist is emitted into `qa_report` with each box explicitly checked or the
  estimate marked not-reportable; the emitter **hard-stops if any result artifact
  predates the WP3.5 pre-registration sentinel** (KD5). A results note records which
  arms/cells cleared the gate and are admissible as `hypothesis:0005`/`0007` /
  `question:0007`/`0013`/`0022` evidence (and explicitly which are *not* — including
  the h0009 conversion limitation, KD6), which are mechanics/robustness-only, and the
  go/no-go for a Wave-2 trait expansion.

## Open questions

1. **Which Long COVID HGI EUR distribution/freeze is the right primary** (WP1 rung 1)
   — DF4 N1 via LocusZoom, a Catalog EUR stratum, or the portal — and does the freeze
   change the case definition vs the pilot's GCST90454541 (bridge assumption 6)?
2. **Does the NatCardioVasc-2025 EUR route resolve to the same HGI LocusZoom study**
   (its data-availability suggests so), making rung 2 a pointer to rung 1 rather than
   a distinct vehicle? Confirm at WP0/WP1.
3. **Does FinnGen clear both authorisation (WP0) and the reproducibility bar** given
   its form/email-mediated results access? If not, it is dropped as an outcome.
4. **Will long-COVID instrument well enough for WP6's reverse direction?** The
   published signal is FOXP4-dominated; the reverse MR may be underpowered — WP6 treats
   that as a reportable negative, not a failure.
5. **MRlap scale conversion:** is any defensible standardised→liability/log-OR
   conversion worth pre-specifying at WP3.5, or does MRlap stand in native units as a
   pure bias-correction sensitivity (KD-scale default)?
6. **LD-score / HapMap3 build+ancestry match** to the GRCh37-native Ruth and the EUR
   outcome — confirm rsID-keyed alignment as WP2's DoD.

## Non-goals

- Reconstructing the D-004-shelved individual-level, ascertainment-structured
  autoimmune × sex × PASC interaction (stays with `hypothesis:0008`).
- Estimating `hypothesis:0009`'s post-infectious latent→overt conversion arrow (KD6).
- Any non-European-ancestry MR.
- New exposure traits beyond SLE and SHBG/testosterone (Wave-2).
- A sex-stratified outcome analysis (no such long-COVID GWAS exists).
- Clinical, diagnostic, or treatment-effect interpretation — the estimate is a
  germline-liability IV effect only (estimand §c).

## Acceptance criteria

An MR estimate from this plan is reportable as evidence toward the target
hypotheses/questions **only if** its per-estimate `qa_report` checklist (handoff §4)
is fully checked:

- [ ] WP0 authorisation recorded: the outcome is the D-005-authorised HGI vehicle (or
      an explicitly authorised addition), references are infrastructure, and any
      FinnGen use is separately authorised + reproducibility-checked (F1).
- [ ] All consumed dataset entities complete + access-verified + reproducibility
      class recorded + `consumed_by` includes `plan:0008` (§4 box 1, F6);
      **ancestry-matched EUR outcome used**, or the mismatch flagged and the estimate
      **not** treated as primary (KD1 demotion).
- [ ] Instrument F-statistics reported; no exposure relies solely on weak
      instruments (§3.1).
- [ ] IVW + MR-Egger + weighted-median all run; concordance/discordance stated
      explicitly (§3.2).
- [ ] Sample overlap quantified; **Arm B MRlap-corrected and reported in its labelled
      native scale** beside the naive log-OR IVW (KD-scale), Arm A shared-cohort check
      recorded (§3.3).
- [ ] A-priori HLA include/exclude decision fixed in the **WP3.5 pre-registration
      sentinel before any estimate**, and QA confirms no result predates it (§3.4,
      KD5); HLA-inclusive reported as sensitivity.
- [ ] All panels ancestry-matched, or mismatch flagged and not primary (§3.5).
- [ ] HGI case-definition stratum stated per estimate; broad/population primary,
      broad/strict + strict-case as sensitivities, never silently mixed (§3.6).
- [ ] Effect **scale** stated for every estimate (log-OR for TwoSampleMR;
      standardised/observed for MRlap) — no cross-scale comparison presented as
      like-for-like (KD-scale).
- [ ] Stated as a germline-liability IV effect, explicitly **not** as closing the
      D-004 gap (estimand §c), and reverse-direction results explicitly **not** read
      as h0009 conversion evidence (KD6).
- [ ] Any sex statement uses only Ruth sex-stratified exposure strata and is scoped to
      the **bounded exposure-architecture** read (§4 box 9, KD3) — no
      sex-modification/interaction claim.
- [ ] Full reproducible bundle present (matrix-aware `datapackage.json` with entity
      cross-refs + provenance DAG, per-cell `qa_report.{json,md}`, `run_metadata.json`
      with seeds/versions/SHA-256s + pinned MRlap commit, updated `r-mr.conda-lock.yml`
      + `ldsc.yaml` lock, `source_adapters.yaml`); no data payload committed.

If any box cannot be checked for a given estimate, that estimate is not reportable
as hypothesis/question evidence — this is the gate, not a post-hoc checklist.
