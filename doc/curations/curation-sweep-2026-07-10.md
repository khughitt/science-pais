---
doc_kind: "curation-sweep"
title: "Curation sweep — 2026-07-10"
generated_at: "2026-07-10T00:00:00Z"
source_commit: "96a18bfc61a5542a154af8a79a46527eab89d1fd"
sweep_scope: "all"
since: null
mode: "propose"
applied_changes: 2
pending_decisions: 2
---

<!-- This is a project-state record, not a KG entity. It lives under doc/ (not
entities/) by design — see fb-2026-07-10-022. Curation sweeps are transient
tidying logs; they carry no `kind:`/`id:` entity frontmatter and are not
materialized into the knowledge graph. -->


# Curation sweep — 2026-07-10

First curation sweep for this project (no prior ledger under
`entities/meta/curation/`). Mode is **propose**: no source edits were applied;
the one high-confidence mechanical fix (AGENTS.md load-bearing digest) is drafted
below and awaits approval.

## Executive Summary

- **Load-bearing digest is empty while 6 decisions are active.** `AGENTS.md`'s
  `load-bearing-constraints` block still says *"none yet"*, but `core/decisions.md`
  now carries **D-001…D-006** (all `active`). This is the single clear applied-fix
  candidate — drafted below, approval-gated.
- **Project synthesis rollup lags ~2 weeks of empirical results.**
  `synthesis:0008` was generated 2026-06-24 (content last touched 06-25) and
  predates three completed analyses that landed real verdicts: t117 (cross-PAIS
  rank — non-identified / fail-closed, `interpretation:0038`), t108 (serum IL-6
  does **not** rank PAIS risk — q0026 corollary refuted, `interpretation:0039`),
  and t107 (HSPC-epigenomics feasibility → monocyte-ATAC pivot,
  `interpretation:0040`, `pre-registration:0006`). Regeneration recommended.
- **`source_refs` gap on a handful of reanalysis/audit interpretations is a
  provenance-field placement issue, not missing provenance** — those entities
  carry their sources via `related:` / `input:` / evidence-lines instead. Low value.
- **New explore-batch questions (q0023–q0047) are thinly linked** — many have no
  outbound `related` edges yet. This is expected of freshly-seeded idea-expansion
  questions already queued under explore-followup tasks (t098–t101); not a defect.
- **One unresolved ref — FIXED (PD-4, applied 2026-07-10):**
  `workflow-run:t035-…-verdict` carried a bare-slug `workflow:` field
  (`t035-cross-trigger-pathway-overlap`) while the canonical id is
  `workflow:t035-cross-trigger-pathway-overlap`; qualified the field. This was the
  only hard graph-audit failure; it now passes (remaining audit items are the 3
  pre-existing `unknown_entity_kind: meta` warns).
- **Cross-project sync is 12 days old** (last 2026-06-27); no action required, noted
  for awareness given the active commons-bridge task (t003).
- Corpus health is otherwise strong: proposition claim-layer and causal-leaning
  coverage are both **100%** (41/41); no long-idle artifacts; no
  no-frontmatter files.

## Corpus Inventory

| Class | Count | | Class | Count |
|---|---|---|---|---|
| paper | 219 | | evidence-line | 88 |
| task | 121 | | question | 57 |
| dataset | 47 | | proposition | 41 |
| interpretation | 40 | | concept | 32 |
| hypothesis | 18 | | topic | 15 |
| plan | 10 | | synthesis | 9 |
| search | 9 | | report | 6 |
| method | 6 | | pre-registration | 6 |
| discussion | 4 | | theme | 2 |
| patch-definition | 2 | | meta | 3 |

Total ≈ 613 entities. Notable coverage observations:

- **Concepts (32) carry `source_refs_count: 0` across the board** and mostly
  `related_count: 1`. These are the covariate/mechanism nodes for the
  reproductive-stage strand (age, BMI, hormone therapy, ascertainment, …); they
  are DAG scaffolding rather than literature-sourced entities, so empty
  `source_refs` is by-design. Not flagged.
- **Propositions (41) have 0 evidence *units*** in the cross-paper aggregator —
  they are the speculative reproductive-stage proposition set plus layered-claim
  props; belief magnitudes read "speculative". Consistent with pre-empirical state.

## Forgotten Insights

None surfaced as *forgotten* this sweep. The corpus is actively worked (30 commits
in the recent window, all t107/t108/t117/t120), and the attention-sample top rows
(`proposition:0017-pais-sfn-cross-trigger-convergence`,
`hypothesis:0008-measurement-channel-…`) are live, not stranded — both are the
subject of open pre-registrations and tasks. The uniform `days_since_last_review:
365` on every sampled node indicates review dates are not being stamped, so that
particular attention signal is currently uninformative (see Self-Reflection).

