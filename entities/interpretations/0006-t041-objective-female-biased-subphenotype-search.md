---
id: interpretation:0006-t041-objective-female-biased-subphenotype-search
type: interpretation
title: 't041 objective female-biased subphenotype search: predominantly null/reinforcing
  across four objective domains, with one weak testosterone-conditioned immune exception'
status: active
source_refs: &id001
- paper:Aid2025
- paper:Shahbaz2025
- paper:Silva2024
- paper:Walitt2024
- paper:Klein2023
- paper:Rojas2022
- paper:Eldokla2022
- paper:Kwan2022
- paper:Wang2026c
- paper:Appelman2024
related:
- proposition:0013-immune-domain-partial-hormone-mediated-objective-exception
- interpretation:0003-t018-subphenotype-sex-reproductive-stage
- question:0007-mechanism-of-female-predominance-in-pais
- proposition:0009-dysautonomia-female-skew-is-baseline-carried-not-pais-amplified
- proposition:0010-cognitive-female-excess-is-self-report-only-absent-in-objective-testing
- proposition:0005-menopause-pais-symptom-overlap-is-a-measurement-process
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- task:t041
created: '2026-06-23'
updated: '2026-06-23'
input: *id001
prior_interpretations:
- interpretation:0003-t018-subphenotype-sex-reproductive-stage
relations:
- predicate: "sci:amends"
  target: "interpretation:0003-t018-subphenotype-sex-reproductive-stage"
