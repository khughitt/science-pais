---
id: interpretation:0033-t079-bc5-pasc-case-definition-lock
type: interpretation
title: "t079/BC-5: PASC case-definition lock — coded U09.9/clinic primary, ML phenotype demoted to flagged sensitivity (its top feature IS the confound), survey index not EHR-computable; every EHR outcome is utilization-gated"
status: active
source_refs:
  - paper:Hill2022
  - paper:Pfaff2022
  - paper:Thaweethai2023
  - cite:WalkerLongCOVID2021
  - cite:Henderson2024
related:
  - task:t079
  - plan:0005-autoimmune-diathesis-sex-modifier-pais-analysis-plan
  - plan:0006-n3c-synthetic-prototype-autoimmune-sex-pais-pipeline
  - interpretation:0031-t079-n3c-vs-opensafely-vehicle-decision
  - interpretation:0032-t079-bc3-autoimmune-stratum-granularity
  - dataset:n3c-recover-longcovid
  - dataset:opensafely-longcovid
  - dataset:recover-adult
  - hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
created: "2026-07-01"
updated: "2026-07-01"
input: "BC-5 case-definition audit (2026-07-01): two paper-researcher passes (Pfaff2022 N3C ML phenotype, Thaweethai2023 RECOVER survey PASC index) + one read-only OpenSAFELY non-coded-phenotype web audit. No participant-level data accessed."
prior_interpretations:
  - interpretation:0031-t079-n3c-vs-opensafely-vehicle-decision
relations: []
---

<!-- Mode: CONCEPTUAL / FEASIBILITY TRIAGE (BC-5 of plan:0005 / task:t079). Outcome-definition
lock only; no participant-level data, no phenotype execution. -->

# Interpretation: t079/BC-5 — PASC case-definition lock

## Verdict

**Lock the primary PASC outcome to a *coded, duration-anchored* computable phenotype in each
vehicle, and demote the "most mature" machine-learned phenotype to a flagged sensitivity
analysis — because its construction is dominated by the utilisation axis this study must keep
clean, with an untested sex-specific error profile on top.** The audit produced one decisive,
slightly counter-intuitive result: the N3C ML computable phenotype (`paper:Pfaff2022`) has
**outpatient visit rate as its single top feature** — so the outcome is, by construction, a
structural function of utilisation, exactly the h0008 differential-ascertainment axis under study
— **and** carries an **untested sex-specific misclassification risk**: 75% of its non-hospitalised
training positives were female, sex was deliberately excluded as a feature, and no sex-stratified
performance was reported, so sex-correlated features can leak an implicit female signal that is
*uncharacterised rather than demonstrably corrected*. (The utilisation argument is the decisive
one and stands alone; the sex concern is a documented risk, not a verified bias — it would take a
by-sex score-distribution / feature-contribution check to confirm.) The
survey-based RECOVER PASC index (`paper:Thaweethai2023`) is **not EHR-computable at all**. The
honest meta-finding: **no EHR PASC outcome is ascertainment-clean** — every one is utilisation-gated
on the outcome side — so BC-5 does not deliver a clean endpoint; it locks the *least-baked-in*
one as primary and pushes the ascertainment defence into the design (utilisation adjustment,
negative-control outcome, E-value, bracketing sensitivity pairs). This also **qualifies**
`interpretation:0031`'s hope that a broad OpenSAFELY phenotype makes it a clean arbiter — it does
not (see rule #4 update).

## Findings Summary — the N3C outcome ladder (primary vehicle)

| Definition | EHR-computable in N3C? | Ascertainment structure | BC-5 role |
|---|---|---|---|
| **U09.9-or-LC-clinic coded** (Hill2022) | **Yes** — ICD-10 U09.9 + long-COVID-specialty-clinic visit | Utilisation-correlated **at the ascertainment step** (needs a coded visit), but utilisation/sex are **not definitional inputs** → adjustable | **PRIMARY** |
| **Pfaff2022 ML phenotype** (3 XGBoost models, 924 OMOP features, prob. score, thr 0.45; AUROC 0.92 int / 0.82 ext) | **Yes** — fully from `condition_occurrence`/`drug_exposure`/`visit_occurrence`/`measurement`/`person`; code `NCTraCSIDSci/n3c-longcovid` | **Utilisation baked into the definition** (outpatient visit rate = top Shapley feature) **+ untested sex-specific error** (75% female positives, sex excluded, no by-sex performance reported → sex-proxy leakage *risk*); site overfit (0.92→0.82); respiratory bias (2/3 training clinics pulmonary) | **FLAGGED SENSITIVITY** — never primary here |
| **RECOVER PASC index** (`Thaweethai2023`; 13 PRO items, smell/taste 8 + PEM 7, thr ≥12/~35) | **No** — every item is patient-reported survey data; authors explicitly contrast it with EHR | N/A (survey) | **Construct gold standard only** — via the `dataset:recover-adult` adjunct's linked PRO, not an N3C endpoint |

**Why coded-primary despite lower sensitivity.** The study's whole threat model is differential
ascertainment by utilisation and sex. The coded definition's utilisation-dependence lives at the
*ascertainment* step, where the plan's existing defences (individual-utilisation adjustment,
negative-control outcome) can act on it. The ML phenotype's utilisation-dependence is *in the
definition itself* — its top predictor is a covariate we must keep clean — which cannot be
adjusted out without collider/over-adjustment pathology. So the "more sensitive, more mature"
phenotype is the **worse** primary for this specific estimand. Divergence between the
coded-primary and the ML-sensitivity endpoint is itself informative about ascertainment (the same
logic as the E1-vs-E2 severity split).

