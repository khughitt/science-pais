---
id: interpretation:0034-t079-bc6-acute-severity-dateability
type: interpretation
title: "t079/BC-6: acute-severity dateability — severity is dateable enough to COMPUTE E2/E3 candidates (identification stays assumption-dependent); the ladder degrades in the middle and the ≥45d survival filter selects on a consequence of severity for E1 as well as E2/E3"
status: active
source_refs:
  - paper:Hill2022
  - cite:Williamson2020
  - cite:Andrews2022
related:
  - task:t079
  - plan:0005-autoimmune-diathesis-sex-modifier-pais-analysis-plan
  - plan:0006-n3c-synthetic-prototype-autoimmune-sex-pais-pipeline
  - interpretation:0031-t079-n3c-vs-opensafely-vehicle-decision
  - interpretation:0032-t079-bc3-autoimmune-stratum-granularity
  - interpretation:0033-t079-bc5-pasc-case-definition-lock
  - dataset:n3c-recover-longcovid
  - dataset:opensafely-longcovid
  - hypothesis:0004-acute-severity-threshold
  - hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
created: "2026-07-01"
updated: "2026-07-01"
input: "BC-6 acute-severity dateability audit (2026-07-01): re-read of paper:Hill2022 dated severity variable set + ≥45d survival exclusion, against the OpenSAFELY severity sources (SGSS/SUS/HES/ECDS/ICNARC) already recorded in dataset:opensafely-longcovid. No participant-level data accessed; no access gate for this check."
prior_interpretations:
  - interpretation:0033-t079-bc5-pasc-case-definition-lock
relations: []
---

<!-- Mode: CONCEPTUAL / FEASIBILITY TRIAGE (BC-6 of plan:0005 / task:t079). Severity-mediator
dateability + identifiability only; no participant-level data, no severity phenotype execution. -->

# Interpretation: t079/BC-6 — acute-severity dateability

## Verdict

**Both vehicles can date acute-COVID severity relative to a dated index event, so severity is
dateable enough to *compute* E2/E3 candidate estimates — BC-6 clears the measurement/timing
gate for the mediator. It does not, by itself, *identify* E2/E3.** A controlled direct effect
still requires **mediator–outcome no-unmeasured-confounding**, **no exposure-induced
mediator–outcome confounder**, **positivity across severity strata**, and a **clearly-chosen
survivor / competing-risk estimand** — all assumption-dependent and unprovable at design stage.
BC-6's job is narrower than "identification": it confirms the mediator can be *built and dated*,
and it surfaces two design threats that matter more than the "yes," one of them load-bearing.
**(1)** The severity *ladder* is captured unevenly: the top
rungs (hospitalisation, ICU, invasive mechanical ventilation, ECMO, vasopressor, death) are
crisply and durably dated by admission/procedure records in *both* vehicles, but the
*moderate* rung — supplemental oxygen / "needed O₂ but not admitted" — is under-captured and
**differentially** so (home/outpatient oxygen rarely coded; capture depends on care setting),
so a fine-grained WHO-ordinal mediator degrades exactly in its middle. **(2, decisive)** The
**≥45-day survival-inclusion filter** carried from Hill2022 into `plan:0005` **conditions on a
downstream consequence of the mediator itself** (severe acute COVID → acute death): requiring
survival to day 45 to be eligible **truncates the top of the severity distribution and
selects on the very autoimmune→severity→outcome path** the E2/E3 estimands decompose. **This
selection is not confined to E2/E3 — it makes E1 itself survivor-conditional:** "PASC among
≥45-day survivors" is a valid but survivor-scoped total effect, a different target from "failed
recovery after infection"; excluding acute deaths (a consequence of the mediator) can induce
exposure/sex/stratum-specific selection on the primary E1 estimate too. So severity is *dateable*
(BC-6 "yes"), but **both** the total effect (explicit labelling + a death sensitivity) **and** the
mediation estimands (competing-risk treatment) need a selection response, not merely a dated
mediator variable. This is the
**mediator-channel** analog of the exposure-channel finding in `interpretation:0032` (BC-3)
and the outcome-channel finding in `interpretation:0033` (BC-5): the same measurement/selection
structure that shapes the apparent signal on exposure and outcome also shapes it on the
mediator — reinforcing `hypothesis:0008` on a third channel, and putting a concrete,
named reason under the plan's existing decision to hold **E3 exploratory**.

## Findings Summary — severity dateability per vehicle