---
<!--
Conclusion chain:
- sci:amends interpretation:0003 — t041 runs the objective-endpoint, ascertainment-symmetric test
  that interpretation:0003 named as "the single most efficient discriminator" and explicitly held
  open in its Data Quality Checks ("until an objective-endpoint, ascertainment-symmetric design tests
  a female-biased domain"). It narrows/qualifies that interpretation's measurement-channel reading;
  it does not replace it.
-->

# Interpretation: t041 — objective female-biased subphenotype search

> **Mode: conceptual.** No new computation. This is a targeted four-domain literature sweep
> (autoantibody/autoimmune serology; small-fiber/peripheral nerve; immune/molecular biomarker;
> autonomic-function/exercise physiology), each probed with one rubric: *is there an
> **objectively-measured**, **sex-symmetrically-ascertained** PAIS endpoint that is **female-biased**,
> and if so is it PAIS-**amplified** or **baseline-carried**?* It runs the discriminator
> `interpretation:0003` named as the most efficient test between the **ascertainment** reading and a
> **biological sex-amplification** reading of the PAIS female excess. All findings are
> `literature_evidence`. The three immune papers that back the minted exception (Aid2025, Shahbaz2025,
> Silva2024) and the corpus papers leaned on for the null/reinforcing domains (Klein2023, Rojas2022,
> Walitt2024, Eldokla2022, Kwan2022, Wang2026c, Appelman2024) carry entity backing and are listed in
> `source_refs`; a handful of web-only studies are cited inline and are *not* in `source_refs`.

## Verdict

**Verdict:** [~] Mixed — **predominantly null/reinforcing**, with **one weak, testosterone-conditioned
exception**. Three of four objectively-measured domains return **no** female-biased,
ascertainment-symmetric endpoint and therefore **reinforce** the measurement-channel/ascertainment
reading (autoantibody **NULL**; autonomic-function/exercise **NULL**; small-fiber/peripheral-nerve a
**gap**, never sex-stratified, with a baseline that runs *against* a female deficit). The
**immune/inflammatory domain is the exception**: a sex-symmetric objective endpoint — persistent
post-acute pro-inflammatory activation — is **female-amplified** (LC-females vs recovered-females,
with a within-recovered sex-null as the interaction control), **disputing the *strong universal*
form** of "every objective domain is sex-null or male-biased." But that exception is
**substantially testosterone-conditioned** (categorical sex non-significant after adjustment in
Silva2024) and reverse-causation-ambiguous, so it points to a **hormone-linked biological channel**,
not a clean categorical-sex amplification. Net: the ascertainment reading survives as the *leading*
structure, now bounded by a hormone-linked immune exception rather than held as a universal.

## Findings Summary

Four domains, one rubric. "Sex direction" is of the *objective* endpoint under
sex-symmetric ascertainment.

| Objective domain | Best objective endpoint | Sex direction | Amplified vs baseline-carried | Verdict |
|---|---|---|---|---|
| **Autoantibody / autoimmune serology** | REAP/exoproteome & GPCR-fAAb screens (Klein2023, Rojas2022, Wang2021; LC GPCR-fAAb bioassay) | **NULL** wherever sex is actually contrasted (Rojas2022: sex moved anti-viral Ab but **not** autoAb in the same assay) | the one female-biased case (post-COVID thyroid TPOAb OR≈2.0) = **baseline-carried** (= ordinary ~2:1 female TPO-Ab), no infection×sex term | **NULL — reinforces** |
| **Small-fiber / peripheral nerve** | skin-biopsy IENFD, corneal confocal, QSART (Oaklander2022, Azcue2025, Novak2022) | **never sex-stratified** (sex is a matching/descriptive var only); cohorts 75–90% female by **referral** | n/a; baseline distal-leg IENFD is **female-higher**, so a fixed threshold makes SFN *harder* to reach in women — runs against a female deficit | **GAP — neither supplies nor contradicts** |
| **Immune / molecular biomarker** | within-sex LC-vs-recovered inflammatory activation (Aid2025, Shahbaz2025, Silva2024) | **female-biased** (LC-F vs recovered-F > male contrast; within-recovered sex-null) | **appears amplified** (within-recovered null argues against simple baseline-carry) **but** substantially **testosterone-conditioned** (Silva2024) | **WEAK POSITIVE — disputes strong universal** |
| **Autonomic / exercise physiology** | 2-day CPET VO₂-drop, HRV recovery, tilt-confirmed POTS (Kwan2022, Eldokla2022, Wang2026c, van Campen, PMC10070276) | **NULL** on objective magnitude (CPET decrement sex-symmetric; HRV-recovery sex-null); POTS female-skew is **referral + baseline** | **baseline-carried** (POTS ~5:1 female regardless of trigger); no infection×sex above baseline | **NULL — reinforces `proposition:0009`** |

**The single positive, stated precisely.** In the within-sex case-control design (the cleanest
available contrast for separating amplification from baseline female immunity), long-COVID females
show **more** persistent
inflammatory activation than recovered females than the male contrast does, and Aid2025 reports **no
sex difference within the recovered group** — evidence against detectable baseline-carry in that
cohort, but underpowered for excluding all baseline-carry explanations. Shahbaz2025 corroborates
with directly-measured cytokines in a long-COVID cohort meeting CCC ME/CFS criteria. This is a
genuine objective, sex-symmetric, female-biased PAIS endpoint — the first the project has found —
and it is minted as `proposition:0013`.

**Why it is not a clean positive.** Silva2024 (the best-powered cohort) shows the operative variable
is **testosterone-associated/conditioned**: lower-testosterone females look immunologically like
LC-males, and after adjusting for testosterone, **sex designation is no longer significant**. So the
exception is better
read as a **low-testosterone / HPG-dysregulation** endpoint that is only *partly* sex-linked — a
hormone-linked channel, consistent with `hypothesis:0005`, not an ascertainment artifact but also
not a categorical-sex amplification. Walitt2024 adds that the immune biology is sex-**dimorphic**
(female B-cell vs male T-cell/NF-κB enrichment, <5% gene overlap), not simply "more disease in
females."

## Evidence Quality

- **All literature-derived**, heterogeneous case definitions, predominantly cross-sectional. The
  strongest designs are the **within-sex case-control** immune studies (Aid2025, Shahbaz2025) and the
  controlled EHR dysautonomia line (Kwan2022).
- **Ascertainment symmetry actually holds in three of four domains** (lab assays / instrument
  readouts applied to both sexes) — autoantibody serology, immune biomarkers, and objective
  autonomic/exercise measures are genuinely symmetric, which is what makes their null results
  *informative* nulls rather than ascertainment artifacts. The small-fiber domain is the exception:
  its female composition is **referral-driven**, not a symmetric finding.
- **Reverse causation is the throughline confound on the one positive.** The female-amplified
  inflammation and the low female testosterone are both cross-sectional; chronic inflammation can
  suppress the HPG axis, so the direction of the testosterone–inflammation relationship is unresolved
  without a pre-infection baseline.
- **The classic objective ME/CFS endpoints are gaps, not nulls.** NK-cell cytotoxicity and
  muscle-OXPHOS day-2 worsening (Appelman2024) are objective and well-characterised but **never
  sex-stratified** — the highest-value untested endpoints.

## Data Quality Checks

No microdata involved. One structural concern carried from `interpretation:0003` is now **partly
resolved**: that interpretation flagged (as `methodological`) that "female-excess subphenotype cells
and self-report measurement channels are confounded… treat the measurement-channel reading as leading
but not closed until an objective-endpoint, ascertainment-symmetric design tests a female-biased
domain." t041 *is* that test. Result: in three symmetric domains the objective endpoint is sex-null
(confound holds — female excess is self-report-channeled there), and in the fourth (immune) the
  symmetric objective endpoint **is** female-biased but **testosterone-conditioned**. So the domain↔channel
  confound is no longer total: there exists at least one objective, symmetric, female-biased endpoint,
  and it is read as a *hormone* channel rather than a self-report channel.

## Proposition-Level Updates

- **`proposition:0013` (minted).** *The immune/inflammatory domain is a partial, testosterone-conditioned
  objective exception to the self-report-channeled female PAIS excess.* `empirical_regularity`,
  three independent-cohort lines (`evidence-line:0033` Aid2025 / `0034` Shahbaz2025 / `0035`
  Silva2024); not `fragile-single-line`. This is the t041 deliverable.
- **`proposition:0009` (dysautonomia baseline-carried) — reinforced.** The autonomic/exercise sweep
  re-confirms it from the *objective* side: 2-day CPET VO₂-decrement is sex-symmetric in magnitude,
  HRV-recovery is sex-null (PMC10070276), and tilt-confirmed POTS female-skew equals the
  trigger-independent ~5:1 baseline. No new line minted (0009 already carries three independent
  lines); recorded here as objective-side corroboration.
- **`proposition:0010` (cognitive self-report-only) — unaffected and consistent.** The cognitive
  domain was not re-probed; the immune exception is a different domain and does not bear on the
  objective-cognition sex-null.
- **`proposition:0005` (menopause/PAIS overlap = measurement process) — *not* strengthened.** t041's
  framing anticipated that "continued absence [of an objective female-biased domain] strengthens
  prop:0005." Because a hormone-linked exception was found, t041 does **not** strengthen the
  pure-measurement-process reading; if anything it surfaces a biological (hormone) channel alongside
  the ascertainment channel. prop:0005 stands on its own evidence, un-amended.
- **The held-back measurement-channel umbrella — do NOT mint in strong universal form.**
  `interpretation:0003` held an umbrella `empirical_regularity` ("the female excess tracks a
  measurement-channel axis"). t041 establishes the *strong* universal form ("every objective domain
  is sex-null or male-biased") is **false** (immune exception). If the umbrella is ever minted, it
  must be in the **bounded** form: predominantly self-report-channeled, with a hormone-linked immune
  exception (`proposition:0013`).

## Question-Level Implications

**`question:0007` (mechanism of female predominance) — the ascertainment branch is bounded, the
hormone branch gains weight.** `interpretation:0003` raised the weight on the
ascertainment/measurement-process branch relative to estrogen-amplification. t041 refines this: the
ascertainment reading is **correct for three of four objective domains** but is **not universal** —
the immune domain carries a genuine objective female-amplified signal, and that signal is
**testosterone-conditioned**. So the residual non-ascertainment mechanism is most credibly a
**gonadal-steroid (HPG-axis) channel**, not an estrogen-amplification-of-symptom-report channel. This
strengthens the link from `question:0007` to `hypothesis:0005` and to the testosterone work
(Silva2024, t032/t036).

**`hypothesis:0005` (reproductive-stage / immune-homeostatic margin) — the immune exception is its
best objective foothold.** The one objective domain that breaks the self-report pattern is also the
one that is conditioned on gonadal-steroid status — exactly the homeostatic-margin mechanism
`hypothesis:0005` posits. Weak support, hormone-linked and reverse-causation-ambiguous, but it is
the first objective (non-self-report) evidence consistent with the bundle.

## Evidence vs. Open Questions

- **"Is any objectively-measured PAIS subphenotype female-biased?" (the New Question raised in
  `interpretation:0003`) — ANSWERED: yes, one (immune/inflammatory), and it is testosterone-conditioned.** The
  answer is qualified, not clean, but the question is no longer open.
- **Cross-trigger generality** — only partly addressed: Shahbaz2025 extends the immune exception to
  a CCC ME/CFS phenotype within long COVID, not to an independent non-COVID ME/CFS cohort;
  the autonomic null spans LC and ME/CFS; the autoantibody null spans LC and ME/CFS (with QFS only
  ~52% female and uninformative). Dengue/Q-fever/PTLDS remain near-empty at the objective×sex level.

## New Questions Raised

- **Is the female-amplified immune activation independent of testosterone in a pre-infection-baseline
  design?** (P2, empirical) The decisive next test: does the LC-vs-recovered inflammatory interaction
  remain female-larger *after* conditioning on (pre-infection) testosterone? Needs a longitudinal
  cohort with pre-infection hormones — the same design class flagged for t013/t036.
- **Is NK-cell cytotoxicity (the classic objective ME/CFS deficit) sex-biased?** (P2, empirical) The
  single highest-value *untested* objective endpoint — currently a gap, not a null. A sex-stratified
  re-analysis of an existing NK-cytotoxicity dataset would be cheap and discriminating.
- **Is muscle-OXPHOS day-2 worsening (Appelman2024) sex-biased?** (P3, empirical) The cleanest
  objective long-COVID lesion, never sex-stratified.
- **Sex-stratified re-analysis of an objective small-fiber (IENFD) dataset against sex-specific
  norms.** (P3, methodological) The small-fiber domain is a pure gap; the meta-analytic IENFD norms
  supply the female-higher baseline reference needed to test for a *deficit* rather than a raw count.

## Limitations & Residual Uncertainty

- The one positive rests on **secondary, within-sex sex-stratifications** in cross-sectional cohorts;
  authors themselves flag the need for larger confirmation.
- **Reverse causation** between low testosterone and high inflammation is unresolved and is the
  central threat to reading the immune exception as a sex-*amplification* rather than a downstream
  consequence.
- Three of the four "nulls" are **measured sex-nulls** (informative); the small-fiber one is a
  **gap** (uninformative) and should not be read as a sex-null.
- The sweep is COVID/ME-CFS-weighted; other triggers contribute almost nothing at the objective×sex
  level.

## Updated Priorities

**DONE (2026-06-23, t041):** ran the four-domain objective discriminator; minted `proposition:0013`
(immune partial testosterone-conditioned exception; lines `evidence-line:0033`/`0034`/`0035`, three
independent cohorts, not fragile); recorded autoantibody + autonomic/exercise as measured sex-nulls
that **reinforce** the ascertainment reading and `proposition:0009`; recorded small-fiber as a gap.
Amends `interpretation:0003` (resolves its held-open objective-endpoint discriminator) and bounds the
held-back measurement-channel umbrella to its non-universal form.

- **Do NOT mint** the measurement-channel umbrella in its strong universal form — t041 falsifies it.
  A bounded version may be minted later if needed.
- **Highest-value follow-ups are the two untested objective ME/CFS endpoints** (NK cytotoxicity;
  muscle-OXPHOS day-2 worsening) — both are gaps a sex-stratified re-analysis could close cheaply.
- **The decisive mechanistic test** for the immune exception is a pre-infection-baseline,
  testosterone-conditioned LC-vs-recovered interaction — overlaps the hormone-triangulation tasks
  (t036) and the deferred within-cohort pre-infection design (t013).
