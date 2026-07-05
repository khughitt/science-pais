---
kind: method
title: "Reproductive-stage exposure operationalization & misclassification model for\
  \ the menopause\u2192PAIS analysis (t020)"
status: active
created: '2026-06-19'
updated: '2026-06-19'
id: method:reproductive-stage-exposure-operationalization
related:
- task:t020
- task:t016
- task:t017
- task:t027
- question:0013-reproductive-stage-failed-immune-recovery-after-infection
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- patch-definition:menopause-pais-causal-dag
- topic:menopause-sex-hormones-and-pais-risk
---

# Reproductive-stage exposure operationalization & misclassification model (t020)

Specifies a **reproducible operationalization** of the t016 treatment node —
*reproductive stage (pre → peri → post), assessed at the time of acute infection* —
and the **misclassification model** that carries its measurement error into the
analysis. This is the second of the two open design gates (with t017) before
`/science:pre-register`.

q0013 names the load-bearing uncertainty precisely: *"whether perimenopause, rather
than menopause as a binary state, is the biologically relevant exposure window."*
The binary menopause variable (Shah2025/Mishra2020 style) collapses exactly the
stratum h0005 cares about. This document defines how to recover an **ordinal**
exposure from UK Biobank, what error that introduces, and how to bound it.

> **Scope.** This owns the *exposure* definition and its measurement-error model.
> The field IDs come from the t027 spec
> (`doc/methods/2026-06-19-ukb-data-field-specification.md` §3); the estimand,
> {age, smoking}-adjustment, and sensitivity-arbitration logic are locked in the t016 plan
> and are referenced, not re-derived.

---

## 1. The target construct: STRAW+10 reproductive stage

The reference standard for reproductive-stage staging is **STRAW+10** (Stages of
Reproductive Aging Workshop +10; Harlow et al. 2012), an ordinal axis anchored at
the final menstrual period (FMP):

| STRAW+10 stage | Principal (menstrual) criterion | Supportive (endocrine) |
|---|---|---|
| Reproductive (−5…−3) | Regular cycles | normal FSH, AMH |
| **Early transition (−2)** | persistent ≥7-day cycle-length variability | FSH variable/↑ |
| **Late transition (−1)** | interval of amenorrhea ≥60 days | FSH ≥25 IU/L; AMH low; vasomotor symptoms likely |
| FMP (0) | last menstrual period (defined retrospectively after 12 mo) | — |
| Early postmenopause (+1a/b/c) | 12 mo amenorrhea → first ~5–6 yr | FSH high/stabilizing |
| Late postmenopause (+2) | — | FSH stable high |

"Perimenopause" = the **menopausal transition** (−2 and −1) plus the first 12 months
after FMP. This is the at-risk window of interest.

---

## 2. The hard constraint: UKB cannot apply STRAW+10 directly

STRAW+10's principal criterion is **prospective menstrual-cycle change**, and its
supportive criterion is **serial FSH / AMH**. **UK Biobank provides neither at the
time of infection:**

| STRAW+10 input | UKB availability | Consequence |
|---|---|---|
| Prospective cycle-length / amenorrhea-interval | ✗ never collected | The principal criterion is unusable |
| FSH | ✗ **not in the UKB biochemistry panel** | No endocrine anchor for the transition |
| AMH | ✗ not in the panel | No ovarian-reserve anchor |
| Oestradiol | ⚠ censored at 175 pmol/L floor (t027 §3.3) | Cannot discriminate post-menopausal range |
| Self-report "had menopause" + age at menopause | ✓ at **baseline only** (2006–2010) | Cross-sectional, decade before infection |

**Conclusion:** the exposure must be an **age-and-questionnaire-based approximation
of STRAW+10**, not STRAW+10 itself. This document is explicit about that gap rather
than implying a staging fidelity UKB does not support — the approximation *is* the
exposure, and its error *is* the misclassification model in §5.

The honest framing for pre-registration: **"projected reproductive stage at
infection,"** a deterministic-plus-probabilistic derivation from baseline
questionnaire + age, validated where UKB repeat-assessment allows.

---

## 3. The staging algorithm (primary operationalization)

Let `T_inf` = first documented SARS-CoV-2 infection date (t027 §5.1), `A_inf` = age
at infection (from fields `34`/`52`), `M` = self-reported age at natural menopause
(`3581`), measured at baseline.

Applied as an ordered decision tree; the **first** matching rule assigns the stratum.

### Step 0 — Iatrogenic / indeterminate strata (assign and set aside)

- **Bilateral oophorectomy before `T_inf`** (2834 + dates) → **surgical
  postmenopause**. Abrupt, non-physiological transition; analyzed as a **separate
  stratum**, never pooled into natural-transition stages (different hormonal
  trajectory; effect may differ).
- **Hysterectomy without oophorectomy** (3591, ovaries retained) → **menstrual-marker
  destroyed**: no FMP observable, ovarian function continues silently. Assign
  **indeterminate** → age-band proxy only (§3, Step 3), flagged low-confidence.
