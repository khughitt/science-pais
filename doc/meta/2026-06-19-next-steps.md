---
id: "meta:0001-next-steps-2026-06-19"
type: "meta"
title: "Next Steps — 2026-06-19"
status: "active"
created: "2026-06-19"
updated: "2026-06-19"
related: []
---

# Next Steps — 2026-06-19

> First next-steps analysis for this project (full mode). No prior analysis, no
> archived/completed tasks, and no `results/` outputs exist yet — the project is
> at the end of its literature-seeding phase and has not begun execution.

## Recent Progress

**Literature ingestion (research)**
- Seeded the corpus from a large post-infectious literature batch: **72 paper entities** now under `entities/papers/`, including the 58-paper batch (`c99a1e3`) and the anchor review Choutka2022 (`dbc3d52`).
- Just added the **menopause / sex-hormone PAIS review summaries** (`e634bdb`, ~10 min ago) — extending the corpus into reproductive-stage modifiers.

**Topic & framework synthesis (documentation)**
- **8 topic syntheses** under `entities/topics/`, most recently thromboinflammation/endothelial dysfunction and biomarkers/objective-endpoints (`5a34534`).
- **5 hypotheses + 13 questions** articulated, organized around the shared-dysregulated-attractor frame plus the new reproductive-stage margin hypothesis (h0005).

**Task scaffolding (planning)**
- 21 tasks queued. A coherent **sex-hormone/menopause causal-inference thread** (t013–t021) was added 2026-06-19 with explicit confounder/collider discipline (clinic-attendance-as-collider note on t014).
- Import disposition logged (`doc/meta/2026-06-10-paper-import-triage.md`, manifest TSV).

## Current State

**Tasks:** 21 tasks, **all `proposed`** — none `in_progress`, none `done`. No critical-path (P0) tasks declared.

- **P2 (active work tier):** t001 (cross-pathogen signature test), t002 (case-definition heterogeneity — synthesis prerequisite), t004 (therapeutics lit-search), t005 (mitochondrial/PEM lit-search), t013–t021 (sex-hormone causal thread).
- **P3:** t003, t006–t012, t019 (mostly targeted lit-searches + the ODE-modeling-substrate evaluation t011).
- **Blocked:** **t003** — promoting PAIS↔immunity bridge papers to commons is blocked by a tooling gap (`fb-2026-06-11-005`: v3 `entities/papers/` commons promotion not yet supported).

**Hypotheses (5, all `proposed`):** shared-dysregulated-attractor (h0001), tissue-reservoir antigen fragment (h0002), immune-exhaustion feedback (h0003), acute-severity threshold (h0004), reproductive-stage homeostatic margin (h0005).

**Questions (13, all `active`):** span molecular signature, antigen-clearance rescue, severity threshold, small-fiber neuropathy, latent→overt autoimmunity, JAK-STAT/IL-6, female predominance, attractor formalization, GPCR autoantibodies, microclot subphenotype, mitochondrial PEM, prevention, reproductive-stage recovery.

**Workflow runs:** none. No `datapackage.json` manifests and no dated `results/` bundles — `results/` holds only `.gitkeep`. Section skipped (nothing to report). Consistent with the project's stated "literature synthesis before computation" scope.

**Knowledge graph:** `knowledge/graph.trig` does **not** exist — `science graph attention-sample` is unavailable, so the weighted-attention queue could not be run.

## Coverage Gaps

### Coverage Map
| Area | Coverage | Direction | Key Gap |
|---|---|---|---|
| Core mechanisms (immune activation, antigen persistence, autoimmunity, thromboinflammation, dysautonomia) | Strong | new | Well-covered by 8 topics + 72 papers |
| Sex/hormone & reproductive-stage modifiers | Strong | new | Freshly built (h0005, t013–t021); needs execution not more reading |
| Mitochondrial / bioenergetics / PEM mechanism | Missing | new | Central to ME/CFS but barely ingested (t005) |
| Therapeutics & clinical-trial landscape | Missing | new | Corpus thin on treatment; no trial/endpoint mapping (t004) |
| Microbiome / gut-brain axis | Partial | new | Only 1 paper (t007) |
| Pediatric PAIS / MIS-C | Missing | new | Adult-focused corpus (t009) |
| Evidence quality / control design | Partial | new | Most cohorts lack pre-infection baseline; not yet catalogued (t008) |
| Case-definition harmonization | Missing | new | Blocks quantitative cross-study synthesis (t002) |
| Formalization / computation | Missing | new | `computational-analysis` aspect enabled but 0 plans, 0 results, no DAG, no graph |
| Cross-project commons sharing | Blocked | new | Bridge papers blocked by tooling gap (t003) |

### High-Impact Gaps

