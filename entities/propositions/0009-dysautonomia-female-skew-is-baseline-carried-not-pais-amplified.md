---
id: "proposition:0009-dysautonomia-female-skew-is-baseline-carried-not-pais-amplified"
type: "proposition"
title: "The female predominance of post-infectious dysautonomia (POTS) is the baseline POTS female-predominance carried through, not a PAIS-specific sex amplification"
status: "active"
claim_layer: "empirical_regularity"
identification_strength: "observational"
proxy_directness: "direct"
supports_scope: "hypothesis_bundle"
discusses:
  - frame: "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
    role: "background"
related:
  - "question:0007-mechanism-of-female-predominance-in-pais"
  - "proposition:0005-menopause-pais-symptom-overlap-is-a-measurement-process"
  - "proposition:0007-vascular-autonomic-pathways-contribute-to-the-stage-pais-link"
  - "interpretation:0003-t018-subphenotype-sex-reproductive-stage"
  - "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
  - "task:t018"
source_refs:
  - "paper:Kwan2022"
  - "paper:Eldokla2022"
  - "paper:Wang2026c"
created: "2026-06-22"
updated: "2026-06-22"
---

# Proposition: The female predominance of post-infectious dysautonomia (POTS) is baseline-carried, not PAIS-amplified

## Claim

Infection genuinely **raises the incidence** of postural orthostatic tachycardia syndrome (POTS) and related dysautonomia after SARS-CoV-2, but the **female skew within** post-infectious dysautonomia is the **pre-existing female predominance of POTS carried through**, not a post-infectious sex *amplification*. POTS is ~5:1 female at baseline regardless of trigger; post-COVID POTS cohorts run ~74–80% female, i.e. **at** that baseline, not above it [@Kwan2022; @Eldokla2022]. This is an `empirical_regularity` about the **sex distribution** of one subphenotype; it is deliberately agnostic about the autonomic mechanism, and it does **not** deny that infection causes dysautonomia — only that no published design shows an infection×sex *interaction* above the POTS baseline.

## Evidence Summary

- **Incidence rises, sex distribution does not shift** — Kwan2022 (large controlled EHR; vaccination cohort n≈284,592) orders infection→POTS in time (infection→POTS odds 2.11 [1.70–2.63]; vaccination→POTS 1.52 [1.36–1.71]; infection-vs-vaccination RR 5.35 [5.05–5.68]) yet its **sex-stratified analyses are "similar between sexes"** and the POTS subgroup is 59% female ≈ the 57% cohort baseline. See `evidence-line:0019`.
- **No per-patient sex difference in autonomic burden** — Eldokla2022 (long COVID, n=322, 73% female) finds **no sex difference** in COMPASS-31 total (male 28.0 vs female 26.5, p=0.937; ≥16.4 threshold 77.0% vs 76.6%, p=0.938). See `evidence-line:0020`.
- **Female cohort proportion does not predict POTS/OH prevalence (age does)** — Wang2026c meta-regression across 21 PASC studies (n=2,916): proportion female is **not** a significant predictor of POTS (P=0.083) or OH (P=0.959) prevalence, whereas younger age is strong and consistent (POTS P<0.001, R²=0.664). See `evidence-line:0024`. (The all-cause POTS baseline ~5:1 female matches post-COVID cohorts; that baseline-rate point is kept inline.)

## Caveats

`empirical_regularity` / `background` role for `hypothesis:0005`: this characterises *where the female excess does and does not amplify*, a constraint any female-predominance account must respect, but it is mechanism-agnostic. Three confounds bound it: (1) **ascertainment** — POTS clinics and long-COVID self-referral cohorts are female-skewed by referral, so observed female predominance is partly manufactured (`proposition:0005`); (2) **baseline-rate confounding** — because POTS is female-predominant regardless of trigger, a female-skewed post-infectious cohort is intrinsically uninformative about a sex interaction; (3) **design** — no study reports a formal infection×sex interaction term, so an interaction *above* baseline can be neither confirmed nor excluded, only shown to be unsupported by current data. The formal evidence base is **three independent lines** (Kwan2022 controlled within-cohort incidence + sex-stratified; Eldokla2022 continuous-burden null; Wang2026c study-level meta-regression), each individually qualified (ICD ascertainment; single-center self-report; ecological + marginal-p), so the convergence — not any one line — carries the claim.
