---
id: "report:0001-bias-audit-menopause-pais-total-effect"
type: "report"
title: "Bias Audit: menopause→PAIS total-effect pre-registration (data-gated)"
status: "proposed"
source_refs:
  - pre-registration:0001-menopause-pais-total-effect
  - task:t016
  - task:t017
  - task:t020
  - task:t027
related:
  - hypothesis:0005-reproductive-stage-immune-homeostatic-margin
  - question:0013-reproductive-stage-failed-immune-recovery-after-infection
  - paper:AlcaldeHerraiz2025
  - patch-definition:menopause-pais-causal-dag
created: "2026-06-19"
updated: "2026-06-19"
---

# Bias Audit: menopause→PAIS total-effect pre-registration (data-gated)

## Scope

Audits the committed data-gated pre-registration
`pre-registration:0001-menopause-pais-total-effect` and its three frozen lock
inputs:

- **t027** — `doc/methods/2026-06-19-ukb-data-field-specification.md` (vehicle / field basket / access)
- **t020** — `doc/methods/2026-06-19-reproductive-stage-exposure-operationalization.md` (exposure + misclassification model)
- **t017** — `doc/methods/2026-06-19-ukb-outcome-and-uproxy-measurement-schema.md` (outcome + U-proxy schema)

The pre-reg is **design-complete, execution-gated** (no UKB data in hand). So this
audit targets *design and framing* blind spots that should be fixed **before** the
UKB AMS application is built, not analysis-execution errors (which cannot exist yet).

**Headline framing (load-bearing — see Author Independence and Corpus Independence
below):** the same agent authored all four artifacts *and* this audit, in one
session, against one precedent paper. This audit is therefore registered as a
**self-audit (internally consistent)**, not an external validation. Its job is to
surface fixable blind spots and to *downgrade the verdict confidence* — not to
ratify.

---

## Cognitive Biases

### Confirmation Bias

- **Rating:** possible → likely (at the literature-grounding layer; *well-contained* at the interpretation layer)
- **Evidence:** The expected-direction prior (earlier menopause / later reproductive
  stage → higher long-COVID risk, RR ≈ 1.3) is grounded in three mutually-aligned
  sources: h0005's own conjecture, the SHBG-protection signal in
  `AlcaldeHerraiz2025`, and `topic:menopause-sex-hormones-and-pais-risk`. **No
  counter-evidence is cited** — there is no entry for studies that found *no*
  sex-hormone / menopause effect on long-COVID, and the t015 search was scoped to
  find a *vehicle for* the h0005 analysis, not to find disconfirming literature. That
  is a one-sided evidence base feeding the prior.
  - *Strong mitigating factor:* the pre-reg's **interpretation** machinery is, by
    contrast, genuinely adversarial — a powered null produces a real downward update,
    there is a pre-specified negative-control outcome, an E-value benchmarked against
    measured proxies, and explicit veto conditions. The confirmation risk lives in
    *what evidence was gathered to form the expectation*, not in *how results will be
    read*. Surfacing counter-literature would close most of the gap.

### Anchoring

- **Rating:** likely
- **Evidence:** Two hard anchors, and one of them is load-bearing in a way the docs
  under-flag.
  1. **Vehicle anchor (UK Biobank).** t015 concluded "ZERO admissible cohort," then
     selected UKB; every artifact since is UKB-shaped (t027 fields → t020 staging of
     *those* fields → t017 outcome from *that* questionnaire). The feasibility check
     then discovered UKB's cohort **aged out of the peri window** — i.e. the chosen
     vehicle structurally cannot deliver q0013's motivating contrast. The response was
     to **demote the question to fit the vehicle** (confirmatory exposure → reproductive
     *timing*; pre/peri routed to "younger triangulation cohorts, exploratory"), rather
     than to re-open whether a younger-skewed cohort should *lead*. That is the
     signature of anchoring: the anchor was kept and the target was moved.
  2. **Method anchor (AlcaldeHerraiz2025).** Outcome engineering, missingness rules
     (>50% exclude / MICE ≤50%), covariate timing, and the questionnaire route are all
     "adopt-or-diverge-from-precedent." The pipeline is shaped by one paper's choices.
- This is the highest-value cognitive finding. It is *not* an argument to abandon UKB
  (it remains the strongest single vehicle for the *timing* estimand) — it is an
  argument to **state explicitly in the pre-reg that the primary vehicle cannot answer
  the peri-window sub-question**, so the reframe reads as an honest scope limit rather
  than a silent substitution.

