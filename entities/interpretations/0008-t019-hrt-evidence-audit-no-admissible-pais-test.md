---
id: interpretation:0008-t019-hrt-evidence-audit-no-admissible-pais-test
type: interpretation
title: "t019: hormone-therapy evidence is acute, ascertainment-confounded, or clinical-management\
  \ only — no admissible direct HRT to PAIS test exists"
status: active
source_refs: &id001
- paper:Costeira2021
- paper:Newson2021
- paper:Stewart2021
- paper:Silva2024
- paper:AlcaldeHerraiz2025
- paper:Neuhouser2024
related:
- proposition:0006-hormone-therapy-effects-on-pais-are-context-dependent
- evidence-line:0037-costeira2021-hrt-cocp-divergence-acute-supports-hormone-therapy-context-dependence
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- question:0013-reproductive-stage-failed-immune-recovery-after-infection
- topic:menopause-sex-hormones-and-pais-risk
- interpretation:0003-t018-subphenotype-sex-reproductive-stage
- task:t019
- paper:Neuhouser2024
- interpretation:0020-t045-neuhouser2024-whi-hrt-gap-triage
- task:t045
created: '2026-06-23'
updated: '2026-06-25'
input: *id001
prior_interpretations: []
relations: []
---
<!-- Mode: CONCEPTUAL. Input is a corpus-level audit of hormone-therapy (exogenous-hormone) evidence
in the project's paper set against the dimensions task:t019 specifies — acute vs post-acute window,
route/dose/timing/indication, comorbidity, healthy-user/indication bias — and a disposition decision
(causal-PAIS-admissible vs clinical-screening/symptom-management context only). No new pipeline output.
Findings are literature_evidence / expert_judgment. -->

# Interpretation: t019 — hormone-therapy evidence is acute, ascertainment-confounded, or clinical-management only; no admissible direct HRT→PAIS test exists

## Verdict

**Verdict:** [⌀] Non-adjudicating — the corpus contains **no admissible direct test of an exogenous-hormone-therapy (HRT/COCP) effect on a post-acute PAIS outcome**. Every hormone-therapy datum falls into one of five non-admissible categories: (a) acute-COVID on a symptom-*predicted* outcome (Costeira2021); (b) a self-selected survey (Newson2021); (c) a clinical-management recommendation (Stewart2021); (d) a post-acute study that treats hormone-therapy use as a *nuisance covariate* rather than the exposure, so it yields no HRT-effect estimate (Silva2024); or (e) an explicit non-test that names the gap from the cohort side (AlcaldeHerraiz2025, UKB long COVID, did not test HRT). The one population-scale HRT signal (Costeira2021, ↑predicted acute COVID, OR 1.32) is endpoint-dependent, direction-divergent from COCP, and vulnerable to menopause-symptom-overlap ascertainment and missing route/dose/indication. Disposition: hormone-therapy evidence is admissible to PAIS work **only as clinical-screening / symptom-management / measurement-confound context**, not as causal evidence for or against an HRT→PAIS effect.

## Findings Summary

The t019 audit sorted every hormone-therapy-relevant source in the corpus by the dimensions the task specifies. Three findings.

1. **No direct HRT→post-acute-PAIS outcome study exists (`null`, `literature_evidence`).** Across the corpus, no study estimates an exogenous-hormone-therapy effect on a *post-acute* PAIS outcome. `paper:AlcaldeHerraiz2025` (UK Biobank long-COVID) states the gap explicitly — it did not test menopause stage, HRT, or oestradiol. `paper:Silva2024` (MY-LC) is post-acute but treats hormone-therapy users only as a **nuisance covariate** (its testosterone–symptom-burden finding is endogenous-hormone evidence, deliberately computed *excluding/adjusting* HT users), so it is not an HRT-effect estimate. The decisive design — HRT exposure → PAIS outcome, with route/dose/timing/indication and severity/comorbidity adjustment — is unrun.

2. **The only population-scale HRT signal is acute, predicted, and confounded (`methodological`/`literature_evidence`).** `paper:Costeira2021` (COVID Symptom Study app) is the sole large hormone-therapy comparison: HRT ↑ predicted COVID (OR 1.32, 1.16–1.49) but **not** hospitalization; COCP ↓ predicted COVID (OR 0.87) and ↓ hospitalization (OR 0.79). This is (i) **acute-COVID**, not post-acute; (ii) on a **symptom-model–predicted** outcome maximally vulnerable to the menopause↔COVID symptom overlap — HRT users are by indication symptomatic menopausal women, so the symptom-predicted outcome is open to inflation in that group (a bias pathway Costeira2021 does not itself identify or rule out); (iii) missing **type/route/dose/duration/indication**; (iv) **direction-divergent** between two estrogen-containing therapies. It cannot be transported to a PAIS causal claim. Its admissible content is exactly the *non-uniformity* it displays — captured as weak proxy support for `proposition:0006` (`evidence-line:0037`).

