---
id: topic:therapeutics-and-clinical-trials
type: topic
title: Therapeutics and Clinical Trials for Post-Acute Infection Syndromes
status: active
ontology_terms:
- randomized controlled trial
- antiviral therapy
- immunomodulation
- immunoadsorption
- metformin
- low-dose naltrexone
- patient-reported outcome
- post-acute infection syndrome
related:
- topic:biomarkers-and-objective-endpoints
- topic:antigen-pathogen-persistence
- question:0002-antigen-clearance-rescues-symptoms
- question:0012-prevention-vaccination-antiviral-reduces-pais
- question:0009-functional-autoantibodies-drive-dysautonomia
- hypothesis:0001-shared-dysregulated-attractor
source_refs:
- cite:Geng2024
- cite:Krumholz2024
- cite:Yotsuyanagi2024
- cite:Bramante2023
- cite:Fluge2019
- cite:Stein2025
- cite:Zeraatkar2024
created: '2026-06-20'
updated: '2026-06-20'
---
# Therapeutics and Clinical Trials for Post-Acute Infection Syndromes

## Summary

The therapeutic landscape for PAIS is defined by a structural mismatch: candidate
mechanisms are abundant, but the controlled-trial evidence is thin, mostly null, and
crippled by the absence of a validated objective endpoint. The clearest signal is for
**prevention, not treatment** — outpatient metformin during acute COVID reduced subsequent
long-COVID incidence (Bramante2023, COVID-OUT), while two independent RCTs of nirmatrelvir-
ritonavir in *established* long COVID returned null (Geng2024 STOP-PASC; Krumholz2024 PAX-LC,
results reported negative in 2025). The canonical immunomodulator trial in ME/CFS — rituximab
— is also definitively negative (Fluge2019 RituxME), overturning earlier open-label
enthusiasm. Autoantibody-removal (Stein2025 immunoadsorption) shows a promising signal but
only in an uncontrolled, biomarker-stratified subgroup. A living systematic review
(Zeraatkar2024) finds moderate-certainty evidence for just three interventions, all
behavioral (online CBT, combined physical-mental rehabilitation, intermittent aerobic
exercise), and high-certainty evidence that vortioxetine does *not* help cognition. The
cross-cutting problem is that essentially every PASC/ME-CFS trial rests on subjective
patient-reported outcomes (PROMIS-29, symptom Likert scores, SF-36, fatigue scales) or weak
provider-diagnosed labels — there is no validated, treatment-responsive objective surrogate,
which makes both positive and null results hard to interpret (the direct dependency on
`topic:biomarkers-and-objective-endpoints`).

## Key Concepts

Trials are best read as **tests of mechanism hypotheses**, each at a different evidence
maturity. The mapping below pairs each drug class with the mechanism it probes, its best
current evidence, and its endpoint.

**Antivirals — testing viral antigen/persistence as a *treatable* driver (established
disease).** Nirmatrelvir-ritonavir is the most-tested agent. Geng2024 (STOP-PASC; N=155,
15-day course vs placebo-ritonavir, median PASC duration 17.5 months, 99% vaccinated) was
**null** on its primary composite PROMIS Likert endpoint at 10 weeks and stopped for futility;
notably, no participant had detectable baseline stool SARS-CoV-2 RNA. Krumholz2024 describes
the decentralized PAX-LC design (N=100, primary PROMIS-29 physical-health summary at Day 28);
its results, reported in 2025, were likewise negative. Two null NMV/r RCTs in protracted,
mostly-vaccinated long COVID **constrain — but do not refute** — the antigen-persistence
treatment hypothesis (`question:0002`): a 5-day-style short course in long-duration disease may
simply be the wrong dose/duration, or persistence may not be the operative driver in these
cohorts. Endpoint: subjective PROs throughout.

