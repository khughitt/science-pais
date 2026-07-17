---
id: "synthesis:0019-cgas-sting-nlrp3-sterile-innate-sensing-driver"
kind: "synthesis"
title: "Synthesis: 0019-cgas-sting-nlrp3-sterile-innate-sensing-driver"
status: "active"
report_kind: "hypothesis-synthesis"
hypothesis: "hypothesis:0019-cgas-sting-nlrp3-sterile-innate-sensing-driver"
generated_at: "2026-07-17T10:26:49Z"
source_commit: "f6365a35a9baa2b2d02bb68e5ed53199312617bf"
created: "2026-07-17"
updated: "2026-07-17"
provenance_coverage: "thin"
---

## State

This is a draft hypothesis entered 2026-07-10 with thin provenance: no recorded interpretations, graph propositions, or edge files have been deposited. Its core claim is that the persistent type-I IFN and IL-1β/IL-18 signatures documented in PAIS are sustained by sterile cytosolic nucleic-acid sensing — cGAS-STING and NLRP3 inflammasome — operating without ongoing viral replication, positioned upstream of the exhaustion and maintenance outputs tracked in `hypothesis:0003-immune-exhaustion-feedback` and `hypothesis:0001-shared-dysregulated-attractor`.

The strongest observational grounding in the bundle is `paper:Vacharathit2025`, which reports persistent IP-10/CXCL10 elevation 6–8 months post-Omicron breakthrough infection in a vaccinated cohort with no evidence of ongoing viral replication. IP-10/CXCL10 is induced downstream of TBK1/IRF3 — the signaling arm cGAS-STING activates — making its persistence consistent with sterile innate sensing (`question:0076-ip10-cxcl10-omicron-persistence-antigen-vs-sterile`). However, `paper:Vacharathit2025` does not measure cGAMP, phospho-TBK1, or any direct activation marker; the sterile-sensing mechanism remains inferred, not demonstrated.

No PAIS cohort has directly measured persistent, replication-dissociated cGAS-STING or NLRP3 activation. The mechanistic grounding in the hypothesis spec draws from acute and non-PAIS models only. `question:0023-cgas-sting-cytosolic-dna-sensing-as-upstream-driver-of-persistent-type-i` and `question:0024-nlrp3-inflammasome-and-gasdermin-d-pyroptosis-as-a-self-amplifying-il-1` — the two mechanism questions this hypothesis homes — remain fully open, and the driver-vs-downstream relationship relative to any myeloid reprogramming in PAIS is unresolved.

## Arc

Arc reconstruction is limited because this hypothesis carries no recorded interpretations with `prior_interpretations` chains.

The hypothesis was introduced in the 2026-07-10 long-COVID paper intake (`paper:synthesis-2026-07-10-long-covid-intake`), framing cGAS-STING and NLRP3 as candidate upstream sterile sensing drivers of PAIS maintenance. Its `related:` links home two orphan mechanism questions (`question:0023-cgas-sting-cytosolic-dna-sensing-as-upstream-driver-of-persistent-type-i`; `question:0024-nlrp3-inflammasome-and-gasdermin-d-pyroptosis-as-a-self-amplifying-il-1`) and position the frame as a candidate cross-trigger node beneath `hypothesis:0001-shared-dysregulated-attractor`. The hypothesis spec records one prior disputing result: a sensor-locus chromatin-imprint sub-idea — postulating that cGAS/STING/NLRP3 loci carry durable activating marks after infection — was sought and not found in the primary epigenomic literature, and that branch has been severed from the frame. No investigative moves beyond this genesis are recorded.

## Research fronts

The two primary open mechanism questions are `question:0023-cgas-sting-cytosolic-dna-sensing-as-upstream-driver-of-persistent-type-i` and `question:0024-nlrp3-inflammasome-and-gasdermin-d-pyroptosis-as-a-self-amplifying-il-1`, both carrying inverse confidence in the bundle, indicating the current evidence does not resolve them. The adjacent driver-vs-marker gap for the IFN-I and IL-6 axis is tracked by `question:0006-jak-stat-il6-driver-vs-marker`.

The most efficient upward-shifting study named in the hypothesis spec is direct measurement of replication-dissociated cGAS-STING or NLRP3 activation markers (cGAMP, phospho-TBK1, cleaved gasdermin-D, or mature IL-18) in an established-PAIS cohort — a design currently absent from the bundle. `question:0076-ip10-cxcl10-omicron-persistence-antigen-vs-sterile` represents the closest available observational gap: the `paper:Vacharathit2025` IP-10/CXCL10 signal is consistent with sterile sensing but cannot discriminate it from residual antigen or alternative IFN-γ sources. The role of mRNA vaccination history in modulating innate sensing is flagged by `question:0084-mrna-vaccine-platform-long-covid-protection` and `paper:Mead2025` but not yet integrated into this hypothesis's evidence base.

**Knowledge gaps**: No knowledge gaps detected this run.
