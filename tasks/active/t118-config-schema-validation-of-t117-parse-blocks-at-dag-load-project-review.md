---
id: t118
project: ''
title: 'Config-schema validation of t117 parse: blocks at DAG-load (project-review
  #2)'
type: ''
aspects: []
priority: P2
status: proposed
blocked_by: []
related: []
parent: ''
group: ''
artifacts: []
findings: []
created: '2026-07-08'
completed: null
---

The per-deposit config.parse[acc] block has become the de-facto program for stage_matrix (member_glob, positional col indices, level_map, ordered group_regex rules, covariate specs, metadata_format). Today a typo'd knob name silently defaults or is ignored — a fail-early violation. Add a schema (jsonschema or pydantic) validating each deposit's parse block (+ its group_source shape and de_models covariate coupling) BEFORE Snakemake builds the DAG (or at stage_matrix entry), so a malformed contract HALTs at load with a precise per-deposit message instead of silently mis-parsing. Do this before the a-rest deposit count climbs (gse226260/gse267625/gse228320). Surfaced in the 2026-07-08 project self-review alongside #1 (arm-partition guard, DONE) and #3 (QA reconciliation, DONE). Plan: entities/plans/0010-crosspais-pathway-response-rank-estimation.md.