**Antivirals / metabolic agents — testing *prevention* by reducing acute burden.** The one
robustly positive RCT is metabolic, not antiviral: Bramante2023 (COVID-OUT) found outpatient
**metformin** during acute COVID reduced provider-diagnosed long COVID (HR ≈0.59, ~41%
relative risk reduction; HR ≈0.37 if started within 3 days), while ivermectin and fluvoxamine
were null. Yotsuyanagi2024 (SCORPIO-SR) reports a pre-specified prevention subanalysis of the
3CLpro inhibitor ensitrelvir: point-estimate risk reductions for post-COVID symptoms but all
confidence intervals crossed zero (non-significant, exploratory). Together these populate
`question:0012` (does reducing acute viral/inflammatory burden prevent PAIS?) with one positive
(metabolic) and one non-significant (antiviral) prevention signal. Endpoint caveat: COVID-OUT's
outcome is a provider-diagnosed label by self-report — methodologically weak.

**B-cell depletion / autoantibody removal — testing autoimmunity.** Fluge2019 (RituxME; N=151,
Canadian Consensus Criteria ME/CFS) is the definitive **negative** rituximab RCT (≈26% vs ≈35%
response; p=0.22), overturning the same group's promising open-label phase-II results via a high
placebo response — the project's canonical cautionary tale on uncontrolled-trial enthusiasm.
Stein2025 (immunoadsorption; N=20 *prospective cohort, uncontrolled*) takes the complementary
strategy of physically removing autoantibodies in a subgroup **pre-selected** for elevated
β2-adrenergic-receptor autoantibodies: SF-36 physical function rose ~17.75 points (70%
responders), sustained at 6 months — but autoantibody depletion was equal in responders and
non-responders, weakening the simple "β2AR-AB drives symptoms" causal claim. Lesson for the
autoimmunity thread (`question:0009`): biomarker *stratification* may be essential, but
uncontrolled designs systematically overstate effects (cf. RituxME).

**Anticoagulation / microclot-targeting — hypothesis-stage.** No completed RCT of anticoagulation
*specifically for PASC* exists; the triple-anticoagulant microclot protocol is uncontrolled, and
an acute-COVID antiplatelet RCT (REMAP-CAP) did not translate to PASC benefit. This remains a
hypothesis awaiting a controlled test.

**Low-dose naltrexone, neuromodulation, pacing.** LDN evidence is entirely observational/pre-post
with a registered RCT pending; vagal/neuromodulation is at pilot stage. For post-exertional
malaise, **pacing** (energy management) is the leading non-pharmacologic strategy and is now
standard of care, while **graded exercise therapy** is contested — the PACE trial's recovery
claims were challenged on reanalysis, and post-2021 NICE guidance holds that PEM contraindicates
incremental GET. (This pacing-vs-GET stance is a candidate `core/decisions.md` entry.)

## Current State of Knowledge

### What the evidence supports

- **Prevention is more tractable than treatment.** Metformin during acute infection lowers
  long-COVID incidence (Bramante2023) — the strongest pharmacologic RCT signal in the field.
- **Some behavioral interventions have moderate-certainty benefit.** Zeraatkar2024 (24 RCTs,
  3,695 patients) grades online CBT (fatigue, concentration), combined physical-mental
  rehabilitation (recovery), and intermittent aerobic exercise (physical function) as
  *probably* beneficial.
- **Biomarker stratification can surface responders** where unselected trials fail — the
  autoantibody-defined immunoadsorption signal (Stein2025) vs the unselected rituximab null
  (Fluge2019).

### What is contested or unresolved

- **Most treatment RCTs are null or low-certainty.** NMV/r in established LC (Geng2024,
  Krumholz2024), rituximab (Fluge2019), and vortioxetine for cognition (high-certainty null,
  Zeraatkar2024) all failed; the large majority of tested agents have no compelling evidence.
- **No validated objective endpoint.** Every PASC/ME-CFS trial relies on subjective PROs or
  weak diagnostic labels; without a treatment-responsive objective surrogate, a null cannot
  distinguish "drug doesn't work" from "endpoint can't detect the effect," and ~25% of RCTs in
  the living SR had integrity concerns.
