---
id: interpretation:0031-t079-n3c-vs-opensafely-vehicle-decision
type: interpretation
title: "t079/BC-1: N3C is the primary vehicle; OpenSAFELY is the pre-committed population-based replication (not primary — coded PASC is differentially under-recorded)"
status: active
source_refs:
  - paper:Hill2022
  - cite:WalkerLongCOVID2021
  - cite:Andrews2022
related:
  - task:t079
  - plan:0005-autoimmune-diathesis-sex-modifier-pais-analysis-plan
  - hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
  - hypothesis:0004-acute-severity-threshold
  - question:0007-mechanism-of-female-predominance-in-pais
  - dataset:n3c-recover-longcovid
  - dataset:opensafely-longcovid
  - dataset:all-of-us-covid
created: "2026-07-01"
updated: "2026-07-01"
input: "Route audit of N3C vs OpenSAFELY against the plan:0005 admissibility gates, with a live OpenSAFELY capability check (docs/OpenCodelists/reports) on 2026-07-01. No participant-level data were accessed."
prior_interpretations: []
relations: []
---

<!-- Mode: CONCEPTUAL / FEASIBILITY TRIAGE (BC-1 of plan:0005). Vehicle decision only; no
participant-level data were available or analyzed. -->

# Interpretation: t079/BC-1 — N3C vs OpenSAFELY vehicle decision

> **⚠️ SUPERSEDED 2026-07-01 (`core/decisions.md` D-004).** The "N3C primary" verdict below rested on
> N3C having an **open synthetic tier to prototype on** — that premise is **false** (N3C synthetic is
> enclave-only and non-downloadable). With the estimand shelved as
> infeasible-under-transparency-standards, this vehicle decision is **void**. Retained as banked
> reasoning; do **not** treat the verdict as operative.

## Verdict

