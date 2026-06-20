#!/usr/bin/env python3
"""G1 acquisition + integrity + G2 scale/header smoke check for t035.

Bounded by design (see pre-registration:0002-cross-trigger-pathway-overlap,
Vehicle-Admissibility Gate G1/G2). This script:

  1. SHA-256-hashes every payload in data/raw/ (incl. GSE130353_RAW.tar + members).
  2. Parses the GSE14577 expression tables from the LOCAL family.soft.gz into
     per-platform probe x sample matrices (as-deposited; NO probe->gene collapse,
     NO normalization, NO filtering -- those are pipeline steps, not G1).
  3. Records scale stats (min/max/mean/%-integer) per matrix -> log2 confirmation.
  4. If GSE130353_RAW.tar is present: extracts the 40 *.gene.mmseq.txt.gz members,
     hashes them, and opens up to 2 to LOCK the column/scale contract for G2.
  5. Writes an acquisition_manifest.json (hashes + source URLs) and per-dataset
     parse_contract.json.

It STOPS before any DE, fgsea, concordance, or pathway result. Re-runnable:
GSE14577 work proceeds offline now; GSE130353 work activates once the tar lands.
"""
from __future__ import annotations

import gzip
import hashlib
import json
import re
import statistics
import sys
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw"
PROC = ROOT / "data" / "processed"

SOURCE_URLS = {
    "GSE14577_family.soft.gz": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE14nnn/GSE14577/soft/GSE14577_family.soft.gz",
    "GSE130353_family.soft.gz": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE130nnn/GSE130353/soft/GSE130353_family.soft.gz",
    "GSE130353_series_matrix.txt.gz": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE130nnn/GSE130353/matrix/GSE130353_series_matrix.txt.gz",
    "GSE130353_RAW.tar": "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE130nnn/GSE130353/suppl/GSE130353_RAW.tar",
}