## Missed Connections

- **(low) `source_refs` placement on reanalysis interpretations.**
  `interpretation:0010, 0011, 0012, 0013, 0014, 0015, 0016, 0017` carry
  `source_refs: []` but reference their sources through `related:` (e.g. 0014 →
  `paper:Oaklander2022`, 0017 → `paper:Goh2022`/`paper:BrandstetterFigueroa2025`)
  and `input:`. Moving the paper refs into `source_refs` would tighten graph
  provenance edges, but the information is not lost and the edit is judgment-laden
  per-entity. Recorded, not applied.
- **(low) Explore-batch question connectivity.** q0023–q0047 (cGAS-STING,
  NLRP3, MR, wearable-EMA, target-trial-emulation, boundary-condition strata, …)
  are thinly `related`-linked. They are correctly parked under explore-followup
  tasks (t098–t101, t110) for later development; linking is part of that work, not
  a curation fix.

## Drift

- **(medium) `synthesis:0008-project-synthesis-rollup` is stale.** Generated at
  commit `05a785b` (2026-06-24); since then t117/t108/t107/t120 produced a
  refutation (q0026 IL-6 corollary), a fail-closed non-identification result
  (cross-PAIS rank), and a feasibility→pivot with a new pre-registration (0006).
  The per-hypothesis synthesis files it aggregates predate these too. Recommend
  re-running `/science:big-picture` to refresh the rollup and the affected
  per-hypothesis files (0001 attractor, 0003 immune-exhaustion, 0005
  reproductive-stage). Not a mechanical fix — deferred to the owning command.

## Duplication and Fragmentation

None found. Topic and question sets are distinct; no overlapping syntheses or
duplicated summaries surfaced.

## Actioned Fixes

- **`AGENTS.md` — populated the load-bearing-constraints digest (PD-1, applied
  2026-07-10 with user approval).** Replaced the placeholder *"none yet"* line
  between the `BEGIN/END: load-bearing-constraints` markers with six imperative
  rules, one per active decision D-001…D-006 (wording as drafted under Pending
  Decisions → PD-1). Rules were written ID-first (`- **D-NNN:**`) so
  `parse_digest_ids` registers them; verified `digest_ids: [D-001…D-006]`,
  `drift_signals: []`. Committed in `82c5cda`. The "why" for each rule stays in
  `core/decisions.md`.
- **`entities/workflow-runs/t035-…-verdict.md` — qualified the `workflow:` ref
  (PD-4, applied 2026-07-10 with user approval).** Changed
  `workflow: "t035-cross-trigger-pathway-overlap"` →
  `workflow: "workflow:t035-cross-trigger-pathway-overlap"`, matching the
  canonical id and the file's own `related:` convention. Clears the sole
  `unresolved_reference` graph-audit failure.

## Pending Decisions

### NEW — 2026-07-10 sweep

**PD-1 (high, approval-gated mechanical fix): Populate the AGENTS.md
load-bearing-constraints digest from D-001…D-006. — ✅ APPLIED 2026-07-10.**
See Actioned Fixes. The proposed digest wording (kept below for provenance) was
applied verbatim.

`inventory.agents_md.drift_signals = ["active_decisions_differ_from_digest"]`;
`digest_ids: []` vs `active_decision_ids: [D-001…D-006]`. Markers are present, so
this is a pure content replacement between the existing
`BEGIN/END: load-bearing-constraints` markers. Proposed digest (one imperative
bullet per active decision; the "why" stays in `core/decisions.md`):

```markdown
- **Scope (D-001):** Keep clinical post-infectious-syndrome work here; route
  general immune-mechanism / autoimmunity / tolerance to `health-immunity`,
  frame-changing cross-project conclusions to `health-meta`, and
  disease-label-vs-biology questions to `pan-disease`. Summarize bridging papers
  once and share via `science commons promote`.
- **Pacing over GET (D-002):** For PEM-positive phenotypes, treat
  pacing / energy-management as the default activity frame and flag
  fixed-increment graded-exercise-therapy designs and endpoints as contested /
  contraindicated; keep provoked-exertion diagnostics (2-day CPET, iCPET)
  endorsed under PEM-crash-risk consent. Always stratify PEM-positive vs
  PEM-absent before applying.
- **Infection-trigger primary scope (D-003):** Admit a syndrome to primary scope
  only if its trigger is an acute infection. Hold PACVS and non-infectious
  GWS/FM as boundary-monitor / read-across — never counted as PAIS cases or as
  independent cross-trigger support for `hypothesis:0001` — and label any
  GWS/FM-leaning convergence claim as a *non-infectious* read-across.
- **No gated-EHR estimands (D-004):** Do not execute the autoimmune×sex×PASC EHR
  estimand or any line requiring population-scale, gated, non-downloadable
  patient EHR (N3C / OpenSAFELY sit below the third-party-reproducible bar). Bank
  the transparent design residue and the `hypothesis:0008` synthesis instead.
- **Seed-stage computational gate (D-005):** Post-seed computational work is
  authorized only for the specific Wave-1 open GWAS/MR pilot (public
  summary-statistic vehicles, IVW primary + the committed sensitivity checklist);
  any other computational line needs its own scope decision.
- **Wave-1 MR maintenance boundary (D-006):** Treat `plan:0008`'s reportable-grade
  Wave-1 MR promotion as direct maintenance of the D-005 pilot (HGI EUR outcome +
  LD-score / HapMap3 infrastructure are in-scope); do not use FinnGen or any
  non-HGI outcome vehicle without a fresh scope decision plus a
  third-party-reproducibility check.
```

