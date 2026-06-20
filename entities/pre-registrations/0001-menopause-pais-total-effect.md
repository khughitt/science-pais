---
id: "pre-registration:0001-menopause-pais-total-effect"
type: "pre-registration"
title: "Pre-registration: total effect of reproductive-stage timing on long COVID in UK Biobank (menopause→PAIS)"
status: "committed"
committed: "2026-06-19"
mode: data-gated
spec: "entities/plans/2026-06-19-menopause-pais-total-effect-analysis-plan.md"
related:
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
  - question:0007-mechanism-of-female-predominance-in-pais
  - patch-definition:menopause-pais-causal-dag
  - task:t016
  - task:t017
  - task:t020
  - task:t027
  - paper:AlcaldeHerraiz2025
commits_to:
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
amendments:
  - date: "2026-06-19"
    ratified_by: "task:t029 (independent out-of-author review)"
    type: "pre-data amendment (not a fresh pre-registration)"
    change: >
      Primary adjustment set {age} → {age, smoking}, named the PRIMARY MEASURED
      adjustment set (NOT 'minimal-sufficient': no valid sufficient set exists while
      U is latent — see DAG critique). Smoking = baseline smoking history
      (never/former/current + pack-years/duration where available); baseline smoking is
      pre-infection but not necessarily pre-FMP, so it is a measured confounder, not a
      clean pre-menopause exposure. E-value benchmark and U-proxy arm redefined relative
      to the new primary set (U = unmeasured confounding BEYOND {age, smoking}).
    rationale: >
      Smoking is a measured strong common cause of earlier menopause and of
      long-COVID/COVID risk and mortality; sensitivity-only placement was an
      identification gap the bias audit missed. Reviewer ratified Q1 with the
      coding/wording modification above.
  - date: "2026-06-20"
    ratified_by: "task:t029 (independent out-of-author second pass; report:0002-t029-second-pass-menopause-pais-pre-registration-review)"
    type: "pre-data amendment (not a fresh pre-registration)"
    change: >
      Out-of-author second-pass corrections (A1–A3 + G6 + IMD), all pre-data:
      (A1) PEM-weighted arm re-described as a PESE/fatigue-weighted questionnaire
      proxy — UKB DOES carry a post-exertional-symptom item; the prior "no PEM-specific
      signal" wording overstated the gap. Still sensitivity-only, not RECOVER-equivalent.
      (A2) Add UKB field 3882 (age at bilateral oophorectomy) to the t027 basket
      [confirm at application]; required for the surgical age-at-surgery gradient and
      for clean pre-infection surgical exclusion.
      (A3) Downgrade "HRT-active-at-infection" to "baseline HRT status / unknown at
      infection": baseline fields 2814/3536/3546 do not reach the 2020–2022 infection
      window; an HRT-on-at-infection tag needs GP/prescription linkage or it is dropped.
      (G6) State def-3 (SF-36 functional gate) is FORMALLY DROPPED for this pre-reg,
      not left as a live "substitute-or-drop" option post-lock.
      (IMD) Resolve the unspecified deprivation field: use Townsend (189) only, or add a
      named IMD field/derivation [confirm at application] — no bare "IMD" reference.
    rationale: >
      Out-of-author review (report:0002) closing the bias-audit author-independence
      finding for the outcome/exposure/feasibility surface. These are corrections and
      tightenings, not criterion loosenings; raised by an independent reviewer, so they
      carry the out-of-author provenance the audit demanded.
  - date: "2026-06-20"
    ratified_by: "task:t029 second pass + user decision 2026-06-20"
    type: "G2 corpus-independence disposition (verdict-confidence, not a criterion change)"
    change: >
      SHBG/sex-hormone prior DOWNGRADED to explicit single-source background. The
      out-of-corpus second-precedent search (report:0002) found only Gao et al. (JAMA
      2024) as a genuinely author-independent UKB precedent — it weakly corroborates
      questionnaire feasibility + the healthy-volunteer/survival-to-2020 selection
      profile, but is hospitalization-conditioned (unusable for effective-n) and tests
      no hormones. Wang et al. and the Prieto-Alhambra preprint share the AlcaldeHerraiz
      author network and are NOT corpus-independent. Net: questionnaire feasibility/
      selection weakly corroborated out-of-corpus; effective-n and the SHBG-protection
      signal remain SINGLE-SOURCE (AlcaldeHerraiz2025) and are labelled as such. G2's
      out-of-corpus prong is dispositioned by this recorded downgrade (not by finding an
      independent SHBG precedent); an opportunistic non-UKB SHBG/long-COVID search is
      tracked separately and would strengthen, not gate.
    rationale: >
      SHBG is on the M1-confirm side (mediator-specific), which UKB can barely confirm
      regardless (oestradiol censored, no FSH/AMH); it is not load-bearing for the
      primary {age, smoking} total-effect estimand. Honest single-source labelling
      preserves the primary while closing the coherence gap left by the open G2 prong.
