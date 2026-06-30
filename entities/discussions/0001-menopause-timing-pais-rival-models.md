---
id: "discussion:0001-menopause-timing-pais-rival-models"
type: "discussion"
title: "Rival models for the menopause-timing↔long-COVID association (h0005 vs aging / selection / SES)"
status: "active"
source_refs:
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
  - question:0007-mechanism-of-female-predominance-in-pais
  - pre-registration:0001-menopause-pais-total-effect
  - report:0001-bias-audit-menopause-pais-total-effect
related:
  - patch-definition:menopause-pais-causal-dag
  - topic:menopause-sex-hormones-and-pais-risk
  - paper:AlcaldeHerraiz2025
  - paper:Shah2025
  - task:t016
created: "2026-06-19"
updated: "2026-06-19"
---

# Hypothesis Comparison: rival models for the menopause-timing↔long-COVID association

This is a **rival-model packet**, not a two-hypothesis duel. The *phenomenon* is
fixed: in midlife/older women, **earlier age at menopause / later reproductive-stage
status is (expected to be) associated with higher long-COVID risk** — the contrast
the committed `pre-registration:0001-menopause-pais-total-effect` will estimate in UK
Biobank. The scientific question is **which account(s) explain that association**, and
in particular whether a residual `h0005` contribution survives once the rivals are
bounded. q0013's own "Thoughts" already names five competitors; this packet collapses
them into four bounded models and — the payoff — ties each **discriminating test to a
specific committed pre-reg sensitivity arm**.

