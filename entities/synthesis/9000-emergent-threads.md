---
id: "synthesis:9000-emergent-threads"
kind: "synthesis"
title: "Emergent threads - health-post-acute-infection"
status: "active"
report_kind: "emergent-threads"
generated_at: "2026-07-10T18:59:35Z"
source_commit: "3fdeec933ba2432408611cc17a462bed7e105161"
created: "2026-06-24"
updated: "2026-07-10"
orphan_question_count: 19
orphan_interpretation_count: 0
orphan_ids:
  - "question:0023-cgas-sting-cytosolic-dna-sensing-as-upstream-driver-of-persistent-type-i"
  - "question:0024-nlrp3-inflammasome-and-gasdermin-d-pyroptosis-as-a-self-amplifying-il-1"
  - "question:0027-two-sample-mendelian-randomization-to-test-causal-direction-of-shared"
  - "question:0028-ambulatory-within-person-wearable-ema-protocol-for-pem-phenotyping"
  - "question:0029-tissue-resolved-spatial-multi-omics-and-molecular-imaging-to-localize"
  - "question:0030-target-trial-emulation-in-multi-trigger-ehr-cohorts-for-cross-pais"
  - "question:0031-pais-incidence-and-mechanism-in-chronically-immunosuppressed-hosts"
  - "question:0032-pais-burden-phenotype-and-mechanism-in-lmic-and-ancestrally-diverse"
  - "question:0033-frailty-and-pre-frailty-as-an-independent-pais-boundary-condition-with"
  - "question:0034-pre-existing-atopic-and-mast-cell-activation-disorders-as-a"
  - "question:0039-negative-control-outcome-designs-to-bound-healthcare-utilization"
  - "question:0040-pregnancy-state-immune-milieu-as-a-modifier-of-pais-risk-and-trajectory"
  - "question:0041-is-female-predominance-in-pais-substantially-an-ascertainment-and"
  - "question:0042-is-the-cross-trigger-1020-chronic-fraction-an-artifact-of-shared-case"
  - "question:0043-bacterial-persister-cell-bet-hedging-as-a-model-for-stochastic-viral"
  - "question:0044-chronic-gvhd-as-analogy-for-post-viral-tolerance-infrastructure-collapse"
  - "question:0045-temporal-causal-ordering-of-homeostatic-domain-failure-in-the-post-acute"
  - "question:0046-mechanistic-basis-of-the-time-limited-acute-phase-intervention-window"
  - "question:0047-menstrual-cycle-and-ultradian-symptom-periodicity-as-a-mechanistic"
---

## Cross-hypothesis questions

Nine questions carry ≥2 hypothesis matches at confidence `inverse` this run.

**`question:0001-shared-molecular-signature-across-triggers`** links `hypothesis:0001-shared-dysregulated-attractor` and `hypothesis:0012-pais-fatigue-cognitive-symptoms-are-a-trigger-nonspecific-neuroimmune`: it is the discriminating empirical bridge between the claim that cross-trigger molecular convergence reflects a shared immunological attractor and the competing account that the signal is a nonspecific neuroimmune stress response common to any prolonged illness.

**`question:0002-antigen-clearance-rescues-symptoms`** links `hypothesis:0002-tissue-reservoir-antigen-fragment` and `hypothesis:0018-circulating-antigen-as-severity-biomarker-not-driver`: the question operationalises the driver-vs-epiphenomenon fork exactly — antigen clearance that rescues symptoms confirms h0002; failure to rescue (even with demonstrated target engagement) would support h0018's severity-biomarker reading.

**`question:0003-acute-severity-threshold-for-self-sustaining-pais`** links `hypothesis:0004-acute-severity-threshold` and `hypothesis:0011-acute-illness-severity-does-not-predict-chronic-fatigue-in-pais-only`: these two hypotheses agree that severity matters during the acute phase but disagree on whether it gates the specifically *chronic fatigue* phenotype, and the question is the direct test of that disagreement across multiple triggers.

**`question:0008-formalize-vicious-cycle-attractor-model`** links `hypothesis:0001-shared-dysregulated-attractor` and `hypothesis:0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a`: both hypotheses use attractor-dynamics language but differ on whether PAIS is a discrete locked state or a continuous slow-recovery gradient, making this question the shared theoretical substrate that either unifies or differentiates them.

