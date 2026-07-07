# science:code
# status: workflow-owned
# task_ids: [t081]
# science:end
"""Resolve autoimmune-stratum SNOMED seed codes to OMOP concept_ids via WebAPI.

task:t081. For each SNOMED seed code in config.yaml, query the public OHDSI
ATLAS demo WebAPI vocabulary search, match the SNOMED concept whose CONCEPT_CODE
equals the seed, and record its OMOP CONCEPT_ID plus the fields that decide
vocabulary-validity (STANDARD_CONCEPT, INVALID_REASON, DOMAIN_ID, VOCABULARY_ID).
Emit one manifest (the reproducible verification record) + a human summary.

SOURCE NOTE: the ATHENA public API (`athena.ohdsi.org/api/v1/concepts`) returns a
hard HTTP 403 for programmatic search — the block that left these concept_ids
[UNVERIFIED] in interpretation:0032. The ATLAS demo WebAPI is the open,
unauthenticated substitute. This tool does NOT build concept sets
(descendants/unions/excludes) — that is plan:0006 WP1 (task:t082).

Failure policy (explicit > defensive; fail early on infrastructure):
  * A NETWORK / HTTP / JSON error while querying => HARD-STOP (exit non-zero):
    the tool could not do its job; do not emit a half-manifest that reads as
    "verified".
  * A concept that resolves but is non-Standard / invalid / wrong-domain, or a
    seed with no SNOMED match, is a recorded FINDING (verdict flag/unresolved),
    not a crash — the manifest carries the verdict.
"""
from __future__ import annotations

import argparse
import gzip
import json
import sys
import urllib.request
from pathlib import Path

import yaml

_UA = {
    "User-Agent": "post-acute-infection/t081-omop-concept-verify (research; contact via repo)",
    "Accept": "application/json",
    "Accept-Encoding": "gzip, identity",
}


def _request(url: str, timeout: int, body: dict | None = None) -> object:
    """GET (body=None) or POST JSON; transparently gunzip; parse JSON. Raises on failure."""
    headers = dict(_UA)
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, headers=headers, data=data)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read()
        if resp.info().get("Content-Encoding", "").lower() == "gzip":
            raw = gzip.decompress(raw)
    return json.loads(raw.decode("utf-8"))


def search_snomed(base: str, endpoint: str, code: str, timeout: int) -> list[dict]:
    """POST a vocabulary search restricted to SNOMED; return the concept rows."""
    data = _request(f"{base}/{endpoint}", timeout, body={"QUERY": code, "VOCABULARY_ID": ["SNOMED"]})
    if not isinstance(data, list):
        raise SystemExit(
            f"t081: WebAPI vocabulary/search returned non-list for code {code}: "
            f"{type(data).__name__} — HALT"
        )
    return data


def _norm(v: object) -> str:
    return "" if v is None else str(v).strip()


