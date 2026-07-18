---
id: question:0047-menstrual-cycle-and-ultradian-symptom-periodicity-as-a-mechanistic
kind: question
title: Menstrual-cycle and ultradian symptom periodicity as a mechanistic discriminator
  of PAIS subphenotypes
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Maybin2025
- cite:Goodship2025
- cite:Sakurada2024
- cite:Boneva2011
- cite:Edelman2022
- cite:Notbohm2023
- cite:Lavery2019
- cite:Nater2008
origins:
- type: assistant
  ref: explore-ideas-temporal
related:
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- question:0007-mechanism-of-female-predominance-in-pais
- theme:0002-temporal-ordering-and-causal-kinetics
created: '2026-07-04'
updated: '2026-07-18'
added_by: explore-ideas:claude-opus-4-8:cand-temporal-menstrual-ultradian-probe
lens_views:
- lens: temporal
  rationale: 'Sharpens hypothesis:0005 by using naturally occurring hormonal oscillation
    as a free high-frequency perturbation probe: different mechanisms predict distinct
    temporal fingerprints (late-follicular immune exacerbation vs sympatho-adrenal
    tracking vs flattened cortisol amplitude vs ovulatory mast-cell peaks), enabling
    within-individual mechanism discrimination and trial stratification. NOTE scope:
    circadian/chronobiology is primarily health-cycles territory; in-scope here only
    because periodicity is used as a PAIS mechanistic discriminator.

    '
  origin_ref: explore-ideas-temporal
---
# Menstrual-cycle and ultradian symptom periodicity as a mechanistic discriminator of PAIS subphenotypes

## Summary

The menstrual cycle is a **naturally occurring, high-frequency hormonal perturbation** — a "free" repeated
provocation of the same person. This question asks whether the **shape** of a patient's symptom fluctuation
across the cycle (and, secondarily, diurnal/ultradian rhythms) is a **mechanistic fingerprint** that could
**discriminate PAIS subphenotypes within an individual**: e.g. a **perimenstrual / luteal immune-
inflammatory** exacerbation vs **sympatho-adrenal** tracking vs a **flattened cortisol amplitude** vs an
**estrogen-linked mast-cell** peak. If distinct mechanisms produce distinct temporal signatures, cyclic
symptom tracking becomes a cheap within-person discriminator and a **trial-stratification** variable. It
sharpens `hypothesis:0005` (reproductive-stage immune-homeostatic margin) and connects to the female-
predominance mechanism question (`question:0007`).

**Scope discipline:** circadian/chronobiology in general is `health-cycles` territory; this question is
in-scope **only** because periodicity is used as a **PAIS mechanistic discriminator**. And the honest status
is that the evidence tier is **low**: a real perimenstrual-worsening signal is now documented, but the
finer "which fingerprint ⇒ which mechanism" discrimination — and any use of it to *subtype* patients — is
**unrealized and, as framed, novel**.

## Why It Matters

- **Decision it affects:** whether the project treats cyclic symptom fluctuation as **noise to average
  out** or as **signal to stratify on**. A validated fingerprint→mechanism map would give a within-person
  mechanism assay and a stratifier for `hypothesis:0005` / `question:0007` analyses and for trial design —
  at near-zero measurement cost (daily diary + wearable).
- **It is a within-person perturbation design** — rarer and more causally informative than the cross-
  sectional snapshots that dominate the field (`theme:0002`): the same patient is probed repeatedly under a
  known, cyclic hormonal input.
- **Risk if unanswered / over-read:** the temptation is to read any perimenstrual worsening as a specific
  mechanism. Current measurements (self-report/app-inferred cycle phase, no confirmed hormones) **cannot
  resolve** the fine "late-follicular vs ovulatory vs perimenstrual" distinctions the fingerprint idea
  needs — so claiming mechanism from phase-timing today would overshoot the data.

## Current Evidence

**Prospective within-person diaries — the real (but small, low-tier) signal.**

- **Long COVID, phase-dependent exacerbation (`cite:Maybin2025`).** Two parts: (a) retrospective survey
  N=12,187 links LC to self-reported menstrual disturbance (**association only**); (b) **prospective daily
  app diary N=54 (930 cycle-days, 29 symptoms)** with symptom severity **highest perimenstrual and
  proliferative** (fatigue, headache, muscle aches, PEM, dizziness). **Estimand:** the diary is genuine
  within-person time-series and the **strongest single anchor** for a phase-locked fingerprint — but small
  N, self-selected app users, **phase inferred from app/self-report (not confirmed hormones)**, and **no
  mechanism stratification**. Licenses "perimenstrual exacerbation is real and within-person," **not**
  "distinct mechanisms produce distinct fingerprints."
- **Cross-condition (LC + ME/CFS) diary (`cite:Goodship2025`, preprint).** Prospectively-collected
  Visible-app data, **N=948** cycling users: menstruation worsens symptoms in both LC and ME/CFS;
  combined-hormonal-contraception users report **lower** burden. **Estimand:** within-person prospective,
  and the contraception contrast is the **nearest thing to using hormone state to stratify** — but
  observational (confounded by indication/user characteristics), self-selected, self-reported diagnoses,
  **preprint**. Closest paper to this question's cross-condition periodicity-as-probe framing; does **not**
  subtype by mechanism.

**Supplementary / context (lower tier or off-target).**

- **LC menstrual symptoms, descriptive (`cite:Sakurada2024`).** Retrospective chart review N=223, single
  clinic: 19.7% had menstrual symptoms (mostly irregularity), worse QOL, elevated cortisol. Cross-sectional,
  referral-selected, no within-cycle tracking — **descriptive prevalence only**.
