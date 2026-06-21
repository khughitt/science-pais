---
id: question:0007-mechanism-of-female-predominance-in-pais
type: question
title: What mechanism underlies the consistent female predominance of post-infectious
  fatigue across PAIS, and does it genuinely track somatic fatigue more than
  post-infectious depression?
status: active
ontology_terms:
- sex differences
- estrogen
- post-infectious fatigue
- immune regulation
datasets: []
source_refs:
- cite:Hertanti2025
- cite:Conde2026
- cite:Gusinow2026
- cite:Shah2025
- cite:Stewart2024
- cite:Humphreys2025
- cite:Averyanova2022
- cite:Costeira2021
- cite:Rebman2026
- cite:Kawai2025
related:
- interpretation:0002-t013-cross-trigger-sex-effect-sizes
- question:0013-reproductive-stage-failed-immune-recovery-after-infection
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
- topic:shared-failure-mode-across-pais
- topic:menopause-sex-hormones-and-pais-risk
- topic:long-covid-immune-dysregulation
- topic:thromboinflammation-and-endothelial-dysfunction
- immunity:topic:sex-as-a-modifier-of-immune-homeostasis
- cycles:topic:menstrual-cycle-menopause-immune-modulation
- cycles:topic:reproductive-aging-and-menopause
created: '2026-06-11'
updated: '2026-06-21'
---

# What mechanism underlies the consistent female predominance of post-infectious fatigue across PAIS, and does it genuinely track somatic fatigue more than post-infectious depression?

## Summary

Female sex is the most consistent predictor of PAIS across triggers (Choutka2022), with female odds for post-dengue fatigue of OR ~1.65-1.69 (Hertanti2025 and Conde2026 — two meta-analyses that share primary studies, so not fully independent) and sharply longer modeled recovery trajectories for older females in long COVID (Gusinow2026). The female excess *appears* to track somatic post-infectious *fatigue* more than post-infectious *depression* (Conde2026), but the depression comparison is severely underpowered (meta-analyzable from only 2 studies / 169 patients: OR 1.05, 95% CI 0.16-6.79, "very low certainty"), so this apparent fatigue/depression dissociation is provisional and may be a power artifact rather than a true neuroimmune subtype boundary. This question asks what mechanism underlies the female predominance and whether the fatigue/depression contrast is real and what it would imply about PAIS neuroimmune subtypes.

## Why It Matters

- A correct mechanism (e.g. estrogen-driven B-cell/autoimmune amplification vs sex-differentiated immune-regulatory resilience) would identify a modifiable risk axis and inform sex-stratified trial design.
- If unanswered, the single most reproducible PAIS risk factor remains unexplained, and the project's covariate-modeling guidance (sex, age, hormonal state) lacks a mechanistic anchor.

## Current Evidence

