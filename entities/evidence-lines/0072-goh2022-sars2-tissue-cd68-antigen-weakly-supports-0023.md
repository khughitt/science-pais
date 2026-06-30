---
id: evidence-line:0072-goh2022-sars2-tissue-cd68-antigen-weakly-supports-0023
type: evidence-line
title: Goh2022 long-COVID tissue case report detects SARS-CoV-2 antigen/RNA with CD68 co-localization — weak partial support for cross-pathogen tissue/macrophage reservoir
status: active
stance: supports
target: proposition:0023-cross-pathogen-tissue-macrophage-reservoir-generalization
source: paper:Goh2022
strength: weak
independence: independent
independence_group: goh2022-long-covid-tissue-antigen-cd68
evidence_role: direct_test
evidence_type: literature_evidence
identification_strength: observational
related:
- proposition:0023-cross-pathogen-tissue-macrophage-reservoir-generalization
- hypothesis:0002-tissue-reservoir-antigen-fragment
- proposition:0022-degradation-resistant-fragments-persist-and-are-bioactive
- question:0002-antigen-clearance-rescues-symptoms
- task:t053
source_refs:
- paper:Goh2022
created: '2026-06-25'
updated: '2026-06-25'
---
# Evidence Line: Goh2022 detects SARS-CoV-2 antigen/RNA in long-COVID tissues with CD68 co-localization

## What this line shows

Goh2022 reports two long-COVID patients whose tissue samples contained residual SARS-CoV-2 nucleocapsid
protein and viral RNA **163 and 426 days** after symptom onset. Multiplex immunohistochemistry detected
nucleocapsid protein in appendix, skin, and breast tissue, and the nucleocapsid signal co-localized with
the macrophage marker **CD68**. Both patients had negative nasopharyngeal PCR at sampling [@Goh2022].

This is a direct, human, non-Borrelia tissue result and therefore weakly supports the tissue/macrophage
part of `proposition:0023`: the fragment-reservoir architecture is not confined to the McClune2025
Borrelia mouse-liver model.

## Why it is independent

`independent` under `independence_group: goh2022-long-covid-tissue-antigen-cd68`. It uses a different
pathogen class (SARS-CoV-2), species/context (human long COVID), tissue set, and assay platform from
McClune2025's Borrelia pPG mouse-liver reservoir line.

## Caveats / scope

`direct_test`, **weak** and only **partial** support. The line demonstrates tissue antigen/RNA and CD68
co-localization, but it does not show degradation-resistant chemistry, a tissue-resident macrophage
clearance defect, a host proteome/metabolic signature overlapping McClune2025, prevalence in a controlled
cohort, or prospective symptom linkage. It lifts `proposition:0023` from wholly unobserved to weakly
observed in SARS-CoV-2 tissue, but it does **not** promote h0002 because `proposition:0024` remains
unsupported and now has an acute-load model-criticism line.
