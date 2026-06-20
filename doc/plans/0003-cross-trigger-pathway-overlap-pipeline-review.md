# Pipeline Review: cross-trigger pathway-overlap Snakemake workflow

**Target:** `plan:0003-cross-trigger-pathway-overlap-pipeline` (`type: plan`, design mode)
**Reviewed:** 2026-06-20
**Overall:** **WARN** — structurally sound and faithful in shape; ship-blocking issues are all
*provenance/specification* gaps, not design errors.
**Related:** `plan:0003-cross-trigger-pathway-overlap-pipeline`, `plan:0002-cross-trigger-pathway-overlap-analysis-plan`,
`pre-registration:0002-cross-trigger-pathway-overlap`, `task:t035`, `task:t037`.

> This is a review note (prose doc), not a graph entity — kept under `doc/plans/` because the project's
> `entities/plans/` enforces `type: plan` + unique plan numbers.

## Summary

The plan is a well-formed orchestration design: the DAG is fully connected raw→`verdict.json`, the QA
discipline matches `t037`, and the five prior review findings are genuinely closed. The residual risk
concentrates in one place: **the plan has started to encode verdict-affecting decisions that the
pre-registration does not contain** (a near-zero filter threshold, a dual-chip combine rule, and — newly
introduced in this revision — a per-DB ρ-direction gate on DB-robustness). Two reproducibility/contract
gaps (unpinned conda versions; unspecified R↔Python table schemas + NA-NES handling) round out the WARN.

## Rubric Results

| Dimension | Score | Issues |
|---|---|---|
| Evidence coverage | **WARN** | τ, min_donors, U133-combine, and a new DB-robustness sub-rule live in the plan, not pre-reg:0002 |
| Assumption audit | **WARN** | τ=−7.0 rests on an *unverified* antimode<−7 assumption; the check that would catch it only warns |
| Data availability | **WARN** | no `dataset:` entities (project-tooling limitation); mitigated by SHA-256 + datapackage |
| Identifiability | **PASS** | BoundaryOut reachable from BoundaryIn; exploratory rank-estimand testable at this n |
| Reproducibility | **WARN** | conda envs not version-pinned / no lockfile; annotation-version coherence still "open" yet verdict-affecting |
| Validation criteria | **PASS** | per-WP DoD + corrupted-fixture halt + small-B smoke + per-label fixtures |
| Scope check | **PASS** | within the user-authorized bounded reanalysis; orchestration-only |
| Integration boundaries | **WARN** | R↔Python intermediate schemas/format unspecified; NA-NES handling in ρ + set-classes undefined |
| Manifest completeness | **WARN** | input `datapackage.json` added; no **output** manifest for `results/` (resources + provenance) |

## Detailed Findings

### 1. Evidence coverage — verdict-affecting parameters live in the plan, not the pre-registration (highest priority)

The plan's guiding principle is "every locked parameter has exactly one home (the config), and the code
reads it… the pipeline is a faithful executor of the pre-registration." But Key decision 9 and the WP7
edit introduce parameters/rules that are **not in `pre-registration:0002`**:

- `τ = −7.0` and `min_donors = 10` (near-zero `log_mu` filter) — **verdict-affecting** (alters the NES
  ranking).
- U133A∪B dual-chip combine = mean-of-platform-collapsed-log2 — **verdict-affecting**.
- *(newly added this revision)* WP7 `db_robustness`: "a theme counts only in DBs whose primary ρ is
  itself directionally consistent." The pre-reg's S3 robustness rule is **theme-sign recurrence across
  ≥2 DBs** with no per-DB ρ gate. This parenthetical **tightens the locked rule** — exactly the kind of
  re-planning the plan elsewhere forswears.

`config.yaml` is a faithful *mirror*, but the pre-reg is the artifact with the `committed`/`data-gated`
status and the `amendments:` audit trail. A verdict-affecting threshold that exists only in the plan has
no no-HARKing provenance. These were all decided **pre-data-result** (no DE/fgsea/concordance run), so a
pre-data amendment is clean and available.

