# Pipeline audit findings - post-acute-infection

Audit date: 2026-06-26. Method: `~/d/science/docs/process/pipeline-audit-and-refactor.md`.

Discovery commands used:

- `rg --files` over workflow definitions, scripts, notebooks, command surfaces, tests.
- `find data results knowledge code models doc entities/datasets -maxdepth 3 -type f`.
- `XDG_CACHE_HOME=/tmp/pais-snakemake-cache uv run --frozen --group pipeline snakemake -s code/workflows/Snakefile -n --use-conda`.
- `XDG_CACHE_HOME=/tmp/pais-snakemake-cache uv run --frozen --group pipeline snakemake -s code/workflows/Snakefile --lint`.
- `uv run --frozen science qa-audit --json`.

## Chain: `t035-gse14577-expression`

- **Axis 1 - Data QA:** WARN - raw parse substrate has a wired structural/distribution QA gate; clean base `expr.gene.tsv.gz` does not have its own separate QA checkpoint.
  - substrates with a wired-in QA step: raw parsed matrices yes; harmonized substrate partial (`harmonize.qa.pass`); clean base prepared matrix no
  - consumer-contract QA: WARN - `limma_de.R` fails early on obvious sheet/matrix mismatches, but there is no separate consumer-contract QA rule over the prepared matrix.
  - companion DAG-validation (output-ownership): PASS from dry-run buildability; no automated single-writer lint beyond Snakemake DAG construction.
  - process-iteration (`science qa-audit`): not assessable - `entities/workflow-runs` absent.
- **Axis 2 - Consistency/quality:** WARN - root Snakemake command exists and config is explicit; no explicit `qa_all` target; code-side task back-links are not in the sanctioned comment-block pattern.
- **Axis 3 - Portability/commons:** WARN - base is factored enough to reuse, but no formal clean-base dataset entity/datapackage points at the prepared gene matrix.

### Findings

| # | Axis | Finding | Severity | Disposition | Task |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | Prepared GSE14577 gene matrix has no separate clean-base QA checkpoint. | structural/distribution | backlog | t062 |
| 2 | 2 | Workflow has no explicit root QA target and code-side task back-links are incomplete. | quality | backlog | t063, t068 |
| 3 | 3 | Reusable GSE14577 clean base is not formalized as a commons-ready dataset entity. | portability | backlog/promote | t065 |

## Chain: `t035-gse130353-expression`

- **Axis 1 - Data QA:** WARN - raw substrate and near-zero filter have structural gates; final prepared matrix still lacks an independent clean-base QA checkpoint.
  - substrates with a wired-in QA step: raw sample sheet/contract yes; harmonized substrate partial (`harmonize.qa.pass`); near-zero filter yes; clean base prepared matrix no
  - consumer-contract QA: WARN - downstream limma/permutation scripts validate some sample/matrix contracts at runtime, but no separate QA rule records the clean-base contract.
  - companion DAG-validation (output-ownership): PASS from dry-run buildability; no automated single-writer lint beyond Snakemake DAG construction.
  - process-iteration (`science qa-audit`): not assessable - `entities/workflow-runs` absent.
- **Axis 2 - Consistency/quality:** PASS/WARN - config-driven near-zero procedure and fail-early behavior are strong; same missing QA target/back-link issue as the workflow overall.
- **Axis 3 - Portability/commons:** WARN - base is reusable and public but not promoted or described by a formal clean-base dataset entity.

### Findings

| # | Axis | Finding | Severity | Disposition | Task |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | Prepared GSE130353 gene matrix has no separate clean-base QA checkpoint. | structural/distribution | backlog | t062 |
| 2 | 3 | Reusable GSE130353 clean base is not formalized as a commons-ready dataset entity. | portability | backlog/promote | t065 |

## Chain: `t035-msigdb-genesets`

- **Axis 1 - Data QA:** WARN - GMT payloads are hash-verified and `prepare_genesets.R` asserts hashes, ID space, multimap policy, and size filters, but the prepared RDS/theme-map substrate has no separate QA checkpoint.
  - substrates with a wired-in QA step: raw GMT hashes yes; prepared gene-set universe no separate QA sentinel/report
  - consumer-contract QA: WARN - consumers expect one row per retained set and db/config vocabulary coverage; some checks occur in scripts, but no standalone QA surface records them.
  - companion DAG-validation (output-ownership): PASS from dry-run buildability.
  - process-iteration (`science qa-audit`): not assessable.
- **Axis 2 - Consistency/quality:** PASS/WARN - config is the single source for release, hashes, regexes, and size filters; no code-side task back-links.
- **Axis 3 - Portability/commons:** WARN - the prepared gene-set universe is reusable, but no formal dataset entity or commons-readiness record exists.

