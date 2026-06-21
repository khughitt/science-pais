---
id: "doc:ukb-data-field-specification-2026-06-19"
title: "UK Biobank data-field specification & access plan for the menopause→PAIS total-effect analysis (t027)"
created: "2026-06-19"
updated: "2026-06-19"
related:
  - task:t027
  - task:t016
  - task:t017
  - task:t020
  - task:t015
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
  - patch-definition:menopause-pais-causal-dag
---

# UK Biobank data-field specification & access plan (t027)

Converts the t015 finding (**UK Biobank = primary t016 vehicle**) into a concrete,
application-ready data-field list and access plan. It is the bridge artifact
between the locked t016 analysis plan
(`entities/plans/2026-06-19-menopause-pais-total-effect-analysis-plan.md`) and the
two remaining design gates — **t017** (U-proxy / measurement schema) and **t020**
(questionnaire-staging misclassification) — after which `/science:pre-register`
becomes runnable.

**Scope of this document.** It specifies *what to request and how to derive each
analysis variable from UKB*, mapped to its causal role in the DAG
(`patch-definition:menopause-pais-causal-dag`). It does **not** re-derive the
estimand, the adjustment set, or the readiness verdict — those are locked in the
t016 plan and are referenced, not relitigated, here.

> **Field-ID verification status.** Field IDs are from the UK Biobank Showcase
> (`biobank.ndph.ox.ac.uk/showcase`). The five menopause/HRT IDs and the three
> assay IDs were carried from the t015/t016 thread and independently re-checked
> in review; the U-proxy, COVID-linkage, and EBV-serology category IDs added here
> are marked **[confirm at application]** and must be validated against the live
> Showcase when the Data Access Application (DAA) basket is assembled — Showcase
> field IDs are stable but category membership and return-array structure are not.

---

## 1. Why UK Biobank (recap, not re-argument)

Per the t015 audit, UKB is the **only** resource that simultaneously satisfies all
t016 vehicle-admissibility gates:

| Gate | UKB status |
|---|---|
| Population-based (low clinic-attendance **collider**) | ✅ ~500k volunteer population cohort, **not** care-seeking-recruited |
| Pre-infection baseline | ✅ baseline assessment 2006–2010, ~decade before SARS-CoV-2 |
| Natal-female-analysable | ✅ ~273k natal females (~54%) |
| Reproductive-stage stageable | ✅ questionnaire age-at-menopause + HRT + menarche |
| Usable hormone assays | ⚠️ testosterone + SHBG usable; **oestradiol censored** (175 pmol/L floor) |
| Linked long-COVID-engineerable outcome | ✅ PHE test results + HES + primary-care + death linkage |

The single decisive measurement constraint — **oestradiol is unusable for
postmenopausal staging** — is what forces the treatment node to be *questionnaire
reproductive stage*, which is exactly what the DAG already specifies. So the
vehicle's main weakness is *consistent with*, not a threat to, the locked design.

---

## 2. Population restriction (natal females)

Applied as a hard inclusion filter before any modelling — the population-definition
given of the estimand, not a covariate.

| Variable | Field | Use |
|---|---|---|
| Sex (self-reported, registry) | **31** | Primary natal-female filter (`Female`) |
| Genetic sex | **22001** | Cross-check; flag and review sex-mismatch records (do not silently drop) |

- **Inclusion:** field 31 = Female.
- **Sex-discordance handling:** where 31 ≠ 22001, quarantine for manual review
  rather than auto-exclude (could be sample mix-up or genuine; either way it
  affects denominator integrity). Report the count.
- The female-vs-male predominance contrast (q0007) is a **different estimand** and
  is explicitly out of scope; males are not a comparison arm here.

---

## 3. Treatment — reproductive stage at infection (feeds t020)

The exposure is **ordinal reproductive stage (pre → peri → post) assessed at the
acute-infection date**, *not* serum estradiol. This section lists the source
fields; the *operationalization and misclassification model* are t020's
deliverable and are only sketched here.

