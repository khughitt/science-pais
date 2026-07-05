---
id: proposition:0031-pais-gut-dysbiosis-scfa-depletion
kind: proposition
title: Gut dysbiosis with depleted SCFA/butyrate-producing capacity recurs across long COVID and ME/CFS, but remains mostly associative
status: active
claim_layer: empirical_regularity
identification_strength: observational
proxy_directness: direct
supports_scope: local_proposition
related:
  - hypothesis:0001-shared-dysregulated-attractor
  - hypothesis:0002-tissue-reservoir-antigen-fragment
  - topic:gut-microbiome-barrier-axis
  - topic:mecfs-long-covid-convergence
  - topic:shared-failure-mode-across-pais
  - interpretation:0023-t007-microbiome-gut-brain-axis
  - evidence-line:0078-liu-su-longcovid-persistent-dysbiosis-supports-0031
  - evidence-line:0079-guo-xiong-mecfs-butyrate-deficit-supports-0031
  - evidence-line:0080-lau2024-sim01-synbiotic-weakly-supports-0031
  - task:t007
source_refs:
  - paper:Liu2022
  - paper:Guo2023
  - paper:Lau2024
created: '2026-06-25'
updated: '2026-06-25'
---
# Proposition: Gut dysbiosis with depleted SCFA/butyrate-producing capacity recurs across long COVID and ME/CFS

## Claim

Long COVID and ME/CFS both show a recurring gut-axis signature: altered gut microbial community structure,
depletion of beneficial SCFA/butyrate-producing taxa or functional capacity, and associations with fatigue,
neurocognitive symptoms, or chronic case status. The claim is an **empirical regularity**, not a causal
claim that dysbiosis is sufficient to maintain PAIS.

This proposition is deliberately `supports_scope: local_proposition`. It is relevant to
`hypothesis:0001` as a plausible loop node and to `hypothesis:0002` as a possible gut-reservoir/barrier
interface, but it should not directly promote either hypothesis. The evidence supports "gut axis recurs
and is modifiable enough to be worth testing," not "microbiome dysbiosis is the reason the shared PAIS
state persists."

## Evidence Summary

- **Long COVID longitudinal leg:** Liu2022 followed 106 COVID-19 patients to 6 months with 258 serial
  shotgun-metagenomic stool samples and 68 non-COVID controls. PACS cases retained dysbiosis; non-PACS
  cases normalized toward controls. Su2023 extends the CUHK finding to roughly 1 year. This supports
  persistence but is not independent of the same research program and remains observational.
- **ME/CFS butyrate leg:** Guo2023 (106 ME/CFS, 91 controls) found reduced *Faecalibacterium prausnitzii*
  and *Eubacterium rectale*, confirmed deficient butyrate-producing capacity by functional metagenomics,
  qPCR, and fecal SCFA metabolomics, and linked *F. prausnitzii* inversely to fatigue severity. Xiong2023
  independently shows reduced microbial butyrate biosynthesis and lower plasma butyrate/bile-acid/benzoate
  signals, but also shows microbial dysbiosis is strongest in short-term ME/CFS and can partly normalize
  in long-duration disease while clinical/metabolic disease persists.
- **Interventional hint:** Lau2024 randomized 463 PACS patients to SIM01 versus placebo for 6 months.
  SIM01 improved several symptoms and shifted microbiome composition, but the product is broad and
  objective functional endpoints did not clearly improve.

## Caveats

The main confounds are diet, antibiotics, acute severity, hospitalization, geography, IBS/GI comorbidity,
illness-duration effects, and reduced activity. Stool composition is also an indirect readout of tissue
barrier function, gut immune tone, and microbial metabolites. Xiong2023 is the most important internal
constraint: persistent symptoms and metabolic abnormalities can outlast overt microbial-composition
dysbiosis, so a simple "fix the microbiome and the chronic state resolves" model is too strong.

## Measurement Model

Direct measures include stool shotgun metagenomics, fecal SCFA metabolomics, functional gene/qPCR assays
for butyrate-producing capacity, and microbiome response to synbiotic modification. Related readouts
include intestinal-barrier proteins, microbial-translocation markers, tryptophan/serotonin metabolism,
and vagal/neurocognitive endpoints. Future confirmatory studies should measure these in the same
participants and distinguish baseline susceptibility, acute-infection injury, chronic-state maintenance,
and recovery.
