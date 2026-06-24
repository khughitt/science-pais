---
id: "synthesis:emergent-threads"
type: synthesis
title: "Emergent threads - health-post-acute-infection"
report_kind: "emergent-threads"
generated_at: "2026-06-24T03:28:17Z"
source_commit: "eb1a5ca60ed1cd69451e2a3d9d6fa16da31fbfec"
orphan_question_count: 2
orphan_interpretation_count: 0
orphan_ids:
  - question:0004-convergent-small-fiber-neuropathy-substrate
  - question:0005-latent-to-overt-autoimmunity-conversion
---

## Cross-hypothesis questions

Three questions show cross-hypothesis reach at confidence `inverse` or `direct`.

**question:0011-mitochondrial-basis-of-pem** resolves primarily to `hypothesis:0006-skeletal-muscle-ischemic-mitochondrial-pem` and carries a back-inverse link to `hypothesis:0001-shared-dysregulated-attractor`. This is interesting because it sits at the seam between a focal muscle-ischemia account (h0006) and the project's umbrella shared-attractor account (h0001): depending on what the mitochondrial evidence actually shows, it either confirms the shared-attractor framing or partitions PEM into a mechanistically distinct subphenotype.

**question:0007-mechanism-of-female-predominance-in-pais** resolves primarily to `hypothesis:0005-reproductive-stage-immune-homeostatic-margin` and transitively reaches `hypothesis:0004-acute-severity-threshold`. The cross-cutting nature reflects that the overall female excess in PAIS cannot be explained by reproductive-stage biology alone; the male-biased reversal on vascular hard endpoints (captured in `interpretation:0005-t042-vascular-male-reversal-survives-severity-adjustment`) forces a severity-threshold account (h0004) into the same explanatory space as the sex-hormone account (h0005).

**question:0019-male-biased-vascular-signal-pasc-persistence** resolves primarily to `hypothesis:0004-acute-severity-threshold` and also reaches `hypothesis:0005-reproductive-stage-immune-homeostatic-margin`. It is interesting precisely because it connects the severity-threshold frame (is the male vascular excess a residual of greater acute illness burden?) to the reproductive-stage frame (or does it reflect a genuinely sex-differentiated vascular biology independent of severity?); `interpretation:0005` documents that the male reversal survives coarse severity restriction, making this a live bridge between h0004 and h0005.

---

## Orphan questions

Total: **2**

**question:0004-convergent-small-fiber-neuropathy-substrate** — asks whether PTLDS, long COVID, and ME/CFS share a non-length-dependent autonomic small-fiber neuropathy (SFN) substrate distinguishing them from primary dysautonomia; the question's own notes link it informally to `hypothesis:0001-shared-dysregulated-attractor`, but no formal primary-hypothesis assignment was made by the resolver, leaving it unhoused. The core gap is the absence of any cross-syndrome study using a standardized skin-biopsy protocol with primary-dysautonomia controls.

**question:0005-latent-to-overt-autoimmunity-conversion** — asks what fraction of post-infectious latent autoimmunity converts to overt autoimmune disease over a 5–10 year horizon and which autoantibodies mark the highest-risk subset; it too references h0001 informally (autoimmune limb), but the conversion-rate question extends beyond the attractor-state frame and is unresolved by any existing hypothesis. The core gap is that no existing PAIS cohort has long enough follow-up to measure conversion rates.

---

## Orphan interpretations

Total: **0**

All eight active interpretations (`interpretation:0001` through `interpretation:0008`) carry at least one direct `hypothesis:` entry in their `related:` field. No orphan interpretations exist in this run.

---

## Candidate hypotheses

Two recurring topics across the orphan questions suggest candidate hypotheses worth considering.

**Peripheral-autonomic neuropathy as PAIS substrate.** Both orphan questions touch the dysautonomia domain indirectly: `question:0004` is explicitly about SFN as the shared structural cause of PAIS dysautonomia. No current hypothesis addresses the *peripheral structural lesion* level (as distinct from the immune-attractor or severity-threshold levels). A candidate hypothesis might be: "A non-length-dependent autoimmune SFN targeting dorsal root ganglia is the shared peripheral substrate for autonomic symptoms across PAIS triggers, and is mechanistically distinct from mast-cell-mediated and central dysautonomia subtypes."

**Post-infectious immune-set-point shift and long-term autoimmune conversion.** `question:0005` concerns the durability of immune reprogramming after acute infection — a question that sits between the existing attractor-state hypothesis (h0001) and the severity-threshold hypothesis (h0004) but is fully addressed by neither. A candidate hypothesis might be: "Post-infectious latent autoimmunity represents a durable shift in immune set-point in a minority subset, with anti-cytokine autoantibody specificity predicting clinical conversion over a multi-year horizon."

These are inferred from two orphan questions apiece — a modest signal. Formal promotion to hypothesis should wait for additional evidence.