- Supporting: Hertanti2025 and Conde2026 report female OR ~1.65-1.69 for post-dengue fatigue, but these are two meta-analyses with partly overlapping primary studies (not fully independent — see Conde2026); the apparent null for post-dengue depression rests on only 2 studies / 169 patients (OR 1.05, 95% CI 0.16-6.79, very low certainty) and is too underpowered to establish a true fatigue-vs-depression dissociation. Gusinow2026 models ~4x longer recovery for women aged >60 (89.46 mo extrapolated) vs young fourth-wave men (20.81 mo), but this is a symptom/HRQoL latent-transition model with no immune measurements, and the contrast confounds age and infection wave rather than isolating a severity-independent immune mechanism. Ganesh2022 reports IL-6 elevation more common in women.
- Conflicting / cautionary: healthcare-seeking and ascertainment differences could inflate apparent female predominance (Zhang2022 raises this for PASC subphenotypes); estrogen-amplification is a hypothesis, not yet demonstrated mechanistically in PAIS.
- Long-COVID anchor: Shah2025 reports higher long-COVID risk in females in RECOVER, with the clearest excess in ages 40-54 years and a smaller excess at age 55 years or older, but the study does not cleanly separate sex assigned at birth, age, menopausal transition, pregnancy, comorbidity, and reporting effects [@Shah2025].
- Menopause/PASC clinic literature: Stewart2024 and Humphreys2025 show that perimenopause, menopause, and long COVID share fatigue, cognitive difficulty, sleep disturbance, palpitations, mood symptoms, and musculoskeletal pain, making symptom overlap a serious measurement problem rather than a mechanism by itself [@Stewart2024; @Humphreys2025].
- Hormone-immune plausibility: Averyanova2022 summarizes pathways by which estrogen and progesterone can modulate cytokines, T-cell balance, B-cell responses, vascular endothelium, and hemostasis, but most of this evidence is indirect for PAIS [@Averyanova2022].
- Acute-infection caution: Costeira2021 and Rebman2026 suggest sex hormones and menopausal state can affect acute infection presentation or symptom reporting, but acute severity, diagnostic behavior, and post-acute persistence may have different sex/hormone relationships [@Costeira2021; @Rebman2026].
- Vascular alternative: Kawai2025 supports viral-infection links to cardiovascular and thromboinflammatory outcomes, offering a plausible menopause-comorbidity interaction that does not require menopause to be the primary PAIS cause [@Kawai2025].
- Cross-trigger synthesis (`interpretation:0002-t013-cross-trigger-sex-effect-sizes`, t013 step 2): assembling the use-now published sex-stratified ORs (Sylvester2022 long COVID; dengue meta; Colombo) shows the female excess **concentrates in post-acute persistence** — in COVID and Q-fever the *acute* phase is male-biased (mortality; occupational exposure) yet the post-acute phase is female-biased, and acute dengue severity is sex-neutral while post-dengue fatigue carries female OR ≈1.65–2.0. Conversely the **fatigue-vs-depression dissociation does not resolve and is directionally inconsistent**: COVID mood is *more* female-biased than the overall (OR 1.58 vs 1.22), whereas dengue shows female fatigue (1.65–1.69) with a null depression arm that is uninterpretable (2 studies/169 pts; the Colombo cohort excluded mood disorders by design). The provisional dissociation flagged above should not be read as leaning toward a fatigue-specific subtype.

## Thoughts

- Best current interpretation: female predominance in PAIS likely reflects a mixture of immune-regulatory setpoint, hormone/life-stage effects, X-linked immune dosage, symptom expression, and ascertainment. Immune dysregulation remains plausible and project-relevant, but the menopause-specific causal claim is unresolved.
- Major uncertainty: whether menopausal transition is a confounder, mediator, effect modifier, competing diagnosis, or downstream consequence in long-COVID studies; future analyses need an explicit estimand before treating menopause as "noise" or mechanism.

## Connections to Project

- Related hypotheses: `hypothesis:0001-shared-dysregulated-attractor` (host-predisposition seeding), `hypothesis:0005-reproductive-stage-immune-homeostatic-margin`; informs the covariate model for all PAIS analyses.
- Required data or analyses: sex-, age-, hormone-, pregnancy-, and menopausal-status-stratified immune profiling across PAIS; mediation analysis of sex/hormone status -> immune/endothelial/autonomic markers -> fatigue vs depression; correction for care-seeking and symptom-overlap bias.
- Priority level: P2 — high cross-PAIS leverage, mechanistically underdetermined.

## Related

- Topic notes: `topic:shared-failure-mode-across-pais`, `topic:post-infectious-dysautonomia-and-autoimmunity`, `topic:menopause-sex-hormones-and-pais-risk`, `topic:thromboinflammation-and-endothelial-dysfunction`, `immunity:topic:endocrine-immune-recovery-thresholds`.
- Article notes: Hertanti2025, Conde2026, Gusinow2026, Choutka2022, Ganesh2022, Shah2025, Stewart2024, Humphreys2025, Averyanova2022, Costeira2021, Rebman2026, Kawai2025.
- Methods/Datasets: dengue PIF meta-analytic data; ORCHESTRA latent-transition cohort (Gusinow2026).