**N3C is the provisional primary vehicle; OpenSAFELY is the pre-committed population-based
replication — not the primary.** Both platforms can carry the *exposure* side of the estimand
well (dated pre-index autoimmune strata, dated infection index, dated acute severity,
individual-level utilisation). The decision is made on two axes where they diverge sharply:
the **outcome** and **prototyping cost**. N3C has the most mature computable PASC phenotype
(`paper:Hill2022` proved the matched design at scale) and an **open synthetic tier we can
build the pipeline on now**. OpenSAFELY's coded long-COVID outcome is **severely and
*differentially* under-recorded** — higher-utilisation patients (including autoimmune
patients) are more likely to be coded, so a coded-only PASC endpoint reintroduces h0008
ascertainment bias **on the outcome side**, which is disqualifying for the *primary* estimate.
OpenSAFELY's population-based sampling frame remains uniquely valuable, so it is retained as
the replication that adjudicates the clinic- vs population-based ascertainment contrast
(`plan:0005` Sensitivity Arbitration rule #4) — conditional on building a non-coded-only PASC
phenotype there.

## Findings Summary

Route triage against the `plan:0005` admissibility gates:

| Vehicle | Role | Decisive strengths | Decisive weaknesses |
|---|---|---|---|
| **N3C** (`dataset:n3c-recover-longcovid`) | **PRIMARY** | Most mature computable PASC phenotype (Hill 1:5 matched, U09.9 + phenotype); millions-scale → best rare-stratum × sex power; **open synthetic tier → prototype now (BC-2 cheaply)**; individual-level utilisation + pre-index ICD history native (fixes Hill's county-proxy + pooled-Charlson gaps) | US healthcare-seeking EHR → sampling-frame ascertainment skew; enclave-only compute; EHR-coded autoimmune/PASC noisy |
| **OpenSAFELY** (`dataset:opensafely-longcovid`) | **POPULATION-BASED REPLICATION** | Near-whole-population England (population-based frame = strongest h0008 defense); dated primary-care autoimmune onset; dated SGSS index + SUS/HES/ICNARC severity; per-patient GP-consultation utilisation | **Coded long-COVID severely & differentially under-recorded** (Walker: 23,273/58M; 26.7% of practices never coded) → coded-only outcome carries outcome-side h0008 bias; **EMIS backend paused → TPP-only ~24M now**; SDC (≤7, round-5) forces rare-cell pooling; England-only |
| All of Us (`dataset:all-of-us-covid`) | diverse-population triangulation (secondary) | intentionally representative US cohort | less-mature PASC phenotype; smaller N than N3C |

**Why not OpenSAFELY-primary despite the better sampling frame:** the estimand's whole point
is to separate a true autoimmune→PASC effect from differential ascertainment. OpenSAFELY fixes
ascertainment on the *sampling-frame/exposure* side but its coded outcome **re-opens the same
bias on the outcome side**, and the two do not cancel. N3C's mature phenotype plus an open
prototyping tier makes it the faster, lower-bias primary — with OpenSAFELY's population frame
deployed exactly where it is decisive (the ascertainment cross-check).

## Evidence Quality

Feasibility-grade, sourced. N3C capabilities are triangulated from the read `paper:Hill2022`
(which executed the matched design in N3C) and the existing `dataset:n3c-recover-longcovid`
entity. OpenSAFELY capabilities are landing-confirmed (2026-07-01) from platform docs
(data-sources, data-access-policy, SDC), the TPP schema report, OpenCodelists, and the
long-COVID-coding [@WalkerLongCOVID2021] and representativeness [@Andrews2022] papers. No
participant-level data were accessed on either platform (N3C
real tier is enclave-gated; OpenSAFELY is federated with no extraction).

## Data Quality Checks

Not an empirical-results interpretation, so no dataset QA was run. The relevant "data quality"
facts are structural and feed the bias model: (a) OpenSAFELY coded-long-COVID under-recording
is **differential by consultation frequency** — the key data-quality hazard; (b) EMIS pause
reduces the OpenSAFELY frame to TPP-only ~24M; (c) SDC suppression (≤7, then round-5)
truncates rare-cell reporting. These are carried into `plan:0005` power-floor and
bias-vs-variance sections, not resolved here.

## Proposition-Level Updates

None. This is a vehicle-feasibility verdict, not an endpoint result; no `proposition:` gains
or loses an evidence-line. In particular nothing here updates `proposition:0039` (immune-state
mediation) — the plan's estimand is upstream of that adjudication.

## Hypothesis-Level Implications

- `hypothesis:0008` (ascertainment meta-finding) is *operationally reinforced*: OpenSAFELY
  concretely demonstrates that even a population-based frame can carry ascertainment bias on
  the **outcome** channel (differential long-COVID coding), sharpening h0008's claim that the
  measurement channel — not only the sampling frame — shapes the apparent signal.
- `hypothesis:0004` (acute-severity threshold): unchanged; both vehicles can date severity in
  the acute window, so the E1-total vs E2-controlled-direct split remains executable.
- No belief update to `hypothesis:0005`; this is infrastructure triage.

## Evidence vs. Open Questions

**Settled (BC-1):** primary = N3C; replication = OpenSAFELY; All of Us as diverse
triangulation. **Still open (BC-2..BC-7):** N3C synthetic-tier prototype + real-tier access
(BC-2); disease-specific autoimmune stratum resolvability with dated onset in each vehicle
(BC-3); sex × stratum × PASC cell counts vs the power floor, especially under OpenSAFELY SDC
and the EMIS pause (BC-4); the non-coded-only PASC phenotype definition (BC-5, now sharper for
OpenSAFELY); severity dateability confirmation (BC-6); individual utilisation covariate
construction (BC-7).

## New Questions Raised

- Does a **broader OpenSAFELY PASC phenotype** (symptom-cluster + functional codes + referral
  codes, not coded "long COVID" alone) recover enough sensitivity to make the population-based
  replication trustworthy? This is the make-or-break for OpenSAFELY's replication role.
- When does the **EMIS research backend reopen**? TPP-only ~24M may underpower the rarest
  strata × sex cells; the timeline changes OpenSAFELY's power.
- (No new `question:` entity reserved — both fold into BC-4/BC-5 on `task:t079` rather than
  warranting standalone questions.)

## Limitations & Residual Uncertainty

- OpenSAFELY autoimmune granularity is **partly unverified**: RA/SLE, IBD, MS codelists
  confirmed on OpenCodelists; Sjögren, systemic vasculitis, inflammatory myositis, and
  autoimmune-thyroid codelist URLs are `[UNVERIFIED]` and must be checked directly (BC-3).
- The exact coded-vs-survey long-COVID under-recording ratio is `[UNVERIFIED]` (full text
  paywalled) — the qualitative "small minority, differential by utilisation" conclusion is
  robust and is what the decision rests on.
- This is a vehicle decision, not an access grant: neither real-N3C nor OpenSAFELY access is
  in hand; both remain gated (BC-2).

## Updated Priorities

1. **BC-2 next:** stand up the analysis on the **N3C open synthetic tier** to prototype the
   matched design, autoimmune strata, severity windows, and the E1/E2 estimands end-to-end
   before pursuing real-tier access.
2. Keep OpenSAFELY warm as the population-based replication; the first OpenSAFELY-specific work
   is BC-5 (design a non-coded-only PASC phenotype) — do not commit to it until BC-2 shows the
   design carries in N3C.
3. Record the primary/replication split into `plan:0005` (BC-1 resolved) and refine its
   Sensitivity Arbitration rule #4 to note OpenSAFELY's outcome-side coding caveat.