## Findings Summary — OpenSAFELY (replication vehicle)

The NHS England / NICE long-COVID SNOMED set is a small **3-cluster** codelist (verified on
OpenCodelists):
- **Diagnosis (2 codes):** `1325161000000102` "Post-COVID-19 syndrome" (≥12 wk, WHO-aligned) +
  `1325181000000106` "Ongoing symptomatic disease caused by SARS-CoV-2" (4–12 wk) — slug
  `opensafely/nice-managing-the-long-term-effects-of-covid-19`.
- **Referral (3 codes,** incl. `1325031000000108` "Referral to post-COVID assessment clinic") —
  slug `opensafely/referral-and-signposting-for-long-covid` (version `12d06dc0`); the **dominant
  coding mode since mid-2022** (35,440 / 55,465 ≈ 64% of coded cases [@Henderson2024]), the
  highest-value low-risk extender.
- **Assessment (10 codes):** slug `opensafely/assessment-instruments-and-outcome-measures-for-long-covid`.

**Lock:** primary = **all-three-clusters pooled** (materially more sensitive than diagnosis-only;
referral codes ~double the count), with **coded-diagnosis-only vs coded-any** as a pre-registered
**bracketing sensitivity pair**. A symptom-cluster + "≥12-week persistent symptom post-infection"
temporal phenotype is **exploratory upper-bound only**, because two blockers documented in the
OpenSAFELY data defeat it as a primary: (a) **59% of coded cases had no positive test recorded
≥12 wk before the long-COVID record** [@Henderson2024], so a confirmed-infection temporal anchor
discards most true cases; (b) symptom codes (fatigue/breathlessness/palpitations) are non-specific
→ low PPV.

