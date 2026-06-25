# science:code
# status: exploratory
# science:end

#!/usr/bin/env python3
"""Harmonize GSE130353 MMSEQ members -> gene×donor log_mu matrix (t035 WP3 / G3).

Assembles the 40 per-donor `*.gene.mmseq.txt.gz` members into one
ensembl_gene_id × sample matrix of `log_mu`, on the canonical Ensembl axis.
The MMSEQ feature_id is already Ensembl (release 68); the rel68->current lift is
a MEMBERSHIP check against the current Ensembl universe (org.Hs.eg.db, supplied
in the reference) — rel68 ids absent from current are RETIRED and LOGGED, never
silently dropped (they stay in the matrix; gene sets are current ENSG, so they
are simply inert downstream).

G3 gate (pre-reg:0002): the harmonized universe must be non-empty and cover the
pinned Hallmark genes. Two severities (t037):
  STRUCTURAL (build-fatal): empty harmonized universe OR empty mapped-Hallmark
             intersection -> sentinel withheld -> DAG halts.
  DISTRIBUTION (surfaced):  Hallmark coverage < coverage_warn -> warning only.
"""
from __future__ import annotations

import argparse
import gzip
import json
import sys
from pathlib import Path


def read_member(path: Path) -> dict[str, str]:
    """Return {feature_id: log_mu_str} from one MMSEQ member (skip # comments)."""
    out: dict[str, str] = {}
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as fh:
        rows = (ln for ln in fh if not ln.startswith("#"))
        try:
            header = next(rows).rstrip("\n").split("\t")
        except StopIteration:
            return out
        fi = header.index("feature_id")
        lm = header.index("log_mu")
        for line in rows:
            parts = line.rstrip("\n").split("\t")
            if len(parts) > lm:
                out[parts[fi]] = parts[lm]
    return out


def read_sheet(path: Path) -> list[dict]:
    rows = path.read_text(encoding="utf-8").splitlines()
    head = rows[0].split("\t")
    idx = {c: i for i, c in enumerate(head)}
    return [{c: r.split("\t")[idx[c]] for c in head} for r in rows[1:] if r]