A note on what `h0005` actually claims, because it changes the logic: `h0005` is a
**threshold-*modifier*** claim ("reproductive-stage transition shifts the immune
homeostatic margin"), explicitly **not** "menopause directly causes PAIS." So the
rivals below are **not** falsifiers of `h0005` in the strict sense — they compete for
*shares of the same observed association*. The realistic truth is a **mixture**; the
estimand's job (partial identification + E-value) is to bound the **non-rival
residual** that `h0005` would own.

---

## Hypotheses Compared

### M1 — Reproductive-stage / hormone-timing effect (`h0005`)
*Layer: `causal_effect` resting on a `mechanistic_narrative`.*
Declining/changing sex-hormone exposure across the menopausal transition lowers the
immune-homeostatic margin (antiviral resolution, Treg/Tfh/Th17 balance, type-I-IFN/B-cell
tone, endothelial/thromboinflammatory state, autonomic regulation), so the same acute
infection more often fails to resolve. **Earlier/longer-post-menopausal exposure →
higher failed-recovery risk**, operating *through* hormone-driven mediators.
**Essential proposition:** a residual association survives flexible age adjustment **and**
U-proxy adjustment **and** is (at least partly) mediated by immune/endothelial/autonomic
markers. **Optional:** monotonic dose-response; peri as the pivotal window.

### M2 — Chronological aging / immunosenescence (no sex-hormone-specific effect)
*Layer: `causal_effect` (age), with menopause timing as a noisy `empirical_regularity` marker.*
The association is **chronological/biological aging** — immunosenescence, inflammaging,
thymic involution, accumulated comorbidity — for which **age at menopause is merely a
correlated age-marker** with no independent hormonal channel. **Essential
proposition:** the menopause-timing effect **collapses under sufficiently flexible age
adjustment**; no residual after a spline on age-at-infection. Predicts no incremental
information from SHBG/testosterone once age is controlled, and a mechanistically
**sex-shared** (not hormone-specific) aging process.

### M3 — Selection / collider artifacts
*Layer: `structural_claim`.* The association is (wholly or partly) **manufactured by
conditioning**, via three distinct nodes flagged in the bias audit:
- **M3a left-truncation / survival-to-2020** — every analyzed woman survived baseline
  (2006–2010) → infection (2020–2022) at age ≈52–83. Earlier menopause ↔ higher
  all-cause/CV mortality, so the earliest-menopause (high-exposure) stratum is
  **differentially depleted before the time origin** → distorts the estimate (most
  plausibly toward the null, possibly other directions under effect heterogeneity).
- **M3b questionnaire-response propensity** — Route-A conditions on completing the
  2022–2023 Health & Well-Being questionnaire; responders are non-random and propensity
  may depend on *post-baseline* (incipient-LC) health.
- **M3c clinic-attendance collider** — the menopause↔long-COVID clinical literature
  (Stewart2024/Humphreys2025) is recruited from post-COVID clinics, conditioning on
  care-seeking (a collider) that can create the association de novo.

### M4 — SES / healthcare-access confounding (the latent U)
*Layer: `causal_effect` via confounding.* A common cause — **socioeconomic deprivation,
smoking, adverse life-course exposures** — drives **both** earlier menopause **and**
higher long-COVID risk/ascertainment. The menopause-timing→LC association is then
**confounded**, not causal. This is precisely the latent **U** the E-value is meant to
bound. **Essential proposition:** the effect **attenuates substantially under the
U-proxy adjustment arm**, and its E-value sits **below** the measured-proxy benchmark.

---

## Proposition-Level Comparison

| Proposition | M1 hormone | M2 aging | M3 selection | M4 SES-conf. |
|---|---|---|---|---|
| Association exists in the population frame | needs it | needs it | **denies** (artifact of conditioning) | needs it |
| Survives **flexible age** adjustment | **requires** | **denies** | agnostic | requires |
| Survives **U-proxy** adjustment / high E-value | **requires** | agnostic | agnostic | **denies** |
| Agrees across Route A (survey) & Route B (HES) | requires | requires | **denies** (M3b) | agnostic |
| Present in population frame but **absent** in clinic-selected subsample | predicts | predicts | **reversed** (M3c: present only when selected) | agnostic |
| Mediated by immune/endothelial/autonomic markers | **requires** (unique) | denies | denies | denies |
| Negative-control outcome (injury code) is **null** | predicts | predicts | **may be non-null** (residual selection) | **may be non-null** (residual confounding) |
| Strengthens after modelling survival depletion | compatible | agnostic | **predicts** (M3a unmasks) | agnostic |

The two rows that **uniquely** separate models are bolded conceptually: **mediation by
hormone-responsive markers** is M1's only positive signature, and **clinic-subsample
reversal** is M3c's only positive signature. Everything else is shared or
attenuation-direction.

---

## Evidence Inventory

| Evidence | Bears on | Reading |
|---|---|---|
| Shah2025 — female LC excess sharpest at **40–54**, smaller at ≥55 | M1 vs M2 | **Ambiguous and pivotal.** A midlife (peri-aged) peak that is *not* monotonic in age is mild evidence *against* pure M2 (pure aging predicts monotone increase) and *for* a transition-window (M1) reading — but age and menopausal status are not separated, so it is equally consistent with a midlife-specific **ascertainment** (M3b) pattern. |
| Stewart2024 / Humphreys2025 — menopause↔LC symptom overlap in **clinic** samples | M3c, measurement | Supports M3c (collider-recruited) and a symptom-overlap measurement threat; does **not** establish causation. The pre-baseline UKB design is specifically chosen to neutralize this. |
| Mishra2020 / Costeira2021 — menopause/hormone proxies lose independence after adjustment (acute COVID) | M2, M4 | Supports that the crude signal is **substantially** aging/confounding-driven; but tests acute outcomes, not post-acute persistence. |
| Averyanova2022 — hormone→immune/endothelial mechanistic plausibility | M1 | Indirect plausibility only; **no PAIS-specific mediation demonstrated**. M1's mechanistic narrative is under-supported at the lower layer. |
| Rebman2026 — sex/menopause affect acute vs post-acute differently | M1, M2 | Weakens any simple monotonic hormone-protection story; nudges toward "modifier, not monotone cause." |
| AlcaldeHerraiz2025 — UKB SHBG female-specific signal | M1 | Suggestive single-source support for a hormone channel — but it is the **same paper** the whole feasibility frame depends on (corpus-closure caveat, see bias audit); not independent. |

**Where uncertainty concentrates:** M1's *positive* signature (hormone-marker
mediation) is the **least-supported** proposition in the whole packet and the one UKB
can **least** test (UKB oestradiol is censored at 175 pmol/L, immune/endothelial
markers are sparse at infection, and the peri cell is near zero [@AlcaldeHerraiz2025]).
M3a (survival depletion) is **newly identified** and currently **unquantified**.

---

## Discriminating Predictions

The committed pre-reg sensitivity arms are, in effect, tests designed to move one rival.

This is the operational core.

