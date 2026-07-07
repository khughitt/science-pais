---
id: interpretation:0036-t103-cross-pathogen-co-enrollment-feasibility
kind: interpretation
title: "t103/q0050: cross-pathogen co-enrollment is feasible only in staged form — CONDITIONAL GO on a COVID+influenza+EBV Tier-1 triad; the simultaneous 5-trigger design is a NO-GO"
status: active
source_refs:
  - cite:Trautmann2025
  - cite:Thomas2026
related:
  - task:t103
  - question:0050-cross-pathogen-co-enrollment-harmonized-multiomics-design
  - question:0001-shared-molecular-signature-across-triggers
  - question:0017-deflationary-alternatives-vs-shared-pathophysiology
  - hypothesis:0001-shared-dysregulated-attractor
  - interpretation:0001-cross-trigger-pathway-overlap-reanalysis-t035-null-nonarbitrating
  - pre-registration:0002-cross-trigger-pathway-overlap
created: "2026-07-07"
updated: "2026-07-07"
input: "Feasibility triage of the q0050 prospective cross-pathogen co-enrollment design against recruitment/incidence, confirmation-assay, control-frame, and power/bias axes, anchored to Trautmann2025 (incompatible-designs motivation), Thomas2026/MELLOW (harmonized dense-omic precedent), and interpretation:0001 (t035 null — the bias-ceiling lesson this design must beat). No participant data; no new cohort exists. Conceptual/feasibility-grade."
prior_interpretations:
  - interpretation:0001-cross-trigger-pathway-overlap-reanalysis-t035-null-nonarbitrating
relations:
  - predicate: "sci:amends"
    target: "interpretation:0001-cross-trigger-pathway-overlap-reanalysis-t035-null-nonarbitrating"
---

<!-- Mode: CONCEPTUAL / FEASIBILITY TRIAGE (t103, deliverable for q0050). Go/no-go + staged-design
recommendation only; no participant-level data, no cohort in hand. No evidence-lines or belief updates
on any proposition are minted — this assesses whether the discriminating experiment is *buildable*,
not what it would find. -->

# Interpretation: t103/q0050 — cross-pathogen co-enrollment feasibility

## Verdict

**Verdict:** [~] **CONDITIONAL GO — staged.** The full q0050 design as written (five *serologically confirmed*
acute triggers — COVID-19, Lyme, influenza, EBV, Q-fever — co-enrolled *simultaneously* within a single
4–12-week window at one site) is **NOT feasible** and should not be pursued in that form. But the design
it stands in for — the "harmonized ≥3-trigger multi-omics with full-recovery controls" that
`hypothesis:0001` names as its strongest discriminating test — **is feasible in a staged build** that
reaches the ≥3-trigger bar with the three highest-incidence, most-confirmable, year-round-recruitable
triggers first: **COVID-19 + influenza + EBV (acute infectious mononucleosis)** as **Tier 1**, with Lyme
(Tier 2, endemic-site + erythema-migrans clinical entry) and Q-fever (Tier 3, outbreak/endemic-gated)
added opportunistically. The binding constraint is **acute recruitment and confirmation heterogeneity,
not scientific value and not omics** — and a staged triad routes around it while still clearing the
"only 2 cohorts" ceiling that made the t035 public-data route non-arbitrating.

Two corrections to the q0050 design are load-bearing for the GO to hold:

1. **Control frame.** `hypothesis:0001`'s discriminating prediction calls for **full-recovery
   (infected-and-recovered) controls**, not q0050's "matched *uninfected* controls." The primary
   contrast must be *within-trigger* (PAIS vs recovered, both infected) so the shared-vs-specific axis
   is estimated *orthogonal* to trigger identity; a shared uninfected frame is a secondary anchor, not
   the primary comparator.
2. **Confirmation is per-arm, not harmonized.** Harmonize the *multi-omic sampling* protocol (the half
   Thomas2026/MELLOW proves feasible); accept **trigger-specific confirmation SOPs** (the half MELLOW
   does not de-risk). "One serological assay within a common window" is unachievable across these five
   pathogens and should not be a design goal.

## Findings Summary

Feasibility triage against four axes. The per-trigger recruitment/confirmation surface is the decisive one:

