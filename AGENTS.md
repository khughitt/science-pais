# health-post-acute-infection - Agent Guide

## What this is

Process-focused research project for **post-acute infection syndromes (PAIS)** in the `~/d/health/` family. It studies long COVID, myalgic encephalomyelitis/chronic fatigue syndrome (ME/CFS), post-treatment Lyme disease syndrome (PTLDS), post-dengue and post-Q-fever fatigue, post-SARS syndrome, "long flu", post-sepsis (PICS), and related conditions as **failed recovery of immune and physiological homeostasis after acute infection**. The working frame treats these syndromes as a shared failure mode with recurring candidate mechanisms — persistent immune activation/exhaustion, antigen or pathogen-fragment persistence, autoimmunity and autoantibodies, viral reactivation (e.g. EBV), thromboinflammation and endothelial dysfunction, dysautonomia/small-fiber neuropathy, mast-cell activation, gut-microbiome dysbiosis, and metabolic/mitochondrial dysfunction. Seeded from a long-COVID / ME/CFS / post-infectious-fatigue literature batch; hypotheses are provisional.

## Profile

`research`, scoped to literature synthesis and future computational analyses of post-acute infection syndromes. No installable package; tooling is project-local.

## Validation

```bash
uv run --frozen science validate --verbose
```

## Conventions

- This project is a `process`-role owner for post-acute infection syndromes in the `~/d/health/` family. **Immune-mechanism** inquiry that is not specific to the post-infectious context belongs in `health-immunity` (`~/d/health/processes/immunity`); cross-project synthesis belongs in `health-meta` (`~/d/health/meta`); disease-label comparison belongs in `pan-disease` (`~/d/health/comparisons/pan-disease`).
- Boundary with `health-immunity`: autoimmunity, tolerance, and immune-homeostasis **mechanisms in general** live in immunity. PAIS houses the **clinical syndromes** and their post-infectious pathophysiology. Papers that bridge both (e.g. immune profiling *of* long COVID, autoimmunity *after* COVID) are summarized in one home and shared via the commons mechanism (`science commons promote`).
- Keep durable literature summaries as paper entities under `entities/papers/` and topic syntheses under `entities/topics/` (layout v3).
- Use `~/d/` paths in documentation, not `/home/keith/d/` or `/mnt/ssd/Dropbox/` paths.
- PAIS causality and mechanism claims are scientifically contested and rapidly evolving; represent claimed mechanisms precisely and do not overstate causation. Distinguish anecdotal reports, case series, mechanistic hypotheses, and controlled epidemiological/longitudinal evidence.
- Post-infectious phenotypes are highly heterogeneous and sensitive to acute-illness severity, age, sex, time-since-infection, prior infection/vaccination history, and case definition; record or model these covariates whenever possible, and state the case definition used.
- Persistent computational outputs belong under `results/`; large raw or processed data payloads stay gitignored under `data/`.

## Task execution

- Tasks live in `tasks/active.md`, managed by `science tasks` (or the `/science:tasks` slash command). Completed/retired tasks archive to `tasks/done/YYYY-MM.md`.
- **Do not use Claude Code's built-in `TaskCreate` / `TaskUpdate` / `TaskList` tools.** They create a parallel task store outside the repo, invisible to other agents and to fresh clones, and they fight the science task system. Use `science tasks` exclusively for task management on this project.
- Common invocations (run from the project root):

  ```bash
  uv run science tasks list
  uv run science tasks add "TITLE" --priority P2 --description "..."
  uv run science tasks done <task_id> --note "..."
  ```

## Known issues / nuances

- PAIS case definitions vary widely (e.g. WHO vs CDC long-COVID definitions; Fukuda vs CCC vs ICC for ME/CFS); apparent prevalence and mechanism differences across studies often reflect definitional and cohort differences rather than biology. Flag the case definition.
- "Post-infectious" attribution is often presumptive; many cohorts lack confirmed acute infection, controls, or pre-infection baselines. Distinguish controlled longitudinal designs from cross-sectional or self-reported associations.
- Mechanistic claims (antigen persistence, autoimmunity, viral reactivation, microclots) are at varying evidence maturity and sometimes contested; hold them at their evidence level and avoid presenting a single unifying mechanism as established.
- Post-infectious phenotypes are highly covariate-sensitive (severity, age, sex, timing, prior immunity); designs that do not account for these should be flagged.

<!-- BEGIN: load-bearing-constraints (managed by /science:curate; edit core/decisions.md instead) -->
## Load-bearing constraints

<!-- One bullet per active decision in core/decisions.md, phrased as an
imperative rule. The "why" stays in core/decisions.md. -->

- _none yet - populated by `/science:curate` once `core/decisions.md` has entries._

<!-- END: load-bearing-constraints -->

## Pointers

- Decisions: `core/decisions.md`
- Project overview: `core/overview.md`
- Active tasks: `tasks/active.md`
- Research question: `specs/research-question.md`
- Scope boundaries: `specs/scope-boundaries.md`
- Hypotheses: `specs/hypotheses/`
- Research plan: `RESEARCH_PLAN.md`
