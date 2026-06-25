# science:code
# status: exploratory
# science:end

#!/usr/bin/env python3
"""Serialize the LOCKED theme map + compartment-marker regex from config.yaml to
JSON (t035 WP4) so the r-bioc steps can apply them VERBATIM without r-yaml.

config.yaml is the single source of truth (it mirrors pre-reg:0002's "Locked
theme map" / "Locked cell-type-marker set"). This step only re-encodes those
PCRE strings as JSON — it ORIGINATES nothing — so the round-trip
YAML→json→jsonlite preserves backslash escapes (e.g. `\\b` word boundaries)
that would be mangled by shell-quoting. The output is sorted by precedence so
first-match-wins is positional.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml


def main() -> int:
    ap = argparse.ArgumentParser(description="emit locked theme spec (config → JSON)")
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    cfg = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    theme_map = sorted(cfg["theme_map"], key=lambda t: t["precedence"])
    spec = {
        "source": "config.yaml theme_map (mirrors pre-reg:0002 Locked theme map)",
        "match_rule": "uppercase set name, strip collection prefix "
                      "(HALLMARK_/REACTOME_/GOBP_), PCRE case-insensitive, first match wins",
        "theme_map": [
            {"precedence": t["precedence"], "theme": t["theme"], "regex": t["regex"]}
            for t in theme_map
        ],
        "compartment_marker_regex": cfg["compartment_marker_regex"],
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"[emit_theme_spec] wrote {len(spec['theme_map'])} themes -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
