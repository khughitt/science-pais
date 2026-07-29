---
id: t145
project: ''
title: Correct the two overstated non-COVID trigger cells in search:0002 / discussion:0002
  and add a comparator-provenance column
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
created: '2026-07-26'
completed: null
---

From t130 (2026-07-26). Reading the four stub papers in full showed two matrix cells overstate their evidence. (1) Post-Ebola: search:0002 line 106/148 records a 'metabolomic signature (Sanford2026)' graded Thin-but-present, but the PES-vs-uninfected-household-contact contrast was NULL - the 34-metabolite signal is survivor-internal (PES n=37 vs asymptomatic EVD survivors n=20). (2) Post-EBV cytokine: the cell reads 'supported - post-EBV cytokine networks (Broderick2012)', but the cytokine comparison is n=9 vs n=12 with the 5-cytokine classifier trained AND evaluated on the same 21 samples, no external validation, and standing tension with the Dubbo negative (Vollmer-Conna 2007) - note Galbraith2011 is already recorded as a head-to-head NEGATIVE spanning EBV. Structural fix: the matrix grades cells by whether a signature EXISTS but has no column for what it was contrasted AGAINST. question:0001 asks for a signature simultaneously shared across triggers AND specific to failed-recovery-vs-full-recovery; a survivor-internal contrast addresses only the second conjunct. Add an explicit 'contrasted against' column so this is visible without re-reading. See paper:synthesis-2026-07-26-non-covid-trigger-legs Findings 1-2.

### Notes

- 2026-07-26: SCOPE EXTENDED 2026-07-26 (user review of t130). Three changes to this task. (A) NEW - stale Galbraith2011 contradiction, treat as the highest-value fix here: search:0002 still describes Galbraith2011 as partial/shared in several places (line ~94 'mixed - shared IFN-class transcripts across EBV/RRV/Q-fever'; line ~111 listing it among genuinely head-to-head cells; line ~124 'EVIDENCE of convergence (head-to-head): Galbraith2011 (partial - some shared transcripts across 3 triggers)'), while discussion:0002 (line ~265), question:0001, AND hypothesis:0001's evidence-bar paragraph all correctly record it as a head-to-head NEGATIVE with no genes consistent across all three triggers. The same entity thus both supports and refutes convergence depending on which file you read. Reconcile in favour of the negative reading. (B) DESIGN CHANGE - do NOT add a single 'contrasted against' column as originally proposed. Build a companion study-level PROVENANCE LEDGER instead, with columns: phenotype / case definition, comparator, assay, analytic N, validation type, design provenance (head-to-head vs assembled). These dimensions vary independently per cell, so one column cannot carry them. (C) CORRECTION to this task's original description - the Broderick2012 issue is NOT a comparator problem. Recovered same-trigger controls are the CORRECT comparator for question:0001's failed-vs-full-recovery conjunct and must not be scored as a deficiency; Broderick2012's actual weaknesses are analytic n=9 vs n=12, a resubstitution classifier (trained and evaluated on the same 21 samples), no external validation, and possible sex confounding (all 9 PI-CFS cases female, control sex composition unstated). Sanford2026 is the genuine comparator case: healthy household contacts WERE enrolled and tested, and the signature did not survive that contrast. Ledger entries must preserve this distinction. Now governed by D-010.
