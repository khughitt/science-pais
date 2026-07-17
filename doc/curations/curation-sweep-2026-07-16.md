---
doc_kind: "curation-sweep"
title: "Curation sweep — 2026-07-16"
generated_at: "2026-07-16T00:00:00Z"
source_commit: "dad91fdb660cce6a94832f6e826668bc82091fde"
sweep_scope: "all"
since: null
mode: "apply-obvious"
applied_changes: 12
pending_decisions: 4
---

<!-- This is a project-state record, not a KG entity. It lives under doc/ (not
entities/) by design — see fb-2026-07-10-022. Curation sweeps are transient
tidying logs; they carry no `kind:`/`id:` entity frontmatter and are not
materialized into the knowledge graph. -->


# Curation sweep — 2026-07-16

Second sweep (prior: `doc/curations/curation-sweep-2026-07-10.md`). Drafted in
**propose** mode; PD-1 (the one high-confidence mechanical fix) was then approved
by the user in-session and applied — see Actioned Fixes. All other findings remain
proposals.

## Executive Summary

- **The 2026-07-10 big-picture output is already stale, and stale in a way that
  will waste work.** `synthesis:9000-emergent-threads` and
  `synthesis:9001-project-synthesis-rollup` were generated at commit `3fdeec9`;
  commit `d7d0616` landed **after** them and added `hypothesis:0019`,
  `hypothesis:0020`, and `theme:0003`. The rollup therefore covers 18 of 20
  hypotheses, and `9000` still proposes — as a *candidate hypothesis to create* —
  the host-reserve gate that **already exists** as `hypothesis:0020`.
- **The single highest-value finding: promotion edges are one-directional, so
  successful synthesis work is invisible to the next synthesis run.** Both new
  hypotheses were built out of `9000`'s orphan-question clusters, and both link
  their source questions in `related:`. But all seven source questions still carry
  `related: []`. The orphan classifier reads a question's **own outbound** links
  (verified against non-orphan `question:0055`, which carries `hypothesis:0001` in
  its `related:`), so a re-run would re-derive those same questions as orphans and
  re-propose hypotheses that now exist. This is a metadata gap masquerading as a
  research gap.
- **Four stub papers are load-bearing for `hypothesis:0001` and tracked by
  nothing.** `Broderick2012` (post-mononucleosis), `Ramundo2025`
  (post-chikungunya), `Sanford2026` (post-Ebola), and `Watton2026` (ME/CFS unified
  model) are cited by `search:0002` and `discussion:0002` as the *non-COVID trigger
  legs* of the cross-trigger convergence claim — `search:0002` literally rates
  post-Ebola "Thin-but-present | Sanford2026". They remain unsummarized, and no
  active task tracks promoting them. `hypothesis:0001` carries the project's
  highest attention weight (8769) and `open_question_debt = 35`.
- **`status: stub` and the plan readiness statuses are undeclared vocabulary, so
  real project conventions surface as validation noise.** 4 papers (`stub`) and
  3 plans (`ready-with-caveats`, `not-ready`) account for 7 of the 21 validation
  warnings. These carry genuine information that remapping to `draft` would
  flatten.
- **Clean surfaces:** DAG audit passes (`ok: true`, no findings), `unresolved_refs`
  is empty, `agents_md.drift_signals` is empty (the D-001…D-006 digest applied on
  2026-07-10 is still in sync), no schema-invalid entities, no archive lag, and
  `claim_layer` / identification coverage are both 45/45.
- **The 28 `[UNVERIFIED]` markers are not drift.** Spot-checked across
  `Tsergas2025`, `interpretation:0031/0032/0039/0040` — these are intentional,
  disposition-matched epistemic-honesty markers on unverified numerics. No action.
- **Cross-project sync is 19 days stale** (threshold 14).

## Corpus Inventory

| Class | N | Class | N |
|---|---|---|---|
| paper | 237 | task | 129 (33 active) |
| evidence-line | 95 | question | 90 |
| proposition | 45 | dataset | 47 |
| interpretation | 40 | concept | 32 |
| hypothesis | 20 | synthesis | 20 |
| topic | 16 | plan | 10 |
| search | 9 | pre-registration | 6 |
| method | 6 | report | 5 |
| discussion | 4 | theme | 3 |