### 3.1 Questionnaire reproductive-stage fields (primary exposure source)

| Variable | Field | Role / use |
|---|---|---|
| Had menopause | **2724** | Baseline menopausal status (Yes/No/Not sure – had hysterectomy/Not sure – other) |
| Age at menopause (last menstrual period) | **3581** | Anchors natural-menopause timing; censoring for surgical menopause |
| Bilateral oophorectomy / had hysterectomy | **2834 / 3591** | **[confirm at application]** surgical-menopause flag — critical: surgical menopause breaks the age↔stage mapping and must be a separate stratum |
| Age at bilateral oophorectomy | **3882** | **[confirm at application]** — added per t029 amendment A2 (`report:0002`): required for the surgical age-at-surgery gradient (pre- vs post-FMP oophorectomy) and for clean pre-infection surgical exclusion. 2834 alone gives the flag, not the timing. |
| Ever used HRT | **2814** | HRT is a **mediator + confounded-by-indication** node — recorded, **not** adjusted (see §7) |
| Age started HRT | **3536** | HRT timing relative to infection |
| Age last used HRT | **3546** | **[confirm at application]** HRT exposure window vs infection date. **Amendment A3 (`report:0002`):** these three baseline HRT fields establish ever-use / start / last-use **at the 2006–2010 assessment**, *not* HRT status at 2020–2022 infection. Any "HRT-active-at-infection" tag (incl. the surgical HRT-stratification arm) therefore needs **GP/prescription linkage**, or is downgraded to "baseline HRT status / unknown at infection." |
| Age at menarche | **2714** | Reproductive-span covariate; t020 staging input |
| Number of live births / parity | **2734** | Pregnancy-history node (competing reproductive exposure) |
| Ever used oral contraceptive pill | **2784** | Exogenous-hormone history; staging nuisance |

### 3.2 The staging-at-infection problem (the load-bearing t020 issue)

UKB reproductive-stage variables are measured at **baseline (2006–2010)**, but the
exposure must be fixed at **infection (2020–2022)** — a **~10–14 year gap**. This
is the single largest measurement threat and is t020's core problem:

- Women **premenopausal at baseline** may be peri- or postmenopausal at infection →
  exposure must be **projected forward** from baseline age-at-menopause where
  reported, or age-band-imputed where not. Every projection is a misclassification
  source.
- Women **postmenopausal at baseline** are reliably postmenopausal at infection
  (monotonic) — the cleanest stratum.
- The **perimenopausal-at-infection** window — the biologically pivotal stratum for
  h0005 — is the **hardest to recover** from decade-old questionnaire data and will
  be the thinnest, most misclassified cell. t020 must deliver an explicit
  misclassification model (and the power-floor section of the t016 plan already
  flags this stratum as the dominant underpowering risk).
- **Repeat assessment:** the instanced fields above also exist at the imaging
  re-visit (instances 2–3) for a subset (~? **[confirm at application]**) — where a
  post-2012 re-measurement exists it tightens the projection for that subset and
  should be used preferentially.

> **Handoff to t020:** this section defines the *inputs*; t020 owns the STRAW+10 /
> age-band staging rule, the forward-projection algorithm, and the
> misclassification model. The binary "had menopause" (2724) alone is the
> Shah2025/Mishra2020-style operationalization and is a **sensitivity arm only** —
> it collapses the peri window the analysis most needs.

### 3.3 Sex-hormone assays — supporting, not primary (the oestradiol caveat)

| Analyte | Field | Usability | Use |
|---|---|---|---|
| Testosterone | **30850** | Usable | Continuous biomarker support for staging; secondary exposure axis |
| SHBG | **30830** | Usable | Free-androgen context; **nearest-precedent analyte** (Alcalde-Herraiz2025) |
| Oestradiol | **30800** | ⚠️ **censored** — assay floor **175 pmol/L**, ~¾ of (post)menopausal women below limit of detection (Tin Tin 2021) | **Do NOT use as a continuous postmenopausal exposure.** At most a coarse above/below-floor indicator; documented dead-end, retained only to show why questionnaire staging is used |

