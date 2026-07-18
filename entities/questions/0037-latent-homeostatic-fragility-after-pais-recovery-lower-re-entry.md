---
id: question:0037-latent-homeostatic-fragility-after-pais-recovery-lower-re-entry
kind: question
title: 'Latent homeostatic fragility after PAIS recovery: lower re-entry threshold
  on reinfection'
status: active
ontology_terms: []
datasets: []
source_refs:
- paper:Bosworth2023
- cite:Bowe2022
- cite:Hadley2024
- cite:Peghin2023
- cite:Hickie2006
- cite:Netea2016
- cite:Prescott2018
- cite:Wang2014sepsis
- cite:Soares2024
origins:
- type: assistant
  ref: explore-ideas-temporal
related:
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a
- question:0012-prevention-vaccination-antiviral-reduces-pais
- theme:0002-temporal-ordering-and-causal-kinetics
created: '2026-07-04'
updated: '2026-07-18'
added_by: explore-ideas:claude-opus-4-8:cand-temporal-reinfection-latent-fragility
lens_views:
- lens: temporal
  rationale: 'Reinfection studies measure new-onset PASC across all prior-infected
    people but do not stratify by whether a first infection caused PAIS that then
    remitted. If the attractor leaves a durable trace (immune memory, epigenetics,
    autonomic wiring), recovered-PAIS patients are a distinct high-vulnerability stratum
    and "recovery" is a metastable near-attractor state. Directly probes whether hypothesis:0001''s
    basin of attraction is structurally remodeled by a PAIS episode. Anchored by Bosworth2023
    (already a project paper, supporting).

    '
  origin_ref: explore-ideas-temporal
---
# Latent homeostatic fragility after PAIS recovery: lower re-entry threshold on reinfection

## Summary

If a first infection drives someone into a post-acute syndrome (long COVID, post-infectious fatigue) that
then **remits**, does that recovered-then-remitted stratum carry a **durable trace** — immune-epigenetic
reprogramming, autonomic rewiring, a remodeled basin of attraction — that makes them a distinct
**high-vulnerability** group who **re-enter** the chronic state more easily on a subsequent infection? Under
this reading "recovery" is **metastable** (a shallow well next to the attractor), not a true return to
baseline, and the discriminating prediction is a **lower re-entry threshold on reinfection specifically in
people with a prior remitted syndrome**. This directly probes whether `hypothesis:0001`'s attractor basin is
**structurally remodeled by a PAIS episode** (vs `hypothesis:0010`, under which recovery is a genuine
one-way return down a gradient).

The central methodological problem — and the reason this question is nearly **unanswered** — is that the
existing reinfection epidemiology estimates **new-onset** syndrome across the *whole* previously-infected
population and does **not** condition on whether the first infection caused a syndrome that remitted. Those
studies answer a **different estimand** than the one this question asks.

## Why It Matters

- **Decision it affects:** whether "recovered" PAIS patients should be counted as returned-to-baseline or
  as a durably-sensitized risk group — which changes reinfection-prevention priority (`question:0012`),
  counseling, and whether attractor-exit is ever complete. It is the empirical test of whether a PAIS
  episode leaves a **permanent scar** on homeostatic set-points.
- **It discriminates the two whole-syndrome dynamical models.** A lower re-entry threshold in the
  remitted-syndrome stratum is a signature of a **retained basin** (`hypothesis:0001`); a re-entry rate no
  higher than in never-affected recoverers is more consistent with a **one-way gradient**
  (`hypothesis:0010`). It is the relapse/hysteresis analogue of the re-entry-threshold falsifier already
  listed under `hypothesis:0010`.
- **Risk if unanswered:** the naive intuition "each reinfection is worse" gets imported unchecked. The
  per-infection data actually point the *other* way (see below), so the specific latent-fragility claim
  must be stated at exactly its estimand or it collapses into a slogan the population data contradict.

## Current Evidence

**Per-infection risk is LOWER on the second infection — but these studies exclude the very stratum the
question is about (estimand mismatch).**