def verify_seed(rows: list[dict], snomed_code: str, require: dict) -> dict:
    """Match the SNOMED concept with CONCEPT_CODE==snomed_code among search rows; grade it."""
    matches = [
        r for r in rows
        if _norm(r.get("CONCEPT_CODE")) == snomed_code
        and _norm(r.get("VOCABULARY_ID")).upper() == require["vocabulary"].upper()
    ]
    rec: dict = {"snomed_code": snomed_code, "n_snomed_matches": len(matches)}

    if not matches:
        rec.update(verdict="unresolved", omop_concept_id=None,
                   note="no SNOMED concept with this CONCEPT_CODE in WebAPI search results")
        return rec
    if len(matches) > 1:
        # SNOMED codes are unique per concept; >1 means a query ambiguity worth surfacing.
        rec.update(verdict="ambiguous", omop_concept_id=None,
                   candidate_ids=[m.get("CONCEPT_ID") for m in matches],
                   note="multiple SNOMED rows share this CONCEPT_CODE — inspect manually")
        return rec

    m = matches[0]
    standard = _norm(m.get("STANDARD_CONCEPT"))
    invalid = _norm(m.get("INVALID_REASON"))
    domain = _norm(m.get("DOMAIN_ID"))
    is_standard = standard.upper() == require["standard_concept"].upper()
    is_valid = invalid.upper() == require["invalid_reason"].upper()
    domain_ok = domain.lower() == require["domain"].lower()

    rec.update(
        omop_concept_id=m.get("CONCEPT_ID"),
        concept_name=m.get("CONCEPT_NAME"),
        vocabulary=m.get("VOCABULARY_ID"),
        concept_class=m.get("CONCEPT_CLASS_ID"),
        domain=domain,
        standard_concept=standard or None,
        standard_concept_caption=m.get("STANDARD_CONCEPT_CAPTION"),
        invalid_reason=invalid or None,
        invalid_reason_caption=m.get("INVALID_REASON_CAPTION"),
        checks={"is_standard": is_standard, "is_valid": is_valid, "domain_is_condition": domain_ok},
        verdict="verified" if (is_standard and is_valid and domain_ok) else "flag",
    )
    return rec


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    p.add_argument("--manifest", required=True)
    p.add_argument("--summary", required=True)
    a = p.parse_args()

    cfg = yaml.safe_load(Path(a.config).read_text())
    api = cfg["vocab_api"]
    base = api["base_url"].rstrip("/")
    require = api["require"]
    timeout = api["timeout_s"]

    # Record the WebAPI/vocabulary build for provenance (fail loud if unreachable).
    info = _request(f"{base}/{api['info_endpoint']}", timeout)
    build = {
        "webapi_version": info.get("version") if isinstance(info, dict) else None,
        "build_timestamp": (info.get("buildInfo", {}) or {}).get("timestamp")
        if isinstance(info, dict) else None,
    }

    strata_out = []
    n_seed = n_verified = n_flag = n_unresolved = 0
    for st in cfg["strata"]:
        concepts_out = []
        for c in st["concepts"]:
            n_seed += 1
            code = str(c["snomed_code"])
            rows = search_snomed(base, api["search_endpoint"], code, timeout)
            v = verify_seed(rows, code, require)
            for k in ("role", "sublabel"):
                if k in c:
                    v[k] = c[k]
            if "ohdsi_cohort" in c:
                v["ohdsi_cohort"] = c["ohdsi_cohort"]
            concepts_out.append(v)
            n_verified += v["verdict"] == "verified"
            n_flag += v["verdict"] == "flag"
            n_unresolved += v["verdict"] in ("unresolved", "ambiguous")
            sys.stderr.write(
                f"t081: {st['stratum']:<18} {code:<12} -> "
                f"concept_id={v.get('omop_concept_id')} verdict={v['verdict']}\n"
            )
        so = {k: st[k] for k in ("stratum", "label", "tier") if k in st}
        if "scoping_note" in st:
            so["scoping_note"] = " ".join(st["scoping_note"].split())
        so["concepts"] = concepts_out
        strata_out.append(so)

    manifest = {
        "task": "t081",
        "purpose": "OMOP concept_id vocabulary-validity verification of autoimmune-stratum SNOMED seeds",
        "source_interpretation": "interpretation:0032-t079-bc3-autoimmune-stratum-granularity",
        "consumes": "dataset:n3c-recover-longcovid",
        "gates": "plan:0006 WP1 (task:t082) concept-set build (NOT performed here)",
        "source": {
            "name": "OHDSI ATLAS demo WebAPI (public, unauthenticated)",
            "base_url": base,
            "note": "ATHENA /concepts search is HTTP 403 (interpretation:0032); this is the open substitute.",
            **build,
        },
        "require": require,
        "summary": {
            "n_seed_codes": n_seed,
            "n_verified": n_verified,
            "n_flag": n_flag,
            "n_unresolved": n_unresolved,
        },
        "strata": strata_out,
    }
    Path(a.manifest).parent.mkdir(parents=True, exist_ok=True)
    Path(a.manifest).write_text(json.dumps(manifest, indent=2) + "\n")

    lines = [
        "# OMOP concept_id verification (task:t081)",
        "",
        f"Resolved {n_seed} SNOMED seed codes via the OHDSI ATLAS demo WebAPI "
        f"({base}, WebAPI {build['webapi_version']}). "
        f"verified={n_verified} flag={n_flag} unresolved={n_unresolved}.",
        "",
        "Source note: ATHENA's `/concepts` search is HTTP 403 (the block recorded in "
        "interpretation:0032); the public ATLAS demo WebAPI is the reproducible substitute. "
        "OMOP concept_ids are permanent identifiers, stable across vocabulary releases.",
        "",
        "Scope: verify the named SNOMED seed concepts only. Concept-set expansion "
        "(descendants / subtype unions / exclude lists) is plan:0006 WP1 (t082), not built here.",
        "",
        "| Stratum | SNOMED code | OMOP concept_id | Name | Class | Standard | Valid | Domain | Verdict |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for st in strata_out:
        for c in st["concepts"]:
            chk = c.get("checks", {})
            lines.append(
                f"| {st['stratum']} | {c['snomed_code']} | {c.get('omop_concept_id') or '—'} "
                f"| {c.get('concept_name') or '—'} | {c.get('concept_class') or '—'} "
                f"| {'✓' if chk.get('is_standard') else '✗'} "
                f"| {'✓' if chk.get('is_valid') else '✗'} "
                f"| {c.get('domain') or '—'} | **{c['verdict']}** |"
            )
    Path(a.summary).write_text("\n".join(lines) + "\n")
    sys.stderr.write(
        f"t081: wrote {a.manifest} + {a.summary} "
        f"(verified={n_verified}/{n_seed}, flag={n_flag}, unresolved={n_unresolved})\n"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
