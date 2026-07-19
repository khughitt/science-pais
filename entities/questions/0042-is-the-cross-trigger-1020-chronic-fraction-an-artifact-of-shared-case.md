---
id: question:0042-is-the-cross-trigger-1020-chronic-fraction-an-artifact-of-shared-case
kind: question
title: "Is the cross-trigger ~10–20% chronic fraction an artifact of shared case\
  \ definitions applied without adequate controls?"
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Woodrow2023
- cite:Matta2022
- cite:Ballouz2023
- cite:Hickie2006
origins:
- type: assistant
  ref: explore-ideas-contrarian
related:
- hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent
- hypothesis:0001-shared-dysregulated-attractor
- question:0014-which-pais-case-definition-is-most-biologically-coherent
- question:0015-does-pem-requirement-improve-cross-study-comparability
- theme:0001-deflationary-nulls-and-biomarker-vs-driver
- topic:measurement-ascertainment-artifacts-in-pais
- topic:pais-case-definition-heterogeneity
- interpretation:0043-t127-nilforoshan-recover-design-sensitivity-reconciliation
created: '2026-07-04'
updated: '2026-07-19'
added_by: explore-ideas:claude-opus-4-8:cand-contrarian-chronic-fraction-artifact
lens_views:
- lens: contrarian
  rationale: "Directly attacks a key epidemiological pillar of hypothesis:0001 and\
    \ relates to hypothesis:0008 and question:0014. Long COVID prevalence at >12 weeks\
    \ spans 0–93% by definition; healthcare-record 13.6% vs self-report 43.9%;\
    \ up to 13-point ranges within one cohort by definition choice. If the ~10–\
    20% convergence is definitional, uncontrolled prevalence estimates should not\
    \ anchor mechanistic inference.\n"
  origin_ref: explore-ideas-contrarian
---
# Is the cross-trigger ~10–20% chronic fraction an artifact of shared case definitions applied without adequate controls?

## Summary

A recurring "convergence" argument for a shared PAIS failure mode (`hypothesis:0001`) is that roughly
**10–20% of people develop a chronic post-infectious syndrome across many different triggers**
(SARS-CoV-2, EBV, Q fever, Ross River virus, etc.) — the apparent stability of that fraction across
pathogens being read as a fingerprint of shared biology. This question asks whether that convergence is
instead **manufactured by measurement**: (a) prevalence estimates that swing wildly with the *case
definition* applied, and (b) uncontrolled designs that omit an uninfected comparator and so count
background symptom burden as infection-attributable. If the ~10–20% figure is a definitional/artifactual
coincidence, uncontrolled prevalence estimates should not anchor mechanistic inference about a shared
attractor. It is the epidemiological-pillar instance of `hypothesis:0008`.

## Why It Matters

- **Decision it affects:** whether cross-trigger prevalence *convergence* can be used as evidence for
  `hypothesis:0001`. If the number is definition-driven, the convergence argument is circular (shared
  definition → shared prevalence) and must be replaced with controlled, uniformly-defined estimates.
- **Risk if unanswered:** the project imports a ~10–20% "cross-pathogen constant" as if it were a
  biological invariant, when much of the long-COVID literature it draws on is uncontrolled self-report
  with definition-dependent prevalence spanning nearly the entire 0–100% range.

## Current Evidence

**Supporting the artifact reading (definition- and control-dependence is large):**

- **Prevalence spans ~0–93% across studies (`cite:Woodrow2023`).** A systematic review of 120 studies
  found persistent-symptom prevalence ranging **0%–93%** (pooled 42.1%, 95% PI 6.8–87.9). **Attribution
  caveat:** this full range reflects heterogeneity in *populations, study designs, follow-up length,
  case definitions, and measurement methods together* — not definition alone. The clean
  *definition-only, single-population* signal is narrower (see the ONS example below); the 0–93% figure
  bounds total methodological variability, not the definitional component in isolation.
- **Data source moves the number several-fold (`cite:Woodrow2023`).** Within the same review, pooled
  prevalence was **13.6% by clinical/coded records vs 43.9% by self-report** (and 51.7% under systematic
  assessment). *Attribution note:* this record-vs-self-report gap is a **between-study pooled**
  comparison, not a within-one-cohort split. The genuine **definition-only, single-population** evidence
  is the review's UK ONS worked example, where the *same* population/period yields **3% / 5% / 11.7%**
  purely by changing the definition — an ~8.7-point swing from definition alone, straddling the "~10%"
  figure the convergence argument leans on.
- **Uncontrolled designs overstate the attributable fraction (`cite:Matta2022`, `cite:Ballouz2023`).**
  In CONSTANCES (`cite:Matta2022`), self-reported *belief* of prior infection predicted most persistent
  symptoms (ORs 1.44–16.61) while serology-confirmed infection predicted only anosmia (OR 2.59) — much
  "long COVID" tracks belief, not confirmed infection. In the uninfected-controlled Zurich cohort
  (`cite:Ballouz2023`), the adjusted **excess** risk of any symptom at 6 months over uninfected controls
  was only **17.0%** (95% CI 11.5–22.4), against a raw prevalence far higher — i.e. subtracting a
  control group removes most of the crude burden.

