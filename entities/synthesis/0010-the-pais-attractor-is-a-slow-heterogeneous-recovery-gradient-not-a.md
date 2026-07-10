---
id: "synthesis:0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a"
kind: "synthesis"
title: "Synthesis: 0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a"
status: "active"
report_kind: "hypothesis-synthesis"
hypothesis: "hypothesis:0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a"
generated_at: "2026-07-10T18:59:35Z"
source_commit: "3fdeec933ba2432408611cc17a462bed7e105161"
created: "2026-07-10"
updated: "2026-07-10"
provenance_coverage: "thin"
---

## State

`hypothesis:0010-the-pais-attractor-is-a-slow-heterogeneous-recovery-gradient-not-a` proposes that
apparent PAIS "chronicity" at 3–12 months is not a genuine bistable attractor but a slow, heterogeneous
recovery gradient sampled too early. Under this framing, most patients are improving monotonically but
slowly, and the population constitutes a mixture of trajectory classes — rapid resolvers, slow improvers,
a small persistently-high stratum, and a late-worsening minority — rather than draws from a single
attractor basin. This is the structural dynamical null of `hypothesis:0001-shared-dysregulated-attractor`
(`http://example.org/project/hypothesis/0001-shared-dysregulated-attractor`), which itself carries
`evidential_fragility(contested)` status in the project graph.

No graph propositions or linked interpretations are registered for h0010; the claim rests at **proposed**
status. Supporting trajectory-mixture evidence (RECOVER-Adult class structure; 4-year UK post-COVID
cohort) is invoked in the hypothesis spec but not yet formalized as graph entities. Three inverse
questions define the discriminating tests: whether bistability fingerprints are detectable before
chronification (`question:0036-critical-slowing-down-fingerprints-as-pre-chronification-early-warning`),
whether re-entry thresholds after apparent recovery fall below the initial-onset threshold
(`question:0037-latent-homeostatic-fragility-after-pais-recovery-lower-re-entry`), and whether the
attractor model can be sharpened into gradient-separating, time-resolved predictions
(`question:0008-formalize-vicious-cycle-attractor-model`). A positive answer to any of these would
challenge the gradient account.

## Arc

Arc reconstruction is limited because no interpretations with `prior_interpretations` chains exist for
this hypothesis.

h0010 was generated on 2026-07-04 as a contrarian lens stress-testing `hypothesis:0001-shared-dysregulated-attractor`, seeded by the
`explore-ideas:claude-opus-4-8:cand-contrarian-pais-recovery-gradient` session. The generative rationale
cited RECOVER-Adult trajectory clustering and a 4-year UK post-COVID cohort as empirical anchors that are
hard to reconcile with a single stable attractor; those sources appear in the hypothesis spec but have not
been entered as formal interpretation or paper entities. No investigation arc — no interpretation chain,
no task history — exists beyond the initial framing. h0010 sits at proposed status, structurally
symmetric with `hypothesis:0001-shared-dysregulated-attractor`: both are dynamical claims the project cannot adjudicate without dense,
multi-year, within-person trajectory data.

## Research fronts

Three inverse questions constitute the live frontier for h0010. `question:0036-critical-slowing-down-fingerprints-as-pre-chronification-early-warning`
(PRIMARY) asks whether variance inflation and autocorrelation lengthening appear before chronification —
a positive finding would favor the attractor account over the gradient.
`question:0037-latent-homeostatic-fragility-after-pais-recovery-lower-re-entry` (PRIMARY) asks whether
recovered individuals re-enter illness at a lower trigger threshold, testing for hysteresis — the
signature of a retained basin rather than a one-way slope.
`question:0008-formalize-vicious-cycle-attractor-model` asks whether vicious-cycle dynamics can be
formalized into predictions that empirically separate bistability from gradient recovery.

No open tasks are registered in the bundle. The gaps_slice flags multiple PAIS hypotheses as
`evidential_fragility(contested)`, including
`http://example.org/project/hypothesis/0001-shared-dysregulated-attractor`, confirming that h0010's
primary competitor is itself unsettled — both dynamical interpretations remain live.
