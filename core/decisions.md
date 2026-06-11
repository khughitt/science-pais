<!--
core/decisions.md — load-bearing decisions and the reasoning behind them.
Loaded at session start via AGENTS.md.

Length cap: ~150 lines. When the file outgrows that, move older entries
to doc/decisions/ and keep only the still-load-bearing ones here.

This file is APPEND-ONLY for individual decisions. Do not rewrite a
decision when it is later superseded — add a new entry that references and
supersedes the old one, and update the "Status" line on the original.

Each entry follows the format below. Number entries sequentially.
-->

# Decisions

## D-001: Split post-acute infection syndromes out as their own process project

- **Date:** 2026-06-10
- **Status:** active
- **Decision:** Post-acute infection syndromes (long COVID, ME/CFS, PTLDS, post-dengue/Q-fever, post-SARS, PICS) are modeled as a dedicated `process` project under `~/d/health/processes/post-acute-infection`, separate from `health-immunity`.

**Why:**
A literature batch on post-acute infection syndromes revealed a large, coherent clinical-syndrome cluster (~60 papers) that is distinct from immunity's mechanism-level autoimmunity/tolerance focus. PAIS spans immune, autonomic, vascular, and metabolic systems and is organized around clinical syndromes and their post-infectious pathophysiology, not around immune mechanism per se. Keeping it in immunity would have ballooned that project's scope and mixed clinical-syndrome work with immune-mechanism work.

**Alternatives considered and rejected:**
- Fold PAIS into `health-immunity` as a subtopic — rejected because it conflates two distinct units of inquiry (immune mechanism vs. post-infectious clinical syndromes) and overloads immunity's scope.
- House PAIS under `health/conditions/` as disease labels — rejected because the unifying object is a *process* (failed recovery after acute infection), not a fixed set of disease labels; framing it as a process matches the `~/d/health/processes/` family and the homeostasis frame.
- Two projects (PAIS + autoimmunity) leaving immunity for pure homeostasis — rejected as premature scaffolding overhead; immunity already owns autoimmunity adequately.

**Implications:**
- Clinical post-infectious syndrome summaries, topics, hypotheses, and tasks belong in this repo.
- General immune-mechanism/autoimmunity/tolerance papers belong in `health-immunity`; bridging papers are summarized once and shared via `science commons promote`.
- Cross-project conclusions that change the general homeostasis frame escalate to `health-meta`; disease-label-vs-biology questions go to `pan-disease`.

**Revisit if:**
- The project fails to develop a distinct cross-syndrome inquiry and reduces to a per-disease literature dump better handled elsewhere.
