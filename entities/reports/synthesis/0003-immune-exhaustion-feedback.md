---
type: synthesis
title: "Synthesis: 0003-immune-exhaustion-feedback"
report_kind: hypothesis-synthesis
id: synthesis:0003-immune-exhaustion-feedback
hypothesis: hypothesis:0003-immune-exhaustion-feedback
generated_at: 2026-06-24T03:28:17Z
source_commit: eb1a5ca60ed1cd69451e2a3d9d6fa16da31fbfec
provenance_coverage: thin
---

## State

`hypothesis:0003-immune-exhaustion-feedback` is **proposed** and in active phase. No graph claims, resolved interpretations, or tasks have been recorded against it; the following draws exclusively from the hypothesis file's own proposition bundle and uncertainty section.

The central claim is that post-acute chronicity is maintained by a positive-feedback loop: unresolved antigen (or a sterile self-sustaining stimulus) drives innate inflammation; chronic stimulation pushes CD8+ T cells into an exhausted state; exhausted T cells fail to clear the stimulus and fail to deliver the regulatory signals that terminate the acute-phase response — so inflammation continues. The hypothesis names persistent JAK-STAT/IL-6/IFN/complement activation co-occurring with CD8+ exhaustion beyond 180 days, with no detectable circulating virus, as its primary empirical anchor (`hypothesis:0003-immune-exhaustion-feedback`, proposition bundle citing Aid2025). A supporting observation is a late bifurcation at 5–6 months — recovery vs. non-recovery — interpreted as the maintenance loop becoming the decisive factor after the shared early acute response resolves (`hypothesis:0003-immune-exhaustion-feedback`, proposition bundle citing Ryan2022).

Key open questions include: (1) whether JAK-STAT/IL-6 signaling is a proximal driver or a downstream marker (`question:0006-jak-stat-il6-driver-vs-marker`); (2) the tension between persistent IFN activation (Aid2025) and IFN-I suppression at 6 months (Ryan2022), which if irreconcilable would mischaracterize the loop's inflammatory arm; and (3) whether the loop requires ongoing antigen from `hypothesis:0002-tissue-reservoir-antigen-fragment` or has become antigen-independent (sterile). Causal direction is asserted from cross-sectional multi-omics, not perturbation experiments — a limitation the hypothesis explicitly acknowledges.

## Arc

Arc reconstruction is limited because no interpretations carry `prior_interpretations` chains and no tasks are tied to this hypothesis.

The hypothesis was created 2026-06-11 and remains at its initial proposed framing. It was apparently seeded from two empirical sources (Aid2025 and Ryan2022) and explicitly positioned as a *maintenance-engine* complement to `hypothesis:0002-tissue-reservoir-antigen-fragment`. The organizing move was to explain the paradox of simultaneous proinflammatory activation and immune exhaustion in long COVID without requiring replicating virus. A single open question (`question:0006-jak-stat-il6-driver-vs-marker`) was registered to operationalize the most critical discriminating test — the JAK1 inhibitor trial (NCT06597396) — but no task or interpretation has been created to pursue it. The investigation has not advanced beyond initial framing.

## Research Fronts

**Open primary question**: `question:0006-jak-stat-il6-driver-vs-marker` — whether persistent JAK-STAT/IL-6 signaling is a proximal driver reversible by inhibition or a downstream marker, and whether the axis generalizes beyond SARS-CoV-2. This is the single registered active question. A positive inhibitor RCT co-endpoint (symptom reduction paired with pathway suppression) would provide the most efficient upward evidence; a clean marker-not-driver result would substantially reduce confidence in the loop as an intervention target.

**Unresolved mechanistic gaps** (from hypothesis uncertainty section):
- Cell source sustaining the IL-6/JAK-STAT signal is unidentified (bulk-assay limitation).
- IFN activation vs. IFN-I suppression tension across Aid2025/Ryan2022 is unreconciled by timing, compartment, or endotype.
- Antigen-dependence of the loop is unknown and therapeutically pivotal (links to `hypothesis:0002-tissue-reservoir-antigen-fragment`).
- Cross-PAIS replication of the coupled activation+exhaustion signature (e.g. PTLDS, post-Q-fever) has not been attempted.

No open tasks, topic gaps, or uncertainty-slice entries are present in the bundle for this hypothesis.
