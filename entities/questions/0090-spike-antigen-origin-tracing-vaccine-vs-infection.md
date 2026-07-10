---
id: question:0090-spike-antigen-origin-tracing-vaccine-vs-infection
kind: question
title: Can vaccine-derived vs infection-derived spike protein persistence be distinguished
  in PAIS biobank samples?
status: active
ontology_terms: []
datasets: []
source_refs:
- cite:Mead2025
related:
- hypothesis:0002-tissue-reservoir-antigen-fragment
- question:0088-vaccination-history-as-pais-effect-modifier
created: '2026-07-10'
updated: '2026-07-10'
---

# Can vaccine-derived vs infection-derived spike protein persistence be distinguished in PAIS biobank samples?

## Summary

When spike protein or mRNA-derived fragments are detected in PAIS patient samples (plasma, tissue), can the source be attributed to natural infection versus prior mRNA vaccination? The antigen persistence hypothesis (h0002) currently frames persistent antigen as infection-derived. In a post-2021 population where the majority of individuals received mRNA vaccines before or concurrent with infection, attributing detected spike to one source is analytically non-trivial. Mead2025 argues vaccine-derived spike dominates; the project's h0002 does not distinguish. Raised by cite:Mead2025 as a methodological gap with implications for mechanistic attribution. Related to question:0088.

## Why It Matters

- If vaccine-derived spike contributes substantially to the persistent antigen burden measured in PAIS samples, then h0002 (tissue-reservoir antigen-fragment as infection-derived initiator) requires modification to account for vaccine-origin antigen.
- PAIS treatment implications differ: if vaccine-derived antigen drives persistence, clearing it requires a different approach than clearing infection-derived fragments.
- Affects experimental design: PAIS antigen-detection studies should stratify by vaccination history and, where possible, use variant-specific sequencing or mass spectrometry to attribute spike origin.
- Risk if unanswered: antigen persistence evidence cited for h0002 may be partially confounded by vaccination-derived signal, weakening or misattributing the mechanistic claim.

## Current Evidence

- **Supporting distinguishability:** Vaccine-derived spike encodes the ancestral (Wuhan-Hu-1) sequence with two proline stabilization mutations (K986P, V987P); infection-derived spike varies by variant. Mass spectrometry or variant-specific PCR on spike fragments could theoretically distinguish these in clinical samples — but this has not been routinely done in PAIS biobank studies.
- **Complicating:** Most commercially available spike-antibody assays detect S1 or S2 without variant specificity. Booster vaccines track variant sequences (bivalent/XBB formulations), reducing distinguishability over time.
- **Current practice:** Existing PAIS antigen-persistence studies (Peluso et al., McClune et al., cited in h0002) generally do not report vaccination-specific spike tracing; they measure total spike or spike antibody burden.
- **Mead2025 claim:** Vaccine-derived spike may persist for 2–3 years; infection-derived spike clears faster. This claim is unverified at the timescales asserted and based on extreme-outlier case reports.

## Thoughts

- Best current interpretation: Distinguishing vaccine- from infection-derived spike is technically feasible via variant-specific sequencing or LC-MS/MS peptide tracing, but has not been applied systematically in PAIS cohorts. The question is worth raising with biobank custodians as a re-analysis priority.
- Major uncertainty: Whether the technical distinguishability survives proteolytic degradation of antigen fragments in tissue or plasma over months to years; whether the proline-stabilized ancestral sequence produces functionally distinct immunological signals compared to variant spike.
- Mead2025 should not be taken as establishing the persistence timescale claim; the question is raised independently of that paper's conclusions.

## Connections to Project

- Related hypotheses: hypothesis:0002-tissue-reservoir-antigen-fragment (primary connection), hypothesis:0001-shared-dysregulated-attractor (affects trigger characterization)
- Required data or analyses: Variant-specific spike tracing in PAIS biobank (Peluso/McClune cohorts); LC-MS/MS peptide identification of vaccine vs infection spike; vaccination history metadata.
- Priority level: Low-to-medium — analytically important for h0002 mechanistic precision but requires specialized proteomics; does not block current cross-trigger analyses.

## Related

- Topic notes: topic:antigen-pathogen-persistence
- Article notes: paper:Mead2025 (source); cite:Peluso2024 and cite:McClune2025 (antigen persistence evidence in h0002)
- Methods/Datasets: Variant-specific spike mass spectrometry; PAIS biobanks with vaccination-history metadata