### Availability Bias

- **Rating:** possible
- **Evidence:** UKB is the most familiar/accessible large biobank (RAP tooling,
  well-trodden long-COVID precedent). The confirmatory **exposure** — age-at-menopause /
  time-since-menopause — is partly chosen because it is *what UKB has variance in*, not
  because it is the sharpest test of h0005 (which q0013 frames as the **peri window**).
  The answerable question has been substituted for the important one. The docs are
  honest that this is a UKB-supportable *realization* of the estimand, but the
  substitution is availability-shaped and should be named as such.

### Sunk Cost

- **Rating:** possible (mild)
- **Evidence:** A full thread (DAG → critique → plan → t002 → t024 → t015 → t027 →
  t020 → t017 → pre-reg; ~14 commits in one ~6-hour session) is invested in the
  UKB/menopause-timing line. The feasibility check found the core peri contrast
  "structurally near-unavailable in UKB" — a finding that, taken cold, points toward
  *leading with a younger cohort*. The thread instead preserved UKB-primary and
  demoted the contrast. This interacts with the anchoring finding; the mitigation is
  the same (name the limit explicitly), so it is not independently severe.

### Process Bias

- **Rating:** likely
- **Evidence:** `git log` shows a single author (Keith Hughitt), ~14 commits in ~6
  hours, **no external review**, and **no cooling-off** — authoring, pre-registering,
  and now auditing all occur in one continuous session by one agent. This is the
  process-side twin of the Author-Independence finding below. Rapid single-analyst
  momentum is exactly the condition under which a shared blind spot (here: the
  single-precedent dependence and the unflagged survival-selection threat) propagates
  uncaught across every artifact, because the same reasoning produced all of them.

---

## Methodological Biases

### Selection Bias

- **Rating:** possible (well-handled at design level; two residuals)
- **Evidence:** Three selection nodes are explicitly handled — the clinic-attendance
  collider (population frame upheld, G4), the questionnaire-response node (restriction
  + IPW + Route-B triangulation, t017 §4), and early-pandemic testing-access (named
  limitation). This is strong, above-typical coverage. **Two residuals survive:**
  1. **Response-propensity IPW uses baseline (2006–2010) predictors**, but propensity
     to complete the 2022–2023 questionnaire plausibly depends on *post-baseline*
     health — including incipient long-COVID itself. Baseline IPW cannot reweight on a
     2022 health state, so the responder estimate retains a residual, outcome-adjacent
     selection that the Route-B arm only partially triangulates.
  2. **Left-truncation / survival-to-2020** (see Confounding matrix) is a selection
     threat the design does not name.

### Survivorship Bias

- **Rating:** possible (two distinct senses — the second is the sharper, and is *new*)
- **Evidence:**
  1. *Literature survivorship:* null-result menopause/long-COVID studies are not
     represented in the evidence base (same root as the Confirmation finding).
  2. *Cohort survivorship (left-truncation) — the under-recognized one:* every analyzed
     woman must have **survived from 2006–2010 baseline to her 2020–2022 infection** at
     age ≈52–83. **Earlier age-at-menopause is associated with higher all-cause and
     cardiovascular mortality.** The earliest-menopause-timing stratum — the high-risk
     end of the *exposure* — is therefore differentially **depleted by death before the
     time origin**. This is a depletion-of-susceptibles / competing-prior-event
     structure that biases the menopause-timing→long-COVID estimate (most likely toward
     the null, but the direction is not guaranteed). None of the four docs names it; the
     t020 misclassification model and the t027 competing-risk note both concern *post*-
     infection censoring, not *pre*-infection left-truncation. This should be added as a
     limitation and a sensitivity consideration before execution.

### HARKing

- **Rating:** not detected (genuinely strong)
- **Evidence:** This is pre-registration done **before any UKB data exists**. Direction
  is committed as the primary commitment; the smallest meaningful effect (RR 1.3),
  primary metric (RR / log-binomial), outcome definition (def-1 primary, def-2
  approximation, def-3 explicitly *not* preregistered as computable), and the **QBA
  priors before any outcome is linked** are all locked. The feasibility-driven reframe
  (stage → timing) was made *pre-data and recorded as committed*, precisely so
  interpret-results treats it as intentional rather than drift. The data-gated mode and
  standing `[?] inconclusive-for-coverage` verdict are the correct anti-HARKing
  posture. No drift between a prior registration and current framing exists to flag.

### Multiple Comparisons / p-hacking Risk

