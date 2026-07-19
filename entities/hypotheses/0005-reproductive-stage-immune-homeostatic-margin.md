---
id: hypothesis:0005-reproductive-stage-immune-homeostatic-margin
kind: hypothesis
title: Reproductive-stage transitions alter immune homeostatic margin and modify risk of failed post-infectious recovery
status: active
source_refs:
- cite:Shah2025
- cite:Stewart2024
- cite:Humphreys2025
- cite:Averyanova2022
- cite:Costeira2021
- cite:Mishra2020
- cite:Rebman2026
- cite:Kawai2025
- cite:Shahbaz2025
- cite:Neuhouser2024
- cite:Boneva2015
related:
- question:0013-reproductive-stage-failed-immune-recovery-after-infection
- question:0007-mechanism-of-female-predominance-in-pais
- interpretation:0008-t019-hrt-evidence-audit-no-admissible-pais-test
- hypothesis:0001-shared-dysregulated-attractor
- hypothesis:0004-acute-severity-threshold
- topic:menopause-sex-hormones-and-pais-risk
- paper:Neuhouser2024
- paper:Boneva2015
- interpretation:0020-t045-neuhouser2024-whi-hrt-gap-triage
- interpretation:0026-t043-boneva2015-early-menopause-directionality
- interpretation:0042-t125-sex-chromosome-vs-hormone-pasc-decomposition
- proposition:0044-female-pasc-bias-x-chromosome-dosage-rival
- question:0080-sex-chromosome-vs-hormone-decomposition-pais
- topic:long-covid-immune-dysregulation
- immunity:topic:endocrine-immune-recovery-thresholds
- immunity:topic:sex-hormone-life-stage-immune-homeostasis
- immunity:topic:sex-as-a-modifier-of-immune-homeostasis
- cycles:topic:menstrual-cycle-menopause-immune-modulation
- cycles:topic:reproductive-aging-and-menopause
- question:0047-menstrual-cycle-and-ultradian-symptom-periodicity-as-a-mechanistic
required_capabilities:
- analysis_role: mr_exposure
  trait: sex-hormone-biomarker
created: "2026-06-19"
updated: "2026-07-19"
datasets:
- dataset:ruth-2020-shbg-testosterone-gwas
- dataset:covid19-hgi-longcovid-gwas
---
# Hypothesis: Reproductive-stage transitions alter immune homeostatic margin and modify risk of failed post-infectious recovery

## Organizing Conjecture

Reproductive-stage transitions, especially perimenopause and menopause, can shift immune homeostatic margin: the distance between a host's baseline immune-regulatory state and the threshold at which an acute infection fails to resolve into normal recovery.
The proposed mechanism is not that menopause directly causes PAIS.
Rather, changing sex-hormone exposure and reproductive-stage context may modify antiviral resolution, Treg/Tfh/Th17 balance, B-cell and type-I-IFN tone, endothelial or thromboinflammatory state, autonomic symptoms, tissue repair, and symptom attribution.
This may lower or raise the effective threshold for entering the shared dysregulated attractor described by `hypothesis:0001-shared-dysregulated-attractor`.

## Proposition Bundle

> **Migrated to first-class entities (t021, 2026-06-21).** Each bundle item is now a standalone
> `proposition` with its own support/dispute `evidence-line`s, and **both causal directions** are
> represented. The role labels below are `membership_role` on each proposition's `cito:discusses`
> edge to this hypothesis — only **`core`** members enter the bundle's weakest-link belief
> conjunction; `rival` and `background` inform interpretation without raising or lowering warranted
> belief. Per-variable confounder/collider roles are **derived** from
> `patch-definition:menopause-pais-causal-dag` + its back-door query, not authored on the propositions.

### Core — enter the belief conjunction

- `proposition:0001-reproductive-stage-transition-shifts-the-failed-recovery-threshold` — **forward (P→) effect**: reproductive-stage transition shifts the effective host-reserve / failed-recovery threshold, so PAIS risk is reproductive-stage-dependent at a given insult.
- `proposition:0002-reproductive-stage-transition-modifies-immune-regulatory-pathways` — **mechanism** beneath P→: the transition modifies immune-regulatory pathways (antiviral resolution, Treg/Tfh/Th17, B-cell/type-I-IFN tone, endothelial, thromboinflammatory). **Caveat: this core leg is single-line fragile** — its support is two weak lines, dropping either flips it to fragile, so the conjunction's weakest link is a *core* member, not just the background ones. Independent corroboration here is the priority — but the t036 feasibility search (`report:0004`) found **no off-the-shelf vehicle** for it (R1 hormone-panel depth and R5 pre-infection baseline are anti-correlated across candidate cohorts); the live paths are `task:t038` (IMPACC, mediator-compatible only) and `task:t040` (RECOVER ancillary study, primary positive test, post-seed-stage). **t125 update (`interpretation:0042`, 2026-07-19):** a re-read of `paper:Chaulagain2026` found the direct-PASC gonadal-steroid evidence "limited" and tilted the PASC-specific weight toward the *sex-chromosome-dosage* axis, raising the rival `proposition:0044` to parity — this **confirms** (does not rescue or refute) the fragility of this leg, and makes the hormone-vs-chromosome decomposition (`question:0080`) the standing blocker for attributing the female PASC excess to hormones above and beyond sex/chromosome dosage.