| Severity rung | N3C (`dataset:n3c-recover-longcovid`) | OpenSAFELY (`dataset:opensafely-longcovid`) | Dating quality for the mediator role |
|---|---|---|---|
| **Death (acute)** | dated death (`death` / OMOP) | ONS dated death linkage | Crisp both — but it is a **competing event**, see below |
| **ICU / ventilation / ECMO** | dated `procedure_occurrence` / device + `visit_detail` (Hill used inv. mech. ventilation, ECMO, vasopressor) | ICNARC dated ICU; SUS/HES procedure/critical-care | **Crisp both** — top of the ladder is where dating is *best* |
| **Hospitalisation ± length-of-stay** | dated `visit_occurrence`; Hill's LOS tiers (1–7 / 8–30 / 31+ d) | SUS/HES dated admitted-patient care; ECDS dated ED | **Crisp both** — the robust primary mediator |
| **Moderate / supplemental oxygen** | inconsistently coded; outpatient/home O₂ sparse | primary-care O₂ coding sparse; home O₂ under-recorded | **Weak & differential both** — the ladder's soft middle |
| **Mild / outpatient only** | defined by *absence* of the above | defined by *absence* of the above | Absence ≠ negative (EHR non-capture) |

**Index anchor (the denominator of "relative to"):** N3C index = earliest positive
test/diagnosis (Hill2022); OpenSAFELY index = dated SGSS test. Severity events are placed in a
fixed **acute window** (candidate index → ≤28 d) so they sit *after* the pre-index autoimmune
exposure and, with a buffer, *before* the ≥90 d PASC ascertainment window (BC-5). A hard upper
bound on the acute window is not optional: without it a *late* hospitalisation — which may be a
PASC *consequence* — would be miscounted as acute-COVID severity, contaminating the mediator
in the reverse-causal direction.

## The load-bearing finding — the ≥45d survival filter selects on a consequence of severity (E1 survivor-conditional; E2/E3 need competing-risk handling)

Hill2022 excludes patients who **died within 45 days of index** (a standard immortal-time /
denominator device, reasonable for the *total-effect* case-control design). But for **E2
(controlled direct effect)** and **E3 (mediation decomposition)**, acute death is not a
neutral exclusion — it is the **terminal rung of the mediator** (autoimmune → severe acute
COVID → death). Conditioning eligibility on ≥45-day survival therefore:

- **Truncates the mediator distribution from the top**, removing realised severe outcomes and
  compressing the severity contrast the CDE is meant to hold fixed;
- **Selects on a common effect of exposure and of severity** — a collider-like selection that
  can bias E2/E3 even when the dated mediator itself is measured perfectly;
- **Interacts with the exposure of interest**: if pre-existing autoimmune disease raises acute
  mortality (plausible — the h0004 path), the excluded set is autoimmune-enriched, so the
  *surviving* analytic cohort is depleted of exactly the high-risk exposed cases, biasing the
  autoimmune → PASC estimate toward the null in a stratum-specific, sex-specific way.

**This bites E1 too, not only the mediation estimands.** The same exclusion makes the *primary
total effect* **survivor-conditional**: "PASC among ≥45-day survivors" is internally valid but
is a different estimand from "failed recovery after infection." Pre-commit one (ideally both) of
two fixes in `plan:0005`: **(a) relabel E1 explicitly as survivor-conditional** — the honest
minimal move, since the ≥45 d filter is Hill-replicable — and **(b) carry a competing-risk /
composite (death-before-ascertainment) sensitivity for E1**, so exposure/sex/stratum-specific
differential acute mortality is not silently absorbed. This is *separate from* the E2/E3
competing-risk treatment.

**This is why severity being "dateable" is necessary but not sufficient.** BC-6's concrete
contribution is to clear the *measurement/timing* gate while converting the plan's
already-committed "E3 is exploratory" from a generic caution into a **named identification
threat with a pre-committed response** (below), attaching a **competing-risk caveat to E2** that
was previously only implicit, and **relabelling E1 as survivor-conditional**. The deeper CDE
identification assumptions (mediator–outcome confounding, no exposure-induced confounder,
positivity across severity strata) remain *unaddressed by BC-6* and stay the substantive E2/E3
risk.

## Design consequences (pre-register; feed `plan:0005` + `plan:0006`)

1. **Primary mediator = coarse, robustly-dated, hospitalisation-based severity** (e.g.
   none / hospitalised-non-ICU / ICU-or-ventilation), which both vehicles date crisply. A
   **finer WHO-style ordinal** that adds the oxygen/moderate rung is a **sensitivity mediator
   only**, because that rung is differentially under-captured (the same measurement-channel
   logic as BC-3/BC-5). Do not let the CDE hinge on the ladder's soft middle.
2. **Enforce temporal order by construction with fixed offsets:** pre-index autoimmune
   exposure → acute-severity window (index → ≤28 d) → **buffer** → PASC ascertainment (≥90 d,
   BC-5). No post-hoc reclassification of late events into "acute severity." Pin **inclusive /
   exclusive boundary conventions** in `windows.yaml` and a rule for **admissions spanning the
   day-28 boundary** (assign by admission date, not discharge) so one long acute admission is
   neither split nor double-counted.