| Trigger | Acute incidence / recruitment channel | Serological/acute confirmation | Dateable onset? | Demographic skew (design confounder) | Tier |
|---|---|---|---|---|---|
| **COVID-19** | Very high, year-round; primary care / test-positive registries | PCR (acute) → anti-N seroconversion; robust | Yes (days) | Broad; spans age/sex | **1** |
| **Influenza** | High but **strongly seasonal**; acute clinics in winter | PCR/antigen — **acute-window-only** (narrow) | Yes (days) | Broad | **1** |
| **EBV (acute IM)** | Moderate in adolescents/young adults; **student-health** channel | VCA-IgM⁺ / EBNA-1-IgG⁻ pattern; heterophile; robust | Yes (weeks) | **Young-adult skew** — age-confounded arm | **1** |
| **Lyme (acute)** | Geographically + seasonally concentrated (endemic NE/upper-Midwest US, parts of EU; late spring–summer) | **Serology insensitive in early disease**; erythema migrans is a *clinical* diagnosis, seroconversion lags | EM gives clinical date; serology window mismatch | Outdoor/occupational skew | **2** |
| **Q-fever (acute)** | **Rare** outside outbreaks; livestock/abattoir/endemic exposure | Phase-II IgG/IgM seroconversion (paired sera) | Weeks; often retrospective | Strong occupational/male/rural skew | **3** |

Axis findings:

- **Recruitment/incidence is the binding constraint.** Three triggers (COVID, influenza, EBV) are
  recruitable through routine acute-care + student-health channels in a single metro region; influenza
  adds only a seasonal window. The remaining two are structurally hard: **Lyme** is endemic-region- and
  season-locked, and **Q-fever** is essentially outbreak-gated (the classic QFS cohorts derive from the
  Dutch 2007–2010 outbreak and Australian abattoir settings). A five-arm *simultaneous* enrollment at one
  site is therefore not realistic; a staged/multi-site accrual is.
- **Confirmation modality is irreducibly heterogeneous.** The gold standard and the confirmable window
  differ per pathogen (acute PCR for flu; IgM/EBNA pattern for EBV; EM-clinical-plus-convalescent-
  seroconversion for Lyme; paired-sera phase-II for Q-fever). "Confirmed within a common 4–12-wk window"
  is internally inconsistent for **acute Lyme** specifically (the most-confirmable acute Lyme is EM, which
  is clinical, while two-tier serology is insensitive early) — this is a design contradiction to fix, not
  a blocker: use **per-arm confirmation SOPs** under one harmonized *omics* protocol.
- **Control frame must be strengthened vs q0050.** `hypothesis:0001` predicts a shared pathway signature
  "present in cases of all triggers **and absent in recovered controls**." Uninfected controls alone
  cannot separate *trigger biology* from *PAIS biology*; infected-recovered controls within each arm can.
  Recommend a within-trigger (PAIS vs recovered) primary contrast + a shared uninfected anchor.
- **Power/bias — the design's actual case.** The t035 null (`interpretation:0001`) established that on the
  public 2-cohort route the effective cross-trigger unit is *the cohort* (n=2), and the dominant error is
  **bias** (platform, compartment, timing, sex) that **no participant N can shrink**. A harmonized
  co-enrollment design's core value is precisely that it **removes that bias term** (one platform, one
  compartment, one timing window, one SOP), converting "effective n = 2 cohorts" into "effective n = ≥3
  harmonized arms × participants-per-arm." At dense-multi-omic cost (MELLOW-scale ⇒ arms of *tens*, not
  thousands), achievable N is adequate for the **shared *pathway/latent-factor* axis** — the level
  `hypothesis:0001` actually operates at (a "degenerately realized" macro-state, not a shared molecule) —
  but underpowered for **trigger-specific fine-molecular discovery**, which should be pre-registered as
  exploratory-only.

## Evidence Quality

Feasibility-grade, partially sourced. The two anchors carry distinct, non-overlapping weight and one hard
boundary:

