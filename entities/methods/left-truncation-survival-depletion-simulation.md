---
kind: method
title: "Left-truncation / survival-depletion bias simulation (M3a) for the menopause\u2192\
  PAIS analysis (t031)"
status: active
created: '2026-06-19'
updated: '2026-06-19'
id: method:left-truncation-survival-depletion-simulation
related:
- task:t031
- task:t016
- task:t028
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- question:0013-reproductive-stage-failed-immune-recovery-after-infection
- pre-registration:0001-menopause-pais-total-effect
- report:0001-bias-audit-menopause-pais-total-effect
- discussion:0001-menopause-timing-pais-rival-models
---

# Left-truncation / survival-depletion bias simulation (M3a) (t031)

Specifies the simulation that **quantifies** the survival-depletion threat named as
Known-Limitation #7 of `pre-registration:0001-menopause-pais-total-effect` and as model
**M3a** in `discussion:0001-menopause-timing-pais-rival-models`. Until now M3a is only
*named*; this turns it into a defined, runnable bias analysis so the independent review
(t029) evaluates a specification rather than a worry.

> **Decision-impact boundary (state up front).** This is a **verdict-confidence**
> instrument: it tunes how a **null** is read (powered downward update vs
> attenuated/uninformative) and may yield an *optional* corrected sensitivity estimate.
> It does **not** change the primary estimand, the {age, smoking} adjustment set, or any
> locked confirmatory criterion. Like t030, it is additive.

---

## 1. The left-truncation structure

UKB enrolled at **baseline 2006–2010, age 40–69**. The analysis risk set is natal
females who are **alive, linkage-resident, and documented-infected in 2020–2022** (age
≈ 52–83). Every analyzed woman must therefore **survive ~10–16 years from baseline to
infection eligibility** and enter the risk set with **delayed entry**:

```
baseline cohort (2006–2010)         risk set (2020–2022)
  age 40–69, exposure fixed   ──►   alive + resident + infected   ──►  outcome (LC)
        |                              ▲
        └── must survive the gap ──────┘   (left truncation / selection on survival)
```

The exposure — **age at menopause / reproductive-stage timing** — is fixed at baseline,
but **entry into the risk set is conditioned on surviving the gap**. That conditioning
is the bias channel.

---

## 2. Why it matters (the depletion mechanism)

**Earlier age at menopause is associated with higher all-cause and cardiovascular
mortality** (well-established epidemiologically). So women in the **earliest-menopause
tertile** — the **high-exposure, M1-highest-risk tail** — are **differentially removed
by death before 2020**. The high-risk exposure tail is **thinner in the analyzed risk
set than in the baseline-eligible population**: a depletion-of-susceptibles /
competing-prior-event structure.

**Expected direction.** If menopause-timing→mortality and menopause-timing→long-COVID
act in the **same** direction (earlier menopause → both more death and more LC), the
women who would most have carried the LC association are **preferentially absent**, so
the observed RR is **biased toward the null (attenuation)**. Secondary possibility:
**frailty selection** — survivors of early menopause may be unusually robust — which
can additionally distort the exposure-response *shape*, not just its magnitude. The
simulation reports the sign explicitly rather than assuming null-ward.

---

## 3. Simulation inputs and priors

A **Monte-Carlo probabilistic bias analysis**, with an analytic
inverse-probability-of-survival-weighting (IPSW) cross-check (§4).

| Input | Source | Prior / form |
|---|---|---|
| Joint (age-at-baseline, age-at-menopause) distribution | **UKB-internal** at execution (field 3581 among natural-menopause stratum); external age-at-menopause distribution (median ≈ 51, IQR ≈ 48–54) for the pre-access run | empirical / parametric |
| **Menopause-timing → mortality hazard** (the load-bearing prior) | published cohorts (e.g. early menopause <45 vs ≥50: all-cause mortality HR ≈ **1.1–1.4**; CV mortality HR somewhat larger) **[confirm sources at write-up]** | **distribution**, not a point — draw HR per draw |
| Baseline → 2020 survival | age + menopause-timing mortality model above, over the 10–16 yr gap | competing-risk survival |
| **Infection-into-risk-set eligibility** | probability of documented SARS-CoV-2 infection 2020–2022 | modelled **≈ conditionally independent of menopause-timing given age** as the base case; a sensitivity allowing mild dependence |
| **Assumed true exposure→LC effect** | the **pre-registered RR 1.3** (earliest-vs-latest timing tertile) | fixed at the meaningful-effect value, to measure how much truncation attenuates a *known* true effect |

