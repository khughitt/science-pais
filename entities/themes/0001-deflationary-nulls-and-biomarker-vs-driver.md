---
id: theme:0001-deflationary-nulls-and-biomarker-vs-driver
kind: theme
title: Deflationary nulls and biomarker-versus-driver adjudication
status: active
theme_kind: methodological
theme_scope: project
related:
- question:0017-deflationary-alternatives-vs-shared-pathophysiology
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a
- hypothesis:0011-acute-illness-severity-does-not-predict-chronic-fatigue-in-pais-only
- hypothesis:0012-pais-fatigue-cognitive-symptoms-are-a-trigger-nonspecific-neuroimmune
- hypothesis:0015-ebv-reactivation-consequence-not-cause-of-pais
- hypothesis:0016-fibrinaloid-microclots-nonspecific-inflammatory-marker
- hypothesis:0017-pem-overdiagnosed-via-self-report-nonspecific
- hypothesis:0018-circulating-antigen-as-severity-biomarker-not-driver
- question:0022-immune-state-displacement-mediator-vs-co-traveler
- question:0041-is-female-predominance-in-pais-substantially-an-ascertainment-and
- question:0042-is-the-cross-trigger-1020-chronic-fraction-an-artifact-of-shared-case
- topic:measurement-ascertainment-artifacts-in-pais
source_refs: []
origins: []
evidence_refs: []
created: '2026-07-06'
updated: '2026-07-18'
---
# Theme: Deflationary nulls and biomarker-versus-driver adjudication

## Definition

The **deflationary / biomarker-versus-driver** frame is the project's null-first discipline: before any
candidate PAIS mechanism is promoted to a *driver*, it must outcompete the deflationary account under
which the same observation requires no post-infectious pathophysiology — coincidence-of-repertoire,
ascertainment artifact, deconditioning, nocebo/illness-perception, and **reverse causation** (the marker
is a *consequence* or *severity index*, not a cause). This theme collects the entities that instantiate
that discipline — the standing deflationary bundle and the mechanism-specific nulls that stress-test the
project's positive claims — so that each promotion is scored against its null rather than confirmed by
weak convergence.

## Why It Matters

- **It gates promotion of the project's core thesis.** A shared-mechanism program (shared-mechanism
  therapeutics, cross-trigger biomarker transfer) is only justified if `hypothesis:0001` outcompetes the
  finite-repertoire-coincidence and ascertainment-artifact nulls tracked in `question:0017`. Making the
  null bundle a first-class organizing frame is the structural guard against a project whose thesis is
  "shared failure mode" sliding into confirmation bias.
- **It sharpens study design.** Naming each null forces the question "what observation separates a real
  driver from *this* deflationary account?" — which is exactly what turns a marker claim into a testable
  one (antigen-clearance RCT for `hypothesis:0018`; severity-adjusted association for `hypothesis:0015`;
  matched-inflammatory-control comparison for `hypothesis:0016`; objective-vs-self-report specificity
  for `hypothesis:0017`).
- **It is the home for a recurring epistemic task** — the standing companion to `/science:bias-audit`,
  where positive claims are re-scored against their nulls.

## Boundaries

- **In-scope:** deflationary *accounts* of PAIS phenomena; mechanism-specific null hypotheses that a
  measured marker is a co-traveler, severity index, non-specific inflammatory readout, or reverse-caused
  artifact rather than a driver; and the adjudication designs that would decide driver-vs-marker.
- **Out-of-scope (stays where it lives):** the *positive* mechanism claims themselves (they remain their
  own hypotheses; this theme only organizes their nulls); generic measurement-artifact cataloguing that
  is not about a specific driver-vs-marker call (that stays in
  `topic:measurement-ascertainment-artifacts-in-pais`); and case-definition heterogeneity as such
  (`topic:pais-case-definition-heterogeneity`), which *feeds* the ascertainment null but is a distinct
  object.

## Current Project Links

- **Hub:** `question:0017-deflationary-alternatives-vs-shared-pathophysiology` — the five-account
  deflationary bundle scored against the project's positive claims.
- **Thesis under test:** `hypothesis:0001-shared-dysregulated-attractor`;
  `question:0022-immune-state-displacement-mediator-vs-co-traveler` (the mediator-vs-co-traveler split).