Sex-hormone assays were measured **mostly at baseline** (2006–2010), with a small
repeat-assessment subset (~2012–2013; testosterone and SHBG each carry two defined
instances) — but **none is an infection-time assay**, so they share the same
decade-gap projection problem as the questionnaire items: they characterize the
*baseline* hormonal milieu, not the milieu at infection.

---

## 4. Confounders — the primary measured adjustment set `{age, smoking}`

Per the critique-corrected DAG (v2, t023), the **primary measured adjustment set is
`{age, smoking}`** under natal-female restriction — **not** a "minimal-sufficient"
set: while U is latent **no valid sufficient adjustment set exists**, and v2 shows
that even with U set aside the formal minimal measured set is the full
`{age, smoking, baseline-comorbidity, baseline-BMI, parity, autoimmune-POI, frailty}`
battery. `{age, smoking}` is the committed measured-subset (t029 Q1); the rest are
sensitivity arms. Age is the dominant load-bearing covariate; smoking is the measured
strong common cause promoted alongside it.

| Variable | Field | Use |
|---|---|---|
| Year / month of birth | **34 / 52** | Compute **age at infection** = (infection date − DOB); this is the adjustment variable, **not** age at recruitment |
| Age at recruitment | **21022** | Baseline-age cross-check only |

- **Adjust age at infection**, not age at baseline — the confounding operates at the
  time origin (infection). Age at recruitment is a fixed offset and is the wrong
  conditioning variable.
- Model age flexibly (spline / fine bands), since age confounds the menopause→PAIS
  relationship strongly and non-linearly; a linear term risks residual confounding.
- **Smoking is the second primary covariate.** Code baseline smoking as
  never/former/current + pack-years/duration (fields 20116 + 20161/2887, confirm at
  application), modelled as a measured confounder (baseline smoking is pre-infection
  but not always pre-FMP).
- **Baseline cardiometabolic comorbidity is a confounder but NOT in the primary
  adjustment set.** In DAG v2 the `baseline-comorbidity → menopause-timing` edge is
  now drawn, so baseline comorbidity *is* a formal confounder — but it is **demoted to
  the pre-committed sensitivity arm** (§8) by judgement (timing/role ambiguity), not
  treated as ignorable. The same holds for baseline BMI, parity, autoimmune-POI, and
  frailty (t023 v2; t029 Q2/Q3). Note the **incident** comorbidity/adiposity
  components remain mediators and must never be adjusted.

---

## 5. Outcome — engineered long-COVID under the t002 case-definition axis

UKB has **no native long-COVID phenotype**; the outcome must be **researcher-engineered**
from linked records, under the t002-resolved definition discipline (WHO 2021 ≥3-month
primary, run across a 3-definition sensitivity axis).

### 5.1 Acute-infection ascertainment (the time origin)

| Source | Field / linkage | Use |
|---|---|---|
| PHE/UKHSA COVID-19 test results | **Field 40100** — *"Records of COVID-19 test results"* ✅ **verified on Showcase** (275,101 records, Mar 2020–Jun 2023; grants the `covid19_result_england/scotland/wales` tables = the PHE SGSS linkage used by AlcaldeHerraiz2025) | Primary positive-test date = **time origin**. (The earlier `Category 100090` pointer was wrong — that is *Diet by 24-hour recall*.) |
| Hospital inpatient (HES/PEDW/SMR) COVID episodes | ICD-10 **U07.1 / U07.2** | Severity + ascertainment where untested |
| Primary-care COVID codes | GP linkage (CTV3/Read v2) **[confirm — partial coverage ~45%]** | Community-managed infection capture |
| Death registry | **40000 / 40001–40002** (U07.1/U07.2) | Competing-risk / censoring |

