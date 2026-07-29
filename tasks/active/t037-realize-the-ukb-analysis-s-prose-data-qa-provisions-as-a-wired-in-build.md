---
id: t037
project: ''
title: Realize the UKB analysis's prose data-QA provisions as a wired-in, build-fatal
  QA checkpoint when implemented
type: ''
aspects: []
priority: P2
status: proposed
blocked_by:
- task:t028
related:
- pre-registration:0001-menopause-pais-total-effect
- hypothesis:0005-reproductive-stage-immune-homeostatic-margin
parent: ''
group: causal-disentanglement
artifacts: []
findings: []
created: '2026-06-20'
completed: null
---

AXIS-1 FORWARD GAP from the 2026-06-20 pipeline-QA audit. The pre-registered UKB menopause->PAIS analysis specifies rich data-QA only in PROSE (sampling-frame/natal-female audit; exposure-timing repeat-assessment validation; dual outcome-route A/B triangulation; U-proxy missingness thresholds >50%; the 3x3 misclassification matrix; oestradiol floor-censoring sentinel at 175 pmol/L). Per ~/d/science/docs/conventions/pipeline-qa-checkpoints.md, prose intentions and side-output counts files do NOT discharge axis-1 QA. When t028 builds the analysis table, add a SEPARATE rule that re-reads the built table with STRUCTURAL (build-fatal: one-row-per-participant; natal-female filter integrity; allowed reproductive-stage codes; outcome-route key alignment) vs DISTRIBUTION (age-at-menopause bounds; 175 pmol/L oestradiol sentinel; missingness) checks, config-driven thresholds shared with the cleaning step. This task exists so the prose QA spec survives into code.