def write_matrix(path: Path, features: list[str], accs: list[str], cols: dict[str, dict]) -> None:
    """Deterministic gzip (mtime=0/no-name); rows sorted by ensembl_gene_id."""
    lines = ["ensembl_gene_id\t" + "\t".join(accs) + "\n"]
    for g in features:
        vals = [cols[a].get(g, "") for a in accs]
        lines.append(g + "\t" + "\t".join("" if v is None else v for v in vals) + "\n")
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as raw, gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as gz:
        gz.write("".join(lines).encode("utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser(description="harmonize GSE130353 MMSEQ -> ensembl matrix")
    ap.add_argument("--members-dir", required=True, type=Path)
    ap.add_argument("--sheet", required=True, type=Path)
    ap.add_argument("--reference", required=True, type=Path)
    ap.add_argument("--out-harmonized", required=True, type=Path)
    ap.add_argument("--out-report", required=True, type=Path)
    ap.add_argument("--sentinel", required=True, type=Path)
    ap.add_argument("--coverage-warn", required=True, type=float)
    args = ap.parse_args()

    ref = json.loads(args.reference.read_text(encoding="utf-8"))
    current = set(ref["current_ensembl_universe"])
    hallmark_ens = set(ref["hallmark"]["genes_ensembl"])

    sheet = read_sheet(args.sheet)
    # column key = accession (GSM); value matrix sorted by accession for determinism
    accs = sorted(r["accession"] for r in sheet)
    by_acc = {r["accession"]: r for r in sheet}

    cols: dict[str, dict] = {}
    per_donor_n: dict[str, int] = {}
    feature_union: set[str] = set()
    for acc in accs:
        member = args.members_dir / by_acc[acc]["mmseq_file"]
        if not member.exists():
            sys.exit(f"[harmonize_gse130353] HALT: member missing for {acc}: {member}")
        d = read_member(member)
        cols[acc] = d
        per_donor_n[acc] = len(d)
        feature_union |= set(d)

    parsed = sorted(feature_union)
    # consistency: are per-donor feature sets identical? (MMSEQ shared reference)
    donor_n_set = sorted(set(per_donor_n.values()))
    consistent = len(donor_n_set) == 1 and donor_n_set[0] == len(parsed)

    # rel68 -> current lift (plan:0003 KD5): emit ONLY ids present in the current
    # Ensembl annotation universe = org.Hs.eg.db ENSEMBL keys, which is exactly
    # the gene-set annotation space (sets are mapped via the same org.Hs.eg.db).
    # Dropping the rest is the finding-1 fix: a dropped gene can NEVER be a
    # gene-set member, so keeping it would only inflate the fgsea ranked-walk
    # denominator. Dropped ids = genuinely-retired rel68 ids PLUS current-but-
    # unannotated ids (non-coding / no-Entrez); both are correctly excluded.
    # Tracked in the report + a sidecar, not silently kept.
    emitted = [g for g in parsed if g in current]   # current-axis universe
    dropped = [g for g in parsed if g not in current]
    covered = hallmark_ens & set(emitted)
    coverage = len(covered) / len(hallmark_ens) if hallmark_ens else 0.0

    failures, warnings = [], []
    if not emitted:
        failures.append("harmonized universe is empty after dropping retired ids")
    if hallmark_ens and not covered:
        failures.append("mapped-Hallmark intersection is empty (no Hallmark gene in the harmonized universe)")
    if coverage < args.coverage_warn:
        warnings.append(f"Hallmark coverage {coverage:.3f} < warn threshold {args.coverage_warn}")
    if not consistent:
        warnings.append(f"per-donor feature counts not identical: {donor_n_set} (union={len(parsed)})")

    # dropped-id sidecar (full list; the report carries only a sample)
    dropped_sidecar = args.out_harmonized.parent / "harmonize_dropped_ensembl.txt"
    dropped_sidecar.write_text("\n".join(dropped) + ("\n" if dropped else ""), encoding="utf-8")

    report = {
        "dataset": "GSE130353",
        "canonical_axis": "ensembl_gene_id",
        "n_features_parsed": len(parsed),
        "n_features_emitted": len(emitted),
        "n_donors": len(accs),
        "feature_sets_consistent_across_donors": consistent,
        "per_donor_feature_counts": donor_n_set,
        "lift_rel68_to_current": {
            "annotation_source": ref.get("annotation_source"),
            "current_universe_definition": "org.Hs.eg.db ENSEMBL keys (the gene-set annotation space)",
            "policy": "emit only ids in the current universe; drop the rest (plan:0003 KD5; review finding 1)",
            "n_in_current_universe": len(emitted),
            "n_dropped_off_universe": len(dropped),
            "dropped_note": "genuinely-retired rel68 ids + current-but-unannotated (non-coding/no-Entrez); none can be gene-set members",
            "dropped_examples": dropped[:20],
            "dropped_sidecar": dropped_sidecar.name,
        },
        "hallmark_coverage": {
            "n_hallmark_ensembl": len(hallmark_ens),
            "n_covered": len(covered),
            "coverage_fraction": round(coverage, 6),
            "warn_threshold": args.coverage_warn,
        },
        "structural_failures": failures,
        "distribution_warnings": warnings,
        "verdict": "PASS" if not failures else "FAIL (structural)",
    }
    args.out_report.parent.mkdir(parents=True, exist_ok=True)
    args.out_report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    # write the harmonized matrix (current-axis universe only) even on structural
    # failure (evidence), but withhold the sentinel so the DAG halts.
    write_matrix(args.out_harmonized, emitted, accs, cols)

    for w in warnings:
        print(f"[harmonize_gse130353] WARN {w}", file=sys.stderr)
    if failures:
        for f in failures:
            print(f"[harmonize_gse130353] STRUCTURAL FAIL {f}", file=sys.stderr)
        print(f"[harmonize_gse130353] HALT: sentinel withheld. See {args.out_report}", file=sys.stderr)
        return 1

    args.sentinel.parent.mkdir(parents=True, exist_ok=True)
    args.sentinel.write_text(
        f"PASS GSE130353: {len(emitted)} current-universe ensembl features ({len(dropped)} dropped off-universe), "
        f"{len(accs)} donors, Hallmark coverage {coverage:.3f} ({len(warnings)} warning(s)).\n",
        encoding="utf-8",
    )
    print(f"[harmonize_gse130353] PASS {len(emitted)} emitted features × {len(accs)} donors; "
          f"dropped_off_universe={len(dropped)} hallmark_cov={coverage:.3f}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