3. **The remaining HRT mentions are clinical-management or hypothesis-generating only (`conceptual`).** `paper:Newson2021` (self-selected social-media survey, n=460, conference abstract) and `paper:Stewart2021` (perspective recommending a *trial-of-HRT response* as a deficiency-screening heuristic) both favor a hormone-deficiency/HRT framing but carry no controlled exposure→outcome estimate; the project's own prior reads already weight them below clinic cohorts and flag the causal overstatement. They belong to clinical screening / symptom management, not causal inference.

## Evidence Quality

Conceptual-mode assessment (grounding / independence / testability):

- **Grounding.** The audit is grounded in the project's existing paper entities and their primary numbers (Costeira2021 ORs and the explicit data-availability gap; AlcaldeHerraiz2025's stated non-coverage of HRT; Silva2024's HT-excluded modeling). The non-existence claim is a corpus-scoped absence, corroborated by AlcaldeHerraiz2025 naming the same gap from the UKB side.
- **Independence.** The two evidence lines now on `proposition:0006` are independent (Costeira2021 CSS cohort vs Averyanova2022 mechanism review); they are both **weak/proxy** and do not raise the proposition above prediction-grade.
- **Load-bearing weakness.** The audit cannot distinguish "HRT has no PAIS effect" from "the effect is unmeasured": this is a **gap verdict**, not a null effect. The one signal that exists (Costeira2021) is in the wrong window (acute) and on the wrong outcome (predicted), so it constrains nothing about PAIS causation.

## Data Quality Checks

Not a data pipeline (corpus audit). Entity-provenance checks: all sourced numbers were read against the existing paper entities (`Costeira2021`, `Newson2021`, `Stewart2021`, `Silva2024`, `AlcaldeHerraiz2025`), which were themselves ingested from PDFs / full text. One methodological flag, carried as Finding 2: the sole population HRT estimate is on a symptom-predicted outcome with indication/ascertainment confounding and no route/dose/indication data. No control/dimensionality/sample-count checks apply.

## Proposition-Level Updates

- **`proposition:0006` (hormone-therapy effects on PAIS are route/dose/timing/indication-dependent) — confirmed and sharpened, still prediction-grade.** New supporting `evidence-line:0037` (Costeira2021, **weak**, **proxy_support**): the within-study HRT↑/COCP↓ divergence on the same outcome, with route/dose/indication unavailable, is a concrete instance of the non-uniformity the proposition asserts. But the audit also *sharpens the caveat*: there is **no admissible direct HRT→PAIS test** in the corpus, and the one population signal is acute + ascertainment-confounded. The proposition remains **more prediction than result**; the t019 fragility flag it carried is now *explained* (it is a genuine evidence gap, not an oversight), not closed. Note on belief state: adding the second line moves the aggregated state from one-line fragile to two-line "supported", which **newly trips `belief.fragile-single-line`** on `proposition:0006` (dropping either weak line reverts it to fragile). This is **expected and honest, not an over-promotion artifact**: the two lines sit in genuinely distinct `independence_group`s (`averyanova-mech` mechanism review vs `costeira2021-css-cohort`), so this is not the same-cohort mis-grouping the check usually catches — it is the correct signal that the proposition rests on two individually-removable weak proxy lines, mirroring the project's pre-existing tolerated flag on `evidence-line:0012`. `proposition:0006` is also a `background` member of the `hypothesis:0005` bundle (excluded from the belief conjunction), so the flag does not move warranted hypothesis belief.
- **No "HRT protects/harms PAIS" proposition minted** — neither direction is licensed; the disposition is explicitly *context-only*.

## Hypothesis-Level Implications