**Recommendation:** record a **third pre-data amendment** in `pre-registration:0002` capturing τ,
`min_donors`, and the U133 combine rule (the genuinely verdict-affecting locks). For the WP7 DB-robustness
sub-rule, **either revert** the parenthetical to the pre-reg's theme-sign-only criterion, **or** amend the
pre-reg to add the ρ-direction gate explicitly. Non-verdict-affecting locks (`hallmark_coverage_warn`,
which only *warns*; the determinism seed/precision) do **not** need pre-reg amendment — note that
classification so the boundary is explicit.

### 2. Assumption audit — τ=−7.0 depends on an unverified distributional claim, and the guard only warns

The justification for τ=−7.0 is "the unexpressed mode sits at `log_mu ≈ −14`, antimode below −7." **This
was never measured.** G2 was a bounded header/scale smoke check on 1–2 MMSEQ files (range, %negative,
%integer) — not a pooled 40-donor per-gene density. The plan adds a structural-QA check that the global
density is bimodal with antimode < τ, but routes a failure to a **surfaced distribution-severity warning,
not a halt**. So if the assumption is wrong, a mis-specified τ silently flows into the ranking and the run
completes anyway — the worst outcome for a verdict-affecting filter.

Two coherent fixes (pick one):
- **(a) Make the antimode-below-τ check build-fatal.** If the pre-committed τ is contradicted by the
  data, halt and force a pre-data amendment to τ. Keeps the hardcoded value but refuses to run on a
  violated premise.
- **(b) Lock a *procedure*, not a number.** Define `τ := antimode of the pooled, contrast-blind log_mu
  density` via a fixed KDE/bin method. Still outcome-blind (never sees group labels), but robust to the
  −14/−7 assumption being slightly off. This is the stronger pre-registration object — a deterministic
  rule rather than a guessed constant.

**Recommendation:** prefer (b); it removes the brittleness *and* the latitude in one move. Whichever is
chosen, fold it into the Finding-1 amendment.

### 3. Reproducibility — "byte-identical verdict.json" is undercut by unpinned analysis packages

Key decision 10's RNG/ordering/serialization contract is correct and necessary, but it is **not
sufficient** for the acceptance criterion. The conda envs (`r-bioc.yaml`) list package *names*
(`bioconductor-limma`, `-fgsea`, `-msigdbr`, annotation `.db`s) with **no version pins and no lockfile**.
limma's eBayes and fgsea's NES are algorithm-version-sensitive; a Bioconductor minor-release bump can
shift NES → a different concordance-carrying set → a different verdict label. Open Question 2 (annotation
vs MSigDB version coherence) flags exactly this but leaves it **open** — for a verdict-affecting pin it
cannot stay open.

**Recommendation:** promote version coherence from Open Question to a **locked WP0 requirement**: pin
exact `=version` for limma/fgsea/msigdbr/org.Hs.eg.db/hgu133[ab].db, and emit a `conda-lock` (or
`environment.yaml` with `--no-builds` hashes) as a build artifact. The "byte-identical on re-run"
criterion should specify *same lockfile* as a precondition.

### 4. Integration boundaries — R↔Python contract and NA-NES handling are unspecified

Two concrete gaps at the language boundary:
- **Table schema/format.** `fgsea_enrich.R` (R) writes NES tables consumed by `specificity.py`,
  `theme_rollup.py`, and the ρ computation (`concordance`); `permutation_null.R` writes `p_perm` for
  `verdict.py`. The intermediate **schema (column names/types/NA encoding) and file format** (TSV vs
  parquet — `py.yaml` implies pyarrow) are not stated. A silent column/NA-encoding mismatch is the
  classic cross-language pipeline bug.