- **Trautmann2025** [@Trautmann2025] establishes the *motivation*: a narrative review documenting the
  shared core-symptom cluster and overlapping trigger list across long COVID / ME-CFS / long Lyme, and
  the covariate-sensitivity (severity, age, sex, timing, prior immunity) that any comparison must design
  in rather than adjust post hoc. It motivates a single harmonized protocol; it does **not** itself
  demonstrate feasibility.
- **Thomas2026 / MELLOW** [@Thomas2026] proves the *omics half*: harmonized dense-sampling multi-omic
  protocols are operationally executable across PAIS conditions. **Boundary (honest):** MELLOW co-samples
  **two established *chronic* conditions** (ME/CFS and long COVID) on a chronobiology dense-sampling
  protocol — it does **not** co-enroll multiple **confirmed-*acute* triggers within a window**, which is
  exactly where the binding constraint of q0050 sits. MELLOW therefore de-risks the sampling/assay
  logistics but **not** the acute recruitment/confirmation logistics. The feasibility verdict rests on
  that split.
- **interpretation:0001 (t035 null)** supplies the quantitative rationale for *why* harmonization is the
  operative lever (bias-not-variance ceiling) and the empirical argument that further public-data pairings
  are the wrong spend.

Incidence and confirmation-window characterizations in the table are general-epidemiology-grade and
[UNVERIFIED] at the level of exact numbers (no region-specific incidence model was built), but the
*structural* facts driving the tiering (flu
seasonality, EBV young-adult/student-health channel, early-Lyme serology insensitivity + EM-as-clinical,
Q-fever outbreak-concentration) are well-established qualitative constraints and are what the decision
rests on.

## Data Quality Checks

Not an empirical-results interpretation; no dataset QA was run. The relevant "data-quality" facts are
structural feasibility hazards that feed the staged design:

- **Confirmation-window mismatch (Lyme):** the acute-serology gate is self-contradictory for the most
  confirmable acute Lyme (EM) — a *design* defect in q0050 as written, resolved by per-arm SOPs.
- **Seasonality (influenza, Lyme):** neither is year-round-recruitable; the enrollment calendar, not just
  the site, is a constraint.
- **Outbreak-dependence (Q-fever):** accrual cannot be scheduled — it must be opportunistic on an active
  outbreak or a standing endemic-region collaboration.
- **Demographic confounding by arm (EBV young; Lyme/Q-fever occupational):** arms are intrinsically
  confounded with age/sex/exposure; this must be designed-in (within-trigger recovered controls + explicit
  cross-arm matching/modelling), consistent with Trautmann2025's covariate warning. **No data-quality
  concerns of the empirical kind identified** (there is no data); these are enumerated as methodological
  findings for the design.

## Proposition-Level Updates

None. This is a buildability verdict, not an endpoint result; no `proposition:` gains or loses an
evidence-line, and no belief on `hypothesis:0001` moves. In particular, the verdict does **not** update
the shared-attractor conjecture in either direction — it establishes only that the experiment able to test
it is constructible in staged form.

## Question- & Hypothesis-Level Implications