**`question:0010-vascular-microclot-subphenotype`** links `hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem`, `hypothesis:0014-nk-failure-clear-senescent-endothelium-sasp-propagation`, and `hypothesis:0016-fibrinaloid-microclots-nonspecific-inflammatory-marker`: microclots sit at a three-way intersection — a causal ischemia mechanism (h0006), a SASP-propagation scaffold (h0014), and a deflationary nonspecific-marker reading (h0016) — and the vascular-subphenotype question is what would distinguish them.

**`question:0015-does-pem-requirement-improve-cross-study-comparability`** links `hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent` and `hypothesis:0017-pem-overdiagnosed-via-self-report-nonspecific`: it straddles the measurement-improvement question (does adding PEM as a case-definition criterion reduce ascertainment noise, as h0008 would predict?) and the skeptical reading that self-reported PEM itself is the noisy channel (h0017).

**`question:0017-deflationary-alternatives-vs-shared-pathophysiology`** links four hypotheses at `inverse`: `hypothesis:0011-acute-illness-severity-does-not-predict-chronic-fatigue-in-pais-only`, `hypothesis:0012-pais-fatigue-cognitive-symptoms-are-a-trigger-nonspecific-neuroimmune`, `hypothesis:0016-fibrinaloid-microclots-nonspecific-inflammatory-marker`, and `hypothesis:0017-pem-overdiagnosed-via-self-report-nonspecific`; it is the omnibus adversarial question that collectively tests the deflationary cluster against the positive accounts (`hypothesis:0001-shared-dysregulated-attractor`, `hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem`), functioning as the meta-level bridge across all four deflation hypotheses simultaneously.

**`question:0022-immune-state-displacement-mediator-vs-co-traveler`** links `hypothesis:0001-shared-dysregulated-attractor`, `hypothesis:0012-pais-fatigue-cognitive-symptoms-are-a-trigger-nonspecific-neuroimmune`, and `hypothesis:0015-ebv-reactivation-consequence-not-cause-of-pais`: the mediation question is cross-cutting because immune-state displacement is causally central in h0001, epiphenomenal in h0012, and a permissive condition for EBV reactivation (not a direct symptom driver) in h0015 — the same observable evidence must satisfy three different causal roles.

**`question:0038-netosis-released-histones-and-extracellular-dna-as-the-structural`** links `hypothesis:0014-nk-failure-clear-senescent-endothelium-sasp-propagation` and `hypothesis:0016-fibrinaloid-microclots-nonspecific-inflammatory-marker`: NETosis products could mechanistically bridge the NK-cell/senescent-endothelium arm (h0014) and the microclot arm (h0016), either linking them into a unified vascular-inflammatory axis or, under h0016's deflationary reading, constituting another nonspecific inflammatory consequence rather than a structural driver.

---

## Orphan questions