- **Rating:** possible (well-accounted; one soft spot)
- **Evidence:** The Total-Comparison-Count table is honest: 1 confirmatory, ~8
  sensitivities (declared as robustness/arbitration, not independent multiplicity), ~5
  exploratory (labelled, reduced weight). Pre-committing *which* test is primary is the
  right multiplicity control. **Soft spot:** the confirmatory verdict is read "jointly
  with its mandatory sensitivities," and the disagreement-resolution rule is "ambiguous
  → do not average → escalate to `/science:discuss`." That escalation clause is a
  researcher degree of freedom in *how* to weigh def-1-vs-def-2, tertile-vs-per-SD, and
  two index-date rules. It is defensible (better than silent averaging) but is the one
  remaining forking-path. Recommend pre-committing the *ordering* of which sensitivity
  governs if they disagree, not only that disagreement triggers discussion.

### Confounding

- **Rating:** possible (the central scientific challenge — handled honestly at the
  design level via partial-identification + E-value, with two confounds to add)
- **Evidence:** The age-at-infection adjustment set is critique-corrected
  *[update 2026-06-21, t029/t023: the primary measured set is now `{age, smoking}` —
  deliberately not "minimal-sufficient", since none exists while U is latent; DAG v2
  adds baseline-comorbidity/BMI/parity/autoimmune-POI/frailty as sensitivity-arm
  confounders]*,
  mediators are correctly left unadjusted (total effect), HRT is correctly treated as
  mediator/confounded-by-indication and not adjusted, and the partial-identification
  posture (U stays latent; E-value load-bearing; U-proxy arm; EBV only on the ~9.6k
  subsample, **not imputed**) is methodologically sound and unusually candid. The gaps
  are two confound/selection structures not currently in the design:

#### Confound Severity Matrix

| Confound | Severity | Fixability | Mitigation |
|---|---|---|---|
| Residual latent U (SES / prior-EBV / HLA / behaviour) not fully measured | HIGH | HARD | Already designed: E-value bound + whole-cohort U-proxy arm; EBV subsample arm. Keep; this is the load-bearing partial-ID limit. |
| **Left-truncation / survival-to-2020** (earlier menopause ↔ higher mortality → earliest-exposure stratum depleted before time origin) | MED–HIGH | HARD | **New — add.** Name as limitation; add a competing-prior-event / selection sensitivity; state expected (likely null-ward) bias direction. |
| **Response propensity depends on post-baseline (incipient-LC) health**, not just baseline covariates | MED | HARD | Baseline IPW insufficient on its own; lean on Route-B (HES) triangulation; state the "estimate in responders" bound explicitly. |
| Decade-gap exposure misclassification (peri cell) | MED (attenuating) | HARD/INFEASIBLE | Already handled: t020 QBA bounds it; peri labelled `underpowered/attenuated`, never `null_meaningful`. |
| Residual age confounding if age modeled coarsely | MED | EASY | Already specified: flexible spline on age-at-infection. |
| HRT confounded-by-indication | LOW–MED | N/A by design | Not adjusted (mediator); incl/excl-HRT-on sensitivity arm already specified. |

### Publication Bias

- **Rating:** possible (literature-context only)
- **Evidence:** No systematic literature review is the *output* here, so classic
  publication bias is limited in scope. But the background that *grounds the expected
  direction* (the SHBG signal, the topic synthesis) is drawn from positive-finding
  sources, and the nearest-precedent paper is itself a published positive
  risk-factor study. Same mitigation as Confirmation/Survivorship-(1): deliberately
  seek and cite at least one null/contrary menopause-or-sex-hormone↔long-COVID result.

### Corpus Independence (Closure Check)

- **Rating:** likely — **HIGH-severity**
- **Artifacts under audit:** the pre-reg + t027 + t020 + t017 (four documents).
- **Shared corpus:** **a single precedent paper, `AlcaldeHerraiz2025`.** It is the sole
  empirical anchor for: the effective-n estimates (8,668 LC cohort → ~1,200–1,600
  female cases), the "questionnaire route exists / 45-item WHO-Delphi" correction that
  overturned t027's pessimism, the missingness and covariate-timing conventions, the
  feasibility verdicts on each outcome definition, **and** part of the expected-direction
  justification (the SHBG signal). Every load-bearing feasibility number traces to this
  one paper.
