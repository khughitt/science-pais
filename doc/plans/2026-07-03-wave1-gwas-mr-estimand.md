---
title: 'Wave-1 GWAS/MR estimand + bridge assumptions (pre-discovery)'
status: active
created: '2026-07-03'
---

# Wave-1 GWAS/MR estimand + bridge assumptions

**Purpose.** This note fixes, *before* dataset discovery (Task 7), exactly what
the Wave-1 open GWAS / Mendelian-randomization (MR) line does and does not claim,
so that discovery is scoped to the right candidates and so that Task 8's handoff
notes can cite a stable estimand contract and bridge-assumption set. It is written
in response to the design's §4 Wave-1 estimand rewrite
(`doc/plans/2026-07-03-data-catalog-expansion-design.md`) and to decision **D-004**
(`core/decisions.md`), which shelved the gated-EHR autoimmune × sex × PASC line as
infeasible under the project's third-party-reproducibility standard.

**Framing constraint (standing project instruction).** PAIS mechanism and causality
claims are contested and evidence-immature. Everything below is stated as a *causal
estimand under explicit identifying assumptions*, not as an established mechanism.
MR on public summary statistics is a **reproducible open substitute** for one facet
of the shelved work — it answers a **narrower, different question**, and it does
**not** replace the shelved EHR estimand. That distinction is load-bearing; the
rest of this note enforces it.

---

## (a) The substitute estimand

The Wave-1 target estimand is:

> The **causal effect of genetic liability to an autoimmune disease** (e.g. an
> autoimmune-disease GWAS such as SLE, RA, thyroid autoimmunity, or a broad
> autoimmune phenotype) — **and, separately, the causal effect of a sex-hormone
> biomarker** (e.g. SHBG, bioavailable/total testosterone, estradiol) — **on a PAIS
> outcome** (long-COVID / post-acute-infection phenotype: liability to a diagnosed
> long-COVID case definition, or a component such as fatigue/PEM where a GWAS
> exists), estimated by **two-sample Mendelian randomization** under
> instrumental-variable (IV) assumptions.

Concretely:

- **Exposures (instrumented).** (i) Genetic liability to autoimmune disease,
  instrumented by genome-wide-significant SNPs from an autoimmune-disease GWAS;
  (ii) a sex-hormone biomarker (SHBG, testosterone, estradiol), instrumented by
  SNPs from a hormone-biomarker GWAS. These map to the capability-vocabulary tokens
  `analysis_role: mr_exposure` with `trait: autoimmune-disease` and
  `trait: sex-hormone-biomarker` respectively
  (`doc/plans/2026-07-03-capability-vocabulary.md`).
- **Outcome.** A PAIS-outcome GWAS (`analysis_role: mr_outcome`,
  `trait: long-covid`), e.g. COVID-19 Host Genetics Initiative (HGI) long-COVID
  summary statistics, or a fatigue/ME-CFS GWAS.
- **Estimator.** Inverse-variance-weighted (IVW) two-sample MR as the primary
  estimate, with the sensitivity analyses named in (d).
- **Interpretation.** The estimate is the effect of *lifelong germline-predicted*
  exposure — a genetic-liability contrast, **not** the effect of clinically
  diagnosing, treating, or acquiring the autoimmune disease at a given age. It is a
  population-average IV effect (LATE/genetic-liability-scale), on the liability
  scale for binary traits.

This is deliberately *narrower* than a total observational autoimmune → PASC
association: it isolates the germline-instrumented component under IV assumptions.

---

## (b) What this estimand answers

Two things the shelved observational EHR line could not cleanly deliver, and which
germline instruments *can* address:

1. **Reverse-causation direction.** Germline genotype is fixed at conception and is
   not caused by the PAIS outcome, so a forward MR (autoimmune liability →
   PAIS outcome) is not confounded by reverse causation in the way an
   observational autoimmune-diagnosis → PASC association is. Bidirectional MR
   (also running PAIS-liability → autoimmune/hormone) can further probe direction.
   This directly serves the mediator-vs-co-traveler question
   (`question:0022-immune-state-displacement-mediator-vs-co-traveler`) and the
   COVID-specific-vs-baseline framing
   (`question:0021-male-vascular-reversal-covid-specific-vs-baseline-carryover`).

