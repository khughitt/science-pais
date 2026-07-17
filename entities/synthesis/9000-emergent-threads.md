---
id: "synthesis:9000-emergent-threads"
kind: "synthesis"
title: "Emergent threads - health-post-acute-infection"
status: "active"
report_kind: "emergent-threads"
generated_at: "2026-07-17T10:26:49Z"
source_commit: "f6365a35a9baa2b2d02bb68e5ed53199312617bf"
created: "2026-06-24"
updated: "2026-07-17"
orphan_question_count: 7
orphan_interpretation_count: 0
orphan_ids:
  - "question:0027-two-sample-mendelian-randomization-to-test-causal-direction-of-shared"
  - "question:0028-ambulatory-within-person-wearable-ema-protocol-for-pem-phenotyping"
  - "question:0029-tissue-resolved-spatial-multi-omics-and-molecular-imaging-to-localize"
  - "question:0030-target-trial-emulation-in-multi-trigger-ehr-cohorts-for-cross-pais"
  - "question:0039-negative-control-outcome-designs-to-bound-healthcare-utilization"
  - "question:0045-temporal-causal-ordering-of-homeostatic-domain-failure-in-the-post-acute"
  - "question:0046-mechanistic-basis-of-the-time-limited-acute-phase-intervention-window"
---

## Cross-hypothesis questions

Eleven questions carry ≥2 hypothesis matches at confidence `inverse` this run — up from 9 on the previous run. Two questions are new to this list: `question:0006-jak-stat-il6-driver-vs-marker` became cross-cutting when `hypothesis:0019-cgas-sting-nlrp3-sterile-innate-sensing-driver` was created, and `question:0042-is-the-cross-trigger-1020-chronic-fraction-an-artifact-of-shared-case` was formerly an orphan but now carries bidirectional links to two hypotheses.

**`question:0001-shared-molecular-signature-across-triggers`** links `hypothesis:0001-shared-dysregulated-attractor` and `hypothesis:0012-pais-fatigue-cognitive-symptoms-are-a-trigger-nonspecific-neuroimmune`: it is the discriminating empirical bridge between the claim that cross-trigger molecular convergence reflects a shared immunological attractor and the competing account that the signal is a nonspecific neuroimmune stress response common to any prolonged illness.

**`question:0002-antigen-clearance-rescues-symptoms`** links `hypothesis:0002-tissue-reservoir-antigen-fragment` and `hypothesis:0018-circulating-antigen-as-severity-biomarker-not-driver`: the question operationalises the driver-vs-epiphenomenon fork exactly — antigen clearance that rescues symptoms confirms h0002; failure to rescue (even with demonstrated target engagement) supports h0018's severity-biomarker reading.

**`question:0003-acute-severity-threshold-for-self-sustaining-pais`** links `hypothesis:0004-acute-severity-threshold` and `hypothesis:0011-acute-illness-severity-does-not-predict-chronic-fatigue-in-pais-only`: these two hypotheses agree that severity matters during the acute phase but disagree on whether it gates the specifically chronic-fatigue phenotype, and the question is the direct test of that disagreement across multiple triggers.

**`question:0006-jak-stat-il6-driver-vs-marker`** — new to this list — links `hypothesis:0003-immune-exhaustion-feedback` and `hypothesis:0019-cgas-sting-nlrp3-sterile-innate-sensing-driver`: the JAK-STAT/IL-6 driver-vs-marker question is now cross-cutting because sterile innate sensing (h0019) would sustain the IL-6/JAK-STAT axis via cGAS-STING and NLRP3 outputs, whereas h0003's exhaustion-feedback frame treats the same axis as a maintenance signal for immune dysfunction rather than a causal upstream driver.

**`question:0008-formalize-vicious-cycle-attractor-model`** links `hypothesis:0001-shared-dysregulated-attractor` and `hypothesis:0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a`: both hypotheses use attractor-dynamics language but differ on whether PAIS is a discrete locked state or a continuous slow-recovery gradient, making this question the shared theoretical substrate that either unifies or differentiates them.

**`question:0010-vascular-microclot-subphenotype`** links `hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem`, `hypothesis:0014-nk-failure-clear-senescent-endothelium-sasp-propagation`, and `hypothesis:0016-fibrinaloid-microclots-nonspecific-inflammatory-marker`: microclots sit at a three-way intersection — a causal ischemia mechanism (h0006), a SASP-propagation scaffold (h0014), and a deflationary nonspecific-marker reading (h0016) — and the vascular-subphenotype question is what would distinguish them.

**`question:0015-does-pem-requirement-improve-cross-study-comparability`** links `hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent` and `hypothesis:0017-pem-overdiagnosed-via-self-report-nonspecific`: it straddles the measurement-improvement question (does adding PEM as a case-definition criterion reduce ascertainment noise, as h0008 would predict?) and the skeptical reading that self-reported PEM itself is the noisy channel (h0017).

**`question:0017-deflationary-alternatives-vs-shared-pathophysiology`** links four hypotheses at `inverse`: `hypothesis:0011-acute-illness-severity-does-not-predict-chronic-fatigue-in-pais-only`, `hypothesis:0012-pais-fatigue-cognitive-symptoms-are-a-trigger-nonspecific-neuroimmune`, `hypothesis:0016-fibrinaloid-microclots-nonspecific-inflammatory-marker`, and `hypothesis:0017-pem-overdiagnosed-via-self-report-nonspecific`; it is the omnibus adversarial question that collectively tests the deflationary cluster against the positive accounts, functioning as the meta-level bridge across all four deflation hypotheses simultaneously.

