---
id: "synthesis:0005-reproductive-stage-immune-homeostatic-margin"
kind: "synthesis"
title: "Synthesis: 0005-reproductive-stage-immune-homeostatic-margin"
status: "active"
report_kind: "hypothesis-synthesis"
hypothesis: "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
generated_at: "2026-07-10T18:59:35Z"
source_commit: "3fdeec933ba2432408611cc17a462bed7e105161"
created: "2026-06-24"
updated: "2026-07-10"
provenance_coverage: "high"
---

## State

`hypothesis:0005-reproductive-stage-immune-homeostatic-margin` proposes that reproductive-stage transitions — especially perimenopause and menopause — shift immune homeostatic margin, modifying the probability of failed post-infectious recovery. The graph records it as contested, with active support and dispute evidence on `proposition:0001-reproductive-stage-transition-shifts-the-failed-recovery-threshold`.

Cross-trigger comparison establishes that the female PAIS excess concentrates in post-acute persistence rather than acute susceptibility: COVID post-acute OR 1.22, dengue fatigue OR 1.65–1.69, Q-fever qualitative (`interpretation:0002-t013-cross-trigger-sex-effect-sizes`; `proposition:0008-female-excess-concentrates-in-post-acute-persistence`). The organizing structure is a measurement-channel axis: self-report domains are female-biased while objectively-measured or hard-endpoint domains are sex-null or reversed. The vascular hard-endpoint reversal (VTE aHR 1.69, CV mortality HR 1.68) survives severity restriction (`interpretation:0005-t042-vascular-male-reversal-survives-severity-adjustment`; `proposition:0012-vascular-hard-endpoint-male-reversal-survives-severity-adjustment`). The sole objective female-biased signal is a testosterone-conditioned inflammatory activation in within-sex case-control designs (`interpretation:0006-t041-objective-female-biased-subphenotype-search`; `proposition:0013-immune-domain-partial-hormone-mediated-objective-exception`; `evidence-line:0033-aid2025-lc-female-inflammatory-amplification-within-recovered-null`; corroborated by `evidence-line:0034-shahbaz2025-lc-female-cytokine-gut-barrier-within-sex-elevation`) — the hypothesis's best current objective foothold.

The threshold claim is under active dispute: Shah2025's within-age-band comparison found near-identical female excess in menopausal and non-menopausal women at ages 40–54 (`evidence-line:0025-shah2025-within-band-menopause-null-disputes-menopause-specific-stage-reading`). The mechanism leg, `proposition:0002-reproductive-stage-transition-modifies-immune-regulatory-pathways`, is single-line fragile. No admissible HRT→PAIS causal estimate exists in the corpus (`interpretation:0008-t019-hrt-evidence-audit-no-admissible-pais-test`; `interpretation:0020-t045-neuhouser2024-whi-hrt-gap-triage`).

## Arc

The investigation opened from a female-predominance framing. Task t013 (`interpretation:0002-t013-cross-trigger-sex-effect-sizes`) made the foundational move: cross-trigger effect-size assembly established that female excess emerges in post-acute persistence, not acute susceptibility — COVID and Q-fever acute phases are male-biased while post-acute phases invert; dengue acute severity is sex-neutral yet post-acute fatigue is female-biased. Task t021 promoted the prose Proposition Bundle to first-class entities, instantiating two causal directions (`proposition:0001-reproductive-stage-transition-shifts-the-failed-recovery-threshold` forward, `proposition:0003-infection-pais-perturbs-the-reproductive-axis-and-menopausal-timing` rival reverse) and separating core from background members.

Task t018's six-domain subphenotype sweep yielded the measurement-channel axis as the organizing structure; Shah2025's within-band menopause null was the critical tempering result, disputing a menopause-specific reading while leaving an age or immunosenescence threshold live. Two follow-up tasks resolved held-open questions: task t042 (`interpretation:0005-t042-vascular-male-reversal-survives-severity-adjustment`) bracketed the male vascular reversal across severity extremes; task t041 (`interpretation:0006-t041-objective-female-biased-subphenotype-search`) found three objective-domain nulls reinforcing the ascertainment reading and one testosterone-conditioned immune exception, minting `proposition:0013-immune-domain-partial-hormone-mediated-objective-exception`. Task t019 (`interpretation:0008-t019-hrt-evidence-audit-no-admissible-pais-test`) reclassified the HRT corpus as ascertainment context only; task t045 (`interpretation:0020-t045-neuhouser2024-whi-hrt-gap-triage`) confirmed no HRT effect estimate emerges from the WHI long-COVID screen. Task t078 completed the autoimmune-diathesis sex-modifier inquiry. A planned EHR autoimmune×sex×PASC estimand, vehicle-triaged via `interpretation:0031-t079-n3c-vs-opensafely-vehicle-decision` and `interpretation:0035-t079-bc7-individual-utilisation`, was subsequently shelved under decision D-004 (gated-EHR transparency bar).

Current position: a measurement-channeled female excess with one bounded hormone-linked immune exception; the decisive longitudinal hormone-measured test remains unexecuted.

## Research Fronts

**Live questions.** `question:0013-reproductive-stage-failed-immune-recovery-after-infection` is the primary unresolved framing question. `question:0007-mechanism-of-female-predominance-in-pais` remains open: the measurement-channel structure is the leading explanation, bounded by the hormone-linked immune exception, and the HPG-axis channel requires pre-infection-baseline confirmation. `question:0019-male-biased-vascular-signal-pasc-persistence` is substantially resolved for post-acute CV mortality; the baseline-carryover question persists via `question:0021-male-vascular-reversal-covid-specific-vs-baseline-carryover`.

**Open task.** `task:t037` (UKB QA-checkpoint wiring, proposed) is the sole open task in the bundle, awaiting implementation of the underlying analysis.

**Gaps.** `proposition:0002-reproductive-stage-transition-modifies-immune-regulatory-pathways` is single-line fragile; task t036 found no cohort jointly satisfying hormone-panel depth and pre-infection baseline requirements. Reverse causation between low gonadal steroids and PAIS inflammation is unresolved across all cross-sectional sources. NK-cell cytotoxicity and muscle-OXPHOS day-2 worsening — the highest-value untested objective ME/CFS endpoints flagged by `interpretation:0006-t041-objective-female-biased-subphenotype-search` — remain sex-unstratified gaps. Future PAIS analyses should apply PC-COS as a minimum dimensional-reporting framework (`interpretation:0021-t026-pc-cos-adoption-policy`). Any hormone-mediator Mendelian randomization extension is gated by D-005 (seed-stage computational gate).