Active tasks: 28 proposed, 3 deferred, 2 blocked (P1 ×3, P2 ×16, P3 ×14).

**Coverage gaps by class:**

- **synthesis 20 vs hypothesis 20 is a false match** — the 20 comprises 18
  per-hypothesis files plus `9000`/`9001`; `hypothesis:0019` and `hypothesis:0020`
  have no per-hypothesis synthesis.
- **questions:** 15 of 90 carry `related: []` (see Missed Connections).
- **papers:** 59 of 237 lack `related`. Low signal — bulk-intake papers connect
  through `source_refs`/`cite:` edges, and the class is dominated by the 17-paper
  July intake. Not proposed for action.

## Forgotten Insights

**FI-1 (medium): four cross-trigger stub papers are already being reasoned from,
but were never summarized.**

| Paper | Trigger leg | Cited by |
|---|---|---|
| `Broderick2012` | post-mononucleosis cytokine imbalance | `search:0002`, `discussion:0002` |
| `Ramundo2025` | post-chikungunya transcriptomics | `search:0002`, `discussion:0002` |
| `Sanford2026` | post-Ebola metabolomics (preprint) | `search:0002` |
| `Watton2026` | ME/CFS unified mechanistic model | `search:0002` |

`search:0002` uses these to grade the strength of the non-COVID trigger legs
(post-Ebola "Thin-but-present", post-chikungunya "Moderate … but **arthr**[algia
-dominant]"). Those gradings are load-bearing for `hypothesis:0001`'s cross-trigger
convergence claim and for D-003's infection-trigger scope discipline, yet they rest
on entities with no summary body. Because their `status: stub` is also
out-of-vocabulary, they read as lint rather than as a backlog. Proposed: a single
task to promote all four (see PD-3), which also clears 4 validation warnings.

## Missed Connections