### Rival — contrasted against; excluded from the conjunction

- `proposition:0003-infection-pais-perturbs-the-reproductive-axis-and-menopausal-timing` — **reverse (P←) direction**: infection/PAIS perturbs the reproductive axis and menopausal timing. Roled `rival` relative to this forward hypothesis; the cross-sectional hormone evidence is **symmetric** between P→ and P← and cannot yet discriminate them. Boneva2015 weakly narrows the ambiguity for surgical menopause because gynecologic surgery preceded CFS onset in most dated cases, but it does not adjudicate natural menopause or infection-indexed reverse causation (`interpretation:0026`).

### Background — inform interpretation; excluded from the conjunction

- `proposition:0004-female-reproductive-stage-excess-requires-confounder-decomposition` — the crude female / reproductive-stage excess is not interpretable without separating sex-at-birth, age, transition, HRT, pregnancy, comorbidity, symptom overlap, and ascertainment.
- `proposition:0005-menopause-pais-symptom-overlap-is-a-measurement-process` — menopause↔PAIS symptom overlap is a measurement process that can inflate, mask, or reshape apparent associations without fully explaining female predominance.
- `proposition:0006-hormone-therapy-effects-on-pais-are-context-dependent` — HRT effects, if present, are route-/dose-/timing-/indication-/comorbidity-dependent rather than uniformly protective or harmful. **Audited (t019, `interpretation:0008`, 2026-06-23; t045 WHI triage, `interpretation:0020`, 2026-06-25):** no admissible direct HRT→post-acute-PAIS test exists in the corpus. Neuhouser2024 supplies WHI long-COVID risk-screen context in postmenopausal women, but no reported HRT/MHT effect estimate. The thinness is a genuine evidence gap; HRT evidence is admissible only as clinical-screening/measurement-confound context, not causal. Two weak/proxy lines now support the context-dependence content (`evidence-line:0014`, `evidence-line:0037`).
- `proposition:0007-vascular-autonomic-pathways-contribute-to-the-stage-pais-link` — vascular and autonomic pathways contribute to the association partly independent of classical adaptive autoimmunity.

## Current Uncertainty

The hypothesis is plausible but fragile.
Current evidence supports female sex as a PAIS risk factor and supports broad hormone-immune mechanisms, but direct hormone-measured longitudinal PAIS evidence is sparse.
The best long-COVID risk evidence does not isolate perimenopause from age, sex, pregnancy, comorbidity, and ascertainment [@Shah2025].
The menopause-long-COVID clinical literature documents symptom overlap and care needs, but it does not establish menopausal transition as an independent causal exposure [@Stewart2024; @Humphreys2025].

## Predictions

- In longitudinal cohorts, the association between reproductive-stage transition and PAIS risk should be stronger when menopausal stage and hormone levels are measured directly than when age bands are used as proxies.
- If this hypothesis is correct, immune/endothelial/autonomic markers should mediate part of the reproductive-stage association with persistent somatic fatigue, PEM, dysautonomia, or vascular symptoms.
- Hormone therapy associations should be heterogeneous by route, dose, timing, comorbidity, and outcome domain rather than showing one uniform effect.
- Female excess should differ across PAIS subphenotypes; the signal should be more pronounced in somatic fatigue, immune/endothelial, or dysautonomic phenotypes than in nonspecific depression outcomes. (This contrast is not yet testable: the only current depression comparison is underpowered — 2 studies / 169 patients, OR 1.05, CI 0.16-6.79 — so adequately powered subphenotype-stratified cohorts are required before the prediction can be evaluated.)

## Falsifiability

Confidence would decrease if large, well-controlled cohorts with measured menopausal stage and sex hormones show no reproductive-stage modification of PAIS risk, symptom trajectory, or immune/endothelial/autonomic recovery after accounting for age, acute severity, comorbidity, pregnancy, hormone therapy, and ascertainment.
Confidence would also decrease if female excess in PAIS is fully explained by reporting, case-definition, or symptom-overlap processes with no residual biological marker differences.
A strong null in hormone-measured cohorts would force the model to treat menopausal context mainly as an ascertainment and comorbidity variable rather than a biological recovery-threshold modifier.