- **Time origin** = first documented SARS-CoV-2 infection date.
- **Denominator** = infected natal females with a usable baseline — *not* a
  test-seeking subset where avoidable (testing-access is a mild selection concern,
  recorded as a limitation).
- **Reinfection / variant era / vaccination status** are mediator-path confounders
  (§7) and are coded from linkage + vaccination records **[confirm category]**.

### 5.2 Long-COVID / PAIS outcome construction (3-definition sensitivity axis)

Engineer **three** pre-committed operationalizations (matching the t016 plan, so the
verdict carries a definition-stability check):

> **Superseded by t017** (`doc/methods/2026-06-19-ukb-outcome-and-uproxy-measurement-schema.md`).
> The precedent (AlcaldeHerraiz2025) shows UKB **does** have a symptom-level
> instrument — the WHO-Delphi **Health & Well-Being questionnaire** — so the
> outcome is built primarily from that (Route A), with HES-coded PACS as
> triangulation (Route B). The feasibility verdicts below are corrected in t017 §2;
> the table here is retained for context only.

| # | Operationalization | UKB construction | t017 feasibility |
|---|---|---|---|
| 1 | **WHO 2021 ≥3-month** (primary) | ≥1 WHO-Delphi symptom ≥90d post-PCR from the **Health & Well-Being questionnaire** (Route A); HES/U09.9 as Route-B triangulation | ✅ feasible |
| 2 | **PEM-weighted (RECOVER PASC-index analogue)** | symptom-count/fatigue-weighted proxy from the questionnaire — **no PASC-index/PEM instrument in UKB** | ⚠️ approximation only |
| 3 | **WHO + functional-impairment gate** | **SF-36 T<45 is not in UKB** → substitute an available functional proxy or drop the arm | ❌ not feasible as specified |

- **U09.9** ("Post COVID-19 condition") ICD-10 code anchors the Route-B coded outcome
  but was **not** used by the precedent (which relied on the questionnaire); coverage
  is partial and clinician-coding-dependent (an outcome-misclassification source).
- **Outcome model:** time-to-resolution (Cox/Weibull) where longitudinal codes
  permit, else PAIS-present-at-fixed-follow-up (log-binomial), per the t016 plan.
- A long-COVID signal **present only under definition 1** likely reflects
  PEM-negative prolonged recovery (changes the h0005 interpretation) — this is the
  definition-stability test, not a robustness footnote.

> **Caveat carried forward (refined by t017):** UKB **does** carry a symptom-level
> WHO-Delphi instrument (Health & Well-Being questionnaire), so def-1 is
> symptom-level — but it is **not PEM-specific** (no PASC-index, no CPET/PEM item),
> so def-2 remains an approximation and any PEM-stratified claim (q0015/t025) cannot
> be fully served by UKB alone (consistent with the t002 finding).

---

## 6. U-proxies — promoting latent U to measured covariates (feeds t017)

The total effect is **not identifiable by adjustment** while U (SES, prior EBV,
autoimmunity, genetic/HLA risk, behaviour) is latent. These fields **partially
close the back-door** and define the t016 plan's "U-proxy adjustment" sensitivity
arm and the E-value benchmark. **t017 owns the final schema**; this is the UKB
field mapping it should consume.

| Latent-U component | UKB proxy | Field(s) | Notes |
|---|---|---|---|
| Socioeconomic status | Townsend deprivation index | **189** | Primary SES proxy (area-level) |
| | Average household income | **738** | **[confirm]** self-reported band; missingness |
| | Educational qualifications | **6138** | Derive years-of-education / degree flag |
| Prior EBV exposure | EBV antigen serology (VCA p18, EBNA-1, ZEBRA, EA-D) | **Category 1307** **[confirm]** | ⚠️ **serology subsample only (~9,600)** — *not* whole-cohort; usable as a sensitivity/triangulation arm, **not** a primary adjustment covariate. This is a major t017 constraint |
| Autoimmune history | Self-reported non-cancer illness | **20002** (+ HES ICD autoimmune codes) | Pre-infection autoimmune dx flag |
| Genetic / HLA risk | HLA imputation + PRS | **22182** (HLA) / PRS fields **[confirm]** | Optional deep U-proxy; analysis-heavy, defer to t017 priority call |
| Health behaviour | Smoking / alcohol / physical activity / BMI | **20116 / 1558 / 22040 / 21001** | Behavioural back-door proxies; BMI also cardiometabolic |