- **HRT active at `T_inf`** (2814/3536/3546 spanning `T_inf`) → stage is assigned on
  **chronological/menstrual criteria as below** (HRT does not move the underlying
  stage), but the record is tagged `HRT-on-at-infection` for the §6 sensitivity arm,
  because exogenous hormones alter the *milieu* the stage is meant to proxy.

### Step 1 — Natural menopause reported at baseline (clean stratum)

If `2724` = Yes (natural) with a valid `M`:
- `A_inf ≥ M` (essentially all, given the ~decade gap) → **postmenopausal**,
  **high confidence** (monotonic: once post, always post).

This is the most reliable stratum — women who had reached natural menopause by
baseline are unambiguously postmenopausal at infection.

### Step 2 — Premenopausal at baseline → forward projection (the hard stratum)

If `2724` = No at baseline, the woman's stage at `T_inf` is **unobserved** and must be
**projected forward** across the ~10–14 yr gap using `A_inf` and menopause-timing
predictors:

| `A_inf` band | Projected stage | Confidence |
|---|---|---|
| `A_inf` < 45 | **Premenopausal** | high |
| 45 ≤ `A_inf` < 48 | **Early transition (peri)** | low |
| 48 ≤ `A_inf` ≤ 55 | **Peri / post uncertain** (straddles median FMP ≈ 51) | **lowest — the pivotal cell** |
| `A_inf` > 55 | **Postmenopausal** | moderate–high |

The band cutpoints approximate the UK natural-menopause distribution (median ≈ 51 yr,
IQR ≈ 48–54). **Refine per-woman** with baseline menopause-timing predictors already
in the basket — **age at menarche (`2714`), smoking (`20116`), parity (`2734`), BMI
(`21001`)** — via a pre-fit time-to-menopause model (e.g. a parametric survival model
of age-at-menopause), so each premenopausal-at-baseline woman gets an individual
*probability of being post / peri / pre at `T_inf`* rather than a flat age-band
assignment. This probability is the input to the probabilistic operationalization
(§4, tier 2) and the misclassification matrix (§5).

### Step 3 — Age-band fallback (missing / indeterminate)

No interpretable menopause status (missing 2724, hysterectomy-only, refused): assign
by `A_inf` bands above with **no per-woman refinement**. Coarsest tier, highest
misclassification, flagged for the §6 completeness audit.

---

## 4. Three pre-committed operationalizations (sensitivity tiers)

Matching the t016 plan's operationalization-sensitivity discipline — pre-committed,
not a post-hoc menu:

| Tier | Operationalization | Role |
|---|---|---|
| **1 — Primary** | **Projected ordinal stage** (pre / peri / post) from the §3 decision tree, peri = transition zone | Verdict-bearing exposure |
| **2 — Probabilistic** | Carry the §3 per-woman stage **probabilities** as a distribution (multiple imputation / Bayesian latent stage), propagating projection uncertainty into the HR/RR interval | Principled QBA; the *honest* interval |
| **3 — Binary (negative-control operationalization)** | **post vs not-post** (the Shah2025/Mishra2020 collapse) | Run **only** to demonstrate what the peri-collapse costs — *not* a robustness confirmation |

**Pre-committed reading:** an effect stable across tiers 1–2 is *staging-robust*. An
effect that appears under tier 3 but **not** tier 1 is an artifact of the
peri-collapse (and vice versa). The t016 plan already states tier-3 binary is a
sensitivity operationalization only; this document makes tiers 1–2 the primary axis.

---

## 5. Misclassification model

The projection in §3 guarantees exposure misclassification; the analysis is only
defensible if that error is **modelled, not ignored**.

### 5.1 Structure & direction

- **Non-differential component** (projection noise unrelated to PAIS): for an ordinal
  3-level exposure, non-differential misclassification **biases the dose-response
  toward the null** (attenuation). Critically, this **compounds the t016 power-floor
  problem**: a null in the peri stratum is then *doubly* non-arbitrating — thin n
  **and** attenuation. Peri nulls must be labelled `underpowered/attenuated`, never
  "no effect."
- **Differential component** (the serious threat): **menopause↔PAIS symptom overlap**
  (Stewart2024/Humphreys2025 — fatigue, cognitive, sleep, palpitations, mood shared
  by both). If PAIS status influences how a woman is staged — e.g. symptomatic women
  more readily coded perimenopausal — misclassification becomes **outcome-dependent**
  and can bias the effect **in either direction**, including manufacturing a spurious
  peri effect. In UKB this risk is *reduced* because staging is derived from
  **pre-infection baseline** data (2006–2010) that PAIS cannot have retro-caused —
  one of the structural advantages of the pre-baseline design. The residual differential
  channel is only via shared *causes* of both staging error and PAIS (already the
  U-proxy concern), not via reverse causation. **State this explicitly: the
  pre-baseline design converts most of the symptom-overlap threat from differential
  to non-differential.**

### 5.2 The misclassification matrix