- **A second design family independently reinforces the narrow thesis (`interpretation:0043` / t127).** Nilforoshan2026's test-based claims design (PCR+ vs PCR− + negative-control outcomes, n = 244.7M) drops the negative-control false-positive rate from 53.1% → 4.1% purely by ascertainment control, and RECOVER's own prevalence falls 23% → 10% under its less-biased Omicron/≤30-day subset. Both show apparent burden is **substantially ascertainment-driven** — complementing the Woodrow/Matta/Ballouz evidence via a different data type. **Scope caveat:** this does **not** convert the ~10–20% convergence into "artifact." Nilforoshan measures *attributable ICD-outcome counts* (near-blind to the subjective fatigue/PEM/cognitive cluster, RR ≥ 1.1 floor), a **non-comparable estimand and channel** from RECOVER's PRO syndrome prevalence, so it cannot directly deflate the 10% figure — the same "different estimands cannot be combined" discipline this question already applies to Dubbo vs Ballouz.

**Conflicting evidence (the convergence is not purely a definitional artifact):**

- **Dubbo — internally-standardized similarity across three triggers (`cite:Hickie2006`).** The Dubbo
  Infection Outcomes Study prospectively followed people with three unrelated confirmed acute infections
  (EBV, *Coxiella burnetii*/Q fever, Ross River virus) using a **single case definition and
  clinician-assessed caseness**, and found **~11% (28/253)** met post-infective fatigue-syndrome criteria
  at 6 months, at *similar incidence after each pathogen*. Holding the definition constant while varying
  the trigger, this **cross-pathogen similarity cannot be a shared-definition artifact** — it is genuine
  internally-standardized convergence across three infections. **Scope limit:** Dubbo has **no uninfected
  control arm**, so its ~11% is not an infection-*attributable* (excess-over-background) estimate.

## Thoughts

- **Best current interpretation:** the **uncontrolled, self-reported, definition-variable** prevalence
  figures that dominate the long-COVID literature *are* substantially artifact-prone — total across-study
  variability spans 0–93%, prevalence moves several-fold by data source, shifts ~9 points by definition
  alone in one population (ONS), and partly reflects belief and background symptom burden. **The
  "~10–20% cross-trigger constant survives" claim is *not* established, however, because the two
  best-controlled anchors measure non-comparable estimands and cannot be combined:**
    - **Dubbo (`cite:Hickie2006`)** gives ~11% under *one clinician-assessed definition across three
      pathogens* — strong evidence of genuine cross-trigger *similarity*, but **uncontrolled** (no
      uninfected arm) and limited to EBV / Q-fever / Ross River virus.
    - **Ballouz (`cite:Ballouz2023`)** gives ~17% *infection-attributable excess over uninfected
      controls* — but for **SARS-CoV-2 alone** and a **broad "any symptom" outcome**, a different quantity
      from Dubbo's PIFS caseness.
  The two are neither jointly cross-trigger nor jointly controlled+uniformly-defined, so their rough
  numerical proximity does **not** demonstrate a controlled cross-trigger low-teens constant. What is
  defensible: (a) uncontrolled self-report prevalence should not anchor mechanistic inference, and (b) at
  least one internally-standardized study (Dubbo) shows real cross-pathogen similarity. **No single study
  yet delivers a jointly controlled + cross-trigger + uniformly-defined estimate** — that is the missing
  design, not a settled fact.
- **Major remaining uncertainty:** whether a *uniformly-defined, control-adjusted* chronic fraction is
  actually stable across the full trigger set the project cares about (post-sepsis, post-dengue,
  post-Lyme), or whether Dubbo's three-pathogen convergence is the exception. Most non-COVID triggers
  lack the Dubbo-grade design, so the cross-trigger constant is asserted more widely than it is
  controlled.
- **Priority:** P3 — a measurement-discipline question; its payoff is replacing an artifact-prone
  convergence pillar of `hypothesis:0001` with a defensible controlled estimand, not new mechanism.

## Connections to Project

- Related hypotheses: `hypothesis:0001` (the shared-attractor thesis whose convergence pillar this
  tests); `hypothesis:0008` (measurement/ascertainment-bias instance).
- Related questions: `question:0014` (which case definition is most biologically coherent — the upstream
  definitional choice); `question:0015` (does a PEM requirement improve cross-study comparability).
- Required datasets: prospective, uninfected-controlled, uniformly-defined multi-trigger cohorts with
  confirmed acute infection (Dubbo-class designs for non-COVID triggers).
- Required analyses: definition-sensitivity of prevalence within one population; control-adjusted
  (excess-over-uninfected) attributable fraction; cross-trigger comparison holding definition constant.
- Priority level: P3.

## Related

- Topic notes: `topic:measurement-ascertainment-artifacts-in-pais`;
  `topic:pais-case-definition-heterogeneity` (the definitional-variance object this draws on);
  `theme:0001-deflationary-nulls-and-biomarker-vs-driver` (the convergence-artifact member of the
  deflationary-null program).
- Article notes: `cite:Woodrow2023`, `cite:Matta2022`, `cite:Ballouz2023`, `cite:Hickie2006`.
- Methods/Datasets: control-adjusted, uniformly-defined cross-trigger prevalence (contrast with
  uncontrolled self-report).