**The consequential downgrade (updates `interpretation:0031` + plan rule #4):** broadening the
OpenSAFELY phenotype **RESHAPES — and may worsen — the differential-by-utilisation bias rather than
removing it.** Every cluster is generated at an encounter; referral/symptom codes are *more*
contact-dependent than a single diagnosis code, so broadening pulls in *more* of the high-utilisation
(autoimmune-enriched, female-enriched: coded LC aHR ~1.33 female) population. OpenSAFELY's
population-based *sampling frame* still blunts frame-level ascertainment, but its *outcome channel*
stays utilisation-gated — so it is **not** a clean outcome-side arbiter even with the broad
phenotype. The utilisation gradient must be handled analytically (pre-pandemic consultation-frequency
adjustment + negative control + bracketing pair) regardless of how the outcome is drawn.

## Case-definition flag (per AGENTS.md)

- **WHO clinical case definition:** symptoms ≥3 months post-infection, lasting ≥2 months.
  **CDC:** ≥4 weeks.
- **Locked primary window = WHO-aligned ≥90 d** post-index for the diagnosis-anchored endpoint
  (matches the OpenSAFELY ≥12-wk diagnosis code `1325161000000102`); a **CDC-aligned ≥28 d** variant
  and the OpenSAFELY 4–12-wk code (`1325181000000106`) are reported as broader variants.
- Distinguish the **survival/observation inclusion window** (Hill's ≥45 d, a denominator filter)
  from the **PASC ascertainment window** (≥90 d, the outcome timing) — they are different offsets
  and were being conflated in the plan's prose; BC-5 separates them.

## Cross-vehicle harmonisation (stated honestly)

The two vehicles' outcomes **will never be identical code** (N3C U09.9/clinic vs OpenSAFELY NICE
3-cluster). BC-5 harmonises them **conceptually, not literally**: both anchored on a WHO-aligned
≥12-wk/≥90-d coded post-COVID condition as primary; both with a broader coded variant as a
bracketing sensitivity endpoint; both understood to be utilisation-gated on the outcome side.
Replication therefore tests whether the autoimmune × sex signal **survives across two different
ascertainment regimes**, not whether two identical measurements agree — which is the stronger
question anyway.

## Evidence Quality

Feasibility-grade, well-sourced. Pfaff2022 and Thaweethai2023 were read to full text (Europe PMC
XML / paper-fetch) and written as durable paper entities; the OpenSAFELY codelist structure and
under-coding statistics are landing-confirmed against OpenCodelists and four OpenSAFELY papers.
The one genuinely load-bearing inference — that adopting Pfaff-as-primary would bake in the study's
target confounds — follows directly from the paper's own reported top-feature (outpatient visit
rate) and training-cohort sex composition, not from conjecture.

## Sources (durable pointers)

Checked 2026-07-01.
- **N3C computable phenotypes:** `paper:Pfaff2022` (Lancet Digit Health 2022, `doi:10.1016/S2589-7500(22)00048-6`,
  PMID 35589549; code `github.com/NCTraCSIDSci/n3c-longcovid`); `paper:Hill2022` (coded U09.9/clinic
  definition); `paper:Thaweethai2023` (JAMA 2023, `doi:10.1001/jama.2023.8823`, PMID 37278994 —
  survey PASC index).
- **OpenSAFELY coded outcome:** diagnosis `opensafely/nice-managing-the-long-term-effects-of-covid-19`
  (`https://www.opencodelists.org/codelist/opensafely/nice-managing-the-long-term-effects-of-covid-19/64f1ae69/`);
  assessment `opensafely/assessment-instruments-and-outcome-measures-for-long-covid`
  (`https://www.opencodelists.org/codelist/opensafely/assessment-instruments-and-outcome-measures-for-long-covid/79c0fa8a/`);
  referral `opensafely/referral-and-signposting-for-long-covid`
  (`https://www.opencodelists.org/codelist/opensafely/referral-and-signposting-for-long-covid/12d06dc0/` —
  3 codes, SNOMED CT, incl. `1325031000000108`).
- **Under-coding evidence:** `cite:WalkerLongCOVID2021` (23,273/58M; 26.7% of practices never coded);
  `cite:Henderson2024` (Henderson et al., *eClinicalMedicine* 2024;72:102638, `doi:10.1016/j.eclinm.2024.102638`,
  PMC11127160 — 55,465 coded; 59% no positive test recorded ≥12 wk prior; referral codes dominant since
  mid-2022, ≈64% of cases; incidence rose with GP-interaction frequency).

## Data Quality Checks

Structural outcome-QA facts carried into `plan:0005`:
- **U09.9 left-truncation / differential availability** — the code became active in US ICD-10-CM on
  **2021-10-01** (`[UNVERIFIED]` exact N3C-site adoption ramp). This is **not** "pre-Oct-2021
  infections can never be U09.9": a pre-activation infection *can* be assigned U09.9 later if the
  patient is still observed after activation. The real issue is **left-truncated, differential
  outcome availability by calendar era and follow-up** — no U09.9 can be recorded during the
  pre-activation window, and early-era cases have a shorter post-activation ascertainment window —
  which correlates with variant era (already a covariate). The LC-clinic-visit arm partially bridges
  the pre-activation window but adds clinic-access skew.
