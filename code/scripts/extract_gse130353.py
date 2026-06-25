# science:code
# status: exploratory
# science:end

#!/usr/bin/env python3
"""Extract GSE130353_RAW.tar -> per-donor MMSEQ members + sample_sheet (t035 WP1).

Rule-callable refactor of the original `g1_acquire.parse_gse130353`. Reads the
LOCAL tar + family SOFT and writes, into `--out-dir`:

  raw_members/<gsm>.gene.mmseq.txt.gz   40 extracted members (gitignored)
  raw_members.ok                        sentinel: all members extracted + hashed
  sample_sheet.tsv                      authoritative group from SOFT `subject status`
  parse_contract.json                   tar/member hashes + G2 scale verdict + G4 admissibility

Group is derived from the SOFT `subject status` (pre-reg:0002 G4), NOT the
filename prefix (QS files prefixed "PQ"; CFS titles carry CSF/FCS typos). The
G2 scale verdict confirms the estimate column is `log_mu` (continuous natural-log
MMSEQ posterior mean) — the depositor "counts" label is inaccurate, so only
continuous limma is admissible (DESeq2/edgeR inadmissible).
"""
from __future__ import annotations

import argparse
import gzip
import json
import sys
import tarfile
from pathlib import Path

from acquire_common import (
    GSE130353_GROUP_MAP,
    inspect_mmseq,
    sha256_bytes,
    sha256_path,
)


