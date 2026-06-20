---
id: "doc:surgical-menopause-discriminating-contrast-2026-06-19"
title: "Surgical menopause as a discriminating contrast (M1 vs M2/M4) for the menopause→PAIS analysis (t030)"
created: "2026-06-19"
updated: "2026-06-19"
related:
  - task:t030
  - task:t016
  - task:t020
  - task:t028
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
  - pre-registration:0001-menopause-pais-total-effect
  - report:0001-bias-audit-menopause-pais-total-effect
  - discussion:0001-menopause-timing-pais-rival-models
  - patch-definition:menopause-pais-causal-dag
---

# Surgical menopause as a discriminating contrast (M1 vs M2/M4) (t030)

Decides **whether and how** the surgical-menopause stratum — currently a set-aside
nuisance stratum in the exposure model (t020 §3 Step 0) — becomes a **pre-specified
discriminating contrast** that separates the rival explanations of the
menopause-timing↔long-COVID association
(`discussion:0001-menopause-timing-pais-rival-models`):

- **M1** — reproductive-stage / hormone-timing modifier (`h0005`)
- **M2** — chronological aging / immunosenescence
- **M4** — SES / healthcare-access confounding

> **Hard boundary (the thing to preserve).** This contrast is **discriminating /
> triangulating only**. It does **not** replace, dilute, or re-weight the **primary
> natural-menopause-timing estimand** of `pre-registration:0001`. Surgical cases stay
> **out** of the natural-transition dose-response (per t020 §6); they are analyzed as a
> **separate, explicitly-labelled arm** whose result informs *interpretation* of the
> primary, never the primary estimate itself.

---

## 1. Why surgical menopause discriminates

Natural menopause **timing** is correlated with both chronological age (M2) and the
SES/life-course gradient (M4) — which is exactly why the primary estimand needs the
age spline, U-proxy arm, and E-value to bound those rivals. **Bilateral oophorectomy
induces an abrupt, near-total estrogen withdrawal whose *timing* is set by surgical
indication, not by ovarian aging.** That makes it a *more exogenous* hormone shock:
its correlation with chronological aging is weaker, and (the empirical question) its
correlation with the SES gradient may also be weaker or differently-signed than
natural-menopause timing.

So if **M1** is a real contributor, an abrupt surgical estrogen withdrawal should carry
the **same directional** long-COVID association the natural-timing exposure predicts —
arising through a channel that M2 (aging) and M4 (SES) do **not** share. If the natural
association is purely M2/M4, surgical withdrawal at a given age + SES should add **no**
risk.

**This is a quasi-experiment, not a clean instrument.** It trades one confounding
structure (age/SES correlation of natural timing) for another (**surgical
indication**). The whole value of the contrast hinges on whether the indication
confounding can be bounded — §4, §6.

---

## 2. The contrast and estimand

Within natal females with a usable pre-infection baseline and a documented infection
(same population frame as the primary):

- **Exposure of interest:** **bilateral oophorectomy before infection** (= surgical
  postmenopause / abrupt total estrogen withdrawal), characterised by **age at
  surgery** and **time-since-surgery at infection**.
- **Comparison:** natural postmenopausal women, **matched / adjusted on age-at-infection
  and time-since-menopause**, so the contrast isolates *mode* of estrogen withdrawal
  (abrupt-surgical vs gradual-natural) at comparable age and post-menopausal duration.
- **Estimand:** the {age}-adjusted RR of WHO ≥90-day long-COVID (Route A primary,
  Route B triangulation — same outcome machinery as the primary) for surgical vs
  natural postmenopause, with the **key planned sub-contrast on age-at-surgery**:
  - **Pre-menopausal bilateral oophorectomy** (surgery before expected natural FMP) =
    the **largest hormone shock** → M1 predicts the **strongest** signal here.
  - **Post-menopausal bilateral oophorectomy** (ovaries removed when already low-estrogen)
    = **minimal additional hormone change** → M1 predicts **little/no** added signal.
    This within-surgical gradient is itself a **built-in negative control** for the
    hormone-withdrawal mechanism, less vulnerable to indication confounding than the
    surgical-vs-natural contrast.