- **Pfaff phenotype PPV** in unbalanced real-world N3C is substantially below the class-balanced
  precision (0.85); the recommended 0.45 threshold needs recalibration per target prevalence — an
  analysis-time step, not a definition change.
- **OpenSAFELY 59%-no-positive-test** anchor failure (above) — the reason the symptom-temporal
  phenotype is exploratory-only.

## Proposition-Level Updates

None. BC-5 is an outcome-definition lock; no `proposition:` gains or loses an evidence-line.

## Hypothesis-Level Implications

- `hypothesis:0008` (measurement-channel / ascertainment) is **strongly and convergently
  reinforced on the outcome side across all three legs**: the coded outcome is utilisation-gated at
  ascertainment; the ML phenotype is utilisation-gated *by construction* (top feature) with an
  untested sex-specific error profile on top; the OpenSAFELY broad phenotype reshapes rather than removes the
  utilisation gradient. h0008's core claim — that the measurement channel, not only the sampling
  frame, shapes the apparent signal — now has three independent outcome-channel instances plus the
  BC-3 exposure-channel instance (`interpretation:0032`). Operationally this means the study's
  validity rests on its **design defences**, not on finding a clean outcome.
- No update to `hypothesis:0004`/`hypothesis:0005`; BC-5 is outcome infrastructure.

## Evidence vs. Open Questions

**Settled (BC-5):** N3C primary = coded U09.9/clinic (WHO-aligned ≥90 d); Pfaff ML = flagged
sensitivity (with the confound caveat); RECOVER index = survey-only construct anchor via
RECOVER-Adult; OpenSAFELY primary = 3-cluster coded pooled + diagnosis-only/any bracketing pair,
symptom-temporal = exploratory; case-definition window flagged; ascertainment-vs-survival windows
separated; OpenSAFELY arbiter role qualified. **Still open:** BC-4 (cell counts — the binding
unknown); BC-6 (severity dateability); BC-7 (individual utilisation — now doubly load-bearing since
it is the primary defence for *both* exposure and outcome ascertainment).

## New Questions Raised

- Does the coded-primary vs Pfaff-ML-sensitivity endpoint **divergence** track the autoimmune ×
  sex interaction (i.e. is the effect larger under the utilisation-baked ML phenotype)? If so, that
  divergence is direct evidence of outcome-side ascertainment inflating the naive estimate — a
  built-in bias probe. (Folds into BC-4/analysis on `task:t079`; no standalone `question:` reserved.)

## Limitations & Residual Uncertainty

- **No outcome is clean** — BC-5 minimises, not eliminates, outcome-side bias; the residual is
  carried by design, and its adequacy is unprovable at design stage (needs the negative-control and
  E-value results).
- **RECOVER-Adult PRO linkage availability** is itself gated (that vehicle's own access track) — the
  construct-validation leg is contingent on it.
- **U09.9 adoption ramp** and the standalone OpenSAFELY referral-codelist slug remain `[UNVERIFIED]`.

## Updated Priorities

1. **BC-4 remains the binding next check** — and BC-5 sharpens it: the coded-primary endpoint is
   *less* sensitive than the ML phenotype, so per-stratum × sex cell counts under the coded
   definition are the conservative (and correct) power test.
2. **Propagate the outcome lock into `plan:0006`'s PASC-outcome WP**: primary = coded U09.9/clinic;
   add the Pfaff ML phenotype as a flagged sensitivity endpoint with the utilisation/sex
   confound recorded; separate the survival vs ascertainment windows in `windows.yaml`. WP stays
   code-gated (t082).
3. **Update `plan:0005` Sensitivity Arbitration rule #4** to record that a broad OpenSAFELY
   phenotype reshapes (does not remove) the utilisation gradient → OpenSAFELY arbitrates the
   sampling-frame contrast but not the outcome channel; the bracketing coded pair + utilisation
   adjustment + negative control are mandatory there.