- **Dose/duration/timing are unsettled.** The NMV/r nulls may reflect too-short courses in
  too-chronic disease rather than a dead mechanism.
- **Uncontrolled-trial inflation is a recurring trap.** Open-label rituximab and the
  uncontrolled immunoadsorption/LDN/microclot studies all risk the high-placebo-response
  pattern RituxME exposed.

### Tensions between papers

The trials pull against each other on the persistence question: STOP-PASC/PAX-LC nulls argue
*against* antiviral-treatable persistence in established disease, while the metformin and
(non-significant) ensitrelvir *prevention* signals keep alive the idea that acute-phase viral
burden shapes PAIS risk — i.e. persistence may matter at onset but not be reversible later.
Fluge2019 (unselected, null) and Stein2025 (stratified, positive-but-uncontrolled) disagree on
whether autoimmunity is treatable, and the disagreement is confounded by design quality, leaving
the autoimmunity-as-target question genuinely open.

## Controversies and Open Questions

- Is post-acute viral antigen/persistence a *reversible* treatment target, or only a risk factor
  fixed at onset (Geng2024, Krumholz2024 vs Bramante2023, Yotsuyanagi2024; `question:0002`,
  `question:0012`)?
- Does autoantibody-guided stratification convert null immunomodulator trials into positive ones,
  or is the immunoadsorption signal placebo/uncontrolled-design inflation (Stein2025 vs
  Fluge2019; `question:0009`)?
- Can the field define a validated, treatment-responsive objective endpoint, without which trial
  interpretation stays ambiguous (`topic:biomarkers-and-objective-endpoints`)?
- For PEM specifically, what is the evidence-based boundary between pacing (beneficial) and graded
  exercise (contraindicated), and how should trials operationalize it?
- Do any positive signals transfer across triggers (ME/CFS vs long COVID vs PTLDS), as
  `hypothesis:0001` would predict if PAIS share a treatable final common pathway?

## Relevance to This Project

This topic closes a long-standing gap: the corpus was previously thin on treatment. It supplies
the interventional counterpart to the mechanism topics — each drug class is a *test* of a
candidate PAIS mechanism, so the trial results feed back as evidence for/against the project's
hypotheses (antigen persistence, autoimmunity, metabolic/mitochondrial dysfunction). It is tightly
coupled to `topic:biomarkers-and-objective-endpoints`: the endpoint problem is the single largest
threat to interpreting this entire literature, and any pre-registered analysis or trial the project
designs must specify an objective, treatment-responsive outcome. It also sharpens `question:0012`
(prevention) and `question:0002` (antigen clearance) with concrete RCT anchors, and it documents
the methodological discipline — controlled designs, biomarker stratification, placebo accounting —
that the RituxME cautionary tale makes non-negotiable.

## Key References

- Bramante2023 — COVID-OUT phase-3 RCT; outpatient metformin reduced long-COVID incidence (~41%
  RRR); ivermectin/fluvoxamine null. Strongest pharmacologic *prevention* signal.
- Geng2024 — STOP-PASC phase-2 RCT; 15-day nirmatrelvir-ritonavir for established PASC, null on
  PROMIS-29; no baseline stool viral RNA.
- Krumholz2024 — PAX-LC decentralized phase-2 NMV/r design paper (results reported negative 2025);
  pairs with STOP-PASC.
- Yotsuyanagi2024 — SCORPIO-SR; pre-specified ensitrelvir post-COVID prevention subanalysis,
  non-significant (CIs cross zero).
- Fluge2019 — RituxME; definitive negative rituximab RCT in ME/CFS; the cautionary null on
  uncontrolled-trial enthusiasm.
- Stein2025 — repeated immunoadsorption in β2AR-autoantibody-stratified post-COVID ME/CFS;
  promising but uncontrolled (N=20).
- Zeraatkar2024 — living systematic review of long-COVID intervention RCTs; moderate-certainty for
  online CBT, combined rehabilitation, intermittent aerobic exercise; high-certainty vortioxetine
  null; no objective endpoints used.
