---
id: "synthesis:0003-immune-exhaustion-feedback"
kind: "synthesis"
title: "Synthesis: 0003-immune-exhaustion-feedback"
status: "active"
report_kind: "hypothesis-synthesis"
hypothesis: "hypothesis:0003-immune-exhaustion-feedback"
generated_at: "2026-07-10T18:59:35Z"
source_commit: "3fdeec933ba2432408611cc17a462bed7e105161"
created: "2026-06-24"
updated: "2026-07-10"
provenance_coverage: "high"
---

## State

`hypothesis:0003-immune-exhaustion-feedback` proposes that post-acute chronicity is maintained by a positive-feedback loop in which unresolved antigenic stimulation drives innate inflammation, chronic stimulation exhausts CD8+ T cells, and exhausted T cells fail to deliver the termination signals that resolve the acute-phase response. The hypothesis is a conjunction of two pillars and grades **speculative** overall.

`proposition:0025-lc-persistent-inflammatory-activation-dissociated-ifn` (**supported**) is grounded in two independent lines: `evidence-line:0061-aid2025-persistent-jakstat-il6-exhaustion-supports-0025` (Aid2025, moderate, two cohorts) documenting persistent JAK-STAT/IL-6/type-II-IFN/complement activation plus CD8 exhaustion beyond 180 days with no circulating virus; and `evidence-line:0062-ryan2022-type-i-ifn-effector-blunting-supports-0025` (Ryan2022, weak) documenting blunted type-I antiviral-effector ISGs at the 6-month bifurcation. `interpretation:0012-t047-h0003-ifn-reconciliation-and-jak1-trial-registration` resolved the apparent Aid2025-vs-Ryan2022 contradiction as a dissociated IFN signature (different arms, compartments, and contrasts), supporting rather than disputing the exhausted-innate-sensing reading.

`proposition:0026-lc-jakstat-exhaustion-loop-is-proximal-driver` (**untested, speculative**) holds that the loop causally maintains chronicity and is reversible by inhibition. It is gated on `pre-registration:0004-jak1-inhibitor-driver-vs-marker` / NCT06597396. `interpretation:0016-t054-abrocitinib-trial-status-snapshot` confirms primary completion (2026-03-27) passed with no posted results; target-engagement criteria remain unverified.

`proposition:0036-non-covid-pais-partially-recapitulate-ifn-cytokine-exhaustion-axis` (`interpretation:0029-t060-cross-pais-ifn-jakstat-pathway-map`) records one-source, not-yet-harmonized IFN/cytokine/exhaustion recurrence in ME/CFS and QFS via `evidence-line:0089-eatonfitch2024-mecfs-longcovid-exhaustion-panel-supports-cross-pais-axis`. Primary discriminating question: `question:0006-jak-stat-il6-driver-vs-marker`.

## Arc

The investigation began with h0003 as a prose-only hypothesis with no coded claims. `interpretation:0012-t047-h0003-ifn-reconciliation-and-jak1-trial-registration` (task t047, 2026-06-24) made the first analytical pass: it formalized `proposition:0025-lc-persistent-inflammatory-activation-dissociated-ifn` and `proposition:0026-lc-jakstat-exhaustion-loop-is-proximal-driver`, coded two evidence-lines, resolved the Aid2025-vs-Ryan2022 apparent IFN contradiction as a dissociated signature, and registered NCT06597396 as the formal causal-driver test via `pre-registration:0004-jak1-inhibitor-driver-vs-marker` with locked decision criteria.

`interpretation:0016-t054-abrocitinib-trial-status-snapshot` (2026-06-25) audited the trial registry. Primary completion had passed without posted results, and the registered biomarker (hsCRP) does not satisfy `pre-registration:0004-jak1-inhibitor-driver-vs-marker`'s target-engagement criterion; `proposition:0026-lc-jakstat-exhaustion-loop-is-proximal-driver` stayed speculative with no belief update. This interpretation formally amends `interpretation:0012-t047-h0003-ifn-reconciliation-and-jak1-trial-registration`.

`interpretation:0029-t060-cross-pais-ifn-jakstat-pathway-map` (task t060, 2026-06-26) reviewed eight papers across LC, ME/CFS, QFS, and PTLDS, yielding `proposition:0036-non-covid-pais-partially-recapitulate-ifn-cytokine-exhaustion-axis` at weak confidence from EatonFitch2024 and Keijmel2016. Galbraith2011's null cross-trigger transcriptomics result and Patterson2024's distinguishable PTLDS/LC cytokine hubs tempered generalization; the finding was kept local to `question:0006-jak-stat-il6-driver-vs-marker` and did not alter h0003's causal grade.

Current position: the descriptive inflammatory state is evidenced; the causal maintenance loop is data-gated on the NCT06597396 readout.

## Research fronts

**Live questions.** `question:0006-jak-stat-il6-driver-vs-marker` is the primary open question: whether JAK-STAT/IL-6 activation causally maintains PAIS chronicity or marks a parallel process. Resolution requires NCT06597396 results meeting `pre-registration:0004-jak1-inhibitor-driver-vs-marker`'s target-engagement and endotype-stratification criteria, not yet verifiable. `question:0022-immune-state-displacement-mediator-vs-co-traveler` (linked to `proposition:0038-persistent-immune-state-displacement-occurs-in-pais` and `proposition:0039-immune-state-displacement-mediates-vs-marks-pais-symptoms`) and `question:0025-ifn-i-tryptophan-malabsorption-platelet-serotonin-depletion-vagal` are related back-inverse questions not yet addressed by h0003's evidence base.

**Uncertainties.** The cell-type source of the sustained IL-6/JAK-STAT signal is unresolved (Aid2025 used bulk assays). The dissociated IFN signature is an inter-study inference; within-individual co-measurement of both arms is lacking. Whether the loop requires ongoing antigen or has become antigen-independent — trained immunity is a candidate sterile-maintenance route noted in the hypothesis — is therapeutically pivotal and open. Assay heterogeneity across PAIS (per `interpretation:0029-t060-cross-pais-ifn-jakstat-pathway-map`) limits confidence in a shared maintenance state beyond long COVID.