3. **Handle the ≥45 d survival filter on both the total effect and the mediation estimands.**
   Keep ≥45 d survival as the E1 denominator filter (Hill-replicable) **only if E1 is explicitly
   labelled survivor-conditional**, and carry an **E1 competing-risk / composite
   (death-before-ascertainment) sensitivity** alongside it. For E2/E3, treat **acute death as a
   competing risk**, not an exclusion: report the mediation estimands under an explicit
   competing-risk framing (or a bounded selection sensitivity analysis / composite
   severe-outcome-or-death mediator), and flag that the ≥45 d-survivors-only estimate is a
   **lower bound biased by differential acute mortality**. This is the E1/E2/E3 analog of BC-5's
   "the ascertainment defence lives in the design."
4. **Carry the variant-era / vaccination interaction on the mediator.** Acute severity is
   strongly **variant-era-dependent** (Omicron milder) and **vaccination-reduced**; since
   variant era is already a covariate and vaccination-at-index already carries the
   partly-post-exposure caveat (`plan:0005` Model Assumptions), note that the *strength* of the
   severity mediator — and thus the E1↔E2 gap — is era- and vaccination-conditional, not a
   fixed quantity.

## Case-definition / window flag (per AGENTS.md)

- **Acute-severity window:** candidate **index → ≤28 d** (CDC-acute-illness-aligned), a fixed
  offset distinct from both the **≥45 d survival/inclusion** window (E1 denominator) and the
  **≥90 d PASC ascertainment** window (BC-5). BC-6 makes the three windows explicitly
  non-interchangeable and pre-registers the buffer between the acute window and the
  ascertainment window.

## Evidence Quality

Feasibility-grade, fully durable and **no access gate**. The N3C dated severity variable set
and the ≥45 d survival exclusion are read directly from `paper:Hill2022` (in-hand, in the bib);
the OpenSAFELY dated-severity sources (SGSS index, SUS/HES admitted-patient care, ECDS ED,
ICNARC ICU, ONS death) are the same linked datasets already recorded and cited in
`dataset:opensafely-longcovid` (`cite:Williamson2020`, `cite:Andrews2022`). The one
load-bearing inference — that the ≥45 d survival filter selects on the mediator path — is a
standard competing-risk/collider argument applied to Hill's own documented exclusion, not a new
empirical claim.

## Sources (durable pointers)

Checked 2026-07-01.
- **N3C dated acute severity:** `paper:Hill2022` (BMC Public Health 2023;23:2103,
  `doi:10.1186/s12889-023-16916-w`, PMID 37880596) — dated hospitalisation, LOS tiers
  (1–7/8–30/31+ d), invasive mechanical ventilation, ECMO, vasopressor, AKI, sepsis; **≥45-day
  survival exclusion** (Methods). The formal N3C ordinal WHO-scale severity phenotype (Bennett
  et al. 2021, N3C) is a further pointer but is **not** relied on here — Hill's dated variable
  set is sufficient and in-hand.
- **OpenSAFELY dated severity:** `cite:Williamson2020` (OpenSAFELY factors associated with
  COVID-19 death; SUS/HES + ONS death linkage) and `cite:Andrews2022`, plus the SGSS/ECDS/ICNARC
  linkages recorded in `dataset:opensafely-longcovid`.

## Data Quality Checks

Structural mediator-QA facts carried into `plan:0005`/`plan:0006`:
- **Top-of-ladder crisp, middle soft.** ICU/ventilation/ECMO/death dated reliably in both
  vehicles; supplemental-oxygen/moderate rung differentially under-captured → coarse mediator
  primary, ordinal sensitivity.
- **≥45 d survival filter = selection on a consequence of severity**, differential by exposure if
  autoimmune disease raises acute mortality → **E1 becomes survivor-conditional** (relabel + carry
  an E1 death-before-ascertainment sensitivity) **and** E2/E3 need competing-risk handling; the
  ≥45 d-only estimates are differentially-biased lower bounds.
- **Acute-window upper bound mandatory** to stop late (possibly PASC-driven) hospitalisations
  from contaminating the acute-severity mediator in reverse.
- **Severity strength is variant-era/vaccination-conditional** → the E1↔E2 gap is not a fixed
  quantity; report by era where power allows.

## Proposition-Level Updates

None. BC-6 is a mediator-infrastructure/identifiability check; no `proposition:` gains or loses
an evidence-line.

## Hypothesis-Level Implications

- `hypothesis:0004` (acute-severity threshold) — BC-6 confirms the **mediator on the h0004 path
  is measurable and dateable** in both vehicles (the E2/E3 machinery is *computable*; whether it
  is *identified* remains assumption-dependent), while
  sharpening *how*: the measurable mediator is a coarse hospitalisation-based severity, and the
  h0004 path's terminal rung (acute death) is a competing risk that the naive ≥45 d-survivor
  design silently conditions away. The autoimmune ⇄ severity interaction that h0004 predicts is
  therefore estimable but must be read against differential acute-mortality selection.