- **Community reinfection cohort (`paper:Bosworth2023`).** In the UK COVID-19 Infection Survey
  (random-sample community; 110,844 first vs 11,244 second infections, age ≥16), new-onset self-reported
  long COVID was **4.0% after first vs 2.4% after second** infection; adjusted odds second-vs-first
  **aOR 0.72** (any) / **0.66** (activity-limiting). **Estimand:** *per-infection* risk of **new-onset**
  long COVID in the **general reinfected population**, and the design **excludes anyone with long COVID at
  the second episode** — so it **cannot** speak to the remitted-then-reinfected stratum. It refutes the
  naive "reinfection is worse per event" reading, but does **not** test latent fragility.
- **Additive cumulative burden (`cite:Bowe2022`).** VA EHR cohort: vs no reinfection, an additional
  infection adds risk of death/hospitalization/multi-organ sequelae. **Estimand:** the **additive burden of
  an extra exposure** (reinfected vs not-reinfected), older/male, **not** a per-event hazard and **not**
  conditioned on prior-syndrome status. Frequently over-read as per-event escalation — it is not.
- **EHR reinfection characterization (`cite:Hadley2024`).** Long-COVID diagnosis proportion was **higher
  after initial than after reinfection** (consistent with Bosworth), with **no stratification by prior-LC
  status and no recurrence analysis**. *(N3C is a gated enclave — cite for estimand framing per D-004, not
  as third-party-reproducible primary evidence.)*

**The actual stratified comparison — remitted-syndrome → re-entry vs recovered-without-syndrome — is
absent, but there is nearer controlled longitudinal evidence than surveys alone.**

- **Prospective cohort, reinfection not associated with worsening (`cite:Peghin2023`).** A prospective
  cohort assessed post-COVID symptoms at **6, 12, and 24 months** and included **38/230 (16.5%)** clinical
  reinfections (median 701 days after first infection); reinfection was **not associated** with worse
  post-COVID syndrome at 24 months (**39.5% vs 35.4%, P=.634**). **Estimand:** controlled longitudinal, but
  it compares reinfected-vs-not in the general prior-infected cohort — it still **does not isolate** the
  exact remitted-PAIS matched estimand (recovered-with-remitted-syndrome vs recovered-without-syndrome). So
  it is *nearer* controlled evidence than the patient surveys, and it leans **against** a gross reinfection-
  driven worsening — but it does not directly test latent re-entry fragility.
- **The precise stratified comparison remains missing.** No controlled, longitudinal study follows people
  whose first infection caused a syndrome that **remitted** and measures their re-entry rate on reinfection
  against a matched recovered-without-syndrome group. The only *directly on-point* signal is **self-selected
  patient survey** data (`cite:Soares2024`, a **preprint**: LC-report likelihood rose ~2-fold from one to two
  infections), **hypothesis-generating only** (LC-enriched, self-report, no controls); a charity survey
  ("~60% recurrence in those in remission") is grey literature at the lowest tier. **The exact estimand is a
  genuine gap** — even though controlled cohorts like `cite:Peghin2023` now bound the coarser reinfection
  question.

**Mechanistic plausibility for a durable latent trace (label: mechanism / read-across, NOT evidence the
re-entry phenomenon occurs).**

- **Trained immunity (`cite:Netea2016`).** Infection/inflammation induces durable epigenetic + metabolic
  reprogramming of innate cells and marrow progenitors that alters responses to *later* unrelated
  challenges — a concrete "immune scarring" mechanism by which a prior episode could lower a re-entry
  threshold. Mechanism only; also note the D-001 boundary (general immune-memory mechanism is
  `health-immunity` territory — imported here strictly as read-across).
- **Post-sepsis persistent fragility (`cite:Prescott2018`, `cite:Wang2014sepsis`).** Sepsis survivors carry
  durable functional/immune impairment and **elevated susceptibility to subsequent infection** (surviving
  sepsis was the strongest predictor of a subsequent infection, RR ~2.83). Post-sepsis / PICS is **within
  this project's primary scope** (sepsis is an acute-infection trigger; see AGENTS.md) — so this is an
  **in-scope post-infectious read-across**, not a non-infectious analogue: durable post-illness vulnerability
  is demonstrated in a *sibling* PAIS. It shows the phenomenon is biologically real in post-infectious
  illness generally; it is still not direct evidence of a lowered *re-entry* threshold in remitted long
  COVID / post-viral fatigue specifically.