created: "2026-06-19"
updated: "2026-06-20"
---

# Pre-registration: total effect of reproductive-stage timing on long COVID in UK Biobank (menopause→PAIS)

**Target class.** Mixed, primarily **epistemic**. The epistemic commitment is an
interpretation rule for `h0005` (and the question `q0013` it answers): how to update
belief about reproductive-stage-as-immune-homeostatic-margin given the observed
effect. The operational portion is "run the **{age, smoking}**-adjusted total-effect
analysis (primary measured adjustment set; amendment Q1) on UK Biobank exactly as the
three design artifacts specify." `q0007` (male-vs-female
predominance) is a **different estimand** and is navigation context only — **not** a
commitment target.

**Execution-timing: `mode: data-gated`.** The vehicle (UK Biobank) is *identified
and admissible in principle* but **not provisioned**: a UKB AMS data-access
application is not yet submitted, and several field IDs await live confirmation. The
analysis is **design-complete but not executable**. Until an admissible, provisioned
vehicle clears the Vehicle-Admissibility Gate below, the standing verdict is
**`[?]` inconclusive-for-coverage** — this pre-reg produces **no `bears_on` belief
update** on h0005 until then. This is distinct from a null result (which would be
evidence).

**Lock inputs (the design is frozen against these):**
- Exposure: `doc/methods/2026-06-19-reproductive-stage-exposure-operationalization.md` §8 (t020)
- Outcome + covariates: `doc/methods/2026-06-19-ukb-outcome-and-uproxy-measurement-schema.md` §8 (t017)
- Vehicle / field basket / access: `doc/methods/2026-06-19-ukb-data-field-specification.md` (t027)
- Estimand / adjustment / arbitration: the t016 analysis plan (`spec` above)

> **Amendment APPLIED — ratified by t029 independent review (2026-06-19).**
> Source: `doc/methods/2026-06-19-confounder-open-questions-and-staged-amendment.md`.
> - **Q1 (applied):** primary adjustment set **`{age}` → `{age, smoking}`**, the
>   **primary measured adjustment set** (deliberately *not* "minimal-sufficient" — no
>   valid sufficient set exists while U is latent; see
>   `doc/inquiries/menopause-pais-causal-dag-critique.md`). Smoking = **baseline smoking
>   history (never/former/current + pack-years/duration where available)**; baseline
>   smoking is pre-infection but **not necessarily pre-FMP**, so it is a measured
>   confounder, not a clean pre-menopause exposure. E-value/U-proxy redefined vs the new
>   set (below).
> - **Q2 (deferred to DAG v2 / t023):** BMI stays **out** of the primary set — ambiguous
>   confounder-vs-mediator role; carried as a **sensitivity** covariate (baseline,
>   timing-split where possible); role fixed in DAG v2.
> - **Q3 (not promoted):** autoimmune-POI → confirmed-POI **quarantined/stratified** as a
>   distinct etiologic stratum (generic autoimmune-hx stays U-proxy); **frailty** →
>   selection/sensitivity model only; **parity** → staging input + DAG-v2 candidate, not
>   primary (avoids drifting to a reproductive-life-course estimand).
> - **Q4 (added):** **Mendelian-randomization triangulation arm** added under Exploratory
>   with a pleiotropy-/selection-robust guardrail battery — **triangulation only, not
>   confirmatory/co-primary**.