### Findings

| # | Axis | Finding | Severity | Disposition | Task |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | Prepared gene-set universe lacks a separate QA checkpoint over RDS/theme-map/release-hash outputs. | structural/distribution | backlog | t062 |
| 2 | 3 | Prepared mapped MSigDB universe is not described as a clean-base reusable substrate. | portability | backlog/promote | t065 |

## Chain: `t035-pathway-overlap-analysis`

- **Axis 1 - Data QA:** WARN - downstream scripts contain useful fail-fast checks and verdict mechanics tests exist, but project-specific analysis substrates/results do not have dedicated QA rules.
  - substrates with a wired-in QA step: DE/fgsea/concordance/permutation/rollup/result bundle no dedicated QA target
  - consumer-contract QA: WARN - `concordance.py`, `specificity.py`, `verdict.py`, and test fixtures check important contracts, but the workflow lacks a recorded QA report over the complete downstream surface.
  - companion DAG-validation (output-ownership): PASS for Snakemake dry-run after `XDG_CACHE_HOME=/tmp/...`; `--lint` returns one advisory on `rules/common.smk`.
  - process-iteration (`science qa-audit`): not assessable - no workflow-run entities.
- **Axis 2 - Consistency/quality:** WARN - command surface and default target exist; no explicit QA target; Snakemake lint reports `rules/common.smk` as "mixed rules and functions" even though it is the helper include; code back-links are incomplete.
- **Axis 3 - Portability/commons:** PASS/WARN - downstream outputs are correctly project-specific and should not be promoted as clean base data, but `results/` lacks a datapackage manifest.

### Findings

| # | Axis | Finding | Severity | Disposition | Task |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | Project-specific downstream substrates lack a dedicated QA/result-QA surface. | analysis-result-QA / consumer-contract | backlog | t063 |
| 2 | 1/2 | There is no explicit root-runnable QA target for the workflow. | quality / workflow-QA | backlog | t063 |
| 3 | 1 | `science qa-audit` cannot inspect t035 because no workflow-run entities exist. | process-QA | backlog | t066 |
| 4 | 2 | Snakemake `--lint` emits an advisory on `rules/common.smk`; current judgment is lint noise because the file is already the common helper include. | quality | leave | defer-no-task:false-positive-snakemake-lint-common-helper |
| 5 | 2 | Workflow scripts/rules have reverse links from plans but lack cheap code-side task comment back-links. | quality | backlog | t068 |
| 6 | 3 | `results/` lacks a datapackage/results manifest for output resources and provenance. | portability / manifest | backlog | t064 |

## Chain: `menopause-dag-adjustment-sets`

- **Axis 1 - Data QA:** WARN - the derivation script parses the authored patch and output is committed, but no wired freshness check verifies `adjustment_sets_v2.txt` still matches the patch.
  - substrates with a wired-in QA step: none; manual script output only
  - consumer-contract QA: WARN - downstream inquiry doc relies on the committed text result.
  - companion DAG-validation (output-ownership): not applicable; this is a standalone derivation script.
  - process-iteration (`science qa-audit`): not applicable.
- **Axis 2 - Consistency/quality:** PASS/WARN - script is simple, relative-path based, and uses networkx directly; output regeneration command is documented.
- **Axis 3 - Portability/commons:** PASS - not a reusable external data substrate.

### Findings

| # | Axis | Finding | Severity | Disposition | Task |
| --- | --- | --- | --- | --- | --- |
| 1 | 1/2 | Committed adjustment-set derivation can drift from the authored DAG patch. | consumer-contract / freshness | backlog | t067 |

## Chain: `science-knowledge-graph`

- **Axis 1 - Data QA:** PASS - graph build, graph validation, reference resolution, and health checks are already first-class project commands.
  - substrates with a wired-in QA step: `science graph build`, `science validate`, `science health`
  - consumer-contract QA: PASS - graph references and frontmatter cross-references are validated.
  - companion DAG-validation (output-ownership): not applicable.
  - process-iteration (`science qa-audit`): not applicable to the graph build itself.
- **Axis 2 - Consistency/quality:** PASS - root validation command is managed and project conventions are explicit.
- **Axis 3 - Portability/commons:** PASS - graph artifacts are project-native, not commons-promoted data substrates.

### Findings

| # | Axis | Finding | Severity | Disposition | Task |
| --- | --- | --- | --- | --- | --- |
| 1 | 1/2/3 | No new workflow-code finding. Existing validation warnings are tracked separately by `science health`. | n/a | leave | defer-no-task:not-a-workflow-refactor-finding |