- **Trigger-agnostic post-infective fatigue (`cite:Hickie2006`).** The Dubbo cohort shows a stereotyped
  post-infective syndrome after a *first* infection across EBV/Q-fever/Ross River virus, establishing
  durable post-infectious fatigue as trigger-nonspecific — but it does **not** test relapse-on-reinfection
  in already-recovered people. Adjacent, not direct.

## Thoughts

- **Best current interpretation:** the latent-fragility hypothesis is **biologically plausible but
  untested at its exact estimand**. The population reinfection data (`paper:Bosworth2023`, `cite:Hadley2024`)
  show *lower* per-infection new-onset risk on reinfection and — decisively — **exclude the remitted
  stratum**, so they answer a different question; `cite:Bowe2022` measures additive burden, not per-event
  re-entry. Controlled longitudinal data now bound the *coarser* reinfection question — `cite:Peghin2023`
  finds reinfection **not associated** with worse post-COVID syndrome at 24 months — which leans against a
  gross reinfection-driven worsening but still does not isolate the remitted-syndrome matched comparison.
  The only *directly on-point* signal remains uncontrolled patient survey data (`cite:Soares2024`).
  Mechanistic plausibility (`cite:Netea2016`; in-scope post-sepsis read-across) is real but domain-general.
- **The discriminating test:** a cohort that (a) documents a **first-infection syndrome that remitted**,
  and (b) follows **reinfection outcomes**, comparing re-entry rate against **matched recoverers who never
  developed a syndrome** — with objective endpoints where possible to avoid the self-report/ascertainment
  confound that dogs `hypothesis:0008`-class questions. A higher re-entry rate in the remitted stratum ⇒
  retained basin (`hypothesis:0001`); parity ⇒ one-way gradient (`hypothesis:0010`).
- **Major remaining uncertainty:** whether the durable traces that trained-immunity / post-sepsis biology
  make *possible* actually translate into a **measurable re-entry excess** in remitted PAIS, or whether
  remission is (for most) a genuine reset. No current design isolates this.

## Connections to Project

- Related hypotheses: `hypothesis:0001` (basin structurally remodeled by an episode — the claim this tests);
  `hypothesis:0010` (one-way gradient — the rival, whose re-entry-threshold falsifier this operationalizes).
- Related questions: `question:0012` (does prevention/vaccination/antiviral reduce PAIS — reinfection-
  prevention priority depends on this answer).
- Required datasets: cohorts documenting a remitted first-infection syndrome **and** reinfection outcomes,
  with a matched recovered-without-syndrome comparator; objective endpoints preferred. None currently held.
- Required analyses: stratified re-entry-rate comparison (remitted-syndrome vs recovered-without-syndrome),
  conditioned on reinfection; time-to-re-entry / hysteresis-threshold estimation.
- Priority level: **P3** — high-value but gated behind a stratified longitudinal design that does not yet
  exist; the population reinfection literature cannot substitute for it.

## Related

- Topic notes: `theme:0002-temporal-ordering-and-causal-kinetics` (re-entry-threshold / metastability member).
- Article notes: `paper:Bosworth2023`, `cite:Bowe2022`, `cite:Hadley2024` (per-infection / additive
  reinfection epidemiology — different estimand); `cite:Peghin2023` (prospective cohort, reinfection not
  associated with worsening at 24 mo — nearer controlled evidence, but not the remitted-stratum estimand);
  `cite:Soares2024` (the only directly on-point, uncontrolled survey signal); `cite:Netea2016`,
  `cite:Prescott2018`, `cite:Wang2014sepsis` (durable-trace mechanism; in-scope post-sepsis read-across),
  `cite:Hickie2006` (trigger-nonspecific post-infective fatigue, first-infection only).
- Methods/Datasets: prior-syndrome-stratified reinfection cohort with matched recovered-without-syndrome
  controls — the missing design.