> **Amendment 2 APPLIED — t029 out-of-author second pass (2026-06-20).**
> Source: `report:0002-t029-second-pass-menopause-pais-pre-registration-review`.
> - **A1 (applied):** PEM-weighted arm re-described as a **PESE/fatigue-weighted
>   questionnaire proxy** (UKB *does* carry a post-exertional-symptom item) — sensitivity
>   only, not RECOVER-equivalent. See Limitation #3.
> - **A2 (applied):** field **3882** (age at bilateral oophorectomy) added to the t027
>   basket `[confirm at application]` — needed for the surgical age-at-surgery gradient.
> - **A3 (applied):** **HRT-active-at-infection downgraded** to "baseline HRT status /
>   unknown at infection" (baseline fields 2814/3536/3546 don't reach 2020; needs GP
>   linkage or it's dropped). The surgical HRT-stratification signature inherits this.
> - **G6 (tightened):** def-3 (SF-36 functional gate) is **formally dropped**, not a live
>   post-lock substitute-or-drop option.
> - **IMD (resolved):** Townsend (189) only, or a *named* deprivation field/derivation
>   `[confirm at application]` — no bare "IMD".
> - **G2 corpus-independence disposition:** SHBG/sex-hormone prior **downgraded to explicit
>   single-source background**; questionnaire feasibility/selection weakly corroborated
>   out-of-corpus (Gao 2024, independent), effective-n + SHBG remain single-source. The two
>   nominal "second precedents" (Wang; Prieto-Alhambra preprint) share the AlcaldeHerraiz
>   author network and are **not** corpus-independent. See G2 below.

---

## Hypotheses Under Test

- **`h0005`** — reproductive-stage transitions alter the immune homeostatic margin and
  modify the risk of failed post-infectious recovery. The directional prediction:
  **lower estrogenic / later-reproductive-stage status → higher long-COVID risk /
  delayed resolution**, operating *through* hormone-driven immune, endothelial, and
  autonomic mediators (a threshold-shift, not a direct cause).
- **`q0013`** — does reproductive-stage transition change the probability of failed
  immune recovery after infection? This pre-reg is the UKB operationalization of that
  question, with the at-risk-window (peri) sub-question explicitly flagged as
  **UKB-underpowered** (see Feasibility).

---

## Feasibility Against Real Input Artifacts (pre-data, load-bearing)

Checked against the nearest precedent (`paper:AlcaldeHerraiz2025`, UKB long-COVID):

- **Cohort-age vs pandemic timing — the decisive constraint.** UKB baseline age is
  **40–69 (2006–2010)**; at infection (2020–2022) participants are **≈ 52–83**
  (precedent mean age-at-infection ≈ 66). With UK median natural menopause ≈ 51,
  **essentially all UKB natal females are postmenopausal at infection.**
  - *Premenopausal-at-infection* requires age < ~50 at infection → < ~37 at baseline
    → **below UKB's age-40 floor → ≈ 0 participants.**
  - *Perimenopausal-at-infection* (≈ 47–55) is a **thin sliver** of the youngest
    enrollees only.
  - ⇒ **The pre → peri → post-at-infection contrast is structurally near-unavailable
    in UKB.** The cohort aged out of the premenopausal window before the pandemic.
- **Consequence — the confirmatory exposure is reproductive-stage *timing*, not
  current stage.** The exposure with real variance in UKB is **age at menopause** and
  **time-since-menopause at infection** among a near-uniformly-postmenopausal cohort.
  This is the UKB-supportable realization of the locked "reproductive stage" estimand;
  the pre/peri-vs-post contrast is **routed to the younger triangulation cohorts**
  (All of Us, Lifelines) and is **exploratory** in UKB.
- **Effective n (order of magnitude, to be confirmed on provisioning).** Precedent LC
  cohort = 8,668 (positive PCR ∧ questionnaire), 2,751 cases. Natal-female restriction
  → ~4,000–4,500 women; female long-COVID rate is higher, so ~1,200–1,600 female
  cases — adequate for a **timing** exposure across the (post) cohort, but the
  **pre/peri cell ≈ 0**, confirming the reframe above. *(These effective-n figures
  remain **single-source** — `AlcaldeHerraiz2025`; the out-of-corpus cross-read found no
  independent UKB precedent that re-confirms the denominator, only the questionnaire
  route + selection profile, per G2/`report:0002`. Confirm exactly on provisioning.)*