| Pre-reg arm (committed) | Primary discriminator between | If effect… |
|---|---|---|
| **Flexible age spline** + **estimand-split {age} vs {age, baseline comorbidity}** | M1 vs **M2** | …dies under fine age control → **M2** wins. …survives → M2 weakened, M1/M4 live. |
| **E-value vs measured-proxy benchmark** + **U-proxy adjustment arm** (+EBV on ~9.6k) | M1 vs **M4** | …collapses under U-proxies / E-value below benchmark → **M4** wins. …E-value beats benchmark → M4 weakened. |
| **Route A vs Route B agreement** + **response-propensity IPW** | M1 vs **M3b** | …Route-A-only & tracks response → **M3b** artifact. …concordant A/B → M3b weakened. |
| **Collider negative-control** (clinic-ascertained subsample) | M1 vs **M3c** | …present *only* when clinic-selected → **M3c** (veto: `collider_confounded`). …present in population frame → M3c weakened. |
| **Negative-control outcome** (injury/accident code → expect null) | M1 vs **M3+M4 residual** | …non-null → residual selection/confounding contaminates the whole design. …null → both weakened. |
| **NEW: competing-prior-event / survival sensitivity** (audit-added) | bounds **M3a** | …effect strengthens after modelling depletion → true effect was **masked** (supports M1/M4 over null). …unchanged → M3a small. |
| **Mediation (SHBG/testosterone; markers where present)** *(exploratory in UKB)* | M1 **positive** test | …mediated → unique **M1** support. …no mediator / sparse → M1 **unconfirmable in UKB** → triangulation required. |

**The load-bearing asymmetry:** the committed UKB design is **strong at refuting M1**
(a powered, definition-stable, bias-adjusted null after all arms = a real downward
update) but **weak at confirming M1** (its unique positive signature — hormone-marker
mediation — is exactly what UKB cannot measure well). So a UKB "supports" verdict is
inherently *softer* than a UKB "weakens" verdict. This mirrors the pre-reg's own
direction-over-magnitude posture and is the honest ceiling on what UKB alone can buy.

---

## Discriminating Evidence Needed (beyond the committed arms)

1. **Hormone-measured / STRAW+10-staged longitudinal cohort with immune-endothelial
   markers** — the only evidence that can give M1 its *positive* mediation signature.
   UKB cannot (censored oestradiol, no FSH/AMH, sparse markers). → the triangulation
   cohorts (All of Us / Lifelines) and any future hormone-panel cohort. Highest M1
   discriminatory power; currently the project's biggest gap.
2. **Within-person / discordant design** (e.g. surgical vs natural menopause timing;
   sibling/discordant-twin) — breaks M4 (shared SES background) and M2 (chronological
   age) more cleanly than covariate adjustment. Surgical-menopause stratum is already
   carved out in t020 §3 as a separate stratum — it is a **natural quasi-experiment**
   for the hormone channel (abrupt, less SES-correlated) and deserves promotion from
   "nuisance stratum" to a **discriminating contrast**.
3. **Quantified survival-depletion bias** (M3a) — a competing-risk / left-truncation
   simulation using published age-at-menopause→mortality hazards, to bound how much the
   aged-cohort design attenuates the estimate *before* interpreting any null.

---

## Rival-Model Packet

- **M1 hormone-timing modifier** — core claim: a residual hormone-mediated
  failed-recovery effect survives age + SES adjustment. Most distinguishing
  observation: **mediation through hormone-responsive immune/endothelial/autonomic
  markers** (and the surgical-menopause quasi-experiment showing an effect despite
  weaker SES correlation).
- **M2 chronological aging** — core claim: menopause timing is a noisy age-marker with
  no hormonal channel. Most distinguishing observation: **effect vanishes under a
  flexible age spline**.
- **M3 selection artifact** (a survival / b response / c collider) — core claim: the
  association is conditioning-induced. Most distinguishing observation: **divergence
  between population-frame and selected-subsample estimates** (Route A vs B; clinic
  negative control; survival sensitivity).
- **M4 SES/healthcare-access confounding** — core claim: deprivation is the common
  cause. Most distinguishing observation: **attenuation under the U-proxy arm with a
  sub-benchmark E-value**.
- **`current_working_model`:** *set, but weakly.* The project favors **M1 as a
  contributor**, but on **current (pre-data) evidence the bulk of the observed midlife
  excess is better explained by M2 + M4**, with **M3 a live, partly-unquantified
  artifact threat** and **M1's independent share unproven**. M1 is the *motivating* model,
  not the *best-supported* one.

---

## Current Verdict

**Contested → insufficiently resolved**, with a clear structure:

- **M1 (`h0005`)** is **more fragile** than its centrality in the thread implies. Its
  essential *positive* proposition (hormone-marker mediation) is the least-supported
  claim in the packet and the one the committed vehicle can least test. Its survival of
  age/SES adjustment is *plausible* but unobserved.