The estimand is reported as a **standalone arm**; the primary natural-timing RR is
estimated on the natural-menopause population **with surgical cases excluded**, exactly
as in the committed pre-reg.

---

## 3. Inclusion / exclusion

| Group | Rule | Fields (confirm at application) |
|---|---|---|
| **Surgical-menopause case** | **Bilateral oophorectomy** (both ovaries) with surgery date **before** infection | bilateral oophorectomy **2834** + age-at-oophorectomy **[confirm: 3882]** |
| **Age-at-surgery split** | pre- vs post-natural-FMP at surgery (relative to self-reported/age-projected natural timing) | derived from 2834-age vs 3581 / age-band projection |
| **Natural-menopause comparator** | natural postmenopause (t020 Step 1), **no oophorectomy** | 2724 + 3581 |
| **EXCLUDE from this contrast — hysterectomy without oophorectomy** | womb removed, **ovaries retained** → **not** surgical menopause; ovarian function continues silently, FMP unobservable | hysterectomy **3591** ∧ ¬2834 |
| **EXCLUDE — unilateral / partial oophorectomy** | not total withdrawal; ambiguous hormone effect | **[confirm laterality coding]** |
| **EXCLUDE — oophorectomy after infection** | post-infection exposure; reverse-time | surgery date vs 40100 index |

**The oophorectomy-vs-hysterectomy ambiguity is the first design trap.** UKB
self-report conflates "had a hysterectomy" with "had ovaries removed"; many
hysterectomies retain ovaries, and coding is imperfect. The contrast is **only** valid
on **confirmed bilateral oophorectomy** — hysterectomy-only women are *not* surgical
menopause and belong to the t020 "indeterminate / menstrual-marker-destroyed" stratum,
used at most as a separate measurement-sensitivity, never as a surgical case here.

---

## 4. Main threats (named, with handling)

| Threat | Why it bites | Handling |
|---|---|---|
| **Indication for surgery** (fibroids, endometriosis, menorrhagia, prophylactic BRCA, malignancy) | The reason for surgery correlates with underlying inflammation, comorbidity, SES, and sometimes cancer/chemo — a back-door from indication → both surgery and PAIS risk. **This is the dominant threat and the reason the contrast might be rejected.** | Where indication is codable (HES pre-surgery dx), **stratify/adjust**; **exclude oncological oophorectomy** (chemo/radiation confound recovery biology); report an indication-restricted (benign-only) sensitivity. Residual indication confounding is the explicit limit on promotion (§6). |
| **Oophorectomy vs hysterectomy ambiguity** | Misclassifying hysterectomy-only as surgical menopause dilutes/biases the contrast | Restrict to **confirmed bilateral oophorectomy** (§3); report the count lost to ambiguity. |
| **HRT** | Surgical-menopause women — especially young oophorectomy — are **preferentially prescribed HRT**, which *replaces* the withdrawn estrogen and **masks** the very exposure being tested | Tag **HRT-on-at-infection** (t020 §6; fields 2814/3536/3546); run the contrast **HRT-stratified** (the M1 signal, if real, should be **attenuated in HRT-users** — itself a confirmatory pattern). HRT remains a **mediator, not adjusted**. |
| **Age-at-surgery timing** | Time-since-withdrawal and age at withdrawal both modify the hormone effect and confound with aging | The age-at-surgery split (§2) is the primary handle; match/adjust on age-at-infection and time-since-surgery. |
| **SES / healthcare access** | Surgical access and indication both track SES (M4); could re-import the confounder the contrast was meant to escape | Apply the **same whole-cohort U-proxy battery** (t017 §5.1); the contrast is only discriminating **if** the surgical signal **survives** U-proxy adjustment where the empirical question is whether surgical timing is *less* SES-loaded than natural timing. |
| **Left-truncation (M3a)** | Surgical-menopause women carry their own survival-to-2020 selection (and oophorectomy affects mortality) | Inherit the t031 survival-depletion sensitivity; do not interpret a surgical null without it. |

