# /// script
# requires-python = ">=3.11"
# dependencies = ["networkx>=3.2", "pyyaml>=6"]
# ///
"""Re-derive the menopause-PAIS DAG v2 back-door adjustment sets from the AUTHORED patch.

This is the reproducible backing for the identifiability claims in
`doc/inquiries/menopause-pais-causal-dag.md` and the patch
`entities/patches/menopause-pais-causal-dag.md`. It does NOT hardcode the edge
list: it parses `flow_edges` straight out of the patch frontmatter, so it stays
in sync with the authored DAG.

`science inquiry validate` reports `pgmpy not installed` in the frozen project
env, so the inquiry tool's identifiability/adjustment_sets checks are warnings,
not assertions. This script is the committed workaround derivation. It uses only
networkx (d-separation on the proper back-door graph) — no pgmpy — and is run
with:

    uv run code/menopause_dag/derive_adjustment_sets.py

Regenerate the committed output with:

    uv run code/menopause_dag/derive_adjustment_sets.py > code/menopause_dag/adjustment_sets_v2.txt
"""

from __future__ import annotations

import itertools
import os
import sys

import networkx as nx
import yaml

PATCH = os.path.join(
    os.path.dirname(__file__), "..", "..", "entities", "patches", "menopause-pais-causal-dag.md"
)

# Measured nodes eligible for the adjustment-set search (sex handled by population
# restriction; U is the latent node, added only for the "U measured" scenario).
MEASURED = [
    "chronological-age",
    "smoking",
    "sex-assigned-at-birth",
    "baseline-cardiometabolic-comorbidity",
    "baseline-bmi-adiposity",
    "pregnancy-history",
    "autoimmune-poi",
    "biological-frailty",
    "calendar-variant-vaccination-era",
]
# Selection/collider nodes that must never be conditioned.
COLLIDERS = {"clinic-attendance", "hospital-ascertainment", "survival-selection"}
TREATMENT = "menopausal-transition-reproductive-stage"
OUTCOME = "pais-outcome"
LATENT = "unmeasured-shared-confounders"


def load_graph() -> nx.DiGraph:
    text = open(PATCH, encoding="utf-8").read()
    fm = text.split("\n---\n", 1)[0].lstrip("-\n")
    inq = yaml.safe_load(fm)["inquiry"]
    g = nx.DiGraph()
    for e in inq["flow_edges"]:
        s = e["subject"].removeprefix("concept:")
        o = e["object"].removeprefix("concept:")
        g.add_edge(s, o)
    return g


def valid_backdoor(g: nx.DiGraph, z: set[str], descendants_t: set[str]) -> bool:
    """Z is a valid back-door set: no descendant of T, no collider, and it
    d-separates T from O in the graph with edges out of T removed."""
    if z & descendants_t or z & COLLIDERS:
        return False
    gb = g.copy()
    gb.remove_edges_from(list(g.out_edges(TREATMENT)))
    return nx.is_d_separator(gb, {TREATMENT}, {OUTCOME}, z)


def minimal_sets(g: nx.DiGraph, pool: list[str]) -> list[tuple[str, ...]]:
    descendants_t = nx.descendants(g, TREATMENT)
    found: list[tuple[str, ...]] = []
    for r in range(len(pool) + 1):
        for combo in itertools.combinations(pool, r):
            if valid_backdoor(g, set(combo), descendants_t):
                if not any(set(f) < set(combo) for f in found):
                    found.append(combo)
        if found:
            break
    return found


def main() -> int:
    g = load_graph()
    print("DAG v2 — derived from", os.path.relpath(PATCH, os.path.join(os.path.dirname(__file__), "..", "..")))
    print(f"nodes={g.number_of_nodes()} edges={g.number_of_edges()} acyclic={nx.is_directed_acyclic_graph(g)}")
    if not nx.is_directed_acyclic_graph(g):
        print("CYCLES:", list(nx.simple_cycles(g))[:5])
        return 1

    print("\n[U latent — real world]")
    latent_sets = minimal_sets(g, MEASURED)
    print("  minimal measured back-door sets:", latent_sets or "NONE -> NON-IDENTIFIABLE by adjustment")

    print("\n[U set aside / measured]")
    g_nou = g.copy()
    g_nou.remove_node(LATENT)
    sets_nou = minimal_sets(g_nou, MEASURED)
    print("  unique minimal measured set:", sets_nou)

    print("\n[selected candidate sets, U set aside]")
    desc = nx.descendants(g_nou, TREATMENT)
    for cand in (
        {"chronological-age", "smoking"},
        {"chronological-age", "smoking", "baseline-cardiometabolic-comorbidity"},
        {"chronological-age", "smoking", "baseline-cardiometabolic-comorbidity",
         "baseline-bmi-adiposity", "pregnancy-history", "autoimmune-poi", "biological-frailty"},
    ):
        print(f"  valid({sorted(cand)}) = {valid_backdoor(g_nou, cand, desc)}")

    print("\n[colliders never appear in a recommended set]")
    print("  colliders:", sorted(COLLIDERS))
    print("  survival-selection parents:", sorted(g.predecessors('survival-selection')))
    return 0


if __name__ == "__main__":
    sys.exit(main())