- **M2 (aging)** and **M4 (SES)** are, on current literature (Mishra2020, Costeira2021,
  the non-monotone Shah2025 age pattern), the **better-supported default explanations**
  for the crude association — which is exactly why the pre-reg's {age}-spline,
  estimand-split, U-proxy arm, and E-value are load-bearing rather than decorative.
- **M3 (selection)** is a **live artifact threat**, now with M3a (survival depletion)
  added and unquantified; it cannot be dismissed pre-data.

The packet does **not** crown a winner. It converts the bias audit's caveats into
**named, arm-matched discriminators**, and surfaces one strategic correction: **promote
the surgical-menopause stratum from nuisance to discriminating quasi-experiment**, and
**recognize that UKB can refute but barely confirm M1** — so the hormone-measured
triangulation cohort is not optional polish but the only path to M1's positive test.

---

## Synthesis Or Coexistence

These are **not mutually exclusive** — they almost certainly **partition** the observed
association. The scientifically honest target is **not "which one"** but **"what residual
share remains for M1 after M2 + M3 + M4 are bounded,"** which is precisely the
partial-identification estimand the pre-reg commits to. Two consequences:

1. A **mixture interpretation should be pre-stated** as the expected truth, so a
   partial attenuation (effect shrinks under U-proxies but does not vanish) is read as
   "M1-share bounded-but-nonzero," not forced into a binary supports/refutes.
2. No new hypothesis is warranted yet — M1 already encompasses the "modifier within a
   mixture" framing. But the **surgical-menopause quasi-experiment** is concrete enough
   that, if promoted, it could justify a focused sub-question (candidate for
   `/science:add-hypothesis` later, not now).

---

## Focus

Adjudicate which account(s) explain the menopause-timing↔long-COVID association that
`pre-registration:0001` will estimate in UK Biobank: **M1** hormone-timing modifier
(`h0005`), **M2** chronological aging, **M3** selection artifacts (survival /
response / collider), **M4** SES-confounding — and whether a residual M1 share
survives once the rivals are bounded. Grounded in q0013, q0007, the
`menopause-pais-causal-dag`.

## Current Position

The **working model is M1-as-contributor, held weakly**. On pre-data evidence the
bulk of the crude association is better explained by **M2 + M4**, with **M3 a live,
partly-unquantified artifact threat** (now including M3a survival-depletion) and
**M1's independent, hormone-mediated share unproven**. M1 is the *motivating* model,
not the *best-supported* one. Verdict: **contested → insufficiently resolved**.

## Critical Analysis

The decisive structural finding is an **asymmetry**: the committed UKB design can
**refute** M1 (a powered, definition-stable, bias-adjusted null after all arms = real
downward update) but can barely **confirm** it, because M1's unique positive signature
— mediation through hormone-responsive immune/endothelial/autonomic markers — is
exactly what UKB cannot measure (oestradiol floor-censored, FSH/AMH absent, markers
sparse, peri cell ≈ 0). The rivals are **not mutually exclusive**; they partition the
association, so the honest target is the M1 *residual share*, not a binary winner. Each
rival maps to a committed sensitivity arm (see *Discriminating Predictions* table), so
the bias audit's caveats are now arm-matched discriminators rather than loose worries.

## Evidence Needed

1. A **hormone-measured / STRAW+10-staged cohort with immune-endothelial markers** —
   the only path to M1's positive mediation test (UKB cannot supply it; triangulation
   via All of Us / Lifelines / a hormone-panel cohort).
2. The **surgical-menopause quasi-experiment** — abrupt, less SES-correlated; promote
   from t020 nuisance stratum to a discriminating contrast against M2/M4.
3. A **quantified survival-depletion (left-truncation) bias** simulation to bound M3a
   before any null is interpreted.

## Prioritized Follow-Ups

1. **(P1)** Promote the surgical-menopause stratum to a pre-specified discriminating
   contrast in the pre-reg's exploratory arms (M1-vs-M2/M4 quasi-experiment).
2. **(P2)** Add an M3a left-truncation / competing-prior-event bias simulation to the
   execution plan (already added as a pre-reg limitation; this makes it a concrete
   analysis step).
3. **(P2)** Carry the M1 positive-mediation test explicitly into the triangulation-cohort
   arms, since UKB cannot perform it — the verdict's upward path depends on it.