Total: **19** (matches the dispatcher's count of 19 research orphans this run).

Questions are clustered by inferred topic. See frontmatter `orphan_ids` for the full enumeration.

**Upstream innate nucleic-acid sensing and cell-death pathways** — `question:0023-cgas-sting-cytosolic-dna-sensing-as-upstream-driver-of-persistent-type-i`, `question:0024-nlrp3-inflammasome-and-gasdermin-d-pyroptosis-as-a-self-amplifying-il-1`: these two questions ask whether cGAS-STING and NLRP3/pyroptosis serve as upstream molecular triggers of chronic PAIS immune activation, a mechanistic layer upstream of all current hypotheses that none of them yet formally claim.

**Disease analogies and systems framing** — `question:0043-bacterial-persister-cell-bet-hedging-as-a-model-for-stochastic-viral`, `question:0044-chronic-gvhd-as-analogy-for-post-viral-tolerance-infrastructure-collapse`, `question:0045-temporal-causal-ordering-of-homeostatic-domain-failure-in-the-post-acute`, `question:0046-mechanistic-basis-of-the-time-limited-acute-phase-intervention-window`: these questions develop mechanistic frameworks and cross-disease analogies (bacterial persister bet-hedging, chronic GvHD as tolerance-collapse model) that could inform hypothesis formalisation but are not yet anchored to any existing hypothesis.

**Causal inference and study design methods** — `question:0027-two-sample-mendelian-randomization-to-test-causal-direction-of-shared`, `question:0028-ambulatory-within-person-wearable-ema-protocol-for-pem-phenotyping`, `question:0029-tissue-resolved-spatial-multi-omics-and-molecular-imaging-to-localize`, `question:0030-target-trial-emulation-in-multi-trigger-ehr-cohorts-for-cross-pais`, `question:0039-negative-control-outcome-designs-to-bound-healthcare-utilization`: methodological and study-design questions whose answers would serve multiple hypotheses but which are not owned by any single one.

**Host-modifier and population boundary conditions** — `question:0031-pais-incidence-and-mechanism-in-chronically-immunosuppressed-hosts`, `question:0032-pais-burden-phenotype-and-mechanism-in-lmic-and-ancestrally-diverse`, `question:0033-frailty-and-pre-frailty-as-an-independent-pais-boundary-condition-with`, `question:0034-pre-existing-atopic-and-mast-cell-activation-disorders-as-a`, `question:0040-pregnancy-state-immune-milieu-as-a-modifier-of-pais-risk-and-trajectory`: questions about distinct host populations and pre-existing immune states that modulate PAIS risk, none of which is housed under a hypothesis that formally claims host-immune-baseline as a risk modifier.

**Ascertainment, case-definition, and cyclical biological signal** — `question:0041-is-female-predominance-in-pais-substantially-an-ascertainment-and`, `question:0042-is-the-cross-trigger-1020-chronic-fraction-an-artifact-of-shared-case`, `question:0047-menstrual-cycle-and-ultradian-symptom-periodicity-as-a-mechanistic`: these questions challenge whether observed PAIS patterns (female excess, cross-trigger incidence floor, symptom periodicity) are biological or artefactual, topics that fall between `hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent` and `hypothesis:0005-reproductive-stage-immune-homeostatic-margin` without being clearly owned by either.

---

## Orphan interpretations

Total: **0**

All 40 active interpretations carry at least one direct hypothesis link via their `related:` fields. No orphan interpretations exist in this run.

---

## Candidate hypotheses

**Upstream innate nucleic-acid sensing as the proximal PAIS inflammatory driver.** Both `question:0023-cgas-sting-cytosolic-dna-sensing-as-upstream-driver-of-persistent-type-i` and `question:0024-nlrp3-inflammasome-and-gasdermin-d-pyroptosis-as-a-self-amplifying-il-1` ask about specific molecular upstream triggers — cGAS-STING-driven type-I IFN persistence and NLRP3/gasdermin-D-driven IL-1β amplification — that sit one mechanistic layer above all existing positive hypotheses. A candidate hypothesis: "Persistent cytosolic nucleic-acid sensing via cGAS-STING and/or NLRP3 inflammasome activation by viral RNA/DNA fragments constitutes the proximal molecular driver of the chronic type-I IFN and IL-1β phenotype in PAIS, upstream of the immune-exhaustion feedback and the shared-attractor state." This would give q0023 and q0024 a formal home and integrate with `hypothesis:0003-immune-exhaustion-feedback` and `hypothesis:0001-shared-dysregulated-attractor` as downstream effectors.

**Pre-existing host immune-baseline perturbation as a shared PAIS vulnerability gate.** Five orphan questions — `question:0031-pais-incidence-and-mechanism-in-chronically-immunosuppressed-hosts`, `question:0032-pais-burden-phenotype-and-mechanism-in-lmic-and-ancestrally-diverse`, `question:0033-frailty-and-pre-frailty-as-an-independent-pais-boundary-condition-with`, `question:0034-pre-existing-atopic-and-mast-cell-activation-disorders-as-a`, and `question:0040-pregnancy-state-immune-milieu-as-a-modifier-of-pais-risk-and-trajectory` — all concern distinct host populations whose pre-existing immune state (immunosuppression, frailty/inflammaging, atopy/mast-cell priming, pregnancy milieu, ancestral immune architecture) is hypothesised to modulate PAIS risk or phenotype. No current hypothesis frames these as instances of a shared mechanism. A candidate hypothesis: "Pre-existing perturbations that reduce post-infection immune homeostatic reserve — chronic immunosuppression, frailty-related inflammaging, atopic/mast-cell hyperreactivity, and pregnancy-phase immune remodelling — gate PAIS risk through a common mechanism of lowered threshold for immune-state lock-in, regardless of pathogen trigger." This would unify the host-modifier cluster and make testable predictions about PAIS incidence rank-ordering across host strata.