**Design fix applied here (not deferred to post-data):** the **primary confirmatory
contrast is the reproductive-timing exposure**; the stage-at-infection ordinal is
demoted to an exploratory/triangulation contrast. This inversion is made pre-data
because the artifacts were inspected before thresholds were locked.

---

## Expected Outcomes

- **Primary (confirmatory):** earlier age at menopause / longer time-since-menopause
  at infection is associated with **higher** probability of WHO ≥90-day long-COVID,
  in natal females, adjusting for age at infection. Pre-declared **smallest
  meaningful effect: RR ≈ 1.3** comparing the earliest-vs-latest menopause-timing
  tertile (equivalently ≈ RR 1.10–1.15 per SD of the continuous timing exposure — to
  be fixed to one scale at provisioning, not both).
- **Why:** h0005's homeostatic-margin conjecture + the precedent's female-specific
  SHBG protection signal (AlcaldeHerraiz2025 — **single-source**; no independent UKB
  precedent re-tests it, per G2/`report:0002`, so this prior is background, not
  corroborated) + the hormone-immune/endothelial mechanisms reviewed under
  `topic:menopause-sex-hormones-and-pais-risk`. The effect
  is expected to be **modest** and **partially confounded** (U latent), hence the
  E-value discipline below.
- **Direction is the primary commitment; magnitude is secondary** given the
  partial-identification design.

---

## Decision Criteria

Epistemic framing — each result class moves belief on h0005 by a stated amount/direction
(not a kill-switch). Thresholds are on the **primary confirmatory** estimate (RR of
WHO ≥90-day long-COVID per reproductive-timing exposure, **{age, smoking}**-adjusted
[primary measured adjustment set], natal-female, UKB), read jointly with its mandatory
sensitivities.

**Moves belief TOWARD h0005 (`supports_threshold_shift`):**
- Primary RR away from null in the predicted direction (earliest-vs-latest tertile RR
  ≥ ~1.3, 95% CI excludes 1), **AND**
- **E-value** for the estimate (and the near-null CI limit) **exceeds** the
  measured-proxy benchmark — the strength of associations for proxies **beyond the
  primary {age, smoking} set** (SES/comorbidity/remaining-behaviour) — **AND**
- the **U-proxy adjustment arm** (adding those beyond-{age, smoking} proxies) does not
  collapse it toward the null, **AND**
- it is **definition-stable** across the *feasible* outcome definitions (def-1 primary
  + def-2 approximation), **AND**
- it **survives** response-selection IPW and is **directionally concordant** with the
  Route-B (HES-PACS) triangulation outcome.

**WEAKENS / `fragile` (belief barely moves or downgrades confidence):**
- Primary RR away from null **but** E-value below the proxy benchmark, **or** the
  U-proxy arm collapses it, **or** it appears only in Route A (questionnaire) and
  tracks response-propensity, **or** it is present only under one outcome definition.

**Moves belief AWAY from h0005 (downward update):**
- Primary RR consistent with null **with an adequate power floor** — i.e. the
  (QBA-bias-adjusted) interval **excludes the meaningful effect (RR 1.3)** — and this
  is definition-stable. A *powered* null is a real downward update on the
  reproductive-timing-as-threshold-shifter claim (it does not falsify h0005's broader
  mechanism set, which other estimands test).

**Vetoes (result is inadmissible, no update either way):**
- `collider_confounded` — effect present **only** in a selection-conditioned subsample
  (clinic/HES-selected or response-propensity stratum) and absent in the population
  frame → reject as selection artifact.
- `reverse_contaminated` — exposure staged post-hoc rather than from the pre-infection
  baseline. (Largely foreclosed in UKB by the 2006–2010 baseline design, but checked.)

---

## Null Result Plan

A null is **evidence weighted by commitment**, not a verdict on h0005.

- **Powered null** (QBA-adjusted interval excludes RR 1.3, definition-stable) →
  **downward** belief update on reproductive-stage *timing* as a long-COVID
  threshold-shifter in this population; redirect effort to within-person/discordant
  designs and to the mediator-specific (direct-effect) estimand.
- **Underpowered / attenuated null** (esp. any peri analysis, or where non-differential
  staging misclassification per t020 has attenuated the estimate) → **no update**;
  label `underpowered/attenuated`, route the at-risk-window contrast to the younger
  triangulation cohorts. The t020 QBA attenuation means even a "true" null must be read
  against the **bias-adjusted** interval, not the naive one.