- **The EBV-serology subsample (~9.6k) is the critical limitation:** prior-EBV
  cannot enter the *primary* adjustment without collapsing N by ~96%. Treatment:
  whole-cohort analysis on {age}, with a **subsample sensitivity arm** adding EBV —
  exactly the partial-identification logic the t016 plan specifies. t017 must
  decide the subsample-vs-proxy tradeoff explicitly.
- **E-value benchmark:** the measured-proxy battery here is what the t016 E-value is
  benchmarked *against* — "how strong an unmeasured U, relative to SES+autoimmune+behaviour,
  would explain away the effect."

---

## 7. Mediators & mediator-path confounders — measure, do not adjust (primary)

Recorded for the **secondary direct-effect estimand** and mediator-path sensitivity
only. **None enters the primary total-effect adjustment.**

| Node | Role | UKB field(s) | Handling |
|---|---|---|---|
| Sex hormones | Mediator (first line) | 30850 / 30830 / (30800) | Do not adjust (total effect) |
| Hormone therapy | Mediator + confounded-by-indication | 2814 / 3536 / 3546 | Do not adjust; separate target-trial estimand (t019) |
| Acute severity | Mediator | U07.1 vs U07.2, ICU/HES, O2 codes | Condition only for the *direct* effect (secondary) |
| Cardiometabolic comorbidity (baseline) | Sensitivity-arm covariate only | 6150 / 2443 / 21001 / HES ICD | Time-split: baseline vs incident; §8 arm only |
| Vaccination / reinfection / variant era | Mediator-path confounder | vaccination linkage + calendar **[confirm]** | Era-harmonization sensitivity |
| Immune / endothelial / autonomic markers | Mediator (mechanism) | sparse in UKB | Mostly unavailable at infection; not a primary input |

---

## 8. Pre-committed sensitivity arms (UKB realization)

Mapping the t016 plan's Sensitivity Arbitration block onto UKB fields:

1. **E-value** — for the {age}-adjusted point estimate and the near-null CI limit;
   benchmarked against the §6 measured proxies.
2. **U-proxy arm** — `{age, Townsend, education, autoimmune-hx, behaviour}` on the
   whole cohort; **+EBV** on the ~9.6k serology subsample.
3. **Collider negative control** — re-estimate within a HES/clinic-ascertained
   subsample; a signal appearing there but absent in the population frame *confirms*
   the collider and vetoes clinic-derived literature estimates.
4. **Estimand-split** — `{age}` vs `{age, baseline comorbidity}` (fields 6150/2443/21001);
   valid only under the DAG-v2 comorbidity→menopause-timing edge (t023); report both,
   do not average.
5. **Operationalization sensitivity** — STRAW+10-projected ordinal (primary, t020)
   vs binary-2724 (secondary); and the 3-definition outcome axis (§5.2).

---

## 9. Access plan & timeline

UKB is **not** open-access; analysis requires an approved application and is
**gated, not in-hand** — this is the residual reason the t016 verdict stays
`not-ready`.