- **NA-NES semantics.** fgsea returns `NES = NA` for sets too small in a given ranked universe (likely
  after harmonization shrinks the gene space). The pre-reg's set-level classes (S1/S2 = same-sign-NES ∧
  p<0.05), the concordance-carrying-set membership, and the Spearman ρ over NES vectors all need a
  **defined NA rule** (e.g., a set with NA NES in either contrast is excluded pairwise from ρ and cannot
  be concordance-carrying; report the dropped count). Undefined, this changes ρ and set membership.

**Recommendation:** add an "intermediate contracts" note to WP5/WP6 fixing the NES/p_perm table schema +
file format, and lock the NA-NES handling rule (this last one is verdict-affecting → fold into the
Finding-1 amendment).

### 5. Manifest completeness — input datapackage exists, output manifest does not

WP1's `datapackage.json` describes acquired **inputs** (good, closes the prior G1 finding). The
manifest-completeness dimension asks for an **output** manifest in `results/` enumerating produced
resources (`verdict.json`, figures, results md, qa reports), their entity cross-references
(`h0001`/`q0001`/`q0017`), and a provenance DAG. The plan emits `run_metadata.json` (a determinism
sidecar) but no results manifest.

**Recommendation:** add a terminal `emit_results_manifest` rule writing `results/datapackage.json` (output
resources + `related:` entity xrefs + the Snakemake provenance/DAG hash). Cheap, and it makes the run
self-describing for the eventual commons promotion.

### 6. Data availability + failure-mode notes (lower priority)

- **No `dataset:` entities** — strict rubric FAIL, scored **WARN** here because the project genuinely
  lacks dataset-entity tooling and provenance is captured by SHA-256 + the new datapackage. Acceptable
  as-is; revisit at commons promotion.
- **Locked-hash recovery path.** If GEO legitimately re-deposits `GSE130353_RAW.tar`, the locked SHA-256
  halts the pipeline with no documented recovery. Add a one-line procedure: re-verify provenance, then
  amend the hash (a logged, deliberate act — not an auto-accept).
- **Optional-toggle hygiene (KD8).** State that the deferred-CEL / `sd`-weighting toggles default
  **off**, that the **confirmatory C1 label always uses toggle=off**, and that toggle state is recorded
  in `run_metadata.json` — so a config toggle can never silently flip the primary verdict.

## Recommendations (priority order)

1. **Record a third pre-data amendment to `pre-registration:0002`** covering the verdict-affecting locks
   (τ + `min_donors`, U133A∪B combine, NA-NES handling) and **resolve the WP7 DB-robustness sub-rule**
   (revert to theme-sign-only, or amend to include the ρ-direction gate). (Findings 1, 2b, 4)
2. **Make the near-zero filter robust:** prefer a locked *procedure* (pooled antimode) over the hardcoded
   τ=−7.0, or make the antimode check build-fatal. (Finding 2)
3. **Pin exact analysis-package versions + emit a lockfile;** close Open Question 2. (Finding 3)
4. **Specify the R↔Python intermediate schema/format** and the NA-NES rule. (Finding 4)
5. **Add an output `results/datapackage.json` manifest.** (Finding 5)
6. **Add the locked-hash recovery note and optional-toggle hygiene.** (Finding 6)

None of these are design changes — they are the specification and provenance work that has to land before
WP0 so the build is faithful and reproducible. Recommend addressing 1–4 before implementation; 5–6 can
ride into WP1/WP8.

## Strengths

- **DAG is fully connected and faithful** raw→`verdict.json`; the exploratory rank-estimand is honestly
  bounded (inherits the pre-reg's `[?]` ceiling at this n).
- **QA discipline is correct:** `*.qa.pass` sentinels, structural=build-fatal / distribution=surfaced,
  `qa_report.md` never the strict output — matches `t037` exactly.
- **The five prior findings are genuinely closed,** including the non-trivial S3 generalization (per
  `pair×DB` null) and the determinism contract.
- **Single-config provenance model** is the right architecture; the gap is only that a few locks haven't
  been pushed back up into the pre-reg yet.
- **Clean separation of concerns:** orchestration-only, no re-litigation of the settled methodology
  (modulo the one WP7 sub-rule this review flags).