- **Ambiguous** (sensitivities disagree) → report as **estimand-/operationalization-dependent**;
  do not average; escalate to `/science:discuss`.

**Power floor (locked):** the confirmatory timing analysis must clear the minimum
female-case count for 80% power at RR 1.3 (α two-sided 0.05); computed exactly on
provisioning (G3 below). A peri-stratum result is reported only if its own cell clears
the floor — otherwise it is `underpowered`, never `null_meaningful`.

---

## Suspicious/Unexpected Result Plan

- **"Too good":** a large peri-specific or timing RR (e.g. > 2.0), or an implausibly
  clean monotonic dose-response across thin cells.
- **Likely inflators:** (a) menopause↔PAIS **symptom-overlap** leaking into both
  exposure-proxy and outcome despite the pre-baseline design; (b) **questionnaire
  response selection** (sicker reproductive-timing strata more likely to respond);
  (c) thin-cell instability in peri; (d) residual age confounding if age modeled too
  coarsely.
- **Pre-committed checks before accepting any strong result:** Route-B (HES)
  triangulation; response-selection IPW; a **negative-control outcome** (an outcome
  not plausibly caused by reproductive-stage timing — e.g. an injury/accident code —
  should show null); E-value plausibility vs the proxy benchmark; ordinal-vs-binary
  and per-SD-vs-tertile concordance; per-cell n inspection.

---

## Known Limitations

This analysis **cannot**, even executed perfectly:
1. **Point-identify** the total effect — even with {age, smoking} measured, U (SES,
   prior EBV, genetic/HLA, residual behaviour beyond smoking) stays partly latent, so
   **no valid sufficient adjustment set exists** (per the DAG critique); {age, smoking}
   is the *primary measured* set, not a sufficient one, and the E-value bound is
   load-bearing.
2. Resolve the **pre/peri-vs-post** contrast in UKB (cohort aged out — Feasibility);
   that requires younger cohorts.
3. Deliver a **PEM-specific** verdict — UKB has WHO-symptom-level data and a
   **post-exertional-symptom (PESE) questionnaire item** with duration/impact fields, but
   **no RECOVER PASC index, no CPET, and no validated PEM instrument**. def-2 is therefore a
   **PESE/fatigue-weighted questionnaire proxy** (sensitivity-only, *not* RECOVER-equivalent;
   q0015/t025 under-served) — corrected from the prior "no PEM-specific signal" wording per
   A1 (report:0002).
4. Compute the **SF-36 functional-gate** definition (def-3) — not in UKB; **formally dropped
   for this pre-reg** (G6), not held open as a post-lock substitute-or-drop option. Adding it
   later would require a *named* UKB functional proxy and a new amendment.
5. Escape **decade-gap exposure misclassification** (t020 QBA bounds, not removes, it).
6. Generalize beyond UKB's **healthy-volunteer, >90% White, questionnaire-responding**
   subset without the IPW + triangulation arms.
7. Escape **left-truncation / survival-to-2020 selection** (added by bias audit
   `report:0001-bias-audit-menopause-pais-total-effect`). Every analyzed woman must
   have survived from the 2006–2010 baseline to her 2020–2022 infection (age ≈ 52–83).
   Because **earlier age at menopause is associated with higher all-cause/CV
   mortality**, the earliest-menopause-timing stratum — the high-risk end of the
   *exposure* — is differentially depleted *before* the time origin (a
   competing-prior-event / depletion-of-susceptibles structure, distinct from the
   post-infection competing-risk censoring already handled). Expected to bias the
   timing→long-COVID estimate **toward the null**, though the direction is not
   guaranteed. Add a competing-prior-event / age-at-menopause-survival sensitivity at
   execution; report the bias direction.
8. Fully de-select on **questionnaire-response propensity** (added by bias audit).
   The response IPW is built from **baseline** predictors, but propensity to complete
   the 2022–2023 questionnaire plausibly depends on *post-baseline* health (including
   incipient long-COVID). Baseline IPW cannot reweight on a 2022 health state, so the
   Route-A estimate is "in responders"; Route-B (HES-PACS) carries the de-selecting
   triangulation weight, not the IPW alone.

