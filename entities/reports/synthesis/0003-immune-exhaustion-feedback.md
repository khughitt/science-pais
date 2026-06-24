---
id: synthesis:0003-immune-exhaustion-feedback
type: synthesis
title: "Synthesis: 0003-immune-exhaustion-feedback"
report_kind: hypothesis-synthesis
hypothesis: hypothesis:0003-immune-exhaustion-feedback
generated_at: 2026-06-24T19:16:12Z
source_commit: 05a785bf71096ea8cc4d486b93f3f920a481cd74
provenance_coverage: thin
---

## State

`hypothesis:0003-immune-exhaustion-feedback` holds that post-acute chronicity is maintained by a
positive-feedback loop between unresolved antigenic stimulation and adaptive immune exhaustion:
persisting antigen drives innate inflammation; chronic stimulation pushes CD8+ T cells into
exhaustion; exhausted T cells fail to clear the stimulus and fail to deliver regulatory termination
signals — closing the loop. The hypothesis grades **speculative** because it is conjunctive over
two propositions at different evidence levels.

The descriptive pillar, `proposition:0025` (persistent inflammatory activation + dissociated IFN
signature), is **supported** by two independent evidence lines: `evidence-line:0061` (Aid2025,
moderate — persistent JAK-STAT/IL-6/type-II-IFN/complement + CD8 exhaustion beyond 180 days with
no circulating virus, two cohorts) and `evidence-line:0062` (Ryan2022, weak — blunted type-I
antiviral-effector ISGs MX1/OAS3/OASL at the 24-week bifurcation point in long-COVID referrals),
per `interpretation:0012-t047-h0003-ifn-reconciliation-and-jak1-trial-registration`.

The causal pillar, `proposition:0026` (the exhaustion loop is a proximal driver, reversible by
inhibition), is **untested**. Observational symptom-correlations from Aid2025 are suggestive but
cannot establish direction or reversibility. The causal conjunct is data-gated on
`pre-registration:0004` (abrocitinib JAK1-inhibitor trial NCT06597396). The cell source sustaining
the IL-6/JAK-STAT signal also remains unresolved (`question:0006-jak-stat-il6-driver-vs-marker`).

## Arc

Arc reconstruction is limited because `interpretation:0012-t047-h0003-ifn-reconciliation-and-jak1-trial-registration`
carries no `prior_interpretations` chain — it is the first formal interpretation on this hypothesis.

`hypothesis:0003` was initially framed in prose (created 2026-06-11) as a self-reinforcing
exhaustion loop but carried no coded propositions or evidence-lines (`claim_count=0`). Task t047
(completed 2026-06-24) performed the first formalization pass: it introduced `proposition:0025` and
`proposition:0026`, coded two evidence-lines (`evidence-line:0061`, `evidence-line:0062`), and
registered `pre-registration:0004`.

The central interpretive move in t047, recorded in
`interpretation:0012-t047-h0003-ifn-reconciliation-and-jak1-trial-registration`, was resolving an
apparent internal contradiction. Aid2025 reported persistent IFN activation while Ryan2022 reported
IFN-I suppression — previously flagged as a tension on the hypothesis. The reconciliation reframes
them as indexing different IFN arms: Aid2025 tracks the type-II/inflammatory arm (IFNγ + IL-6/
JAK-STAT, PBMC, day 90–700+), while Ryan2022 tracks the type-I antiviral-effector arm (terminal
ISGs MX1/OAS3/OASL, whole blood, 24-week bifurcation). A dissociated pattern — persistent type-II
tone alongside tolerized type-I effectors — is the predicted innate-sensing exhaustion signature,
so Ryan2022 was recoded from a disputing tension into a supporting arm of `proposition:0025`. The
investigation now stands at: one supported descriptive pillar, one untested causal pillar, and a
locked pre-registration awaiting trial readout.

## Research Fronts

**Live question.** `question:0006-jak-stat-il6-driver-vs-marker` is the primary open question:
does JAK-STAT/IL-6 activation drive chronicity (reversible by inhibition) or merely mark it, and
is the axis shared beyond SARS-CoV-2? The driver-vs-marker arm is now formally registered
(`pre-registration:0004`); the cross-PAIS comparative arm (PTLDS, post-Q-fever, ME/CFS) has no
pathway-level comparison and remains open.

**Open task.** Task t054 (P2, proposed) is the standing tracking task: monitor NCT06597396
(abrocitinib) to readout and discharge `pre-registration:0004` via locked decision criteria.
Symptom + pathway co-suppression would produce a supporting line on `proposition:0026`; pathway
suppression without symptom benefit would produce a disputing (marker-not-driver) line; an
unstratified flat null constitutes only weak disconfirmation given the multi-loop confound flagged
in `interpretation:0012-t047-h0003-ifn-reconciliation-and-jak1-trial-registration`.

**Residual structural gaps.** The reconciliation in
`interpretation:0012-t047-h0003-ifn-reconciliation-and-jak1-trial-registration` is a cross-study
inference — both IFN arms have not been co-measured within the same patients. A single-cohort design
combining type-II inflammatory tone and type-I effector ISG readout longitudinally would confirm
tolerization vs alternative explanations (pre-existing IFN-I deficiency; antigen-driven suppression).
Both source studies are pre-Omicron/pre-vaccine, limiting generalizability. Whether the loop requires
ongoing antigen (linking to `hypothesis:0002-tissue-reservoir-antigen-fragment`) or has become
antigen-independent remains unknown and therapeutically pivotal.