- `hypothesis:0008` (measurement-channel / ascertainment) — **reinforced on a third channel.**
  BC-3 hit the exposure channel (autoimmune-thyroid mis-capture), BC-5 hit the outcome channel
  (every EHR PASC outcome utilisation-gated), and BC-6 now hits the **mediator channel**
  (ladder-middle under-capture + survival-selection on the mediation path). h0008's core claim —
  that measurement/selection structure, not only the sampling frame, shapes the apparent signal
  — now has instances on all three legs of the E1/E2/E3 estimand triad. The practical
  restatement stands: validity rests on **design defences**, not on any clean channel.

## Evidence vs. Open Questions

**Settled (BC-6):** both vehicles date acute severity relative to a dated index (mediator
*computable*; CDE *identification* remains assumption-dependent); primary mediator = coarse dated
hospitalisation-based severity, fine WHO-ordinal = sensitivity (moderate/oxygen rung differentially
under-captured); temporal order enforced by fixed offsets with an acute-window upper bound and a
buffer before ≥90 d ascertainment; the ≥45 d survival filter makes **E1 survivor-conditional**
(relabelled + E1 death-sensitivity) and is handled as a **competing risk for E2/E3**. **Still open:** **BC-4** (sex × stratum × PASC cell counts — the binding
unknown; BC-6 adds that competing-risk handling of acute death will *further* thin the most
severe exposed cells, so the power test must be run on the survivor-and-mediation cohort, not
just the raw cohort); **BC-7** (individual-level utilisation — load-bearing across exposure
(BC-3) and outcome (BC-5). **Boundary correction:** BC-7 is *not* the fix for the oxygen/moderate-rung
under-capture — utilisation adjustment probes *encounter opportunity*, but outpatient/home-oxygen
missingness is **workflow/site/system-dependent**, not merely a function of contact frequency, so
it is the **coarse-mediator-primary** choice, not BC-7, that handles the oxygen rung).

## New Questions Raised

- Does modelling acute death as a **competing risk** (vs. Hill's ≥45 d exclusion) materially
  change the autoimmune × sex interaction on E2/E3 — i.e. is a non-trivial part of any apparent
  autoimmune→PASC effect being masked by differential acute mortality among exposed cases?
  (Folds into BC-4/analysis on `task:t079`; no standalone `question:` reserved.)

## Limitations & Residual Uncertainty

- **No participant-level counts** — the *magnitude* of the survival-selection bias (how many
  severe exposed cases the ≥45 d filter removes, and its sex/stratum skew) is unquantifiable at
  design stage; it becomes a BC-4 measurement once cohorts are buildable.
- **Oxygen/moderate-rung capture rates** are asserted qualitatively from the coding structure,
  not measured; the exact differential under-capture is an inspection item on the real tier.
- **Identification ≠ dateability (the load-bearing caveat).** BC-6 clears only the
  measurement/timing gate. The CDE's substantive assumptions — **mediator–outcome
  no-unmeasured-confounding**, **no exposure-induced mediator–outcome confounder**, and
  **positivity across severity strata** (some rare-stratum × severity × sex cells may have no
  exposed-severe or no exposed-mild observations) — are **unaddressed here** and remain the real
  E2/E3 risk; they are checked at analysis time, not at design stage.
- **Bennett2021 ordinal-severity phenotype** specifics are a pointer only, deliberately not
  relied on (kept out of the source_refs to avoid an unverified durability claim).

## Updated Priorities

1. **BC-4 remains the binding next check**, now with a BC-6 rider: run the sex × stratum ×
   PASC power test on the **competing-risk / survivor cohort**, since acute-death handling
   thins the most severe exposed cells further — the conservative and correct power test.
2. **Propagate the mediator lock into `plan:0006`'s covariate/severity WP**: primary mediator =
   coarse dated hospitalisation-based severity (index → ≤28 d window), ordinal WHO-style variant
   = flagged sensitivity mediator; encode acute death as a competing event, not a row-drop;
   fix the acute-window upper bound + buffer in `windows.yaml`. WP stays code-gated (`t082`).
3. **Update `plan:0005`**: mark BC-6 resolved; separate the acute-severity window from the
   survival and ascertainment windows in Preprocessing; add the competing-risk/selection caveat
   to E2 and the named survival-selection reason under E3-exploratory; **relabel E1 as
   survivor-conditional and add an E1 competing-risk/composite-death sensitivity** (the ≥45 d
   filter biases E1, not only E2/E3); note the variant-era/vaccination conditionality of the
   mediator strength.