## Supporting Evidence

- Shah2025 supports female sex as a reproducible long-COVID risk factor and identifies the clearest excess in a midlife age band, but it does not identify a menopause-specific causal mechanism [@Shah2025].
- Stewart2024 and Humphreys2025 support the practical importance of menopausal symptom burden and overlap in post-COVID clinical populations [@Stewart2024; @Humphreys2025].
- Averyanova2022 provides indirect mechanistic plausibility for hormone effects on immune, endothelial, and hemostatic pathways relevant to recovery [@Averyanova2022].
- Kawai2025 supports viral-infection links to vascular and thromboinflammatory outcomes that could interact with menopause-associated cardiometabolic risk [@Kawai2025].
- Shahbaz2025 provides a second independent, non-UK-Biobank corroboration of low non-dominant sex hormone in long COVID ME/CFS: reduced testosterone in female LC patients and reduced estradiol in male LC patients, measured directly from plasma in an Edmonton clinical cohort (n=140, CCC ME/CFS case definition, ~12 months post-infection). Inverse correlations between testosterone and inflammatory cytokines (IL-6, TNF-α, IFN-γ, MCP-1, IL-17a, IP-10) in LCF patients provide mechanistic plausibility for testosterone's anti-inflammatory role. Reverse causation unresolved (cross-sectional; menopausal status not collected) [@Shahbaz2025].
- Boneva2015 supplies the strongest non-COVID reproductive-stage signal in the corpus: early/surgical menopause and gynecologic morbidity are enriched in CFS, and hysterectomy/oophorectomy preceded CFS onset in 71% of the dated-surgery subset. This weakly supports an antecedent gynecologic/reproductive-stage vulnerability, but it is surgical-pathway-heavy, retrospective, and not infection-indexed [@Boneva2015].

## Disputing Evidence

Note: the items below are largely **confounding cautions against a *direct* menopause→PAIS cause** — a claim this hypothesis explicitly disclaims (see Organizing Conjecture) — rather than disconfirmations of reproductive-stage modification of a recovery threshold. A genuine disconfirmation (a strong null in a hormone-measured PAIS cohort after adjustment for age, severity, comorbidity, pregnancy, hormone therapy, and ascertainment) does not yet exist; this section is therefore currently thin, which is itself a fragility signal.

- Mishra2020 and Costeira2021 (acute-COVID) find that menopausal status and hormone proxies may not remain independent predictors after adjustment for age, severity, comorbidity, route, and indication. This primarily *supports* the auxiliary proposition that the female/reproductive-stage signal must be decomposed before any causal reading, and shows that a direct menopause-as-cause story is fragile in the acute setting — but it does not test the post-acute recovery-threshold claim [@Mishra2020; @Costeira2021].
- Rebman2026 suggests sex and menopausal status can affect acute presentation and diagnostic markers differently from post-acute persistence, which weakens any simple monotonic hormone-protection story [@Rebman2026].
- Symptom overlap may explain some apparent menopausal-stage associations without requiring a distinct PAIS causal mechanism [@Stewart2024; @Humphreys2025].

## Evidence Needed To Shift Belief

The most efficient upward evidence would be a hormone-measured longitudinal PAIS cohort showing that estradiol/progesterone/testosterone/FSH/LH or carefully ascertained menopausal transition predicts persistent symptoms through immune, endothelial, or autonomic markers after controlling acute severity and ascertainment.
The most efficient downward evidence would be a similarly strong cohort showing that the reproductive-stage association disappears after case-definition, symptom-overlap, comorbidity, and care-seeking correction.
Cross-trigger comparison across long COVID, PTLD, post-dengue fatigue, and other PAIS would help distinguish a general failed-recovery mechanism from a SARS-CoV-2-specific association.

## Related Work

- `question:0013-reproductive-stage-failed-immune-recovery-after-infection` is the primary framing question.
- `question:0007-mechanism-of-female-predominance-in-pais` captures the broader female-predominance mechanism.
- `hypothesis:0001-shared-dysregulated-attractor` provides the attractor outcome this hypothesis may modify.
- `hypothesis:0004-acute-severity-threshold` provides the severity/reserve threshold model this hypothesis extends.
- `topic:menopause-sex-hormones-and-pais-risk` summarizes the current long-COVID and menopause evidence.
- `immunity:topic:sex-hormone-life-stage-immune-homeostasis` and `immunity:topic:endocrine-immune-recovery-thresholds` are the immune-mechanism bridge.