**Vehicle-scope concession (bias audit, anchoring finding).** UKB is the primary
vehicle for the reproductive-**timing** estimand, but it **cannot answer q0013's
motivating peri-window sub-question** — the cohort aged out of the premenopausal/peri
window before the pandemic (Feasibility §). The stage→timing reframe is therefore an
honest scope concession, not a silent substitution; the peri/at-risk-window contrast
is owned by the younger triangulation cohorts. When the feasible outcome definitions
or exposure scales disagree, the governing order is **def-1 (WHO ≥90d) over def-2
(approximation)** and **tertile-contrast over per-SD** before any `/science:discuss`
escalation — so the escalation clause is not an open forking path.

---

## Metric Selection Rationale

- **Primary metric: risk ratio (RR) via log-binomial (or log-Poisson with robust SE)
  regression** for WHO ≥90-day long-COVID **present** at the Health & Well-Being
  questionnaire. Rationale: the questionnaire is a **single cross-sectional snapshot
  (2022–2023)**, so time-to-resolution is not cleanly observable on Route A → a
  prevalence/risk contrast is the honest estimand. (Route B / HES supports a
  time-to-event HR as a secondary, where longitudinal codes permit.)
- This **diverges** from the t016 plan's "HR or RR" wording by committing to **RR as
  primary**, justified by the Route-A cross-sectional outcome — a feasibility-driven
  refinement, recorded here so interpret-results treats it as committed, not drift.
- **Known limitation:** RR at a single snapshot conflates incidence and persistence;
  the Route-B HR triangulation partially addresses this.

---

## Exploratory vs. Confirmatory

**Confirmatory (1 primary test):**
- Reproductive-timing exposure (age-at-menopause / time-since-menopause) → WHO ≥90-day
  long-COVID RR, **{age-at-infection, smoking}**-adjusted (primary measured set;
  amendment Q1), natal-female, UKB, Route A.

**Pre-specified mandatory sensitivities (robustness, not discovery — do not multiply-correct as independent tests):**
E-value bound; U-proxy adjustment arm (proxies beyond {age, smoking}, +EBV on the ~9.6k
Category-1307 subsample, reported with its own power floor); response-selection IPW;
Route-B (HES-PACS) triangulation; estimand-split **{age, smoking}** vs
**{age, smoking, baseline comorbidity}**; BMI sensitivity (baseline, timing-split where
possible — role deferred to DAG v2 per Q2); outcome-definition axis (def-1 primary,
def-2 approximation); ordinal-vs-binary / per-SD-vs-tertile.

**Exploratory (explicitly labelled, hypothesis-generating):**
- Stage-at-infection ordinal (pre/peri/post) contrast in UKB (peri ≈ underpowered).
- Severity-controlled **direct** effect (additionally conditioning on acute severity).
- Mediator-specific (SHBG/testosterone) analyses.
- Triangulation pre/peri contrast in All of Us / Lifelines (separate pre-regs/arms).
- **Surgical-menopause discriminating contrast** (t030;
  `doc/methods/2026-06-19-surgical-menopause-discriminating-contrast.md`): bilateral
  oophorectomy vs natural postmenopause, with the **age-at-surgery gradient**
  (pre- vs post-FMP oophorectomy) and **HRT-stratification** as the
  confounding-resistant signatures that separate **M1** (hormone-withdrawal) from
  **M2** (aging) / **M4** (SES). **Exploratory / triangulating only** — estimated on a
  separate stratum with surgical cases **excluded from the primary natural-timing
  estimand**; promotable to a verdict-bearing sensitivity only if surgical *indication*
  is adequately bounded (reviewer call, t029).
- **Mendelian-randomization triangulation arm** (Q4; ratified t029): MR of
  genetically-instrumented **age-at-natural-menopause (ANM) → long-COVID**, exogenous to
  SES/smoking/survival and so attacking M2/M4/M3a jointly. **Triangulation only — not
  confirmatory or co-primary.** Pre-committed guardrails: prefer **external ANM
  instruments**; ancestry/PC handling; **sample-overlap disclosure**; clumping;
  **Steiger directionality**; heterogeneity tests; leave-one-out; **MR-Egger**, weighted
  median/mode; and a **pleiotropy-focused analysis excluding or separately reporting
  immune / DNA-repair / MHC-adjacent instrument subsets**. The DNA-repair/immune-gene
  overlap is grounds to **down-weight** the MR verdict, not to drop the arm.