**MC-1 (high, mechanical — this sweep's main proposal, PD-1).** Seven questions
were promoted into two new hypotheses on 2026-07-10; the hypothesis→question edges
exist, the question→hypothesis edges do not. Every one of these is *evidence-backed
by the reciprocal edge already present in the hypothesis file* — this is
backfilling a known edge, not inferring a new claim:

| Question | Reciprocal edge already in | Proposed `related:` addition |
|---|---|---|
| `question:0023` (cGAS-STING) | `hypothesis:0019` | `hypothesis:0019-cgas-sting-nlrp3-sterile-innate-sensing-driver` |
| `question:0024` (NLRP3/GSDMD) | `hypothesis:0019` | `hypothesis:0019-…` |
| `question:0031` (immunosuppressed hosts) | `hypothesis:0020` | `hypothesis:0020-host-immune-baseline-reserve-gate` |
| `question:0032` (LMIC / ancestry) | `hypothesis:0020` | `hypothesis:0020-…` |
| `question:0033` (frailty) | `hypothesis:0020` | `hypothesis:0020-…` |
| `question:0034` (atopy / MCAS) | `hypothesis:0020` | `hypothesis:0020-…` |
| `question:0040` (pregnancy milieu) | `hypothesis:0020` | `hypothesis:0020-…` |

**MC-2 (high, same class, pre-dating 07-10).** Five further orphan-classified
questions are linked inbound by an existing hypothesis but carry `related: []`:

| Question | Inbound from | Proposed addition |
|---|---|---|
| `question:0041` (female predominance = ascertainment?) | `hypothesis:0008` | `hypothesis:0008-…` |
| `question:0042` (cross-trigger 10–20% artifact?) | `hypothesis:0008` | `hypothesis:0008-…` |
| `question:0043` (persister bet-hedging) | `hypothesis:0002` | `hypothesis:0002-…` |
| `question:0044` (chronic GvHD analogy) | `hypothesis:0009` | `hypothesis:0009-…` |
| `question:0047` (menstrual/ultradian periodicity) | `hypothesis:0005` | `hypothesis:0005-…` |

**Explicitly NOT proposed** (guarding against fabricating edges): `question:0027`,
`0028`, `0029`, `0030` are linked only from `theme:0003-demonstrability-ceiling…`,
not from any hypothesis, and `question:0039`, `0045`, `0046` have no non-synthesis
backlink at all. These are **genuine** hypothesis-orphans and should stay
orphan-classified. Of the 19 orphans in `9000`, 12 are metadata artifacts and 7 are
real.

## Drift

**DR-1 (medium-high): `9000`/`9001` predate `d7d0616`.** Both carry
`generated_at: 2026-07-10T18:59:35Z`, `source_commit: 3fdeec9`. Since then:
`hypothesis:0019`, `hypothesis:0020`, `theme:0003` added; `proposition:0043/0044/
0045` added; and the 2026-07-15 health triage recorded `accepted_validation`
rulings on `hypothesis:0020` and `proposition:0043/0045`. Consequences:

- `9001` synthesizes 18 of 20 hypotheses.
- `9000`'s host-modifier section proposes creating a hypothesis that exists
  (`hypothesis:0020`); its text and `hypothesis:0020`'s "rank-ordering prediction"
  (P3) are near-verbatim, confirming the promotion happened and the file is simply
  behind.
- `hypothesis:0020` reaches `well_supported` on a single Azhir2026 mediation line
  (intentionally held fragile per the accepted-validation ruling) — a state the
  rollup does not reflect at all.

Regeneration via `/science:big-picture` is the fix (PD-2). **Constraint:** the
regenerated rollup/emergent files must **overwrite `9000`/`9001` in place**.
Renaming or renumbering them to hypothesis-mirrored `00NN` collides with the
per-hypothesis series and trips `science validate` entity-number-hygiene, and
leaves the graph stale.

**DR-2 (medium): undeclared status vocabulary — 7 of 21 validation warnings.**

- `paper.status-vocabulary` ×4: `stub` ∉ (active, retired) — the four FI-1 papers.
- `plan.status-vocabulary` ×3: `ready-with-caveats` (`plan:0002`,
  `plan:2026-06-19-menopause-pais-total-effect-analysis`), `not-ready`
  (`plan:0005`) ∉ (active, archived, complete, draft, retired, superseded).

Both are real conventions, not typos. `ready-with-caveats` and `not-ready` encode
review verdicts that `draft` would erase, and `stub` distinguishes "seeded, not yet
read" from "active". Needs a convention decision (PD-4), not a mechanical remap.

**DR-3 (low): freshness signal is inert.** Every entity in the attention sample
reports `days_since_last_review: 365`, so `freshness_state` is effectively constant
and attention ranking is driven almost entirely by `open_question_debt`. Not
actionable inside this project's data; noted in Self-Reflection.

**DR-4 (low): cross-project sync 19 days stale** (last `2026-06-27`, threshold 14).
`health-post-acute-infection` publishes 613 entities. Note `task:t110` is explicitly
sync-gated.

## Duplication and Fragmentation

No substantive duplication found. The one near-duplication is **DR-1's**
`9000`-proposes-what-`hypothesis:0020`-already-is, which is staleness rather than
fragmentation and resolves on regeneration. Checked and found clean: no overlapping
topic entities, no repeated questions across the 90 (the explore-ideas batches
q0023–q0047 are distinct), no parallel notes competing with the entity tree.

## Actioned Fixes

**PD-1 applied — 12 files, `related:` backfill (MC-1 + MC-2).** Approved in-session
after the ledger was drafted. Each edit adds one `related:` entry plus an `updated:`
bump to `2026-07-16`; no prose or claim content was touched.

Two guards ran per file before any write, and all 12 passed both:

1. the question must carry a bare `related: []` (never overwrite existing links);
2. the target hypothesis must **already** name `question:<id>` in its own
   `related:` — i.e. only reciprocate an edge that demonstrably exists. A failure
   here would have aborted the whole batch rather than fabricate an edge.

| File | Added |
|---|---|
| `entities/questions/0023-cgas-sting-…` | `hypothesis:0019-…` |
| `entities/questions/0024-nlrp3-inflammasome-…` | `hypothesis:0019-…` |
| `entities/questions/0031-…-immunosuppressed-hosts` | `hypothesis:0020-…` |
| `entities/questions/0032-…-lmic-and-ancestrally-diverse` | `hypothesis:0020-…` |
| `entities/questions/0033-frailty-…` | `hypothesis:0020-…` |
| `entities/questions/0034-…-atopic-and-mast-cell-…` | `hypothesis:0020-…` |
| `entities/questions/0040-pregnancy-state-immune-milieu-…` | `hypothesis:0020-…` |
| `entities/questions/0041-…-female-predominance-…` | `hypothesis:0008-…` |
| `entities/questions/0042-…-cross-trigger-1020-…` | `hypothesis:0008-…` |
| `entities/questions/0043-bacterial-persister-…` | `hypothesis:0002-…` |
| `entities/questions/0044-chronic-gvhd-…` | `hypothesis:0009-…` |
| `entities/questions/0047-menstrual-cycle-…` | `hypothesis:0005-…` |

**Verification (not asserted — run):** `science graph build` rematerialized
`graph.trig` + `composite.trig`; `science validate` returns **PASSED with 21
warning(s)**, identical in composition to the pre-edit baseline (4
`paper.status-vocabulary`, 3 `plan.status-vocabulary`, 13
`prose_lints.bare-author-year`, 1 `unresolved_markers`) — no warning added or
removed. `science graph audit` returns `rows: []`.

The intended effect is confirmed by `big-picture resolve-questions`: all 12
questions now resolve to their hypothesis at confidence **`inverse`** (a direct
outbound edge) where they previously carried none. `question:0042` additionally
picks up `hypothesis:0001` as primary (2 matches). The next `/science:big-picture`
run should therefore report **7** orphan questions, not 19.

One transient worth recording: immediately after the edits, `validate` reported 22
warnings — a `graph has 13 stale input file(s)` flag. That was the expected
source-vs-graph staleness, cleared by `graph build`, not a defect in the edits.

## Pending Decisions

### NEW — 2026-07-16 sweep

**PD-1 (high, approval-gated mechanical fix): backfill `related:` on the 12
inbound-only questions (MC-1 + MC-2). — ✅ APPLIED 2026-07-16.** See Actioned
Fixes. Approved in-session; applied verbatim as drafted, graph rematerialized,
verified. Its blocking relationship to PD-2 is now discharged.

**PD-2 (medium): regenerate `9000`/`9001` (+ add per-hypothesis synthesis for
`hypothesis:0019` and `hypothesis:0020`) via `/science:big-picture` — ✅ APPLIED
2026-07-17.** Ran at `f6365a3`. `9000`/`9001` overwritten **in place** (DR-1
honored — the resolver `science big-picture synthesis-path` confirmed the
numbered-entity convention, which is exactly the duplicate-entity trap the
command warns about); `entities/synthesis/0019-*.md` and `0020-*.md` created.

The predicted orphan count was **confirmed exactly**: `list_research_orphans`
returns **7**, and the 7 are precisely the ones this sweep classified as real
(`q0027`–`q0030` theme-only; `q0039`/`q0045`/`q0046` no hypothesis backlink).
No orphan-specific edit was made between the prediction and the run, so this is
an independent check that PD-1's backfill was correct rather than merely
count-reducing. `9000` and `9001` both record the 19 → 7 drop as a **metadata
correction, not research progress**.

FI-1 is now closed in the artifact itself: the previous `9000` proposed creating
a hypothesis that already existed as `hypothesis:0020`, and the regenerated
`9000` records that one-directional promotion edges made prior synthesis work
invisible to the next run.

Verification: `big-picture validate` exit 0; `science validate` PASSED at the
unchanged 21-warning baseline (13 bare-author-year, 4 paper.status-vocabulary,
3 plan.status-vocabulary, 1 unresolved_markers); `graph diff` empty;
`synthesized_from` 20/20 entries non-stale with `orphan_question_count`
agreeing with the resolver in both `9000` and `9001`.

**PD-3 (medium): promote the four cross-trigger stub papers — ✅ TRACKED as
`task:t130` (P3), 2026-07-16.**
(`Broderick2012`, `Ramundo2025`, `Sanford2026`, `Watton2026`) from `stub` to
summarized. Sibling to the existing `t106`/`t114`/`t115` seeding tasks. Clears 4
validation warnings as a side effect, and firms up the non-COVID trigger legs that
`search:0002` and `discussion:0002` already lean on. Note `Sanford2026` is a
preprint — intake should hold it at that evidence level.

**PD-4 (medium): decide the status-vocabulary convention for `paper` and `plan`
(DR-2). — ✅ TRACKED as `task:t131` (P3), 2026-07-16.** Sequence `t131` before
`t130`: the vocabulary decision governs what status the promoted papers land on.
Either declare `stub` / `ready-with-caveats` / `not-ready` in the kind
vocabularies, or move the information into a dedicated field. Do **not** flatten to
`draft` — the readiness verdicts are load-bearing (`plan:0005` `not-ready` is the
D-004-blocked gated-EHR plan; its status is the record of that ruling).

### CARRY-OVERS

**Carry-over from 2026-07-10 sweep — PD-3 (low): the `source_refs` convention for
reanalysis/audit interpretations. — ✅ TRACKED as `task:t132` (P3), 2026-07-16.**
Re-verified as unresolved: still 9 flagged (`interpretation:0010`–`0017` plus
`paper:BrandstetterFigueroa2025`), unchanged since the prior ledger. Filed as a
task rather than carried a third time — two sweeps of no movement is the signal
that a ledger entry alone isn't going to resolve it.

**Carry-over from 2026-07-10 sweep — PD-2 (regenerate `synthesis:0008`): RESOLVED,
not carried.** Re-evaluated per the carry-over rule rather than blindly carried:
commit `e23205b` ("doc(big-picture): regenerate synthesis 2026-07-10") post-dates
the prior ledger's `source_commit` (`96a18bf`), and `synthesis:0008` now carries
`generated_at: 2026-07-10T18:59:35Z` with the t117/t108/t107 verdicts incorporated.
Superseded by DR-1, which is *new* drift introduced by `d7d0616` afterward.

**Carry-over from 2026-07-10 sweep — PD-1 (AGENTS.md digest) and PD-4 (t035
workflow ref): confirmed still applied.** `agents_md.drift_signals` is empty and
`digest_ids` == `active_decision_ids` == D-001…D-006; `unresolved_refs` is empty.
No action.

## Suggested Follow-Ups

1. ~~Apply PD-1, then rebuild the graph.~~ **Done** — see Actioned Fixes.
2. Run `/science:big-picture` (PD-2) — now unblocked; orphan counts are honest.
   This is the only pending decision **not** carried by a task, because it is a
   command to run rather than a judgement to make.
3. ~~File a task for PD-3.~~ **Done** — `t130` (papers), `t131` (vocabulary),
   `t132` (source_refs carry-over) all filed 2026-07-16. Run `t131` before `t130`.
4. Run `science sync run` — 19 days stale, and `t110` is sync-gated (DR-4).
5. Consider `/science:review-tasks`: 28 of 33 active tasks sit at `proposed` with
   3 P1s from the July intake (`t124` Al-Aly 2025 intake, `t125` female-PASC
   decomposition, `t126` vaccine-AE scope ruling) that look like the real front.

## Self-Reflection

> What did this curation sweep make harder than it should have been?

**1. The command points at the wrong ledger location.** `/science:curate` says to
write `entities/meta/curation/curation-sweep-*.md` in five places, but this project
deliberately relocated ledgers to `doc/curations/` (commit `3fdeec9`,
fb-2026-07-10-022) precisely because sweeps are transient state-records, not KG
entities. The Phase-1 carry-over step reads *"the most recent prior ledger at
`entities/meta/curation/`"* — that path is empty here, so a literal reading finds no
prior ledger and silently re-derives every carry-over as a fresh finding, which is
the exact failure fb-2026-05-01-003 exists to prevent. *Smallest fix:* have the
command resolve the ledger directory from project convention (glob both paths, or
read a `curation.ledger_dir` key) rather than hardcoding the entity tree.

**2. The orphan classifier is outbound-only, and that manufactured a fake research
gap.** `9000` reported 19 orphan questions; 12 were fully connected — just
connected *inbound*. Worse, the failure is self-perpetuating: promoting orphans
into a hypothesis (exactly what `9000` recommends) does not clear their orphan
status, so each big-picture run re-proposes hypotheses that already exist, and the
project pays for the same synthesis twice. *Smallest fix:* make the orphan check
edge-direction-agnostic — a question with any inbound `hypothesis:` edge is not an
orphan. That one change would have made 12 of this sweep's findings unnecessary.

**3. `curate inventory`'s `no_outbound_links` conflates two very different
things.** It reported 35 entities, of which 20 are generated synthesis files
(outbound-empty by design, pure noise) and 15 are the questions above. The
actionable class — "inbound-connected but outbound-empty", i.e. an asymmetric edge —
isn't surfaced at all; I had to reconstruct it with a manual backlink grep over
every flagged file. *Smallest fix:* split the signal into `no_links_either_way`
(real) vs `inbound_only` (asymmetric, usually a one-line backfill), and exclude
generated `report_kind:` artifacts from both.

**4. `days_since_last_review: 365` on every single entity.** No command writes a
`last_reviewed` field, so `freshness_state` is a constant and contributes nothing to
attention ranking — which collapses to `open_question_debt` alone. That makes
`attention-sample` much less useful for choosing a reading set than its weighting
implies. Either have the review-writing commands (`/science:review`,
`/science:interpret-results`, health triage) stamp `last_reviewed`, or drop the term
from the weight so the ranking doesn't imply evidence it lacks.

**5. Two parallel evidence surfaces, one dead.** `science health` reports
`cross_paper_evidence` with 0 units and `speculative` belief for all 45 propositions
(`empty_state: no_cross_paper_evidence`), while the belief machinery that actually
runs — `belief.fragile-single-line`, `evidence-line:*`, the 20 `accepted_validation`
rulings — works off a different surface entirely and reports `proposition:0011` at
4 support / 2 dispute. A reader trusting the first surface would conclude the
project has no evidence at all. *Smallest fix:* if `cross_paper_evidence` is
superseded by evidence-lines, drop it from the health payload or mark it
`not_adopted` rather than reporting a uniformly-empty belief table.

**6. The ledger was a graph input, contradicting what the ledger says it is. —
✅ FIXED 2026-07-16; reported as `fb-2026-07-17-001`.**
This file opens with a comment stating it is "not materialized into the knowledge
graph" — which was half true. It contributes no triples, but `graph.trig` embeds a
revision manifest (880 entries) that **did** hash `doc/curations/*.md`, so every
edit to the sweep log re-staled the graph and added a `[graph]` warning to
`validate`. I ran `graph build` three times this sweep: once for the real entity
edits, twice purely because I'd updated this log afterward. The natural order —
edit entities, rebuild, *then* write the ledger recording what you did —
**guarantees** a dirty graph, because the ledger is necessarily written last.

*Fix applied:* a knob already ships for this
(`science_tool/graph/io.py::_revision_manifest_excludes`); it just wasn't set.
`science.yaml` now carries:

```yaml
graph:
  revision_manifest_excludes:
  - doc/curations/*.md
  - doc/meta/*-next-steps.md
```

Verified: manifest 880 → 876 (exactly the 2 sweep ledgers + 2 next-steps files);
editing this ledger no longer stales the graph (`graph diff` empty, `validate`
unchanged at 21 warnings). The pattern is deliberately
`doc/meta/*-next-steps.md`, **not** `doc/meta/*`: that directory mixes transient
ledgers with durable reference artifacts (`case-definition-crosswalk.md/.tsv`,
`t079-vehicle-feasibility-memo.md`, `paper-import-manifest.tsv`), all three of
which were confirmed still tracked after the change.

*Left deliberately unfixed:* ledgers remain **version-controlled**. The owner's
preference is that transient artifacts stay out of VCS, but `/science:curate`
Phase 1 depends on reading the prior ledger for carry-overs — `task:t132` above
exists only because the 2026-07-10 ledger was readable — so gitignoring them today
would silently reintroduce the fb-2026-05-01-003 failure, especially in worktrees.
`fb-2026-07-17-001` carries the design question upstream: the transient-state layer
needs a home that is out of VCS *and* reachable from worktrees (either in-tree and
untracked, resolved via `git rev-parse --git-common-dir`, or centralized under
`XDG_STATE_HOME` keyed by `science.yaml`'s `id:` — notably **not** `~/.cache`,
which may be deleted, nor `~/.config`, which is for configuration).

**7. Minor:** `science tasks list --format json` returns `{format, rows, meta}`
while `curate inventory` returns bare top-level keys and `graph attention-sample`
returns `{format, rows}` — three shapes across four helpers in one phase. Not
harmful, just friction when scripting the evidence pass.