**`question:0022-immune-state-displacement-mediator-vs-co-traveler`** links `hypothesis:0001-shared-dysregulated-attractor`, `hypothesis:0012-pais-fatigue-cognitive-symptoms-are-a-trigger-nonspecific-neuroimmune`, and `hypothesis:0015-ebv-reactivation-consequence-not-cause-of-pais`: the mediation question is cross-cutting because immune-state displacement is causally central in h0001, epiphenomenal in h0012, and a permissive condition for EBV reactivation (not a direct symptom driver) in h0015.

**`question:0038-netosis-released-histones-and-extracellular-dna-as-the-structural`** links `hypothesis:0014-nk-failure-clear-senescent-endothelium-sasp-propagation` and `hypothesis:0016-fibrinaloid-microclots-nonspecific-inflammatory-marker`: NETosis products could mechanistically bridge the NK-cell/senescent-endothelium arm (h0014) and the microclot arm (h0016), either linking them into a unified vascular-inflammatory axis or constituting another nonspecific inflammatory consequence under h0016's deflationary reading.

**`question:0042-is-the-cross-trigger-1020-chronic-fraction-an-artifact-of-shared-case`** — new to this list, formerly an orphan — links `hypothesis:0001-shared-dysregulated-attractor` and `hypothesis:0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent`: the question asks whether the cross-trigger 10–20% chronic fraction is real biology or a shared case-definition artefact, which is the precise fork between h0001's attractor claim and h0008's bias-shapes-apparent-prevalence claim.

---

## Orphan questions

Total: **7**. The previous run reported 19 orphans; the drop to 7 is a **metadata correction, not research progress** and must not be read as 12 questions having been answered.

Root cause (established by the 2026-07-16 curation sweep): the orphan classifier reads a question's own outbound `related:` field for a hypothesis link; inbound hypothesis-to-question edges do not clear orphan status. Promotion edges were being written one-directionally (hypothesis → question), so 12 questions already claimed by a hypothesis still appeared as orphans because the reciprocal outbound edge was absent. The sweep backfilled those outbound edges; the hypothesis-to-question edges already existed, so no new hypothesis claims were made.

This failure mode had a concrete, documented consequence: the previous version of this file proposed creating a candidate hypothesis that already existed as `hypothesis:0020-host-immune-baseline-reserve-gate`. The synthesis could not see the hypothesis its own prior run had motivated. That is a durable lesson in the tooling: one-directional promotion edges make successful synthesis work invisible to the next synthesis run.

The 7 genuine orphans fall into two clusters.

**Method and study-design questions** — `question:0027-two-sample-mendelian-randomization-to-test-causal-direction-of-shared`, `question:0028-ambulatory-within-person-wearable-ema-protocol-for-pem-phenotyping`, `question:0029-tissue-resolved-spatial-multi-omics-and-molecular-imaging-to-localize`, `question:0030-target-trial-emulation-in-multi-trigger-ehr-cohorts-for-cross-pais`, `question:0039-negative-control-outcome-designs-to-bound-healthcare-utilization`: all five describe *how* to test claims across multiple hypotheses rather than asserting a specific mechanistic claim of their own; their hypothesis-free status is plausibly structural — method and design questions may not have a natural single-hypothesis home. Note: q0030 and q0039 concern multi-trigger EHR cohorts and healthcare-utilization bias bounding respectively; population-scale gated EHR analyses (N3C / OpenSAFELY) are outside this project's third-party-reproducible bar under decision D-004, which constrains any route to resolving them via that study type.

**Temporal-ordering questions** — `question:0045-temporal-causal-ordering-of-homeostatic-domain-failure-in-the-post-acute` and `question:0046-mechanistic-basis-of-the-time-limited-acute-phase-intervention-window`: both concern the temporal structure of PAIS chronification — what homeostatic domain fails first and why early intervention may have a closing window — with no current hypothesis claiming the causal-ordering frame.

---

## Orphan interpretations

Total: **0**

All active interpretations carry at least one direct hypothesis link via their `related:` fields. No orphan interpretations exist in this run.

Data-quality note: `topic:thromboinflammation-and-endothelial-dysfunction` carries a malformed `source_refs` entry (`paper:Spetz2025` in place of the expected `cite:<key>` format); the coverage instrument logs and ignores it. No synthesis consequence, but the malformed entry should be corrected.

---

## Candidate hypotheses

The two candidate hypotheses flagged in the previous run are now housed:
- The cGAS-STING / NLRP3 sterile-sensing candidate is `hypothesis:0019-cgas-sting-nlrp3-sterile-innate-sensing-driver` (created 2026-07-17; draft, thin provenance).
- The host-immune-baseline-reserve gate candidate is `hypothesis:0020-host-immune-baseline-reserve-gate` (created 2026-07-17; draft, partial provenance).

**Temporal ordering and chronification window.** `question:0045-temporal-causal-ordering-of-homeostatic-domain-failure-in-the-post-acute` and `question:0046-mechanistic-basis-of-the-time-limited-acute-phase-intervention-window` share the claim that PAIS chronification is temporally structured: homeostatic domain failures have a causal order, and there may be a window during which interruption prevents downstream lock-in. If the failure sequence (e.g., immune → metabolic → autonomic → CNS) is predictable and cross-trigger, and early interruption of the leading failure prevents cascade, that is a testable claim distinct from any current hypothesis. The evidence base for either question is thin and no grounded supporting papers are yet attached; the cluster is flagged as a candidate, not asserted.