| Step | Action | Notes / dependency |
|---|---|---|
| 1 | Register / confirm an **Approved Research** account on the UKB Access Management System (AMS) | Institutional affiliation + bona-fide-researcher check |
| 2 | Submit / amend a **project application** with the menopause→PAIS aim | Must cover the COVID + GP/HES + serology return categories |
| 3 | Assemble the **field basket** from §2–§7; verify every **[confirm at application]** ID on the live Showcase | The field list in this doc is the basket draft |
| 4 | Request **record-linkage returns**: PHE/UKHSA COVID tests, HES, primary-care GP, death, vaccination | GP linkage is **partial (~45%)** — a coverage limitation, not a blocker |
| 5 | Pay access fee / await provisioning; data delivered to a **UKB RAP** (Research Analysis Platform, DNAnexus) or download per current policy | Cost + RAP-compute budget item |
| 6 | On provisioning, run **input QA** per the t016 plan's Required Input Inspection (sampling-frame, exposure-timing, outcome-definition, U-proxy-completeness, independent-unit audits) | Gates execution |

**Critical-path dependency:** steps 1–2 (account + application approval) typically
take **weeks to a few months** and are the true rate-limiter — they should start in
parallel with t017/t020, not after, since the *design* gates and the *access* gate
are independent.

> This is a future external obligation with no fixed date yet (application not
> submitted), so it is **not** a `/schedule` candidate until an application ID and
> an AMS decision ETA exist.

---

## 10. Triangulation / replication arms (per t015)

UKB alone cannot carry the verdict (no symptom-level PEM, censored oestradiol,
partial GP coverage). Pre-specify replication:

| Cohort | Role | Adds | Limit |
|---|---|---|---|
| **All of Us** | US primary/replication | Survey+EHR menopause; some hormone labs; pre-2020 enrollees | Volunteer self-selection; sparse hormone N; U09.9 ascertainment |
| **Lifelines** | EU replication | Population, pre-infection baseline, matched-control long-COVID (Ballering2022) | No baseline hormone assays; self-report menopause |
| **Generation Scotland** | EU replication | Population/family, age-at-menopause + HRT | No hormone panel; thin long-COVID (CovidLife ~5k) |
| ONS-CIS / N3C | Triangulation only | Large-N, low-collider | No menopause/hormone depth — age-proxied effect only |

Replication runs the **same {age}-only estimand under the same definition axis**;
cross-cohort agreement (hierarchical/frailty pooling, study as random intercept) is
the credibility lever, given each cohort's distinct biases.

---

## 11. Known limitations to carry into pre-registration

1. **Oestradiol censored** (175 pmol/L floor) → exposure is questionnaire staging,
   not serum estrogen. *(Consistent with the DAG; not a defect.)*
2. **~10–14 yr baseline→infection gap** → forward-projection misclassification,
   worst in the peri window (t020).
3. **EBV serology in ~9.6k subsample only** → prior-EBV is a sensitivity arm, not a
   primary covariate (t017).
4. **GP linkage ~45% partial** → community long-COVID under-ascertainment.
5. **No symptom-level PEM** → outcome definition 2 is an approximation; PEM-stratified
   claims under-served (t002/t025).
6. **Testing-access selection** in early-pandemic COVID ascertainment → mild
   denominator selection, recorded.
7. **Partial identification persists** → even the full U-proxy battery does not point-identify
   the total effect; the E-value bound is load-bearing, not decorative.

---

## 12. Handoff

| Downstream | What this spec hands it |
|---|---|
| **t017** (measurement schema) | §6 U-proxy field map + the EBV-subsample tradeoff + §7 mediator field map to formalize into the minimum schema |
| **t020** (staging misclassification) | §3.1 questionnaire fields + §3.2 forward-projection problem statement to build the STRAW+10/age-band model |
| **`/science:pre-register`** | the full field basket + 3-definition outcome axis + 5 sensitivity arms, runnable once t017/t020 lock and an access decision exists |
| **`/science:plan-pipeline`** | §9 access→QA→staging→model→sensitivity execution order, once data is provisioned |

Until t017 and t020 close and a UKB access decision is in hand, the t016 plan
remains **not-ready** for the narrow, documented reasons — this spec resolves the
*vehicle-field* uncertainty but not the *access* or *measurement-model* gates.