Applying this replaces only the placeholder line between the markers in
`AGENTS.md`. **Awaiting approval** (rule wording is a semantic judgement, per the
agents-md theme rules).

**PD-2 (medium): Regenerate `synthesis:0008` and stale per-hypothesis synthesis
files** via `/science:big-picture` to incorporate t117/t108/t107/t120 verdicts.
Owner decision — not applied here.

**PD-3 (low): Decide the `source_refs` convention for reanalysis/audit
interpretations** — either backfill `source_refs` from `related:` paper edges on
the 4–8 flagged interpretations, or accept `related`/`input` as the provenance
channel for this artifact class and suppress the signal. Recorded for judgement.

**PD-4 (low): Kind-prefix normalization for the t035 workflow-run ref. — ✅
APPLIED 2026-07-10.** Qualified the `workflow:` field to
`workflow:t035-cross-trigger-pathway-overlap`; see Actioned Fixes. Clears the sole
`unresolved_reference` audit failure. (Open upstream question — filed as an
observation, not blocking: whether the resolver *should* accept a bare slug in a
typed `workflow` field; local fix taken because it matches the file's own
`related:` convention.)

_No carry-overs: this is the first sweep._

## Suggested Follow-Ups

1. Approve PD-1 → apply the digest edit (single-file, reversible).
2. Queue `/science:big-picture` regeneration (PD-2) after the current
   t117/t120 analysis arc settles.
3. Run `science sync` — cross-project state is 12 days old and t003 (commons-bridge
   promotion) depends on it.
4. If review-date stamping is desired, wire `days_since_last_review` to actual
   review events so the attention sample regains signal (see Self-Reflection).

## Self-Reflection

> What did this curation sweep make harder than it should have been?

- **The `meta` kind is unregistered**, so `science health` and
  `resolve-questions` spam `skipping entities/meta/…: unknown entity kind 'meta'`
  on every run (three files: `0001-next-steps-…`, two `explorations/*`). It also
  means this ledger's own `kind: "curation-sweep"` / the `meta` class sit outside
  the validated schema. Smallest fix: register `meta` (and its sub-kinds
  `curation-sweep`, `next-steps`, `exploration`) in the active profile so these
  artifacts validate and stop generating noise.
- **`inventory` and the command spec diverged.** The command's Phase-1 helper
  description promises `long_idle`, `missing_related`, `unresolved refs`, and
  `stale-task evidence` in one payload, but the installed `curate inventory`
  returns only `{agents_md, artifact_counts, artifacts, candidate_signals}` —
  unresolved-ref and stale-task evidence had to be pulled from `science health`
  and manual `git log` instead. Aligning the helper's output keys with the command
  doc (or updating the doc) would remove a guessing step.
- **`missing_source_refs` over-reports** by not recognizing `related:` / `input:`
  as alternative provenance channels for interpretations, producing low-value
  candidates that each need manual triage. A class-aware check ("has *any*
  provenance edge") would cut the noise.
- **The digest-bullet format is strictly parsed but under-documented.**
  `parse_digest_ids` only recognizes bullets that begin exactly with
  `- **D-NNN:**` (regex `^-\s+\*\*(D-\d+):\*\*`). A first, natural draft that led
  with a topic label — `- **Scope (D-001):** …` — parsed to `digest_ids: []` and
  left the drift signal *un*cleared even though every decision was present. Had to
  reformat to ID-first. The command's agents-md theme should state this exact
  leading-token requirement (or point at `templates/agents-md.md`) so the digest
  is written in the parseable shape the first time.
- **`days_since_last_review` is a constant 365** across the attention sample —
  review events aren't stamped, so the freshness signal can't discriminate.
  Until stamped, treat attention weights as structural (edge-count) signals only.