2. **Sex-effect modification — *only where sex-stratified or interaction summary
   statistics exist*.** Whether the genetic effect of autoimmune liability or of a
   sex-hormone biomarker on the PAIS outcome differs by sex is testable **only** by
   running MR within sex-stratified summary statistics (male-only vs female-only
   sumstats on exposure and/or outcome) or by using genotype × sex interaction
   sumstats. Absent those, sex modification is **not** estimable from public
   sumstats and must not be asserted. This is the hinge for
   `question:0007-mechanism-of-female-predominance-in-pais`,
   `question:0013-reproductive-stage-failed-immune-recovery-after-infection`, and the
   male-vascular-signal cluster
   (`question:0019`/`question:0020`/`question:0021`), and it is what makes the
   discovery filter below mandatory rather than optional.

A confirmed MR result here is evidence *toward* the causal readings in
`hypothesis:0005` (reproductive-stage immune-homeostatic margin),
`hypothesis:0007` (autoimmune small-fiber-neuropathy substrate), and
`hypothesis:0009` (post-infectious immune-set-point shift → autoimmune conversion),
**subject to the bridge assumptions in (d)**.

> **Narrowed by `plan:0008` KD6 (2026-07-04).** Two-sample MR on germline liability —
> in *either* direction — does **not** identify `hypothesis:0009`'s *post-infectious
> acquired-state → later autoimmune conversion* arrow (genotype is fixed
> pre-infection; at best MR probes shared inherited liability). For the Wave-1
> design, h0009 is **shared-liability / directionality context only**, not an
> admissible MR-evidence target. `hypothesis:0005` and `hypothesis:0007` are
> unaffected. See `plan:0008` KD6.

---

## (c) What this estimand does NOT replace

It does **not** reconstitute the shelved estimand. Per **D-004**, the
autoimmune-diathesis × sex × PASC line required a **population-scale,
individual-level EHR interaction** — an effect-modifier estimate structured by real
disease **prevalence**, healthcare **utilisation**, and diagnostic
**ascertainment** — which is a categorically access-gated, non-downloadable data
class (N3C/OpenSAFELY) and therefore not third-party-reproducible. MR on public
summary statistics answers a *different* causal question (germline-liability IV
effect) and:

- does **not** estimate the individual-level, ascertainment-structured interaction
  among diagnosed patients;
- does **not** recover prevalence-, utilisation-, or coding-driven differential
  measurement effects;
- does **not** speak to the effect of *acquiring or being diagnosed with* an
  autoimmune disease (as opposed to lifelong genetic liability).

That population-scale prevalence/utilisation/ascertainment residue stays with
**`hypothesis:0008`** (measurement-channel and ascertainment bias), exactly as
banked in D-004. Wave-1 therefore keeps **causal-MR** targets
(`analysis_role: mr_exposure`/`mr_outcome`) **separate** from **descriptive
coverage** targets — a sex-stratified descriptive cohort and an MR-usable GWAS must
not silently satisfy the same causal target
(`doc/plans/2026-07-03-capability-vocabulary.md`). MR does not close the gap D-004
shelved; it opens an adjacent, reproducible one.

---

## (d) Bridge assumptions

An MR result counts as evidence for `hypothesis:0005`/`hypothesis:0007` (and, as
shared-liability context only, `hypothesis:0009` — see the KD6 note in (b)) or for
`question:0007`/`question:0013`/`question:0019`–
`question:0022` **only if all of the following are stated and defended in the
candidate's handoff note** (§4a fit/limitation paragraph). Failing one does not
merely weaken the estimate — it can invalidate the causal reading, so each is a gate,
not a caveat.

1. **Instrument relevance (IV1).** Instruments are genome-wide significant for the
   exposure with adequate strength (report per-instrument and mean **F-statistic**;
   flag weak-instrument bias, which in two-sample MR biases toward the null).
   State the variance explained where available.

