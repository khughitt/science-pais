---
id: "doc:ukb-outcome-and-uproxy-measurement-schema-2026-06-19"
title: "UKB implementable long-COVID outcome & U-proxy measurement schema for pre-registration (t017)"
created: "2026-06-19"
updated: "2026-06-19"
related:
  - task:t017
  - task:t016
  - task:t027
  - task:t020
  - task:t002
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - patch-definition:menopause-pais-causal-dag
  - paper:AlcaldeHerraiz2025
---

# UKB long-COVID outcome & U-proxy measurement schema (t017)

Defines the **UKB-implementable outcome and U-proxy measurement schema** needed for
pre-registration: the case-definition→UKB mapping, the linkage fields/tables,
missingness rules, covariate timing, and which schema elements are eligible to serve
each t016 sensitivity arm. It is the **last open design gate**; with it closed,
`/science:pre-register` has its inputs (the UKB AMS access application runs
separately as the access gate).

> **Scope (tight).** This owns the **outcome** and the **U-proxy / covariate**
> measurement schema only. The **exposure** (reproductive-stage staging +
> misclassification) is t020's deliverable
> (`doc/methods/2026-06-19-reproductive-stage-exposure-operationalization.md`); the
> field basket is t027's
> (`doc/methods/2026-06-19-ukb-data-field-specification.md`). This document does not
> re-derive the estimand or adjustment set.