def parse_soft(soft: Path) -> dict:
    """Authoritative GSM -> {title, group, donor_id, mmseq_basename} from the SOFT."""
    samples: dict[str, dict] = {}
    cur = None
    with gzip.open(soft, "rt", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith("^SAMPLE = "):
                cur = line.split(" = ", 1)[1].strip()
                samples[cur] = {"accession": cur}
            elif not cur:
                continue
            elif line.startswith("!Sample_title = "):
                samples[cur]["title"] = line.split(" = ", 1)[1].strip()
            elif line.startswith("!Sample_characteristics_ch1 = subject status:"):
                status = line.split("subject status:", 1)[1].strip()
                samples[cur]["subject_status"] = status
                grp = "unknown"
                for key, code in GSE130353_GROUP_MAP.items():
                    if key in status:
                        grp = code
                        break
                samples[cur]["group"] = grp
            elif line.startswith("!Sample_characteristics_ch1 = donor id:"):
                samples[cur]["donor_id"] = line.split("donor id:", 1)[1].strip()
            elif line.startswith("!Sample_supplementary_file_1 = "):
                url = line.split(" = ", 1)[1].strip()
                samples[cur]["mmseq_basename"] = url.rsplit("/", 1)[-1]
    return samples


def extract_members(tar: Path, extract_dir: Path) -> tuple[list, list]:
    """Extract every file member to disk; return (member records, <=2 mmseq inspections)."""
    extract_dir.mkdir(parents=True, exist_ok=True)
    members: list[dict] = []
    mmseq_inspections: list[dict] = []
    with tarfile.open(tar, "r") as tf:
        names = [m for m in tf.getmembers() if m.isfile()]
        for m in sorted(names, key=lambda x: x.name):
            ef = tf.extractfile(m)
            if ef is None:
                continue
            data = ef.read()
            members.append({"name": m.name, "bytes": m.size, "sha256": sha256_bytes(data)})
            (extract_dir / Path(m.name).name).write_bytes(data)
            if len(mmseq_inspections) < 2 and m.name.endswith(".gene.mmseq.txt.gz"):
                mmseq_inspections.append(inspect_mmseq(m.name, data))
    return members, mmseq_inspections


def build_sheet(soft_samples: dict, members: list) -> tuple[list, dict, set]:
    member_basenames = {Path(m["name"]).name for m in members}
    rows = []
    group_counts: dict[str, int] = {}
    donors: set[str] = set()
    for gsm, s in sorted(soft_samples.items()):
        grp = s.get("group", "unknown")
        group_counts[grp] = group_counts.get(grp, 0) + 1
        donors.add(s.get("donor_id", gsm))
        base = s.get("mmseq_basename", "")
        rows.append({
            "accession": gsm,
            "title": s.get("title", ""),
            "subject_status": s.get("subject_status", ""),
            "group": grp,
            "donor_id": s.get("donor_id", ""),
            "mmseq_file": base,
            "member_present": base in member_basenames,
        })
    return rows, group_counts, donors


def run(tar: Path, soft: Path, out_dir: Path) -> dict:
    """Extract + write all GSE130353 outputs into out_dir; return the contract dict."""
    for p in (tar, soft):
        if not p.exists():
            sys.exit(f"[extract_gse130353] HALT: missing {p}")
    out_dir.mkdir(parents=True, exist_ok=True)
    extract_dir = out_dir / "raw_members"

    members, mmseq_inspections = extract_members(tar, extract_dir)
    soft_samples = parse_soft(soft)
    rows, group_counts, donors = build_sheet(soft_samples, members)

    sheet_path = out_dir / "sample_sheet.tsv"
    cols = ["accession", "group", "donor_id", "title", "subject_status", "mmseq_file", "member_present"]
    with sheet_path.open("w", encoding="utf-8") as w:
        w.write("\t".join(cols) + "\n")
        for r in rows:
            w.write("\t".join(str(r[c]) for c in cols) + "\n")

    # G4 admissibility: 10/10/10/10, every SOFT sample matched to a tar member.
    required = {"HC": 10, "CFS": 10, "QFS": 10, "QS": 10}
    member_basenames = {Path(m["name"]).name for m in members}
    unmatched = [r["accession"] for r in rows if not r["member_present"]]
    g4 = {
        "required_group_counts": required,
        "observed_group_counts": group_counts,
        "groups_admissible": group_counts == required,
        "n_unique_donors": len(donors),
        "soft_samples_matched_to_members": len(member_basenames & {r["mmseq_file"] for r in rows}),
        "unmatched_samples": unmatched,
        "qfs_vs_qs_constructable": group_counts.get("QFS", 0) >= 2 and group_counts.get("QS", 0) >= 2,
        "verdict": "PASS" if (group_counts == required and not unmatched) else "REVIEW",
    }

    # G2 verdict (mechanical) from the locked column inspection
    est_col = "log_mu"
    g2_pass = all(
        est_col in insp["header_columns"]
        and insp["numeric_column_scale_stats"].get(est_col, {}).get("pct_integer_like", 100) < 1.0
        for insp in mmseq_inspections
    ) if mmseq_inspections else False

    contract = {
        "dataset": "GSE130353",
        "status": "extracted",
        "tar_sha256": sha256_path(tar),
        "n_members": len(members),
        "members": members,
        "sample_sheet": sheet_path.name,
        "depositor_processing_claim": "SOFT says '.gene.mmseq.txt ... containing counts per gene' "
                                      "(MMSEQ via Bowtie1, Ensembl release 68)",
        "g2_verdict": {
            "expression_estimate_column": est_col,
            "scale": "natural-log MMSEQ posterior mean (continuous, ~30% negative, 0% integer)",
            "counts_column_present_but_not_used": "unique_hits (integer; ignores MMSEQ multi-map model)",
            "uncertainty_column": "sd (per-estimate posterior SD; candidate limma precision weights)",
            "feature_id_namespace": "Ensembl gene IDs (ENSG..., release 68)",
            "depositor_counts_label": "INACCURATE -- estimate is log_mu, not counts; continuous limma only (DESeq2/edgeR inadmissible)",
            "halt_on_triggered": not g2_pass,
            "verdict": "PASS" if g2_pass else "HALT",
        },
        "g2_mmseq_inspection": mmseq_inspections,
        "g4_admissibility": g4,
        "extract_dir": extract_dir.name,
    }
    (out_dir / "parse_contract.json").write_text(json.dumps(contract, indent=2) + "\n")

    # sentinel: members extracted + hashed (consumed by qa.smk via the .ok output)
    (out_dir / "raw_members.ok").write_text(
        f"{len(members)} members extracted from {tar.name}\n", encoding="utf-8"
    )

    print(f"[extract_gse130353] members={len(members)} groups={group_counts} "
          f"donors={len(donors)} G2={contract['g2_verdict']['verdict']} G4={g4['verdict']}",
          file=sys.stderr)
    return contract


def main() -> int:
    ap = argparse.ArgumentParser(description="extract GSE130353 RAW.tar -> sheet + contract")
    ap.add_argument("--tar", required=True, type=Path)
    ap.add_argument("--soft", required=True, type=Path)
    ap.add_argument("--out-dir", required=True, type=Path)
    args = ap.parse_args()
    run(args.tar, args.soft, args.out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
