---
id: search:0007-microbiome-gut-brain-pais
kind: search
title: "Literature search: microbiome, microbial metabolites, and gut-brain axis in PAIS (t007)"
status: active
created: "2026-06-25"
updated: "2026-06-25"
source_refs:
  - cite:Iqbal2025
  - cite:Liu2022
  - cite:Su2023
  - cite:Guo2023
  - cite:Xiong2023
  - cite:Lau2024
  - cite:Wong2023
  - cite:Che2025
  - cite:Walitt2024
related:
  - task:t007
  - proposition:0031-pais-gut-dysbiosis-scfa-depletion
  - interpretation:0023-t007-microbiome-gut-brain-axis
  - topic:gut-microbiome-barrier-axis
  - hypothesis:0001-shared-dysregulated-attractor
  - hypothesis:0002-tissue-reservoir-antigen-fragment
---
# Search: microbiome, microbial metabolites, and gut-brain axis in PAIS

## Search Focus

`task:t007` asked for gut dysbiosis, microbial metabolites, serotonin/tryptophan, and gut-brain signaling
in long COVID and ME/CFS. The actionable corpus is now long COVID + ME/CFS; post-Lyme, post-Q-fever,
post-dengue, and post-SARS microbiome data were not found at comparable maturity in this pass.

## Query Set

This pass combined local corpus review with web/PubMed/publisher checks for:

1. long-COVID fecal microbiome longitudinal studies;
2. ME/CFS stool metagenomics and SCFA/butyrate studies;
3. microbial metabolite and gut-barrier signals in ME/CFS/long COVID multi-omics;
4. serotonin/tryptophan/vagus gut-brain mechanisms;
5. microbiome-targeted long-COVID intervention trials.

## Search Verdict

**[+] Gut axis is real and recurring; [~] causality remains unresolved.**

The strongest recurring signal is not a specific pathogen taxon but a functional axis: depletion of
beneficial SCFA/butyrate-producing capacity and enrichment or persistence of dysbiotic/pathobiont
communities. It appears in long COVID (Liu2022/Su2023), ME/CFS (Guo2023/Xiong2023), and ME/CFS
multi-omics/gut-barrier metabolites (Che2025/Walitt2024 context). SIM01 provides a weak randomized
perturbation signal in long COVID. Wong2023 supplies a separate gut-brain mechanism through intestinal
tryptophan absorption, serotonin, and vagal signaling.

## Evidence Map

| Claim | Best anchors | Net |
|---|---|---|
| Long COVID retains dysbiosis after acute infection | Liu2022, Su2023 | Supported observationally; same CUHK program |
| ME/CFS has deficient butyrate/SCFA-producing capacity | Guo2023, Xiong2023 | Supported observationally; duration-dependent |
| Gut-barrier/metabolite abnormalities sit inside broader PAIS multi-omics | Che2025, Walitt2024, Shahbaz2025 | Compatible context, not isolated microbiome proof |
| Gut-brain mechanism can link intestinal inflammation to cognition | Wong2023 | Mechanistically strong but not microbiome-composition evidence |
| Microbiome modulation can improve PACS symptoms | Lau2024 | Weak positive RCT; objective function not clearly improved |

## Interpretation

The honest model is a loop node, not a single-cause model:

- acute infection can disrupt gut ecology and intestinal absorption/barrier function;
- dysbiosis/SCFA depletion can plausibly amplify immune and neuroendocrine signaling;
- gut-brain pathways can connect peripheral inflammation to cognition and autonomic symptoms;
- in established disease, the gut axis may become one of several reinforcing loops or may partially
  normalize while downstream metabolic/immune abnormalities persist.

## Recommended Graph Disposition

Mint one local proposition (`proposition:0031`) and three evidence lines. Do **not** make it a core member
of `hypothesis:0001` or `hypothesis:0002`, and do **not** let it directly promote either hypothesis. The
evidence supports recurrence and testability of a gut-axis loop, not the full shared-attractor or
pathogen-fragment-reservoir conjectures.

## Follow-up

The most useful next design is a same-cohort longitudinal study with stool metagenomics, fecal/plasma
SCFAs, gut-barrier/translocation markers, tryptophan/serotonin pathway metabolites, antibiotics/diet
metadata, and symptom recovery. The decisive contrast is improvers versus non-improvers over time, not
another cross-sectional case-control stool profile.