`hypothesis:0005-reproductive-stage-immune-homeostatic-margin` — **unchanged in belief; provenance updated.** `proposition:0006` is a `background` member and does not enter the bundle's weakest-link conjunction, so this audit does not move warranted belief in H0005. It does close one of H0005's open bookkeeping items (the t019 HRT-evidence audit) and confirms that the hormone-*therapy* arm of the reproductive-stage story is, for now, evidentially empty for causal purposes — consistent with H0005's own Organizing Conjecture, which disclaims a direct menopause/hormone→PAIS cause. The live mediator-level signal for H0005 stays the **endogenous** gonadal-steroid work (Silva2024 testosterone; Shahbaz2025; AlcaldeHerraiz2025 SHBG), not hormone therapy.

## Evidence vs. Open Questions

- **`question:0013` (does reproductive-stage transition change the probability of failed recovery?)** — **unchanged.** The audit removes hormone-therapy observational associations from the admissible-causal-evidence pool for this question, leaving the endogenous-hormone and longitudinal-design routes as the only live paths. The HRT literature is reclassified as ascertainment/measurement context.
- **`question:0007` (mechanism of female predominance)** — unchanged; HRT evidence does not bear on the mechanism, only on a confound to watch.

## New Questions Raised

1. **(empirical, medium)** Does any accessible cohort carry **validated HRT exposure with route/dose/timing/indication** *and* a post-acute PAIS outcome (e.g. All of Us prescription records — cf. `task:t039`; UKB primary-care HRT prescriptions)? This is the design that would convert `proposition:0006` from prediction to test. Indication bias must be handled by design (active-comparator / new-user), not adjustment alone.
2. **(methodological, medium)** Is the COCP acute-protective signal (Costeira2021) reproducible on a *tested* (not symptom-predicted) outcome and on a younger-female active-comparator design that breaks healthy-user confounding? Even if so, it remains an acute-window result and does not transport to PAIS without a post-acute endpoint.
3. **(methodological, low)** Can the menopause↔PAIS symptom-overlap ascertainment bias (the pathway Costeira2021's HRT↑ signal is vulnerable to) be quantified, so future symptom-defined PAIS outcomes can be de-biased for HRT-user status?

## Limitations & Residual Uncertainty

- This is a **corpus-scoped audit**, not a registered systematic review; a future HRT-prescription-linked long-COVID study could overturn the non-existence finding. The disposition is correct *for the current corpus*.
- The verdict is a **gap** (`[⌀]` non-adjudicating), not a null effect: it asserts no admissible HRT→PAIS estimate exists, not that HRT has no PAIS effect.
- `evidence-line:0037` rests on an **acute, symptom-predicted** outcome; its only admissible content is the non-uniformity/heterogeneity of exogenous-hormone effects, deliberately held **weak/proxy** so it cannot promote `proposition:0006` toward an effect estimate.
- **Neuhouser2024 triaged (WHI, `Annals of Epidemiology`; `interpretation:0020`).** A WHI long-COVID risk-factor analysis in postmenopausal women (1,237 COVID-positive respondents; 425 long COVID; machine-learning top-20 risk-factor screen) exists and corrects the old shorthand that WHI had not analyzed long COVID in this population. But it does **not** supply an admissible HRT→PAIS estimate: hormone therapy is absent from the article text, absent from the reported top-20 predictors, and no HRT/MHT odds ratio or null estimate is reported. The Supplementary Table S1 candidate list was blocked by PMC reCAPTCHA during t045, so whether MHT was an unselected candidate versus never included remains unresolved. The `[⌀]` gap verdict stands.

## Updated Priorities

- **Close `task:t019`** with the disposition: hormone-therapy evidence is admissible to PAIS work **only as clinical-screening / symptom-management / measurement-confound context**; no causal HRT→PAIS reading is licensed; `proposition:0006` confirmed as prediction-grade with the fragility now explained as a real gap.
- **Route the "test it" path through `task:t039`** (All of Us hormone/prescription coverage) and the UKB primary-care HRT-prescription option — the only realistic vehicles for a route/dose/indication-resolved, active-comparator HRT→PAIS design. Keep `task:t040` (RECOVER ancillary) as the endogenous-hormone primary test; it is a separate exposure axis.
- **Keep HRT out of the causal-covariate exposure role** in PAIS analysis design: enter HRT status as a confounder/ascertainment variable with route/dose/indication where available, never as a clean estrogen-dose exposure (the Costeira2021 lesson).
- **Neuhouser2024 resolved by `task:t045`:** keep it as WHI risk-screen context, not as a `proposition:0006` evidence-line. The decisive HRT test still requires explicit HRT exposure modeling with route/dose/timing/indication and active-comparator/new-user handling.