- **question:0050 — resolved on its stated axis.** q0050 asks whether the design is *feasible* ("the crux
  is logistics and power, not desirability"). Answer: **feasible in staged form, not as a simultaneous
  5-trigger build**, with two load-bearing design corrections (full-recovery control frame; per-arm
  confirmation). q0050 remains `active` as an empirical question — nothing here answers the shared-vs-
  specific biology; it clears the go/no-go gate that stood in front of it.
- **hypothesis:0001 — the discriminating test is buildable, and harmonization defeats the t035 ceiling.**
  The single most discriminating positive prediction (harmonized ≥3-trigger multi-omics vs full-recovery
  controls → shared pathway signature) moves from "named but un-costed" to "feasible via a COVID+flu+EBV
  triad." No belief update — but the *route to adjudication* is now concrete, which is the higher-value
  outcome for a hypothesis whose promotion has been held (interp 0001) precisely for lack of an
  arbitrating vehicle.
- **question:0017 (deflationary bundle) — a design that can *score against it* now exists.** The staged
  triad, powered at the pathway-axis level with full-recovery controls, is the first vehicle capable of
  returning an *arbitrating* result (shared-axis present-and-trigger-invariant vs absent), rather than the
  non-arbitrating null the 2-cohort route is structurally bound to.

## Evidence vs. Open Questions

- **question:0001 (shared molecular signature) — route unblocked, not answered.** The decisive ≥3-trigger
  harmonized test is now shown constructible; what it would find is still open. The estimand it can
  actually deliver is a **pathway/latent-factor shared axis** (well-powered at dense-omic N), not a
  fine-grained trigger-specific molecular catalog (underpowered — exploratory only).
- **question:0050 — feasibility gate cleared** (staged GO); the empirical question is handed forward to a
  pre-registration + costed protocol.
- **question:0017 — unchanged standing**, now with a buildable arbitrating vehicle on the horizon.

## New Questions Raised

- **(design, P2):** Should the primary control frame be **infected-recovered** (within-trigger) rather
  than uninfected? This interpretation recommends yes (aligns to h0001's stated prediction); it warrants a
  locked decision in the eventual pre-registration. *Not* reserved as a standalone `question:` — it is a
  design parameter of q0050, folded into the staged-design recommendation below.
- **(methodology, P2) — links to interp-0001 "Q-A":** At the achievable dense-omic per-arm N (tens), does
  a shared-latent-factor test across ≥3 harmonized arms clear the *arbitrating* bar (not merely the
  Monte-Carlo bar)? This is the same power/bias-floor simulation interp 0001 already flagged as Q-A;
  running it is now the gating analytic step *before* committing to the cohort. Suggested next evidence: a
  simulation seeded with MELLOW-scale multi-omic dispersion + the t035 observed NES dispersion.
- **(feasibility, P3):** Is a standing endemic-region collaboration (Netherlands/Australia for Q-fever;
  US-NE/EU for Lyme) securable to make Tiers 2–3 opportunistically reachable, or should the design cap at
  the Tier-1 triad as its permanent ≥3-trigger form?

## Limitations & Residual Uncertainty

- **Incidence figures are `[UNVERIFIED]` at the numeric level.** The tiering rests on qualitative
  structural constraints (robust) rather than on a formal region-specific incidence/power model — which is
  the natural next deliverable if this GO is acted on.
- **MELLOW de-risks omics, not acute recruitment.** The single largest residual uncertainty is whether
  *acute* multi-arm accrual (catching confirmed-acute cases inside 4–12 wk across channels) sustains the
  needed per-arm N on a realistic calendar — MELLOW's chronic-condition precedent does not speak to it.
- **Power verdict is estimand-conditional.** "Feasible/adequately-powered" holds for the *shared
  pathway-axis* contrast only; a stakeholder wanting trigger-specific molecular discovery would find the
  achievable N insufficient, and should be told so before funding.
- **This is a feasibility verdict, not a protocol.** No site, IRB, assay panel, sampling cadence, or
  power calculation is committed here; the GO licenses drafting those, not skipping them.

## Updated Priorities

1. **Adopt the staged design as the operative form of q0050.** Tier 1 = **COVID-19 + influenza + EBV**
   (single-metro acute-care + student-health accrual; influenza seasonal), reaching the ≥3-trigger bar on
   its own. Tier 2 = **Lyme** (endemic-site, erythema-migrans clinical entry + convalescent seroconversion).
   Tier 3 = **Q-fever** (outbreak/endemic-gated, opportunistic).
2. **Lock two design corrections into the eventual pre-registration:** (a) primary contrast =
   within-trigger PAIS-vs-**recovered** (full-recovery controls per h0001), shared uninfected frame
   secondary; (b) **per-arm confirmation SOPs** under one harmonized multi-omic sampling protocol.
3. **Pre-register the shared *pathway-axis* signature as primary; trigger-specific molecular discovery as
   exploratory** — matching the estimand the achievable N can actually carry and the level h0001 predicts.
4. **Run the power/bias-floor simulation (interp-0001 Q-A) *before* any cohort commitment** — seed it with
   MELLOW-scale dispersion; it is the cheap gate that decides whether even the harmonized triad clears the
   arbitrating bar. Recommend a follow-up task for this simulation.
5. **Do not pursue the simultaneous 5-trigger single-site design** — recorded here as an explicit NO-GO so
   it is not re-proposed.