---

## 5. What result pattern discriminates M1 from M2/M4

| Observed pattern | Reads as |
|---|---|
| Surgical (esp. **pre-menopausal**) oophorectomy → **higher** long-COVID RR, **surviving** age + U-proxy + benign-indication restriction, **attenuated in HRT-users**, **stronger** than post-menopausal oophorectomy | **Supports M1** — a hormone-withdrawal channel that M2/M4 do not share; the within-surgical age gradient + HRT attenuation are hard for pure confounding to mimic. |
| **No** surgical effect after age + U-proxy + indication adjustment, **while** the natural-timing effect persists | Points the **natural-timing** association toward **M2/M4** — i.e. the primary signal is aging/SES, not hormone withdrawal. |
| Surgical effect present **but** tracks **indication / SES / oncological cases**, vanishes under benign-only restriction | **M4-like confounding** — not a hormone channel; the contrast is **not** discriminating here. |
| Pre- and post-menopausal oophorectomy show the **same** effect | **Against** the hormone-withdrawal mechanism (post-menopausal removal withdraws little estrogen) → favours a non-hormonal (surgery-generic / indication) pathway. |

The **within-surgical age-at-surgery gradient** and the **HRT-attenuation** pattern are
the two signatures most resistant to indication/SES confounding, because indication
confounding does not naturally predict *either* a pre-vs-post-FMP dose-response *or*
masking-by-HRT. Weight these over the bare surgical-vs-natural contrast.

---

## 6. Decision: **pre-registered EXPLORATORY triangulation contrast** (not a confirmatory sensitivity; not rejected)

**Verdict — promote to exploratory, gate further promotion on indication-bounding:**

- **Not rejected.** The contrast is genuinely discriminating — it attacks M2 and M4 on
  an axis (exogenous hormone-withdrawal timing) the primary design cannot, and the
  within-surgical age gradient + HRT-attenuation give it confounding-resistant
  signatures. Discarding it would waste the one quasi-experimental lever UKB offers.
- **Not a confirmatory / verdict-bearing sensitivity.** Surgical **indication**
  confounding is serious and only partially codable in UKB; the contrast cannot carry
  the weight the primary's locked sensitivities carry. Letting the confirmatory verdict
  rest on it would import indication bias into the headline result.
- **Therefore: pre-registered as an EXPLORATORY triangulation arm** — labelled,
  hypothesis-generating, reported with exploratory weight, **isolated from the primary
  natural-menopause estimand**. It strengthens or qualifies the *interpretation* of the
  primary (which rival is doing the work) without changing the primary estimate.

**Upgrade condition (stated now to avoid post-hoc promotion):** this arm may be
elevated to a verdict-bearing sensitivity **only if** indication can be adequately
coded and the benign-indication-restricted estimate is stable — a decision for the
independent reviewer (t029), to whom this spec is a visible input. Until then it stays
exploratory.

---

## 7. Handoff

| Downstream | What this hands it |
|---|---|
| **`pre-registration:0001`** | a new **exploratory** arm (surgical-vs-natural + age-at-surgery gradient + HRT-stratified), added under "Exploratory" — **no change to any locked confirmatory criterion**, so this is an additive amendment, not a fresh pre-reg (confirm via `statistics-prereg-amendment-vs-fresh` if the reviewer disagrees). |
| **t029 (independent review)** | the sharp object requested: *is surgical menopause a valid discriminating contrast, or too indication/SES-confounded to elevate?* §4 + §6 frame exactly that call. |
| **t020 exposure model** | promotes the set-aside surgical stratum (§3 Step 0) to a defined contrast; the exclusion rules here refine t020's stratum handling. |
| **t031 (left-truncation sim)** | the surgical arm inherits the same survival-depletion sensitivity. |

**Boundary restated:** the primary natural-menopause-timing analysis is estimated with
surgical cases **excluded** and is **unaffected** by anything in this document.
