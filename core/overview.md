<!--
core/overview.md — curated project orientation, loaded at session start.

Length cap: ~150 lines including this comment. If you exceed it, something
belongs in doc/ instead. The point of this file is to be the smallest thing
a fresh collaborator (human or agent) can read to be useful in five minutes.

Keep it durable. Avoid:
- duplicating science.yaml or README.md (those are loaded separately)
- pasting recent /science:status output (that's regenerated each session)
- play-by-play history (use git log + doc/meta/ for that)

Include only the judgment calls and context that machine-readable manifests
cannot capture.
-->

# Project Overview

## What this project is

`health-post-acute-infection` is a process project for **post-acute infection syndromes (PAIS)** in the `~/d/health/` family. It studies long COVID, ME/CFS, post-treatment Lyme disease syndrome (PTLDS), post-dengue and post-Q-fever fatigue, post-SARS syndrome, "long flu", and post-sepsis (PICS) as instances of failed return to homeostasis after acute infection.

## Why it exists

Post-acute infection syndromes are clinically enormous (long COVID alone affects tens of millions), mechanistically rich, and historically fragmented into pathogen-specific silos that rarely talk to each other. The COVID-19 pandemic produced an unprecedented, well-characterized cohort of post-infectious illness and revived interest in ME/CFS, post-Lyme, and other post-infectious syndromes that share strikingly similar phenotypes. Treating them together — as a shared homeostatic-recovery failure mode — is the bet of this project, and it is a high-value test case for the health-meta frame of health as multiscale homeostasis.

## Boundary with health-immunity

This project was split out from `health-immunity` so that immunity can own **general immune-mechanism/autoimmunity/tolerance biology** while PAIS owns the **clinical post-infectious syndromes** and their pathophysiology. Papers that bridge both (immune profiling *of* long COVID, autoimmunity *after* infection, trained immunity, EBV-driven autoimmunity) are summarized in one home and shared via `science commons promote`.

## Current state

- Scaffolded on 2026-06-10 to house a long-COVID / ME/CFS / post-infectious-fatigue literature batch (~60 papers) being triaged from a larger download set.
- Seed state: paper summaries are being added; topics, hypotheses, and datasets are not yet established.
- Immediate need: summarize the seed batch, then synthesize cross-cutting topics (antigen/pathogen persistence, persistent immune activation, infection-triggered autoimmunity, dysautonomia, the cross-pathogen "shared PAIS" question) and seed hypotheses.

## Open fronts

- Long COVID: mechanisms, antigen persistence, organ-specific sequelae (pulmonary, cardiovascular, neuro, rheumatic, GI), subphenotyping, epidemiology and long-term outcomes, therapeutics.
- ME/CFS: viral origin, immune/proteomic signatures, and its overlap with long COVID.
- Non-COVID post-infectious syndromes: PTLDS, post-dengue, post-Q-fever, post-SARS — what generalizes across triggers.
- Cross-syndrome synthesis: is there a shared PAIS failure mode, and what distinguishes the syndromes?

## Domain context an outsider would miss

- Case definitions vary widely (WHO vs CDC long COVID; Fukuda/CCC/ICC for ME/CFS); apparent prevalence/mechanism differences often reflect definitions and cohorts, not biology. Always note the case definition.
- "Post-infectious" attribution is frequently presumptive; many cohorts lack confirmed infection, controls, or pre-infection baselines. Controlled longitudinal designs are the gold standard and are rarer than cross-sectional associations.
- Mechanistic claims (antigen persistence, microclots, autoimmunity, viral reactivation) sit at different evidence-maturity levels and some are contested; do not collapse them into one unifying mechanism.
- Phenotypes are highly covariate-sensitive (acute severity, age, sex, time-since-infection, prior immunity); ignore these and treatment/disease signals may be confounded.

## Pointers

- Research question: `entities/research-question.md`
- Active tasks: `tasks/active.md`
- Decisions log: `core/decisions.md`
- Scope boundaries: `specs/scope-boundaries.md`