Pre-specify `P(assigned stage | true stage)` as a 3×3 (×stratum) matrix. Anchor its
parameters from three sources, in priority order:

1. **UKB repeat-assessment validation (internal, preferred):** the instance-1
   (~2012–2013, ~20k) and instance-2/3 imaging (~2014+, ~60k) re-assessments asked
   menopause status again. Women premenopausal at baseline who reported menopause at
   re-assessment give **empirical individual-level transition rates** by age — a
   direct calibration of the §3 projection over a real (shorter) interval, extrapolated
   to `T_inf`. **This is the single most valuable internal validation and should be
   computed first.**
2. **Baseline age-at-menopause distribution (internal):** the observed `M`
   distribution among the natural-menopause stratum calibrates the survival model's
   forward projection.
3. **External STRAW+10 validation literature:** published sensitivity/specificity of
   age-band and questionnaire staging vs biomarker-confirmed STRAW+10, as priors where
   internal data is thin (esp. the peri cell).

### 5.3 Quantitative bias analysis (QBA)

- Run **probabilistic bias analysis**: draw misclassification parameters from
  pre-registered priors (from §5.2), reclassify, re-estimate, and report a
  **bias-adjusted HR/RR with a simulation interval** that combines random error +
  misclassification uncertainty.
- Tier-2 (probabilistic stage) and the QBA are two routes to the same honest
  interval; pre-commit one as primary (recommend **tier-2 latent-stage** as primary,
  QBA as the cross-check) so they are not double-counted.
- **Pre-commit the priors before any outcome is linked** — QBA priors chosen after
  seeing the effect are HARKing.

---

## 6. Auxiliary measurement issues

- **Surgical-menopause stratum:** report separately; do not let abrupt surgical
  postmenopause borrow strength from the natural-transition dose-response.
- **HRT-on-at-infection tag:** sensitivity arm re-running the primary with
  HRT-active women (a) excluded and (b) retained — divergence flags exogenous-hormone
  contamination of the stage proxy. (HRT remains a **mediator, not adjusted**, per the
  DAG — this is about *staging measurement*, not confounding control.)
- **Independent corroboration (weak):** baseline **SHBG/testosterone** (usable assays,
  t027 §3.3) shift across the transition; a coarse concordance check between projected
  stage and baseline androgen profile is an independent (if noisy) staging signal. Not
  a primary criterion — oestradiol cannot serve (floor-censored).

---

## 7. Power & arbitration consequences (feeds back to t016)

- The **peri stratum** is simultaneously the **thinnest** (premenopausal-at-baseline
  × narrow age band × natal-female × infected) and the **most misclassified**. The
  t016 plan's power-floor section already names it the dominant underpowering risk;
  this document supplies the *reason* (projection + attenuation) and the *label*
  (`underpowered/attenuated`, distinct from `null_meaningful`).
- **Verdict coupling:** the t016 Sensitivity Arbitration `unresolved/underpowered`
  branch fires whenever (a) the peri power floor is inadequate **or** (b) staging-at-
  infection is unverifiable for a stratum. This document operationalizes branch (b):
  the surgical/indeterminate/age-band-fallback strata are the "unverifiable" cases.

---

## 8. Reproducibility checklist (pre-registration inputs)

Lock these before linking the outcome:

1. ✅ Decision-tree cutpoints (§3) and age bands.
2. ✅ Menopause-timing predictor set for the forward-projection survival model
   (menarche, smoking, parity, BMI).
3. ✅ The three operationalization tiers (§4) and their pre-committed reading.
4. ✅ Misclassification-matrix anchor sources & priority (§5.2).
5. ✅ QBA priors and the primary-vs-cross-check choice (§5.3).
6. ✅ Stratum handling: surgical / indeterminate / HRT-on tags (§6).

---

## 9. Handoff

| Downstream | What this hands it |
|---|---|
| **t017** (measurement schema) | the exact exposure-derivation field set (2724/3581/2834/3591/2814/3536/3546/2714/2734/20116/21001 + age) and the repeat-assessment validation requirement, to fold into the minimum schema |
| **t016 plan** | replaces the placeholder "STRAW+10 staging where available" with a UKB-specific projected-stage definition + QBA; tightens the power-floor/arbitration coupling (§7) |
| **`/science:pre-register`** | §8 checklist = the exposure half of the confirmatory lock (t017 supplies the U-proxy/outcome half) |
| **Triangulation (All of Us / Lifelines)** | same projected-stage logic; Lifelines/GS have age-at-menopause but, like UKB, no FSH/AMH — the approximation transfers, the misclassification priors must be re-anchored per cohort |

**Net effect on the thread:** t020 closes the exposure-definition gate at the
*design* level. The residual is empirical — the §5.2 internal validation (repeat-
assessment transition rates) can only be computed once UKB data is provisioned, so
it becomes an **input-QA step** (t016 plan's Required Input Inspection), not a
pre-registration blocker. With t017 still open and the AMS access gate parallel, the
t016 verdict stays `not-ready` for those reasons — but the exposure is now
pre-registerable.
