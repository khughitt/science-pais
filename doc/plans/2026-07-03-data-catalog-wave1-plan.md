# Data-Catalog Gate-0 + Wave-1 GWAS/MR Pilot — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the PAIS dataset-coverage scan trustworthy (Gate-0: reconcile prose links, annotate capabilities against a controlled vocabulary, baseline + triage coverage), then run the highest-leverage open-substitute discovery arc end-to-end on the GWAS/MR vehicle as a Wave-1 pilot — stopping at the `/science:plan-pipeline` handoff.

**Architecture:** This is a **curation plan, not a code plan** (per the design's "lightweight, no ledger code" decision). Deliverables are entity-file edits, capability metadata, committed coverage snapshots, discovery-authored dataset entities, and handoff docs. The "test" for each task is `science validate` (capability warnings → 0, no new errors) and `science dataset prioritize --coverage --format json` (coverage-state transitions). No pytest/Python module is built.

**Tech Stack:** the `science` CLI (`science dataset {link,add,verify-access,identity,prioritize,reconcile-links}`, `science validate`, `science tasks`), the `/science:find-datasets` discovery subagent, hand-authored YAML frontmatter + Markdown.

**Design contract:** `doc/plans/2026-07-03-data-catalog-expansion-design.md` (§2c terrain, §4 Gate-0 + estimand, §4a handoff contract, §5 gates, §6 boundaries/t088).

## Global Constraints

- Package management is `uv` — **never `pip`**. Run every command through `uv run --frozen …` from the project root `~/d/health/processes/post-acute-infection`.
- **No AI-attribution trailer/footer** on commits (no `Co-Authored-By`, no "Generated with"). Use conventional-commit prefixes (`chore:`/`feat:`/`docs:`).
- **Paths in committed files use `~/d/…`**, never `/home/keith/…` or `/mnt/ssd/Dropbox/…` (AGENTS.md).
- **Do NOT use Claude Code's `TaskCreate`/`TaskUpdate` tools** — task management is `science tasks` only (AGENTS.md).
- **Capability metadata is hand-authored frontmatter** — there is no `science dataset set-capabilities` command. `provided_capabilities` (on datasets) and `required_capabilities` (on Q/H) are each **a non-empty list of string→string mappings**. Matching semantics (verified in `datasets/capabilities.py`): a target is *compatible* with a dataset iff **some provided set matches every key/value of some required set** (provider may be a superset; multiple sets are OR'd; values compared by exact string equality). **Therefore keys and value tokens MUST come from the controlled vocabulary (Task 1) verbatim, or nothing ever matches.**
- **Reproducibility gate:** every new dataset entity is classified under `science.yaml` `reproducibility_policy` (`bar: third-party-reproducible`, `unknown: halt`, `below_bar: halt`). A Wave-1 GWAS candidate must be `third-party-reproducible` to carry `tier: use-now`.
- **Front-half only (t088 boundary):** this plan ends at the `/science:plan-pipeline` handoff artifact. **No MR/analysis code, no cohort ingestion, no runnable pipeline** — those are gated by `t088` (§6 of the design). Cataloging/discovery proceed without t088.
- **Branch, don't worktree.** The work is sequential metadata curation on entity files; a git worktree would need `UV_PROJECT_ENVIRONMENT` reuse (the `.venv` lives at the project root). Work on a feature branch in the main tree instead (Task 0).
- **Verification is non-optional:** a task is done only when its stated `science validate` / coverage assertion is observed. Do not claim a warning is cleared without re-running validate.

---

## Task 0: Preflight — branch, env sanity, capture baselines

**Files:**
- Create: `doc/plans/coverage-baseline-2026-07-03.json` (pre-annotation coverage snapshot)

**Interfaces:**
- Produces: a feature branch, a confirmed-working `science` CLI, and the committed pre-Gate-0 coverage baseline that Task 5 diffs against.

- [ ] **Step 1: Create the feature branch**

Run:
```bash
cd ~/d/health/processes/post-acute-infection
git checkout -b data-catalog-wave1
```
Expected: `Switched to a new branch 'data-catalog-wave1'`.

- [ ] **Step 2: Confirm the science CLI runs**

Run: `uv run --frozen science dataset list | head -5`
Expected: a table of dataset entities (≥21 rows total). If it errors, stop and report — the env is broken.

- [ ] **Step 3: Capture the capability-warning baseline (record the numbers)**

Run:
```bash
uv run --frozen science validate 2>&1 | grep -c "provided-missing"
uv run --frozen science validate 2>&1 | grep -c "required-missing"
```
Expected: `20` and `9` respectively. Record these — Tasks 3/4 must drive both to `0`.

- [ ] **Step 4: Capture the coverage baseline snapshot**

Run:
```bash
uv run --frozen science dataset prioritize --coverage --format json > doc/plans/coverage-baseline-2026-07-03.json
uv run --frozen python -c "
import json
d=json.load(open('doc/plans/coverage-baseline-2026-07-03.json'))
rows=d.get('rows',d)
from collections import Counter
c=Counter(r['coverage_state'] for r in rows)
print('total:',len(rows)); [print(f'  {v:3d} {k}') for k,v in sorted(c.items(),key=lambda x:-x[1])]
"
```
Expected: `total: 31`; `22 no-candidate`; `9 missing-required-capabilities`. If the mix differs materially, note it in the commit message — the terrain moved since the design scan.

- [ ] **Step 5: Commit the baseline**

```bash
git add doc/plans/coverage-baseline-2026-07-03.json
git commit -m "chore(data-catalog): capture pre-Gate-0 coverage baseline (31 targets: 22 no-candidate, 9 missing-capabilities)"
```

---

## Task 1: Author the capability vocabulary note

**Files:**
- Create: `doc/plans/2026-07-03-capability-vocabulary.md`

**Interfaces:**
- Produces: the controlled field/value set that Tasks 3–4 and Task 8 annotate against. Every `provided_capabilities` / `required_capabilities` key and value used later MUST appear here (or be added here first).

- [ ] **Step 1: Write the vocabulary note**

Create `doc/plans/2026-07-03-capability-vocabulary.md` with exactly this content (seeded from the design §4 Gate-0 step 2; extend only by adding rows, never by ad-hoc values in entity files):

````markdown
---
title: 'PAIS dataset capability vocabulary (v0)'
status: active
created: '2026-07-03'
---

# PAIS capability vocabulary (v0)

Controlled keys/values for `provided_capabilities` (datasets) and
`required_capabilities` (questions/hypotheses). **Matching is exact string
equality per key** (`datasets/capabilities.py::_satisfies`), so both sides must
draw from this list verbatim. A target is covered when *some* provided set
matches *every* key/value of *some* required set (provider may be a superset).

**Authoring rules**
- **Providers annotate richly** — list every capability a dataset genuinely has.
- **Requirers annotate minimally** — a target's required set names only the
  *discriminating* need (usually 1–3 keys), else no dataset will ever match.
- Multiple sets in a list are OR'd — use them for "either modality X or Y".
- Extend this vocabulary by adding a row here in the same commit that first
  uses the new token; never introduce a token only in an entity file.
- **`stratification: sex` is a truth claim, not a wish** — a dataset may declare it
  ONLY if the source actually exposes sex-stratified or sex-interaction estimates
  (for GWAS: sex-stratified or interaction summary statistics). Do not add it to a
  candidate just to make a sex-target match.
- **`analysis_role` / `trait` separate descriptive from causal-MR coverage** — a
  sex-stratified *descriptive* cohort and an MR-usable GWAS must not both silently
  satisfy the same causal target. Causal-MR targets require an `analysis_role` +
  `trait`; purely descriptive targets require only `stratification`/`modality`.

| Key | Allowed values |
|---|---|
| `modality` | `transcriptomics`, `genetics`, `proteomics`, `metabolomics`, `clinical-ehr`, `epidemiology`, `immunophenotype` |
| `assay` | `bulk-rna`, `microarray`, `gwas-sumstats`, `olink`, `cytof`, `metabolomics-panel`, `ehr-coded`, `survey-pro`, `wearable` |
| `cohort_design` | `case-control`, `prospective-longitudinal`, `cross-sectional`, `summary-stats`, `meta-analysis` |
| `trigger` | `sars-cov-2`, `dengue`, `q-fever`, `ebv`, `mixed`, `not-applicable` |
| `case_definition` | `who-lc`, `cdc-lc`, `fukuda`, `ccc`, `icc`, `not-applicable` |
| `outcome` | `fatigue`, `pem`, `autoimmune-dx`, `dysautonomia`, `recovery-status`, `sex-hormone-level` |
| `stratification` | `sex`, `age`, `time-since-infection`, `severity`, `none` |
| `analysis_role` | `mr_exposure`, `mr_outcome`, `descriptive_covariate` |
| `trait` | `long-covid`, `autoimmune-disease`, `sex-hormone-biomarker` |

## Worked examples

**Descriptive coverage.** `question:0001-shared-molecular-signature-across-triggers`
requires only a cross-trigger molecular readout:
```yaml
required_capabilities:
  - modality: transcriptomics
```
`dataset:gse130353-qfs-cfs-monocytes` provides:
```yaml
provided_capabilities:
  - modality: transcriptomics
    assay: bulk-rna
    trigger: q-fever
    cohort_design: case-control
```
The provided set matches every key of the required set → **compatible**.

**Causal-MR coverage (role-gated).** A causal target that needs a genetic instrument
for autoimmune liability requires:
```yaml
required_capabilities:
  - analysis_role: mr_exposure
    trait: autoimmune-disease
```
Only a GWAS declaring *both* tokens (see Task 8) satisfies it — a sex-stratified
descriptive cohort (which lacks `analysis_role`) does **not**, so descriptive and
causal coverage cannot collapse into each other.
````

- [ ] **Step 2: Sanity-check it renders and commit**

Run: `head -20 doc/plans/2026-07-03-capability-vocabulary.md`
Expected: frontmatter + heading visible.

```bash
git add doc/plans/2026-07-03-capability-vocabulary.md
git commit -m "docs(data-catalog): seed PAIS capability vocabulary v0"
```

---

## Task 2: Reconcile prose-only dataset citations

**Files:**
- Modify (via CLI): Q/H files under `entities/questions/` and `entities/hypotheses/` whose bodies cite a real dataset that is not yet wired into reach.

**Interfaces:**
- Consumes: nothing. Produces: additional `datasets:` edges so genuinely-reaching datasets stop showing as `no-candidate`, sharpening the Task 5 triage (reconcilable vs genuine-discovery).

- [ ] **Step 1: Check the CLI's own free-text reconcile first (lossless)**

Run: `uv run --frozen science dataset reconcile-links`
Expected: either nothing, or `would fix:` lines for free-text `datasets:` labels that resolve to a canonical slug. If any appear, apply them:
```bash
uv run --frozen science dataset reconcile-links --fix
```
Then re-run without `--fix` and confirm no residual lines.

- [ ] **Step 2: Find prose citations that are NOT yet wired**

For each of the 3 tenuous, currently `no-candidate` hypotheses the design flags (h0006, h0002, h0003), list the datasets their prose mentions and whether an entity exists:
```bash
uv run --frozen science dataset list | awk '{print $1}' | sed 's/^/dataset:/' > /tmp/pais_ds_ids.txt
for h in 0006-skeletal-muscle-ischemic-mitochondrial-pem \
         0002-tissue-reservoir-antigen-fragment \
         0003-immune-exhaustion-feedback; do
  echo "=== hypothesis:$h ==="
  grep -oiE "recover|gse[0-9]+|q-?fever|dengue|impacc|opensafely|uk-?biobank|mcam|all-of-us" \
    entities/hypotheses/$h*.md | sort -u
done
```
Expected: a short list of dataset mentions per hypothesis (e.g. h0006 → RECOVER).

- [ ] **Step 3: Wire only the citations where the dataset genuinely reaches the target**

Judgement step: a prose mention is *reconcilable* only if the dataset can actually inform that target (not just co-occur in the text). For each confirmed case, run `science dataset link <dataset_ref> <target_ref>`. Example (h0006 is prose-cited by RECOVER, per the design §2c):
```bash
uv run --frozen science dataset link dataset:recover-adult hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem
```
Expected: idempotent append to the hypothesis's `datasets:` list. **Do not blind-link** — only wire mentions you judge genuinely reaching; record the ones you deliberately skip (and why) for the Task 5 triage note.

- [ ] **Step 4: Verify the new reach shows up**

Run:
```bash
uv run --frozen science dataset prioritize --coverage --format json | uv run --frozen python -c "
import json,sys; d=json.load(sys.stdin); rows=d.get('rows',d)
for r in rows:
    if r['target'].startswith('hypothesis:0006') or r['target'].startswith('hypothesis:0002') or r['target'].startswith('hypothesis:0003'):
        print(r['coverage_state'], r['target'], r.get('datasets'))
"
```
Expected: any hypothesis you wired now shows its dataset in reach (state moves off `no-candidate`, typically to `missing-required-capabilities` until Task 4).

- [ ] **Step 5: Commit**

```bash
git add entities/hypotheses entities/questions
git commit -m "chore(data-catalog): reconcile prose-only dataset citations into reach edges"
```

---

## Task 3: Annotate `provided_capabilities` on all reaching datasets

**Files:**
- Modify: each dataset file under `entities/datasets/` that `science validate` flags with `provided-missing` (the 20 from Task 0).

**Interfaces:**
- Consumes: the Task 1 vocabulary. Produces: `provided_capabilities` on every reaching dataset, clearing all `provided-missing` / `provided-malformed` warnings.

- [ ] **Step 1: List the datasets needing annotation**

Run: `uv run --frozen science validate 2>&1 | grep "provided-missing" | grep -oE "dataset:[a-z0-9-]+" | sort -u`
Expected: ~20 dataset ids.

- [ ] **Step 2: Add a `provided_capabilities` block to each, using ONLY vocabulary tokens**

For each dataset, insert a `provided_capabilities:` list into the frontmatter (top level, e.g. after `ontology_terms:`). Annotate richly and truthfully from the dataset's `## What it is` section. Examples (author the rest by the same pattern, drawing every token from Task 1):

```yaml
# entities/datasets/gse130353-qfs-cfs-monocytes.md
provided_capabilities:
  - modality: transcriptomics
    assay: bulk-rna
    trigger: q-fever
    cohort_design: case-control
```
```yaml
# entities/datasets/recover-adult.md
provided_capabilities:
  - modality: clinical-ehr
    assay: ehr-coded
    trigger: sars-cov-2
    cohort_design: prospective-longitudinal
    case_definition: who-lc
    stratification: sex
```
```yaml
# entities/datasets/dengue-postinfective-fatigue-meta.md
provided_capabilities:
  - cohort_design: meta-analysis
    trigger: dengue
    outcome: fatigue
    stratification: sex
```
```yaml
# entities/datasets/impacc-immunophenotyping-covid.md
provided_capabilities:
  - modality: immunophenotype
    assay: olink
    trigger: sars-cov-2
    cohort_design: prospective-longitudinal
  - modality: transcriptomics
    assay: bulk-rna
    trigger: sars-cov-2
```
(Use multiple sets, as IMPACC shows, for genuinely multi-assay datasets.)

- [ ] **Step 3: Verify all `provided-*` warnings are gone**

Run: `uv run --frozen science validate 2>&1 | grep -cE "provided-missing|provided-malformed"`
Expected: `0`. If nonzero, the printed ids/paths show which datasets are still missing or malformed (a malformed block = a non-string value, an empty mapping, or a non-list) — fix and re-run.

- [ ] **Step 4: Commit**

```bash
git add entities/datasets
git commit -m "feat(data-catalog): annotate provided_capabilities on reaching datasets"
```

---

## Task 4: Annotate `required_capabilities` on reached targets

**Files:**
- Modify: each Q/H file flagged `required-missing` (the 9 from Task 0, plus any newly-reached targets from Task 2).

**Interfaces:**
- Consumes: Task 1 vocabulary + Task 3 provided sets. Produces: minimal `required_capabilities` on each reached target, clearing `required-missing`, and turning capability-compatible reaches into `covered-*` states.

- [ ] **Step 1: List targets needing annotation**

Run: `uv run --frozen science validate 2>&1 | grep "required-missing" | grep -oE "(question|hypothesis):[a-z0-9-]+" | sort -u`
Expected: ~9 target ids (e.g. `question:0001`, `question:0007`, `question:0013`, `question:0015`, `hypothesis:0001`, `hypothesis:0008`, …).

- [ ] **Step 2: Add a MINIMAL `required_capabilities` block to each**

Author only the *discriminating* need (1–3 keys), so real datasets can match. **Choose
the required set by the target's role** (vocabulary authoring rules): a *descriptive*
question requires modality/stratification; a *causal-MR* question requires
`analysis_role` + `trait` so a sex-stratified descriptive cohort cannot satisfy it by
accident (F2). Insert into frontmatter (e.g. after `related:`). Examples:

```yaml
# entities/questions/0001-shared-molecular-signature-across-triggers.md  (descriptive)
required_capabilities:
  - modality: transcriptomics
```
```yaml
# entities/questions/0007-mechanism-of-female-predominance-in-pais.md  (descriptive: any sex-resolved evidence)
required_capabilities:
  - stratification: sex
```
```yaml
# entities/questions/0013-reproductive-stage-failed-immune-recovery-after-infection.md  (descriptive, trigger-scoped)
required_capabilities:
  - stratification: sex
    trigger: sars-cov-2
```
```yaml
# entities/hypotheses/0008-measurement-channel-and-ascertainment-bias-predictably-shapes-apparent.md  (descriptive)
required_capabilities:
  - modality: clinical-ehr
```
For the **causal-MR** targets that Wave-1 GWAS is meant to serve (e.g.
`hypothesis:0009` post-infectious autoimmune conversion, and the causal reading of
q0013/q0019–q0022), use a role-gated set so only an MR-usable GWAS matches — author
these in **Task 8 Step 4** alongside the GWAS `provided` sets so the pair stays
consistent, not here:
```yaml
# example (authored in Task 8): a causal autoimmune→PAIS target
required_capabilities:
  - analysis_role: mr_exposure
    trait: autoimmune-disease
```
Guard: if a target's required set names a key/value that no provided set carries, it will stay `missing`/`mismatch` — that is a legitimate signal it needs discovery, not a reason to weaken the requirement. Record such cases for the Task 5 triage.

- [ ] **Step 3: Verify `required-*` warnings gone + observe coverage movement**

Run:
```bash
uv run --frozen science validate 2>&1 | grep -cE "required-missing|required-malformed"   # expect 0
uv run --frozen science dataset prioritize --coverage --format json | uv run --frozen python -c "
import json,sys; d=json.load(sys.stdin); rows=d.get('rows',d)
from collections import Counter
print(Counter(r['coverage_state'] for r in rows))
"
```
Expected: first command `0`; second shows some targets now in `covered-runnable` / `covered-reference` / `covered-unverified` rather than `missing-required-capabilities`.

- [ ] **Step 4: Confirm no new validate ERRORs**

Run: `uv run --frozen science validate 2>&1 | grep -c "^ERROR"`
Expected: `0` (same as the Task 0 baseline).

- [ ] **Step 5: Commit**

```bash
git add entities/questions entities/hypotheses
git commit -m "feat(data-catalog): annotate required_capabilities on reached targets"
```

---

## Task 5: Baseline-vs-now coverage snapshot + triage table (Gate-0 close)

**Files:**
- Create: `doc/plans/coverage-postgate0-2026-07-03.json`
- Create: `doc/plans/2026-07-03-gate0-triage.md`

**Interfaces:**
- Consumes: Tasks 2–4. Produces: the committed post-Gate-0 coverage snapshot and the triage table classifying every remaining `no-candidate` target as **reconcilable** or **genuine-discovery** — the Gate-0 deliverable and the input to Wave-1 target selection.

- [ ] **Step 1: Capture the post-Gate-0 coverage snapshot**

Run:
```bash
uv run --frozen science dataset prioritize --coverage --format json > doc/plans/coverage-postgate0-2026-07-03.json
```

- [ ] **Step 2: Enumerate the remaining no-candidate targets**

Run:
```bash
uv run --frozen python -c "
import json
d=json.load(open('doc/plans/coverage-postgate0-2026-07-03.json'))
rows=d.get('rows',d)
nc=[r['target'] for r in rows if r['coverage_state']=='no-candidate']
print(len(nc),'no-candidate:'); [print(' ',t) for t in sorted(nc)]
"
```
Expected: the residual list (≤22, fewer if Task 2 wired some).

- [ ] **Step 3: Write the triage table**

Create `doc/plans/2026-07-03-gate0-triage.md`. For **every** no-candidate target, one row, classified `reconcilable` (an existing dataset could be wired — name it, say why it wasn't in Task 2) or `genuine-discovery` (no existing dataset reaches it — names the modality/data-role needed, feeds the waves). Use this shape:
```markdown
---
title: 'Gate-0 coverage triage (2026-07-03)'
status: active
created: '2026-07-03'
see_also:
- doc:2026-07-03-data-catalog-expansion-design
---

# Gate-0 coverage triage

Baseline: `coverage-baseline-2026-07-03.json` (31 targets: 22 no-candidate, 9 missing-capabilities).
Post-Gate-0: `coverage-postgate0-2026-07-03.json`.

| target | class | note (dataset to wire / modality needed) | wave |
|---|---|---|---|
| hypothesis:0007-autoimmune-sfn-peripheral-dysautonomia-substrate | genuine-discovery | needs open SFN/autonomic dataset; t050-gated | 2 |
| question:0019-<full-slug> | genuine-discovery | male vascular/VTE — needs open VTE/vascular-by-sex cohort | 1/2 |
| …one row per no-candidate target, full slug in column 1… | | | |
```
Every no-candidate target from Step 2 MUST appear exactly once, with its **full slug**
in column 1 (no `…` truncation there — Step 4b matches column 1 against the JSON
exactly; put any shortening in the note column).

- [ ] **Step 4: Record the coverage delta**

Append a short delta section to the triage doc:
```bash
uv run --frozen python -c "
import json
from collections import Counter
b=json.load(open('doc/plans/coverage-baseline-2026-07-03.json')); b=b.get('rows',b)
a=json.load(open('doc/plans/coverage-postgate0-2026-07-03.json')); a=a.get('rows',a)
print('BEFORE',Counter(r['coverage_state'] for r in b))
print('AFTER ',Counter(r['coverage_state'] for r in a))
"
```
Paste both lines under a `## Coverage delta` heading in the triage doc.

- [ ] **Step 4b: Machine-check triage completeness (F4)**

The triage table is the key Gate-0 deliverable, so verify — not eyeball — that its
first column is exactly the JSON's `no-candidate` set (no missing, extra, or
duplicate rows). This reads the table's `target` column (first cell of each data row
whose target starts with `question:`/`hypothesis:`):
```bash
uv run --frozen python -c "
import json,re,sys
d=json.load(open('doc/plans/coverage-postgate0-2026-07-03.json')); rows=d.get('rows',d)
want={r['target'] for r in rows if r['coverage_state']=='no-candidate'}
got=[]
for ln in open('doc/plans/2026-07-03-gate0-triage.md'):
    m=re.match(r'\s*\|\s*((?:question|hypothesis):[a-z0-9-]+)', ln)
    if m: got.append(m.group(1))
from collections import Counter
dupes=[t for t,n in Counter(got).items() if n>1]
gotset=set(got)
missing, extra = want-gotset, gotset-want
ok = not (missing or extra or dupes)
print('triage OK' if ok else 'triage FAIL')
if missing: print('  MISSING:', sorted(missing))
if extra:   print('  EXTRA  :', sorted(extra))
if dupes:   print('  DUPES  :', sorted(dupes))
sys.exit(0 if ok else 1)
"
```
Expected: `triage OK`, exit 0. If it fails, fix the table (note: full target slugs
must match the JSON exactly — do not abbreviate them with `…` in the first column;
put any abbreviation in the note column instead) and re-run until it passes.

```bash
git add doc/plans/coverage-postgate0-2026-07-03.json doc/plans/2026-07-03-gate0-triage.md
git commit -m "feat(data-catalog): Gate-0 close — post-annotation coverage + no-candidate triage"
```

> **Gate-0 acceptance check (design §4):** capability-vocabulary note committed (Task 1); zero `provided-*`/`required-*` warnings (Tasks 3–4); every no-candidate target classified in the triage (this task); baseline + post JSON committed. Confirm all four before proceeding.

---

## Task 6: Write the Wave-1 GWAS/MR estimand + bridge-assumption note (before discovery)

**Files:**
- Create: `doc/plans/2026-07-03-wave1-gwas-mr-estimand.md`

**Interfaces:**
- Consumes: design §4 Wave-1 estimand rewrite. Produces: the pre-discovery estimand contract that Task 8's handoff notes cite, and the discovery filter (sex-stratified sumstats) that scopes Task 7.

- [ ] **Step 1: Write the estimand note**

Create `doc/plans/2026-07-03-wave1-gwas-mr-estimand.md` stating, concretely (no placeholders): (a) the **substitute estimand** — causal effect of *genetic liability* to autoimmune disease (and of sex-hormone biomarkers, e.g. SHBG) on a PAIS outcome under IV assumptions; (b) **what it answers** — reverse-causation direction; sex-effect modification *only where sex-stratified/interaction sumstats exist*; (c) **what it does NOT replace** — the population-scale prevalence/utilisation/ascertainment-structured EHR interaction (stays with h0008, per D-004); (d) **bridge assumptions** to count a result as evidence for h0005/h0007/h0009 or q0007/q0013/q0019–q0022: instrument relevance + no horizontal pleiotropy (MR-Egger/weighted-median sensitivity), no uncorrected sample overlap, ancestry-matched panels, an *a priori* HLA include/exclude decision, PAIS case-definition comparability across the outcome GWAS. End with a **discovery filter**: candidates must expose (or enable) sex-stratified or interaction summary statistics to serve the sex-modification targets.

- [ ] **Step 2: Commit**

```bash
git add doc/plans/2026-07-03-wave1-gwas-mr-estimand.md
git commit -m "docs(data-catalog): Wave-1 GWAS/MR estimand + bridge assumptions (pre-discovery)"
```

---

## Task 7: Wave-1 discovery — author GWAS/MR candidate dataset entities

**Files:**
- Create: 2–3 dataset entities under `entities/datasets/` (e.g. `covid19-hgi-longcovid-gwas.md`, an autoimmune GWAS, a sex-hormone/SHBG GWAS)
- Create: `entities/searches/0010-gwas-mr-open-substitutes.json` (discovery record, if `/science:find-datasets` is used)

**Interfaces:**
- Consumes: the Task 6 estimand/discovery filter. Produces: candidate GWAS-summary-stat dataset entities (unverified, unlinked), ready for Task 8's verify → classify → annotate → link → handoff.

- [ ] **Step 1: Run discovery**

Invoke the discovery worker for open GWAS summary statistics matching the Task 6 filter:
```
/science:find-datasets  open GWAS summary statistics for: long COVID (COVID-19 Host Genetics Initiative), autoimmune diseases (e.g. SLE/RA), and sex-hormone biomarkers (SHBG/testosterone); prefer sex-stratified sumstats; sources GWAS Catalog, IEU OpenGWAS, Open Targets, COVID-19 HGI.
```
Expected: a ranked candidate list (and a `entities/searches/…json` record). If the subagent is unavailable, hand-identify 2–3 canonical open sources (COVID-19 HGI release, a GWAS Catalog autoimmune study accession, an IEU OpenGWAS SHBG id) and proceed.

- [ ] **Step 2: Author each candidate entity via the CLI**

For each selected source, create a candidate entity (example for the HGI long-COVID GWAS — substitute the real accession/URL you confirmed):
```bash
uv run --frozen science dataset add covid19-hgi-longcovid-gwas \
  --title "COVID-19 Host Genetics Initiative — long-COVID GWAS summary statistics" \
  --origin external --class reference --tier evaluate-next --level public \
  --source-url "https://www.covid19hg.org/results/" \
  --related question:0007-mechanism-of-female-predominance-in-pais
```
Expected: a new `entities/datasets/covid19-hgi-longcovid-gwas.md`. Repeat for the autoimmune-GWAS and sex-hormone-GWAS candidates. (`--class reference` because summary stats are a re-poolable reference grain, not staged microdata; Task 8 revisits class on verify.)

- [ ] **Step 3: Scaffold identity_context for the assembly-bearing GWAS entities**

GWAS sumstats are genome-assembly-bearing. Scaffold (and degrade to UNKNOWN if unresolved, to avoid blocking):
```bash
uv run --frozen science dataset identity suggest dataset:covid19-hgi-longcovid-gwas
```
Apply the suggested block (or set assembly UNKNOWN) via `science dataset identity resolve` per its `--help`. Keep this light — identity precision is not the pilot's point.

- [ ] **Step 4: Verify the entities validate (expected-unverified is OK)**

Run: `uv run --frozen science validate 2>&1 | grep -E "covid19-hgi|gwas" | grep "^ERROR"`
Expected: no ERROR lines for the new entities (WARNs like `verified:false`, or `provided-missing` until Task 8, are expected).

- [ ] **Step 5: Commit**

```bash
git add entities/datasets entities/searches
git commit -m "feat(data-catalog): author Wave-1 GWAS/MR candidate dataset entities"
```

---

## Task 8: Verify-access, reproducibility-classify, capability-annotate, link (apply §4a handoff contract)

**Files:**
- Modify: the Task 7 GWAS entities (access verification, reproducibility block, `provided_capabilities`)
- Modify (via CLI): the sex/autoimmune targets they reach (`datasets:` links)

**Interfaces:**
- Consumes: Task 7 entities + Task 1 vocabulary + Task 6 estimand. Produces: candidates that meet the §4a done-definition and move the sex/autoimmune targets' coverage.

- [ ] **Step 1: Verify access + set class (one atomic call per dataset)**

For each GWAS entity, confirm the landing page/download and set access. **The
`--method` allowed for each class is whitelisted** (`datasets_catalog.py:431`):
`reference` accepts only `{credential-confirmed, landing-confirmed, metadata-confirmed}`;
`retrieved` is **deposit-only** (F1). So pick the branch by whether you actually stage files:

- **Stay `reference`** (the default — summary stats as a re-poolable reference grain):
```bash
uv run --frozen science dataset verify-access dataset:covid19-hgi-longcovid-gwas \
  --level public --method landing-confirmed --license unknown --class reference \
  --note "COVID-19 HGI public summary-statistics release; downloadable flat files observed on the landing page."
```
- **Convert to `deposit`** (only if you download/stage the sumstats now) — deposit
  accepts `--method retrieved`, and a deposit with a runtime artifact then requires a
  `datapackage`/`local_path` + SHA-256 hashes (per the §4a handoff contract, staged row):
```bash
uv run --frozen science dataset verify-access dataset:covid19-hgi-longcovid-gwas \
  --level public --method retrieved --license unknown --class deposit \
  --note "Downloaded HGI sumstats; staged locally (datapackage + hashes recorded)."
```
Do **not** pair `--class reference` with `--method retrieved` — the CLI rejects it.
Expected: `access.verified: true`, a verification-log line appended.

- [ ] **Step 2: Add the reproducibility block (third-party-reproducible)**

Hand-author an `access.reproducibility` block on each entity, matching the project pattern (see `entities/datasets/dengue-postinfective-fatigue-meta.md`):
```yaml
  reproducibility:
    obtainability: public
    execution: local
    extractability: full-dataset
    notes: "Public GWAS summary statistics: downloadable flat files, re-poolable/re-analyzable locally at the summary grain — third-party-reproducible. Not individual-level genotypes (a scientific-strength limit, not an access one)."
```
This is what clears the `reproducibility_policy` bar for `tier`. If any candidate is NOT third-party-reproducible (e.g. requires an application), set its tier to `track` and note it — do not mark it `use-now`.

- [ ] **Step 3: Annotate `provided_capabilities` (vocabulary tokens, incl. role/trait)**

Annotate each GWAS with its `analysis_role` + `trait` (so causal targets match) and add
`stratification: sex` **only if the discovered files are genuinely sex-stratified /
interaction sumstats** (F2 — it is a truth claim, not a wish). Examples:
```yaml
# dataset:covid19-hgi-longcovid-gwas  (the long-COVID OUTCOME GWAS)
provided_capabilities:
  - modality: genetics
    assay: gwas-sumstats
    cohort_design: summary-stats
    trigger: sars-cov-2
    analysis_role: mr_outcome
    trait: long-covid
    # add `stratification: sex` ONLY if a sex-stratified HGI release is used
```
```yaml
# dataset:<autoimmune>-gwas  (the EXPOSURE instrument)
provided_capabilities:
  - modality: genetics
    assay: gwas-sumstats
    cohort_design: summary-stats
    analysis_role: mr_exposure
    trait: autoimmune-disease
```
```yaml
# dataset:<shbg>-gwas  (sex-hormone biomarker exposure)
provided_capabilities:
  - modality: genetics
    assay: gwas-sumstats
    cohort_design: summary-stats
    analysis_role: mr_exposure
    trait: sex-hormone-biomarker
    outcome: sex-hormone-level
```
Draw every token from Task 1; if you need a new one, add it to the vocabulary note in
this same commit.

- [ ] **Step 4: Author the causal-MR `required_capabilities`, then link (paired, so they match)**

For each causal target the GWAS serves, add a role-gated `required_capabilities` set
whose keys are a subset of the GWAS `provided` set above — author these here, paired
with the links, so the pair is provably compatible. Example for a causal
autoimmune→PAIS target (`hypothesis:0009`):
```yaml
# entities/hypotheses/0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune…md
required_capabilities:
  - analysis_role: mr_exposure
    trait: autoimmune-disease
```
Then link, and verify compatibility on the spot:
```bash
uv run --frozen science dataset link dataset:<autoimmune>-gwas hypothesis:0009-post-infectious-immune-set-point-shift-drives-long-term-autoimmune
uv run --frozen science dataset prioritize --coverage --format json | uv run --frozen python -c "
import json,sys; d=json.load(sys.stdin); rows=d.get('rows',d)
r=[x for x in rows if x['target'].startswith('hypothesis:0009')][0]
print(r['coverage_state'], r['target'], r.get('datasets'))
"
```
Expected: `hypothesis:0009` moves off `no-candidate` to a `covered-*` state (not
`missing-required-capabilities`/`capability-mismatch`) — if it stays mismatched, the
`required` set names a key the GWAS `provided` set lacks; fix one side. Link the
long-COVID *outcome* GWAS only to targets whose requirement it actually satisfies
(e.g. a `stratification: sex` descriptive target **only if** you added that token in
Step 3). Do not link a GWAS to a target it cannot satisfy under exact-match.

- [ ] **Step 5: Verify done-definition + coverage movement**

Run:
```bash
uv run --frozen science validate 2>&1 | grep -cE "provided-missing|required-missing|^ERROR"   # expect 0
uv run --frozen science dataset prioritize --coverage --format json | uv run --frozen python -c "
import json,sys; d=json.load(sys.stdin); rows=d.get('rows',d)
for r in rows:
    if 'dataset:covid19-hgi-longcovid-gwas' in (r.get('datasets') or []):
        print(r['coverage_state'], r['target'])
"
```
Expected: 0 warnings/errors; the sex/autoimmune targets now list the GWAS dataset and sit at `covered-reference`/`covered-unverified` (not `no-candidate`). Confirm each candidate satisfies the §4a table (entity, verified/exception, `last_reviewed`, source_url, reproducibility, provided_capabilities, target required_capabilities, backlink, bridge note).

- [ ] **Step 6: Commit**

```bash
git add entities/datasets entities/questions entities/hypotheses doc/plans/2026-07-03-capability-vocabulary.md
git commit -m "feat(data-catalog): verify, classify, annotate, and link Wave-1 GWAS candidates"
```

---

## Task 9: Wave-1 checkpoint + plan-pipeline handoff + follow-up task

**Files:**
- Create: `doc/plans/2026-07-03-wave1-checkpoint.md`
- Create: `doc/plans/2026-07-03-gwas-mr-ingestion-handoff.md`

**Interfaces:**
- Consumes: everything above. Produces: the Wave-1 coverage-delta record, the front→back `/science:plan-pipeline` handoff artifact (execution gated by t088), and the follow-up task — the design's Wave-1 hard checkpoint.

- [ ] **Step 1: Write the checkpoint record**

Create `doc/plans/2026-07-03-wave1-checkpoint.md`: the before/after coverage counts (baseline vs post-Task-8, via the Step-4 delta snippet from Task 5 pointed at the latest scan), which blocked clusters Wave 1 lifted, and the **decision rule** for whether Wave 2/3 proceed as scoped or re-weight (design §4 hard checkpoint).

- [ ] **Step 2: Write the ingestion/analysis handoff artifact**

Create `doc/plans/2026-07-03-gwas-mr-ingestion-handoff.md`: the front→back boundary. State, per GWAS candidate, the exact accession/URL + files to stage, the MR estimand + bridge assumptions (cite Task 6), the sensitivity analyses required (MR-Egger/weighted-median, sample-overlap, HLA handling), and the acceptance check. **State plainly that running MR is gated by `t088`** and name `/science:plan-pipeline` as the next skill — this plan does not run it.

- [ ] **Step 3: File the MR-execution follow-up task (blocked on t088)**

Use the first-class `--blocked-by` field (verified in `science tasks add --help`) so
the backlog knows this is dependency-gated, not merely proposed (F3) — the prose note
stays too, but is not the only blocker representation:
```bash
uv run --frozen science tasks add "Wave-1: run open GWAS/MR analysis for sex×autoimmune PAIS questions" \
  --priority P3 \
  --blocked-by task:t088 \
  --related task:t088 \
  --description "Execute the MR handoff in doc/plans/2026-07-03-gwas-mr-ingestion-handoff.md. BLOCKED on t088 (open-analysis scope decision) — this is analysis EXECUTION, gated by entities/specs/0001-scope-boundaries-for-health-post-acute-infection.md. Cataloging/handoff already done (Wave-1 pilot)."
```
Expected: a new task id printed, shown as blocked-by t088. Record the id in the
handoff doc. If `--related task:t088` is rejected as a ref-form mismatch, drop it and
keep `--blocked-by`.

- [ ] **Step 4: Final validate + coverage sweep**

Run:
```bash
uv run --frozen science validate 2>&1 | grep -c "^ERROR"                       # expect 0
uv run --frozen science validate 2>&1 | grep -cE "provided-missing|required-missing"   # expect 0
```
Expected: both `0`.

- [ ] **Step 5: Commit**

```bash
git add doc/plans/2026-07-03-wave1-checkpoint.md doc/plans/2026-07-03-gwas-mr-ingestion-handoff.md tasks/active.md
git commit -m "docs(data-catalog): Wave-1 checkpoint + GWAS/MR plan-pipeline handoff"
```

- [ ] **Step 6: Open a PR / merge decision**

Summarize the branch (`data-catalog-wave1`): Gate-0 closed (coverage now trustworthy), Wave-1 GWAS/MR vehicle cataloged + handed off, MR execution deferred to t088. Present merge vs PR per the project's convention (recent history commits directly to `main`).

---

## Out of scope (deferred behind the Wave-1 checkpoint)

- **Running MR / ingesting sumstats** — gated by **t088**; handed to `/science:plan-pipeline` (Task 9 artifact).
- **Waves 2–3** — thin-link repair (h0006/h0002/h0003/h0007), modality breadth (metabolomics/microbiome/wearables/healthy-recovered), pan-disease contrast, commons promotion, demand-gated adapters. Re-planned only after the Task 9 checkpoint records the coverage delta (design §4).
- **Epidemiology/surveillance vehicle** (the other Wave-1 open substitute, for h0008) — same arc as the GWAS pilot; add after the pilot validates the flow, or fold into Wave-1 round 2.
- **A capability-vocabulary validator** — the note is hand-authored convention; machine enforcement is a later upgrade only if the vocabulary drifts.

## Self-review notes

- **Spec coverage:** Gate-0 reach+capability audit (Tasks 2–5), capability vocabulary (Task 1, gate in Task 5), acceptance criteria (Task 5 checkpoint + Step 4b machine-check), estimand rewrite before discovery (Task 6), §4a handoff contract (Task 8 Step 5 + Task 9), GWAS/MR pilot end-to-end (Tasks 6–9), t088 front-half boundary (Global Constraints + Tasks 8–9 + Out of scope), Wave-1 hard checkpoint (Task 9). Reproducibility gate realized in Task 8 Step 2.
- **Placeholder scan:** the only intentional fill-ins are real-data lookups that must be run to be known (Task 2 prose-citation list; Task 7 accessions/URLs; the exact per-target required sets, authored paired-with-links in Task 8 Step 4) — each marked with the command that produces it, not a vague TODO.
- **Name/type consistency:** capability fields `provided_capabilities`/`required_capabilities` (list of string→string maps) used identically in Tasks 1/3/4/8; CLI verbs (`link`, `add`, `verify-access`, `identity`, `prioritize --coverage`, `tasks add --blocked-by`) match their verified `--help`; coverage states (`no-candidate`, `missing-required-capabilities`, `covered-reference`, `covered-runnable`) match `dataset_prioritize.py`.
- **Review fixes applied (2026-07-03 pipeline review):** F1 — Task 8 Step 1 splits the `verify-access` method by class (`retrieved` is deposit-only per `datasets_catalog.py:431`; `reference` uses landing/metadata-confirmed). F2 — vocabulary gains `analysis_role`/`trait`, `stratification: sex` is a truth-claim guard, and Task 8 authors causal-MR `required` sets paired with links so descriptive and causal coverage cannot collapse. F3 — Task 9 uses `--blocked-by task:t088`. F4 — Task 5 Step 4b machine-checks triage completeness (no missing/extra/dupe targets).