2. **No horizontal pleiotropy (IV2/exclusion restriction).** Instruments must affect
   the PAIS outcome *only through* the exposure. This is untestable directly, so it
   is supported by **named sensitivity analyses that must be pre-committed and
   reported**: **MR-Egger** (intercept as a directional-pleiotropy test; slope as a
   pleiotropy-robust estimate) and **weighted-median** (consistent if <50% of weight
   is invalid). Concordance across IVW / MR-Egger / weighted-median is the minimum
   robustness bar; discordance is reported, not hidden.

3. **No uncorrected sample overlap.** Exposure and outcome GWAS should be
   non-overlapping samples, or overlap must be quantified and corrected (overlap
   biases two-sample MR toward the confounded observational association). Record the
   contributing cohorts for both GWAS and whether overlap exists; where the outcome
   is COVID-19 HGI, check for shared biobanks with the exposure GWAS.

4. **Ancestry-matched panels.** Exposure GWAS, outcome GWAS, and any LD reference
   panel must be **ancestry-matched** (e.g. all European, or all East Asian) to
   avoid LD-mismatch and population-stratification bias. Cross-ancestry MR is
   flagged and not treated as primary. Record the ancestry of every panel.

5. **An *a priori* HLA include/exclude decision.** The autoimmune signal is
   **HLA-dense**; the MHC region carries strong, pleiotropic, long-range-LD
   associations that can dominate an autoimmune instrument. The include-or-exclude-HLA
   decision must be made **before** seeing outcome results and stated explicitly
   (e.g. "primary analysis excludes the extended MHC chr6:25–34 Mb; HLA-inclusive
   run reported as sensitivity"). Post-hoc HLA handling is a researcher-degrees-of-freedom
   hole and is disallowed.

6. **PAIS case-definition comparability across the outcome GWAS.** The outcome GWAS's
   PAIS phenotype definition (WHO-LC vs CDC-LC; strict vs broad long-COVID; ME/CFS
   Fukuda/CCC/ICC; fatigue-only) must be recorded and its comparability to the
   hypothesis's target phenotype assessed. Case-definition heterogeneity is a primary
   PAIS confound (project standing note): an MR estimate is only as interpretable as
   the outcome phenotype is well-defined, and mixing definitions across exposure
   assumptions or across sensitivity GWAS is flagged.

For the **sex-hormone-biomarker** exposure specifically, note that SHBG/testosterone
GWAS are frequently sex-specific in their genetic architecture; the sex-stratified
sumstats requirement in (b) and in the discovery filter applies with particular
force there.

---

## Discovery filter (scopes Task 7)

Beyond the generic MR-usability requirements (public genome-wide summary statistics,
declared build/ancestry, resolvable accession), Wave-1 discovery must apply this
**gating filter for the sex-modification targets**:

> **A candidate may serve a sex-effect-modification target only if it exposes — or
> makes it possible to derive — sex-stratified (male-only / female-only) or genotype
> × sex interaction summary statistics for the relevant exposure or outcome. A
> sex-combined GWAS, or a dataset that merely reports sex-balanced descriptive
> statistics, does NOT qualify and must not be annotated `stratification: sex` for a
> causal-MR target.**

Operationally, per candidate for a sex target, discovery records: (i) whether
sex-stratified/interaction sumstats are published or derivable and where; (ii) the
ancestry of each panel; (iii) sample-overlap risk against the intended outcome GWAS;
and (iv) the outcome-GWAS case definition. Candidates lacking sex-stratified or
interaction sumstats may still serve the **sex-agnostic** MR estimand in (a) and the
reverse-causation direction in (b), but they are explicitly **out of scope** for the
sex-modification questions (`question:0007`/`question:0013`/`question:0019`–
`question:0022`) and must be catalogued as such — a truthful `stratification`
annotation, per the capability-vocabulary rule that `stratification: sex` is a truth
claim, not a wish.