This schema is grounded in the nearest precedent, **`paper:AlcaldeHerraiz2025`**
(*"Sociodemographic factors, biomarkers and comorbidities associated with post-acute
COVID-19 sequelae in UK Biobank,"* Nat Commun 2025) — which ran a UKB
pre-infection-baseline long-COVID analysis and whose outcome-engineering mechanics
are directly reusable. Where it made a design choice, this schema either adopts or
deliberately diverges and says which.

---

## 1. The key empirical correction: UKB *does* have a symptom-level LC instrument

The t027 spec (§5.2) assumed the long-COVID outcome would be engineered from
**GP/HES codes + U09.9**, and flagged "no symptom-level PASC instrument." The
precedent shows this is **too pessimistic**: AlcaldeHerraiz2025 built its primary LC
outcome from the **UKB Health and Well-Being online questionnaire** — a self-report
instrument with **45 COVID-related symptom questions**, completed by **~201,684
participants (June 2022–May 2023)**, mapped to the **WHO Delphi consensus** long-COVID
symptom list. Notably, that study **did not use U09.9 or GP linkage at all** for LC.

So UKB offers **two structurally different outcome routes**, with different selection
and ascertainment properties — and using **both** is the design's main credibility
lever (agreement across two differently-selected outcomes):

| Route | Source | Strength | Selection / ascertainment weakness |
|---|---|---|---|
| **A — symptom questionnaire** (primary) | Health & Well-Being questionnaire (WHO-Delphi 45-item) | **Symptom-level**, WHO-mappable, community-inclusive | Conditions on **questionnaire response** (~201k of ~500k) — a self-selection node (§4) |
| **B — coded PACS** (triangulation) | HES ICD-10 (U07.1/U07.2; U09.9 where coded) | Objective codes, no survey-response selection | **Hospitalization-biased** — undercounts mild, misses primary-care entirely |

---

## 2. Case-definition → UKB operationalization mapping (concept vs feasibility)

The t002 synthesis resolved the case-definition **concept** (WHO-2021 ≥3-month
primary, 3-definition sensitivity axis). It did **not** establish that each
definition is **computable in UKB**. This is that check — and it is the heart of the
"concept resolved ≠ operationalization resolved" distinction. **Each row is a
feasibility verdict, not an assumption.**

| t002 / t016 definition | UKB operationalization | Feasibility verdict |
|---|---|---|
| **(1) WHO 2021 ≥3-month** (primary, inclusive) | Route A: ≥1 WHO-Delphi symptom persisting **≥90 days** post-PCR (field 40100 index), pre-existing symptoms excluded | ✅ **FEASIBLE.** Precedent implemented it at 30d and 90d; 90d ≈ WHO ≥3-month. Carries the §4 response-selection caveat |
| **(2) PEM-weighted (RECOVER PASC-index ≥12)** | No PASC-index instrument in UKB. The questionnaire has fatigue/cognitive/exertional items but **not** the RECOVER weighted index and **no CPET/PEM-specific item** | ⚠️ **FEASIBILITY-LIMITED.** Can build a *symptom-count / fatigue-weighted proxy* only — **not** the PASC index. Pre-register it as an explicit **approximation**, never as equivalent. Any PEM-stratified claim (q0015/t025) remains under-served (consistent with t002) |
| **(3) WHO + functional-impairment gate (SF-36 T<45)** | **UKB has no SF-36 at the LC window.** Functional proxies are sparse | ❌ **NOT FEASIBLE AS SPECIFIED.** SF-36 T<45 cannot be computed. **Correction to the t016 plan:** either substitute an available functional proxy (self-rated overall health change; questionnaire's own impact/limitation items if present — **[confirm in questionnaire schema]**) or drop arm (3) and state the 2-definition axis. Do **not** carry SF-36 T<45 into the pre-registration as if available |

**Net:** the outcome sensitivity axis is **partially feasible** — definition (1) is
solid, (2) is an approximation, (3) must be substituted or dropped. This is a
concrete, pre-registration-ready resolution of the outcome gate, replacing the t016
plan's optimistic "t017 only needs to ensure the cohort carries symptom-level data."

---

## 3. Outcome ascertainment schema (linkage fields & tables)

| Element | UKB field / linkage | Status | Rule |
|---|---|---|---|
| **Acute infection / time origin** | **Field 40100** — *Records of COVID-19 test results* (`covid19_result_england/scotland/wales`) | ✅ verified on Showcase (275,101 records, Mar 2020–Jun 2023) | First **PCR-positive** = time origin. **Pre-commit index rule:** earliest positive (incident-PACS framing) vs most-recent-before-questionnaire (precedent's LC framing). Recommend **earliest positive** for the survival time-origin, with the precedent's most-recent rule as a sensitivity arm |
| **Symptom LC outcome (Route A)** | Health & Well-Being questionnaire (WHO-Delphi 45-item) | category/field IDs in precedent Suppl. Table 5 — **[confirm IDs at application]** | Case = ≥1 WHO symptom ≥90d (def 1); ≥3-symptom as a robustness check (precedent: 594 vs 2,751 cases — **threshold is highly sensitive**, must be pre-committed) |
| **Coded PACS outcome (Route B)** | HES ICD-10 **U07.1 / U07.2 / U09.9** | available | Hospitalization-ascertained; triangulation + collider-control role (§6) |
| **Primary-care LC (optional)** | GP linkage (CTV3/Read) | ~45% partial coverage; **unused by precedent** | Community capture for a coverage-sensitivity arm only; not primary (differential coverage) |
| **Death / competing risk** | Field 40000 / 40001–40002 (U07.1/U07.2) | available | Censoring / competing-risk handling |
| **Acute severity (mediator)** | U07.1 vs U07.2, HES inpatient/ICU/O2 | available | Recorded; conditioned only for the *direct*-effect secondary estimand |

---

## 4. The questionnaire-response selection node (new admissibility concern)

Route A conditions the LC cohort on **completing the Health & Well-Being
questionnaire** — only ~201k of ~500k, and responders are not a random sample
(healthier, older, more engaged). This is a **selection node distinct from the
clinic-attendance collider** but in the same family: conditioning on a
post-baseline behaviour. It must be handled, not ignored:

1. **Primary:** restrict to questionnaire responders, **state the selection
   explicitly** as a generalizability bound (estimate is "in responders").
2. **IPW arm:** inverse-probability-of-response weights from baseline predictors
   (age, sex, IMD, education, baseline health) to reweight toward the full cohort.
3. **Triangulation veto/confirm:** re-estimate with the **Route B (HES-coded) PACS**
   outcome, which has a *different* selection (hospitalization, no survey response).
   An effect present in Route A but absent in Route B that tracks response-propensity
   flags response selection; agreement across the two differently-selected outcomes
   is the credibility lever. (This mirrors the t016 collider-negative-control logic.)

This selection node is added to the t016 admissibility discipline alongside the
clinic collider and the exposure-timing gate.

---

## 5. U-proxy & covariate measurement schema

Promotes the latent-U battery to measured covariates (partial back-door closure) and
fixes covariate **timing** and **missingness**. The whole-cohort battery is what the
t016 E-value is benchmarked against.

### 5.1 Whole-cohort U-proxy battery (available for all participants)

| Latent-U component | UKB field(s) | Timing | Coding |
|---|---|---|---|
| SES — deprivation | Townsend **189** (locked); IMD only via a **named** country-specific index-of-multiple-deprivation field **[confirm at application]** | baseline (area-level, fixed) | continuous + categorized; flag area-level temporal drift. **Amendment IMD (`report:0002`):** "IMD" is not a bare UKB field — use Townsend 189 as the primary deprivation measure; add a specific IMD field/derivation only if confirmed live, else drop the bare reference. |
| SES — education | **6138** | baseline | years-of-ed / degree flag |
| SES — income | **738** | baseline | self-report band; high "prefer not to answer" → missing |
| Ethnicity | **21000** | baseline | White / non-White (precedent); finer if N allows |
| Behaviour | smoking **20116**, alcohol **1558**, physical activity **22040**, BMI **21001** | baseline | never/prev/current; BMI normal/overweight/obese |
| Comorbidity (Charlson) | HES ICD-10 → Charlson index | **accumulated up to the COVID-test date** (pre-infection, time-correct) | precedent method; 19 conditions |
| Autoimmune history | self-report **20002** + HES ICD pre-test | baseline + pre-test | binary autoimmune-dx flag |

### 5.2 EBV — explicitly a subsample, explicitly modelled

Per your caution, EBV is **sensitivity-only unless the schema models the subsample
directly** — so it does:

- **Source:** **Category 1307** *Infectious Disease Antigens* (EBV VCA/EBNA/ZEBRA/EA-D),
  the UKB serology **pilot subsample ≈ 9,600 participants** (exact N **[confirm on
  Showcase]**) — **not** whole-cohort, and pre-infection by construction (baseline bloods).
- **Handling (explicit):**
  1. **Primary analysis runs WITHOUT EBV on the full cohort** ({age, smoking}-adjusted).
  2. **EBV-augmented arm runs on the ~9.6k subsample only**, with its **own reduced
     power floor** reported (this stratum is ~4% of the cohort — expect wide
     intervals, likely `underpowered`).
  3. **Do NOT impute EBV across the ~96% without serology** — there is no basis;
     imputation would fabricate the very confounder-control the arm exists to test.
- This realizes the t016 plan's "U-proxy adjustment arm (+prior-EBV)" as a
  *subsample* arm, not a whole-cohort covariate — the only honest implementation.

### 5.3 Covariate timing rules (pre-committed)

- **Age:** at **infection** (computed from 34/52 + index date), modelled as a flexible
  spline — *not* age at recruitment (t027 §4).
- **SES / education / behaviour / BMI:** **baseline 2006–2010** (fixed); the ~decade
  drift is a known limitation (precedent notes it attenuates rather than inflates).
- **Comorbidity:** **time-varying, censored at the COVID-test date** (pre-infection
  accumulation) — the only covariate that must respect infection-time ordering, and
  the basis for the baseline-vs-incident split the estimand-split arm needs.
- **EBV / autoimmune serology:** baseline subsample, pre-infection by construction.

### 5.4 Missingness rules (adopted from precedent, extended)

- **Covariate >50% missing → exclude** the covariate.
- **Covariate ≤50% missing → multiple imputation (MICE)**; report the imputation
  model and a complete-case sensitivity.
- **"Prefer not to answer" / "Do not know" → coded missing** (not a category).
- **Outcome non-response is NOT covariate-missingness** — questionnaire non-response
  is the §4 *selection* problem (restriction + IPW), never imputed as outcome.
- **EBV "missing" is structural** (not-in-subsample), handled by the §5.2 subsample
  design, never imputed.

---

## 6. Sensitivity-arm eligibility (which schema element serves which t016 arm)

| t016 sensitivity arm | Schema element it needs | Eligible? |
|---|---|---|
| **E-value bound** | whole-cohort measured-proxy battery (§5.1) as the benchmark | ✅ |
| **U-proxy adjustment arm** | `{age, IMD, education, smoking/PA/BMI, Charlson}` whole-cohort | ✅ |
| **+EBV arm** | Category 1307 subsample (§5.2) | ⚠️ eligible **on ~9.6k only**, power-reduced |
| **Collider negative control** | a differently-selected outcome/subsample | ✅ via **Route B HES-PACS** + questionnaire-response IPW (§4) |
| **Estimand-split** `{age, smoking}` vs `{age, smoking, baseline comorbidity}` | Charlson timestamped pre-infection (§5.3) | ✅ |
| **Outcome-definition axis** | def 1 / 2 / 3 (§2) | ⚠️ **partial** — def 1 ✅, def 2 approximation, def 3 infeasible-as-specified |
| **Exposure operationalization** (t020) | — | (owned by t020; not this schema) |

---

## 7. Corrections this schema pushes upstream

1. **COVID linkage pointer** → **field 40100** (verified live); the `Category 100090`
   pointer was wrong (= Diet). *(t027 updated.)*
2. **"No symptom-level PASC instrument" was too strong** → UKB has the WHO-Delphi
   **Health & Well-Being questionnaire**; symptom-level def-1 is feasible. *(Update
   t027 §5.2 / §11-#5.)*
3. **Functional-gate def 3 (SF-36 T<45) is not computable in UKB** → substitute or
   drop. *(Correction to the t016 plan's outcome axis.)*
4. **New selection node** — questionnaire-response selection (§4) — joins the
   admissibility discipline. *(Add to t016.)*
5. **No vaccination data in the precedent's analysis** — UKB vaccination linkage
   *exists* but was unused; this schema **includes** it as a mediator-path / era
   covariate **[confirm linkage category]**, improving on the precedent.

---

## 8. Reproducibility checklist (pre-registration inputs — outcome & covariates)

1. ✅ Outcome routes A (questionnaire, def 1 primary) + B (HES-PACS triangulation).
2. ✅ Index-date rule (earliest-positive primary; most-recent sensitivity).
3. ✅ Case-definition axis with **feasibility verdicts** (def 1 ✅ / def 2 approx / def 3 substitute-or-drop).
4. ✅ Questionnaire-response selection handling (restriction + IPW + Route-B triangulation).
5. ✅ Whole-cohort U-proxy battery + timing rules.
6. ✅ EBV ~9.6k-subsample arm (no imputation).
7. ✅ Missingness rules (>50% exclude; MICE ≤50%; PNA→missing).

(The exposure half of the pre-registration lock is t020's §8 checklist.)

---

## 9. Handoff

| Downstream | What this hands it |
|---|---|
| **t016 plan** | resolves the outcome operationalization gate (feasibility verdicts), adds the response-selection node, corrects def-3; the plan's last design gate is now closed |
| **`/science:pre-register`** | §8 (outcome/covariate) + t020 §8 (exposure) = the full confirmatory lock; runnable once UKB access is granted |
| **`/science:plan-pipeline`** | linkage→outcome-construction→covariate-assembly→QA execution order, once data is provisioned |
| **Triangulation (All of Us / Lifelines)** | the A/B dual-outcome logic transfers; each cohort re-anchors its own ascertainment + selection model |

**Verdict.** With t017 closed, **all three menopause→PAIS design gates are
resolved** (t027 fields, t020 exposure, t017 outcome/covariates). The t016 plan can
move to `ready-with-caveats` on the **design** axis; it remains **not-ready to
execute** only because **UKB data is not in hand** (the AMS access gate) and the
EBV/questionnaire-schema field IDs await live confirmation at application. The next
command is `/science:pre-register`, with the AMS application running in parallel.