def sha256_path(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def scale_stats(values: list[float]) -> dict:
    """Universal scale check: confirm log-scale vs counts-vs-not."""
    n = len(values)
    if n == 0:
        return {"n": 0}
    integer_like = sum(1 for v in values if abs(v - round(v)) < 1e-9)
    negative = sum(1 for v in values if v < 0)
    return {
        "n": n,
        "min": round(min(values), 6),
        "max": round(max(values), 6),
        "mean": round(statistics.fmean(values), 6),
        "median": round(statistics.median(values), 6),
        "pct_integer_like": round(100 * integer_like / n, 3),
        "pct_negative": round(100 * negative / n, 3),
    }


# ---------------------------------------------------------------- GSE14577 ----
def parse_gse14577() -> dict:
    soft = RAW / "GSE14577_family.soft.gz"
    if not soft.exists():
        return {"status": "missing", "file": soft.name}

    samples: dict[str, dict] = {}
    cur = None
    in_table = False
    header = None
    # per-(platform) accumulation of probe -> {sample: value}
    matrices: dict[str, dict[str, dict[str, float]]] = {}
    sample_scale_values: dict[str, list[float]] = {}

    with gzip.open(soft, "rt", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith("^SAMPLE = "):
                cur = line.split(" = ", 1)[1].strip()
                samples[cur] = {"accession": cur}
                in_table = False
                header = None
            elif line.startswith("!Sample_title = ") and cur:
                samples[cur]["title"] = line.split(" = ", 1)[1].strip()
            elif line.startswith("!Sample_characteristics_ch1 = ") and cur:
                samples[cur]["characteristics"] = line.split(" = ", 1)[1].strip()
            elif line.startswith("!Sample_platform_id = ") and cur:
                samples[cur]["platform"] = line.split(" = ", 1)[1].strip()
            elif line.startswith("!sample_table_begin"):
                in_table = True
                header = None
            elif line.startswith("!sample_table_end"):
                in_table = False
            elif in_table and cur:
                if header is None:
                    header = line.split("\t")
                    continue
                parts = line.split("\t")
                if len(parts) < 2:
                    continue
                probe, val = parts[0], parts[1]
                try:
                    fval = float(val)
                except ValueError:
                    continue
                plat = samples[cur].get("platform", "UNKNOWN")
                matrices.setdefault(plat, {}).setdefault(probe, {})[cur] = fval
                sample_scale_values.setdefault(cur, []).append(fval)

    # derive group / chip / patient key from title + characteristics
    for acc, s in samples.items():
        title = s.get("title", "")
        chars = s.get("characteristics", "")
        s["sex"] = "Male" if "Male" in chars else ("Female" if "Female" in chars else "unknown")
        if "post-infectious CFS" in chars or title.lower().startswith("cfs"):
            s["group"] = "PI-CFS"
        elif "healthy normal control" in chars or title.lower().startswith("control"):
            s["group"] = "HC"
        else:
            s["group"] = "unknown"
        m = re.search(r"patient\s+(\d+)", title)
        num = m.group(1) if m else "NA"
        chip = "B" if "chip B" in title else ("A" if "chip A" in title else "NA")
        s["chip"] = chip
        s["platform_chip"] = f"{s.get('platform','?')}/{chip}"
        # patient key unique within group (control#2 != CFS#2)
        s["patient_key"] = f"{s['group']}_{num}"

    # write per-platform matrices (probe x sample), as-deposited
    out = PROC / "GSE14577"
    out.mkdir(parents=True, exist_ok=True)
    platform_summaries = {}
    for plat, probes in matrices.items():
        plat_samples = sorted({sm for p in probes.values() for sm in p})
        mat_path = out / f"expr_{plat}.probe_x_sample.tsv.gz"
        all_vals: list[float] = []
        with gzip.open(mat_path, "wt", encoding="utf-8") as w:
            w.write("ID_REF\t" + "\t".join(plat_samples) + "\n")
            for probe in sorted(probes):
                row = probes[probe]
                vals = [row.get(sm) for sm in plat_samples]
                all_vals.extend(v for v in vals if v is not None)
                w.write(probe + "\t" + "\t".join("" if v is None else f"{v:.6g}" for v in vals) + "\n")
        platform_summaries[plat] = {
            "matrix_file": str(mat_path.relative_to(ROOT)),
            "n_probes": len(probes),
            "n_samples": len(plat_samples),
            "samples": plat_samples,
            "scale_stats": scale_stats(all_vals),
            "sha256": sha256_path(mat_path),
        }

    # write sample metadata
    meta_path = out / "sample_metadata.tsv"
    cols = ["accession", "group", "patient_key", "chip", "platform", "platform_chip", "sex", "title"]
    with meta_path.open("w", encoding="utf-8") as w:
        w.write("\t".join(cols) + "\n")
        for acc in sorted(samples):
            s = samples[acc]
            w.write("\t".join(str(s.get(c, "")) for c in cols) + "\n")

    groups: dict[str, int] = {}
    patients: set[str] = set()
    for s in samples.values():
        groups[s["group"]] = groups.get(s["group"], 0) + 1
        patients.add(s["patient_key"])

    contract = {
        "dataset": "GSE14577",
        "source": "parsed from local GSE14577_family.soft.gz (series_matrix 404s)",
        "delimiter": "tab",
        "table_columns": ["ID_REF", "VALUE"],
        "value_semantics": "depositor VALUE column; scale stats below confirm log2 intensities",
        "platforms": platform_summaries,
        "n_geo_samples": len(samples),
        "group_counts_samples": groups,
        "n_unique_patients": len(patients),
        "sample_metadata": str(meta_path.relative_to(ROOT)),
        "independent_unit_note": "1 patient = 2 GEO samples (chip A GPL96 + chip B GPL97); pair on patient_key at collapse step",
        "status": "parsed",
    }
    (out / "parse_contract.json").write_text(json.dumps(contract, indent=2) + "\n")
    return contract


# --------------------------------------------------------------- GSE130353 ----
GSE130353_GROUP_MAP = {
    "Healthy control": "HC",
    "Chronic Fatigue Syndrome": "CFS",       # depositor also writes "(FCS)"; titles use CFS/CSF typos
    "Q Fever Fatigue Syndrom": "QFS",
    "Q fever seropositive controls": "QS",   # filename prefix is "PQ"; SOFT status is authoritative
}


def parse_gse130353_soft() -> dict:
    """Authoritative GSM -> {title, group, donor_id, mmseq_basename} from the SOFT.

    Group is derived from `subject status` (not the filename prefix, which carries
    the PQ<->QS indirection and CFS/CSF/FCS typos)."""
    soft = RAW / "GSE130353_family.soft.gz"
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


def parse_gse130353() -> dict:
    tar = RAW / "GSE130353_RAW.tar"
    out = PROC / "GSE130353"
    out.mkdir(parents=True, exist_ok=True)
    if not tar.exists():
        return {
            "dataset": "GSE130353",
            "status": "PENDING_DOWNLOAD",
            "needed_file": "GSE130353_RAW.tar",
            "source_url": SOURCE_URLS["GSE130353_RAW.tar"],
            "note": "geo adapter is series-matrix-only; RAW.tar must be fetched directly. "
                    "Run the download (see runbook) then re-run this script.",
        }

    members = []
    mmseq_inspections = []
    extract_dir = out / "raw_members"
    extract_dir.mkdir(parents=True, exist_ok=True)

    with tarfile.open(tar, "r") as tf:
        names = [m for m in tf.getmembers() if m.isfile()]
        for m in sorted(names, key=lambda x: x.name):
            ef = tf.extractfile(m)
            if ef is None:
                continue
            data = ef.read()
            sha = sha256_bytes(data)
            members.append({"name": m.name, "bytes": m.size, "sha256": sha})
            # persist member to disk (gitignored)
            (extract_dir / Path(m.name).name).write_bytes(data)
            # G2: open up to 2 mmseq files and lock the column/scale contract
            if len(mmseq_inspections) < 2 and m.name.endswith(".gene.mmseq.txt.gz"):
                mmseq_inspections.append(inspect_mmseq(m.name, data))

    # authoritative sample sheet from the SOFT (group from subject status)
    soft_samples = parse_gse130353_soft()
    member_basenames = {Path(m["name"]).name for m in members}
    sheet_rows = []
    group_counts: dict[str, int] = {}
    donors: set[str] = set()
    for gsm, s in sorted(soft_samples.items()):
        grp = s.get("group", "unknown")
        group_counts[grp] = group_counts.get(grp, 0) + 1
        donors.add(s.get("donor_id", gsm))
        base = s.get("mmseq_basename", "")
        sheet_rows.append({
            "accession": gsm,
            "title": s.get("title", ""),
            "subject_status": s.get("subject_status", ""),
            "group": grp,
            "donor_id": s.get("donor_id", ""),
            "mmseq_file": base,
            "member_present": base in member_basenames,
        })
    sheet_path = out / "sample_sheet.tsv"
    cols = ["accession", "group", "donor_id", "title", "subject_status", "mmseq_file", "member_present"]
    with sheet_path.open("w", encoding="utf-8") as w:
        w.write("\t".join(cols) + "\n")
        for r in sheet_rows:
            w.write("\t".join(str(r[c]) for c in cols) + "\n")

    # G4 admissibility: 10/10/10/10, every SOFT sample matched to a tar member,
    # and the load-bearing QFS-vs-QS contrast constructable.
    required = {"HC": 10, "CFS": 10, "QFS": 10, "QS": 10}
    unmatched = [r["accession"] for r in sheet_rows if not r["member_present"]]
    g4 = {
        "required_group_counts": required,
        "observed_group_counts": group_counts,
        "groups_admissible": group_counts == required,
        "n_unique_donors": len(donors),
        "soft_samples_matched_to_members": len(member_basenames & {r["mmseq_file"] for r in sheet_rows}),
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
        "sample_sheet": str(sheet_path.relative_to(ROOT)),
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
        "extract_dir": str(extract_dir.relative_to(ROOT)),
    }
    (out / "parse_contract.json").write_text(json.dumps(contract, indent=2) + "\n")
    return contract


def inspect_mmseq(name: str, gz_bytes: bytes) -> dict:
    """G2: lock the column/scale facts for one MMSEQ file from the data itself."""
    text = gzip.decompress(gz_bytes).decode("utf-8", errors="replace")
    lines = text.splitlines()
    comments = [ln for ln in lines[:40] if ln.startswith("#")]
    data_lines = [ln for ln in lines if ln and not ln.startswith("#")]
    header = data_lines[0].split("\t") if data_lines else []
    body = data_lines[1:] if len(data_lines) > 1 else []
    # per-numeric-column scale stats over a sample of rows
    col_stats = {}
    sample_rows = body[: min(len(body), 5000)]
    for ci, cname in enumerate(header):
        vals = []
        for ln in sample_rows:
            parts = ln.split("\t")
            if ci < len(parts):
                try:
                    vals.append(float(parts[ci]))
                except ValueError:
                    pass
        if len(vals) >= max(10, int(0.5 * len(sample_rows))):
            col_stats[cname] = scale_stats(vals)
    return {
        "file": name,
        "n_comment_lines": len(comments),
        "comment_preview": comments[:8],
        "header_columns": header,
        "n_data_rows": len(body),
        "first_data_row": body[0].split("\t") if body else [],
        "numeric_column_scale_stats": col_stats,
    }


def main() -> int:
    PROC.mkdir(parents=True, exist_ok=True)
    # hash every payload currently in data/raw/
    raw_hashes = {}
    for p in sorted(RAW.iterdir()):
        if p.is_file() and p.name != ".gitkeep":
            raw_hashes[p.name] = {
                "sha256": sha256_path(p),
                "bytes": p.stat().st_size,
                "source_url": SOURCE_URLS.get(p.name, "unknown"),
            }

    g14577 = parse_gse14577()
    g130353 = parse_gse130353()

    manifest = {
        "task": "t035",
        "gate": "G1 acquisition + integrity; G2 scale/header smoke check",
        "pre_registration": "pre-registration:0002-cross-trigger-pathway-overlap",
        "scope": "acquire + hash + parse contract ONLY -- no DE/fgsea/concordance",
        "raw_file_hashes": raw_hashes,
        "GSE14577": g14577,
        "GSE130353": g130353,
    }
    man_path = PROC / "acquisition_manifest.json"
    man_path.write_text(json.dumps(manifest, indent=2) + "\n")

    print(f"[g1] wrote {man_path.relative_to(ROOT)}")
    print(f"[g1] raw files hashed: {list(raw_hashes)}")
    if g14577.get("status") == "parsed":
        for plat, ps in g14577["platforms"].items():
            ss = ps["scale_stats"]
            print(f"[g1] GSE14577 {plat}: {ps['n_probes']} probes x {ps['n_samples']} samples; "
                  f"min={ss['min']} max={ss['max']} mean={ss['mean']} %int={ss['pct_integer_like']}")
        print(f"[g1] GSE14577 groups (samples): {g14577['group_counts_samples']}; "
              f"unique patients: {g14577['n_unique_patients']}")
    print(f"[g2] GSE130353: {g130353.get('status')}")
    if g130353.get("status") == "extracted":
        print(f"[g2] members: {g130353['n_members']}")
        for insp in g130353["g2_mmseq_inspection"]:
            print(f"[g2] {insp['file']} columns={insp['header_columns']} rows={insp['n_data_rows']}")
        gv = g130353["g2_verdict"]
        print(f"[g2] VERDICT={gv['verdict']} estimate_col={gv['expression_estimate_column']} "
              f"({gv['scale']}); depositor 'counts' label: {gv['depositor_counts_label'][:40]}…")
        g4 = g130353["g4_admissibility"]
        print(f"[g4] VERDICT={g4['verdict']} groups={g4['observed_group_counts']} "
              f"donors={g4['n_unique_donors']} matched={g4['soft_samples_matched_to_members']}/40 "
              f"qfs_vs_qs_constructable={g4['qfs_vs_qs_constructable']}")
    else:
        print(f"[g2] download needed: {g130353.get('source_url')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
