---
id: "proposition:0002-reproductive-stage-transition-modifies-immune-regulatory-pathways"
type: "proposition"
title: "Reproductive-stage transition modifies immune-regulatory pathways relevant to post-infectious recovery"
status: "active"
claim_layer: "mechanistic_narrative"
identification_strength: "analogical"
proxy_directness: "indirect"
supports_scope: "hypothesis_bundle"
measurement_model:
  observed_entity: "circulating sex-hormone and cytokine levels (e.g. testosterone, IL-6, TNF-α)"
  latent_construct: "immune-regulatory pathway state governing post-infectious recovery"
  measurement_relation: "analyte concentrations index, but do not equal, the multi-node regulatory-pathway balance the proposition is about"
  known_failure_modes:
    - "cross-sectional levels conflate cause and consequence of inflammation"
    - "single analytes are noisy proxies for multi-node pathway state"
discusses:
  - "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
related:
  - "hypothesis:0005-reproductive-stage-immune-homeostatic-margin"
  - "question:0013-reproductive-stage-failed-immune-recovery-after-infection"
  - "proposition:0001-reproductive-stage-transition-shifts-the-failed-recovery-threshold"
  - "immunity:topic:sex-hormone-life-stage-immune-homeostasis"
source_refs:
  - "paper:Averyanova2022"
  - "paper:Shahbaz2025"
created: "2026-06-21"
updated: "2026-06-21"
---

# Proposition: Reproductive-stage transition modifies immune-regulatory pathways relevant to post-infectious recovery

## Claim

Reproductive-stage transition modifies one or more immune-regulatory pathways governing post-infectious recovery — antiviral inflammation resolution, Treg/Tfh/Th17 balance, B-cell and type-I-IFN tone, endothelial activation, or thromboinflammatory state. This is the mechanistic narrative beneath `proposition:0001`: the candidate biological channel through which a reproductive-stage threshold shift would operate.

## Evidence Summary

`paper:Averyanova2022` provides indirect mechanistic plausibility for sex-hormone effects on immune, endothelial, and hemostatic pathways relevant to recovery. `paper:Shahbaz2025` reports testosterone **inversely correlated with inflammatory cytokines** (IL-6, TNF-α, IFN-γ, MCP-1, IL-17a, IP-10) in female long-COVID patients — a directional immune–hormone link consistent with an anti-inflammatory hormonal role.

## Caveats

Mechanistic plausibility, not a staged-mediation test. The cytokine correlation is cross-sectional and shares the reverse-causation ambiguity of `proposition:0003`. No in-vivo evidence yet shows that a stage-driven pathway change *causes* the recovery-threshold shift of `proposition:0001` rather than co-occurring with it. Held as a `mechanistic_narrative`-layer claim; the discriminating evidence is mediation analysis in a hormone-measured cohort.

**Single-line fragile — and it is a `core` member.** This proposition is one of the two `core` legs of the `hypothesis:0005` belief conjunction, yet its support rests on just two weak lines (`evidence-line:0006`, analogical; `evidence-line:0007`, cross-sectional): dropping either flips it supported → fragile (`belief.fragile-single-line`). The **core mechanism leg is thus the conjunction's weakest link** — the highest-priority target for independent corroboration (a hormone-measured, mediation-capable cohort). The t036 dataset-feasibility search (`report:0004`) found **no off-the-shelf vehicle** for this positive test — R1 hormone-panel depth and R5 pre-infection baseline are anti-correlated across the candidate cohorts — which *explains* this fragility rather than resolving it. The live corroboration paths are `task:t038` (IMPACC, mediator-compatible only, near-term) and `task:t040` (RECOVER ancillary biospecimen study, the eventual primary positive test, post-seed-stage).