**Procedure (per Monte-Carlo draw):**
1. Generate a baseline-eligible cohort with joint (age, menopause-timing).
2. Apply the differential mortality model → survival indicator to 2020.
3. Apply infection eligibility → risk-set membership.
4. Impose the true RR 1.3 LC effect on risk-set members.
5. **Estimate the observed (truncated) RR**; record the **attenuation factor**
   = observed log-RR ÷ true log-RR.
6. Repeat over draws from the mortality-HR prior → a **distribution** of attenuation.

The mortality-HR prior is the dominant uncertainty; the whole exercise is a sensitivity
**to that prior**.

---

## 4. IPSW cross-check / optional correction

As an analytic cross-check (and, at execution, an optional corrected estimate):
**inverse-probability-of-survival weighting** — reweight risk-set members by the inverse
modelled probability of surviving the gap given (age, menopause-timing), reconstructing
the baseline-eligible exposure distribution. The IPSW-corrected RR is reported **only as
a sensitivity**; the primary estimand stays the unweighted {age, smoking}-adjusted RR. Agreement
between the simulation attenuation factor and the IPSW shift is the internal validity
check.

---

## 5. What gets reported

1. **Direction** of the bias (sign; expected null-ward, confirmed or not).
2. **Plausible magnitude** as a **bound**, not a point: the attenuation-factor
   distribution (e.g. central + 80% interval), translated to "a true RR 1.3 is observed
   as RR ≈ X–Y under plausible mortality priors."
3. **Materiality verdict** — does correcting for depletion **shift the confirmatory
   estimate materially**? Operationalised against the pre-reg's meaningful-effect
   boundary:
   - **Attenuation small** (e.g. observed log-RR ≥ ~90% of true) → the naive estimate
     and **powered-null** reading **stand**; M3a is a minor caveat.
   - **Attenuation large** (observed materially below true; bias-adjusted interval would
     cross RR 1.3 when the naive interval does not) → a naive null **must be downgraded**
     from `null_meaningful` to `underpowered/attenuated`.

---

## 6. Decision impact (and what it does NOT do)

- **Feeds the Null Result Plan, mandatory before reading any null.** Per the pre-reg, a
  null is a powered downward update on h0005 **only if** the bias-adjusted interval
  excludes RR 1.3. This simulation supplies the **bias adjustment for the survival
  channel** that the "(QBA-bias-adjusted) interval" clause depends on — so a null cannot
  be read as `powered` until M3a is quantified. This is the concrete content of
  Limitation #7.
- **Verdict-confidence only.** It changes **how a result is interpreted**, not the
  primary estimate, the adjustment set, or any locked criterion. No amendment to
  confirmatory criteria; it is the execution-design realisation of an already-registered
  limitation.
- **Partly runnable pre-access.** Steps 1–6 run **now** as a pure simulation using
  external age-at-menopause and published mortality priors (a useful object for t029);
  it is **refined at execution** with UKB-internal age-at-menopause and (where linkage
  permits) cohort-specific mortality, and only then can the optional IPSW correction use
  real survival data.

---

## 7. Handoff

| Downstream | What this hands it |
|---|---|
| **t029 (independent review)** | M3a as a *specified* bias analysis (priors, procedure, reporting, materiality rule) rather than a named worry — sharper to evaluate. |
| **`pre-registration:0001`** | the quantitative backing for Limitation #7 and the survival-channel term in the Null Result Plan's "bias-adjusted interval"; **no locked-criterion change**. |
| **t028 (execution)** | a pre-interpretation step: compute the attenuation bound (and optional IPSW estimate) **before** any null is classified `null_meaningful`. |
| **t030 (surgical contrast)** | the surgical arm inherits the same survival-depletion logic (oophorectomy also affects mortality); reuse this model there. |

**Boundary restated:** this quantifies and bounds a threat to the **interpretation** of
a null; it leaves the primary natural-menopause-timing estimand and all locked
confirmatory criteria unchanged.