---

## Total Comparison Count

| Category | Count | Correction |
|---|---|---|
| Confirmatory tests | 1 | none needed (single primary); verdict rests on it + mandatory sensitivities |
| Pre-specified sensitivities | ~9 | interpreted as robustness/arbitration, not multiplicity (adds BMI sensitivity per Q2) |
| Exploratory tests | ~6+ | none (exploratory — reported with exploratory weight; adds MR triangulation per Q4) |
| **Total** | **~16** | confirmatory verdict is multiplicity-free; sensitivities/exploratory carry their own (reduced) evidential weight |

---

## Vehicle-Admissibility Gate (data-gated mode)

**Standing verdict while gated:** `[?] inconclusive-for-coverage` — no `bears_on`
update on h0005/q0013 until a provisioned vehicle clears **all** G-gates below. These
G-gates **are** the "Blocking Checks Before Execution" that `/science:plan-analysis`
reports for this committed pre-reg (defined once here; referenced there).

- **G1 — Access provisioned.** An approved UKB AMS application with the required return
  categories (COVID-test field 40100; HES; GP; death; Health & Well-Being
  questionnaire; Category-1307 serology; vaccination linkage) delivered to a UKB RAP /
  approved environment.
- **G2 — Field IDs confirmed live + out-of-corpus feasibility check.** Questionnaire
  item IDs (WHO-Delphi), EBV-subsample N (Category 1307), vaccination-linkage category,
  **and field 3882 (age at bilateral oophorectomy, added per A2)** confirmed on the
  Showcase (COVID-test field 40100 already verified). **Out-of-corpus prong — DISPOSITIONED
  (`report:0002`, 2026-06-20):** the second-precedent cross-read found only **Gao et al.
  (JAMA 2024)** as a genuinely author-independent UKB precedent — it weakly corroborates
  questionnaire feasibility + the healthy-volunteer/survival-to-2020 selection profile, but
  is hospitalization-conditioned (unusable for effective-n) and tests no hormones. The two
  other candidates (Wang; Prieto-Alhambra preprint) **share the AlcaldeHerraiz author
  network** and are not corpus-independent. Disposition: **questionnaire feasibility/
  selection = weakly corroborated out-of-corpus; effective-n + the SHBG-protection signal =
  remain SINGLE-SOURCE (`AlcaldeHerraiz2025`) and are labelled as such.** The SHBG prior is
  **downgraded to single-source background** (it is mediator-specific / M1-confirm-side, not
  load-bearing for the primary {age, smoking} total effect). G2's out-of-corpus prong is
  satisfied by this **recorded downgrade**, not by finding an independent SHBG precedent; an
  opportunistic non-UKB SHBG/long-COVID search (tracked separately) would strengthen, not
  gate. Live-Showcase field confirmation at application still required.
- **G3 — Power floor met.** Female-case count for the **timing** exposure clears 80%
  power at RR 1.3 (α 0.05) after natal-female restriction ∧ valid menopause-timing ∧
  questionnaire-response ∧ positive-PCR. (The pre/peri stratum is *not* required to
  clear it — it is exploratory by Feasibility.)
- **G4 — Sampling-frame admissibility.** Recruitment not conditioned on symptomatic
  care-seeking (population frame upheld); the questionnaire-response selection handled
  by restriction + IPW; Route-B available for triangulation.
- **G5 — Exposure-timing integrity.** Reproductive-timing exposure derivable from the
  **pre-infection (2006–2010) baseline**; post-hoc-staged records quarantined.
- **G6 — Outcome computability.** Def-1 (WHO ≥90d, Route A) computable; def-2
  (PESE/fatigue-weighted) proxy constructable; **def-3 (SF-36 functional gate) is
  formally DROPPED** for this pre-reg (not held open as a substitute-or-drop option) —
  re-adding it requires a named UKB functional proxy and a new amendment.

A **spent** vehicle that fails any G-gate does not qualify; the standing verdict
remains `[?]` until one does. Tracked by a `status: blocked` task whose blocker is
this gate.