- **Independent evidence sources:** **none, until UKB data is actually provisioned.**
  The triangulation cohorts (All of Us, Lifelines) are named but not yet consulted; no
  second UKB long-COVID paper is cross-checked; the field-ID and effective-n claims are
  marked "[confirm at application]" precisely because they are *not* yet independently
  verified.
- **Verdict:** The audit corpus has **no out-of-corpus check by construction** — if
  `AlcaldeHerraiz2025`'s cohort numbers, selection profile, or SHBG signal are atypical
  or were misread, *all four artifacts inherit the error coherently*, and nothing in
  the current design would catch it. This does not invalidate the design, but it
  **downgrades the feasibility claims from "established" to "single-source, pending live
  confirmation."** Mitigations: (a) the G2 live-Showcase confirmation and G3 power-floor
  recomputation already partially serve this — make them *explicitly* the out-of-corpus
  check and gate the standing verdict on them; (b) cross-read at least one *second* UKB
  long-COVID cohort paper for the effective-n and selection profile before submitting
  the AMS basket; (c) keep the verdict labelled "internally consistent," not "validated."

### Author Independence (Self-Audit Check)

- **Rating:** likely — **HIGH-severity (structural)**
- **Audit author = artifact author?:** **Yes.** The same agent, in this same session,
  authored the pre-registration *and* all three lock inputs (t027, t020, t017) *and* is
  now running this audit. There has been no cooling-off and no second reviewer.
- **Verdict:** Register this audit as a **"self-audit (internally consistent)"**, not an
  external validation. The same reasoning that produced the artifacts is structurally
  unlikely to falsify them — the two genuinely-new findings here (survival
  left-truncation; post-baseline response propensity) are exactly the kind of shared
  blind spot a same-author pass tends to *under*-detect, and they were only surfaced by
  deliberately running the template's closure checks against my own output. Before the
  pre-reg's feasibility claims are treated as externally validated, obtain an
  **independent pass**: a different reviewer (human domain expert or a fresh agent with
  no authorship stake), ideally after a cooling-off period, ideally cross-reading a
  second precedent. This downgrades the claim; it does not ratify it.

---

## Summary

- **Overall threat level:** **moderate.** The substantive *design* is unusually
  well-armored — genuine pre-registration, partial-identification with a load-bearing
  E-value, a pre-specified negative-control outcome, QBA priors locked before outcome
  linkage, honest multiplicity accounting, and a data-gated standing-inconclusive
  verdict. The threats are concentrated not in the methodology but in **(a) verdict
  *confidence*** — compromised by same-author / single-precedent closure — **and (b)
  two specific confound/selection structures the design does not yet name.** Nothing
  here is a "stop"; everything is a "fix before the AMS application is built."

- **Top mitigations:**
  1. **Treat the verdict as self-audit + single-source, and get one independent pass.**
     Register this audit as "internally consistent," and before relying on the
     feasibility claims, obtain an out-of-author review and cross-read a *second* UKB
     long-COVID paper so the effective-n / selection / SHBG claims no longer rest on
     `AlcaldeHerraiz2025` alone. (Closes Author + Corpus Independence.)
  2. **Add the two missing threats to the pre-reg's Known Limitations + sensitivities:**
     (i) left-truncation / survival-to-2020 depletion of the earliest-menopause stratum,
     with an expected bias direction and a competing-prior-event sensitivity; (ii)
     response propensity depending on post-baseline health, with the "estimate in
     responders" bound stated and Route-B carrying more triangulation weight.
  3. **Name the vehicle-anchoring limit explicitly.** State in the pre-reg that UKB
     *cannot* answer q0013's peri-window sub-question (cohort aged out), so the
     timing-exposure reframe is an honest scope concession, and pre-commit which
     sensitivity governs when def-1/def-2 or tertile/per-SD disagree (close the
     escalation-clause forking path).

- **Recommended next actions:**
  - Apply mitigations 2 and 3 as small edits to the pre-reg's *Known Limitations* and
    *Suspicious/Unexpected* / sensitivity sections (these are additive caveats, **not**
    changes to a committed decision criterion, so they do not require a formal
    amendment — but log them in `updated:`). If any touches a locked criterion, route
    through `statistics-prereg-amendment-vs-fresh` instead.
  - Fold the second-precedent cross-read and the independent pass into the **G2** gate
    description so the out-of-corpus check is a named admissibility precondition, not an
    afterthought.
  - Optional follow-ups: `/science:compare-hypotheses` would force the
    counter-explanation (no-sex-hormone-effect) into the evidence base, addressing the
    Confirmation/Publication findings at their root.