1. **The project has never moved past "proposed."** Every task, hypothesis, and question sits at its initial status. The dominant risk is not a missing topic — it is that reading keeps accreting without an analysis or formalization step closing any loop. The highest-value move is to *execute* one thread end-to-end.
2. **Case-definition heterogeneity (t002) is an unaddressed prerequisite.** Per AGENTS.md and scope-boundaries, apparent cross-study differences often reflect WHO/CDC vs Fukuda/CCC/ICC definitions rather than biology. t001 (cross-pathogen signature) and any quantitative synthesis are not safely doable until this is resolved.
3. **Mechanism gaps that are central, not peripheral:** mitochondrial/PEM (t005) and therapeutics/endpoints (t004) are both P2 and both `Missing`. PEM is the defining ME/CFS feature; treatment/endpoint mapping is what makes the biomarkers topic actionable.
4. **No knowledge graph.** Without `graph.trig`, the project loses attention-sampling, cross-entity `bears_on` analysis, and the graph-backed review loop — all of which become more valuable as the entity count grows (already 95 entities synced).

## Status Transitions

No prior analysis exists, so there are no transitions to compute. This file establishes the baseline; the next run will diff against it.

## Task Tracking Gaps

- `entities/plans/` is **empty** — no pipeline or analysis plans exist, so there is no buried implementation work to surface. Expected at this stage.
- **Analysis-plan artifacts missing for analysis-shaped tasks.** Several tasks describe data analyses with no linked `analysis-plan:<slug>`: **t013, t014, t018** (comparisons/DAG) and **t016, t017, t020** (estimand/measurement-schema design). When these move toward execution, run `/science:plan-analysis` (and `/science:critique-approach` for the t014 DAG) before implementation. No `entities/plans/*-analysis-plan.md` exist yet, so this is net-new.

### Status Drift (mandatory audit — performed)

Audited every `proposed`/`blocked` task against `results/`, `doc/interpretations|findings|reports|discussions/` frontmatter `source_refs`, post-creation commits, and workflow manifests. **No drift found** — no task's work appears already done. `tasks/done/` is empty and `archive_lag` is zero, so there are no recent completions to surface as positive signal either. The just-added menopause paper summaries (`e634bdb`) are corpus growth supporting the t013–t021 thread, not a task completion.

## Strategic Decision Point

**The fork: breadth (keep reading) vs. depth (execute a thread).**

- **What the decision is:** whether to spend the next sessions closing the remaining lit-search gaps (t004–t010) or to drive one existing thread from `proposed` → analysis-plan → result/interpretation.
- **Evidence bearing on it:** the corpus is already strong on core mechanisms (8 topics, 72 papers); the `computational-analysis` aspect is enabled but completely unexploited; nothing has yet been *concluded*. The sex-hormone thread (t013–t021) is unusually well-specified, with estimands, collider cautions, and a measurement schema already scoped — it is the most execution-ready thread in the project.
- **Options & tradeoffs:**
  - *Breadth* — lowers future risk of missing a mechanism, but compounds the "everything stays proposed" failure mode and defers any validation of the framework.
  - *Depth* — converts the framework into a falsifiable artifact (a DAG + estimand set, or the attractor formalization q0008/t011), surfaces what data is actually needed, and exercises the project's analysis tooling. Risk: may reveal the corpus is still missing a key input.
- **Recommendation: depth, on the sex-hormone thread.** Run `/science:plan-analysis` on the menopause/PAIS estimands (t016) and `/science:critique-approach` on the t014 DAG. This is the most-ready thread, the DAG forces the confounder/collider discipline the project already flagged, and t015 (hormone-measured cohorts) tells you precisely which datasets would make it executable — pulling in exactly the breadth that matters instead of all of it. Pair with t002 (case definitions) as the one breadth item that gates everything.

## Recommended Next Actions

| Priority | Action | Rationale | Command |
|---|---|---|---|
| P1 | Plan the menopause/PAIS causal analysis (t016/t014) | Most execution-ready thread; forces estimand + confounder/collider discipline already scoped | `/science:plan-analysis` then `/science:critique-approach` |
| P1 | Resolve case-definition heterogeneity (t002) | Prerequisite gating t001 and all quantitative cross-study synthesis | `/science:research-topic` (case-definition harmonization) |
| P2 | Fill the PEM/mitochondrial gap (t005) | Defining ME/CFS feature, currently `Missing` | `/science:search-literature` |
| P2 | Map therapeutics & trial endpoints (t004) | Makes the biomarkers/endpoints topic actionable | `/science:search-literature` |
| P2 | Build the knowledge graph | Unlocks attention-sampling + cross-entity analysis as entity count grows (95 entities) | `/science:create-graph` |
| P3 | Cross-project sync | Sync is 5 days stale; immunity/cycles/health-meta carry 22 `bears_on`-linked refs (cycles topics + immunity sex-hormone topics) | `/science:sync` |
| P3 | Unblock or close t003 | Bridge-paper commons promotion blocked by tooling gap `fb-2026-06-11-005`; confirm whether v3 promotion is now supported | `science tasks` |

## Session Summary

The project has completed a strong literature-seeding phase — 72 papers, 8 topics, 5 hypotheses, 13 questions, 21 tasks — and most recently grew a well-specified sex-hormone/menopause causal thread with explicit confounder/collider discipline. But it sits entirely at `proposed`/`active` status with zero executed analyses and no knowledge graph. The defining choice now is to stop accreting reading and drive one thread to a falsifiable artifact; the menopause thread is the readiest, and case-definition harmonization is the one breadth item that gates synthesis. This baseline file anchors the next analysis's diff.