- **ME/CFS gynecological burden (`cite:Boneva2011`).** Population-based case-control (36/48): higher pelvic
  pain, endometriosis, amenorrhea in CFS. **Comorbidity association, NOT within-cycle periodicity.** *(No
  dedicated prospective daily-diary study of ME/CFS symptom worsening by menstrual phase exists outside the
  `cite:Goodship2025` cross-condition preprint — the common clinical claim of premenstrual ME/CFS worsening
  rests on survey/anecdote. State the gap.)*
- **The axis is perturbable by immune activation (`cite:Edelman2022`).** COVID-19 **vaccination** linked to
  a small (~1 day), temporary, self-resolving cycle-length increase (app data, N=3,959). **Context only**
  (vaccine, not infection) — establishes the reproductive axis is a live perturbation channel, not the
  discriminator itself.

**Mechanistic grounding for *why* a periodic fingerprint would exist (label: general mechanism).**

- **Menstrual immune variation (`cite:Notbohm2023`).** PRISMA meta-analysis (159/110 studies, healthy
  women): immune/inflammatory markers vary across phases (luteal pro-inflammatory shift; peri-ovulatory
  estrogen anti-inflammatory). Grounds the **general premise** that a periodic immune fingerprint *would*
  exist — **not** PAIS-specific, not symptom data.
- **Estrogen–mast-cell / catamenial pattern (`cite:Lavery2019`).** Review + case literature: perimenstrual
  hormone-withdrawal symptom peaks; estrogen upregulates and progesterone suppresses mast-cell activity.
  **Lowest tier** (review + case reports) — plausibility of a hormone-phase-locked mast-cell fingerprint
  only. (Note: catamenial timing is **perimenstrual**, so the candidate "ovulatory mast-cell peak" is one
  of several possible phase-locks, not established.)
- **Cortisol/HPA diurnal flattening (`cite:Nater2008`).** Population-based CFS cases show flattened diurnal
  salivary cortisol amplitude. **Scope-flag:** this is **diurnal (not menstrual)** periodicity — in-scope
  only as one candidate temporal fingerprint; HPA findings in ME/CFS are **heterogeneous** (subgroup, not
  universal), so represent as a subgroup feature.

**The whitespace (the point of the question).** No study operationalizes "distinct temporal fingerprints ⇒
distinct mechanisms ⇒ within-individual mechanism call." `cite:Goodship2025` uses contraception status as a
burden modifier (stratification-adjacent, observational); `cite:Maybin2025` links a phase fingerprint to an
endometrial-inflammatory mechanism at the **group** level. Neither achieves within-person mechanism
discrimination — so the discriminator hypothesis is, as framed, **novel**.

## Thoughts

- **Best current interpretation:** perimenstrual symptom worsening in LC and ME/CFS is now a **real,
  prospectively-observed** within-person signal (`cite:Maybin2025`, `cite:Goodship2025`), and there is
  solid general grounding for *why* a cyclic immune/mast-cell/HPA fingerprint could exist
  (`cite:Notbohm2023`, `cite:Lavery2019`, `cite:Nater2008`). **But** the specific claim — that the *shape*
  of the fingerprint discriminates underlying mechanisms *within a person* — is **unrealized and untested**,
  and current measurements (app/self-report phase, no confirmed hormones, no mechanism readouts) **cannot
  resolve** the fine phase-timing distinctions the discrimination requires. So the defensible verdict is:
  *the periodic signal is real and the discriminator design is worth building; the fingerprint→mechanism
  map itself is not yet evidence, it is the hypothesis.*
- **The discriminating design:** prospective daily symptom + wearable-physiology diaries with
  **hormone-confirmed** cycle phase and **paired mechanism readouts** (perimenstrual inflammatory markers,
  autonomic/HRV, mast-cell mediators, cortisol amplitude), tested for whether distinct fingerprint shapes
  co-segregate with distinct mechanism profiles. **PEM stratification (D-002):** the diary papers report
  PEM/fatigue worsening perimenstrually but do **not** stratify PEM-positive vs PEM-absent — any build-out
  must stratify PEM status.
- **Major remaining uncertainty:** whether fingerprint shape actually maps one-to-one to mechanism (vs many
  mechanisms all producing generic perimenstrual worsening), and whether hormone-confirmed phasing changes
  the picture the app-inferred diaries currently paint.

## Connections to Project

- Related hypotheses: `hypothesis:0005-reproductive-stage-immune-homeostatic-margin` (the reproductive-
  hormone margin this probes); `question:0007-mechanism-of-female-predominance-in-pais` (cyclic-fingerprint
  evidence feeds the female-predominance mechanism).
- Required datasets: prospective hormone-confirmed cycle-phase symptom + wearable diaries with paired
  mechanism readouts, PEM-stratified. None currently held — list in frontmatter `datasets:` when identified.
- Required analyses: within-person periodicity/phase-locking estimation; fingerprint-shape clustering vs
  mechanism-marker profiles; contraception/hormone-state contrasts with confounding controlled.
- Priority level: **P3** — low current evidence tier; value is a cheap within-person discriminator/
  stratifier if the fingerprint→mechanism map validates. Scope-bounded (periodicity as PAIS discriminator
  only; general chronobiology stays in `health-cycles`).

## Related

- Topic notes: `theme:0002-temporal-ordering-and-causal-kinetics` (periodic-perturbation member).
- Article notes: `cite:Maybin2025`, `cite:Goodship2025` (prospective within-person diaries — the real
  signal); `cite:Sakurada2024`, `cite:Boneva2011` (descriptive / comorbidity, not periodicity);
  `cite:Edelman2022` (axis-perturbable context); `cite:Notbohm2023`, `cite:Lavery2019`, `cite:Nater2008`
  (general mechanistic grounding for why a fingerprint would exist).
- Methods/Datasets: hormone-confirmed cyclic symptom + mechanism-marker co-tracking — the missing design.