- **Ascertainment-artifact nulls (grounded 2026-07-06 → 2026-07-18, t099):**
  `question:0041` (is female predominance substantially an ascertainment / healthcare-seeking artifact —
  answer: ascertainment *plausibly inflates* the observed excess [cleanest as a *mechanism* in
  fibromyalgia, a non-infectious D-003 read-across], but the *biological-vs-reporting composition of the
  residual is unresolved* — not "real biology persists") and `question:0042` (is the cross-trigger
  ~10–20% chronic fraction a shared-case-definition artifact — answer: uncontrolled self-report prevalence
  is heterogeneity/definition-driven and overstates the attributable fraction; a controlled + cross-
  trigger + uniformly-defined constant is *not* established because the best anchors [Dubbo ~11%
  uncontrolled/3-pathogen; Ballouz ~17% controlled/COVID-only-broad-outcome] measure non-comparable
  estimands). Both are sex/epidemiology-specific instances of `hypothesis:0008`.
- **Structural / whole-syndrome nulls:**
  `hypothesis:0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a`,
  `hypothesis:0011-acute-illness-severity-does-not-predict-chronic-fatigue-in-pais-only`,
  `hypothesis:0012-pais-fatigue-cognitive-symptoms-are-a-trigger-nonspecific-neuroimmune`.
- **Mechanism-specific nulls (2026-07-06 pass):**
  `hypothesis:0015-ebv-reactivation-consequence-not-cause-of-pais`,
  `hypothesis:0016-fibrinaloid-microclots-nonspecific-inflammatory-marker`,
  `hypothesis:0017-pem-overdiagnosed-via-self-report-nonspecific`,
  `hypothesis:0018-circulating-antigen-as-severity-biomarker-not-driver`.
- **Feeder topic:** `topic:measurement-ascertainment-artifacts-in-pais`.

## Guardrails

- **Absence of a positive signal is not evidence for the null.** A non-arbitrating null at low power (e.g.
  the t035 cross-trigger pathway-overlap reanalysis) neither confirms coincidence-of-repertoire nor
  refutes the attractor — it enters only as "existing data cannot adjudicate." Do not let underpowered
  nulls masquerade as support for the deflationary account.
- **Deflationary ≠ nihilistic.** Several nulls are two-sided: objective post-exertional pathology exists
  (`hypothesis:0017` must stay scoped to self-report specificity); tissue-reservoir antigen is not
  refuted by plasma-antigen nulls (`hypothesis:0018` constrains circulating, not sequestered, antigen).
  Hold each null at the exact scope its evidence supports.
- **Don't collapse layers:** a *severity biomarker* claim, a *reverse-causation* claim, and a
  *non-specificity* claim are distinct null structures with distinct discriminating tests; keep them
  separate rather than lumping as "it's probably not real."

## Downstream Work

- Recurring bias-audit scoring of the mechanism-specific nulls (h0015–h0018) against `hypothesis:0001`.
  First pass: `report:0006-bias-audit-deflationary-nulls-vs-shared-attractor` (t104, 2026-07-07) — all four
  nulls LIVE + currently non-adjudicable (every discriminating test prospective); h0017's "no objective
  basis" strong form already refuted; h0018 plasma-driver reading under genuine threat (Mateu2026). Answers
  the convergence question below: nulls **fragment by structure but three of four converge on a shared
  "severity-index confound" axis** (h0015/h0017/h0018 → h0011/h0008). Scored as *self-audit / internally
  consistent* — an out-of-lineage `/science:compare-hypotheses` pass is the recommended independent check.
- The discriminating designs each null implies: antigen-clearance RCT readout (`question:0002`),
  severity-adjusted EBV association + ordering (`question:0054`), matched-inflammatory-control microclot
  comparison, and objective PEM specificity (`question:0049`).
- See the `explore-followups` task group (contrarian-null batch) for the enumerated follow-ups.

## Open Questions

- Does the mechanism-specific-null set converge on a single deflationary reading (most "drivers" are
  severity indices) or fragment (each mechanism fails its null differently)?
- Is "biomarker-vs-driver" better modeled as a per-mechanism call or as one shared severity axis that
  many markers load onto?

## Update Triggers

- A new positive mechanism claim entering the project (it should arrive with its null registered here).
- Any adjudicating result — a positive antigen-clearance or anti-EBV trial, a specificity-confirming PEM
  assay, or a severity-adjusted association that survives — which would retire or promote the
  corresponding null.
- A `/science:bias-audit` pass that re-scores the bundle.
