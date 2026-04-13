#!/usr/bin/env python3
"""Repository-wide validator for TSMM-native packages.

This script is intentionally small and direct. It acts as the first integrity gate
for the repository and is meant to be easy for developers to read, run, and extend.

Current scope:
- validate package metadata against the package schema
- validate graph surfaces against the TSMM graph schema
- confirm the valid example passes
- confirm the invalid example fails

Future extensions could add:
- registry reference checks
- package-to-evidence coverage checks
- lifecycle and decision integrity checks
"""

import json
import sys
from pathlib import Path

import jsonschema

# Repository root and the two schemas that define the minimum structural contract.
ROOT = Path(__file__).resolve().parents[1]
GRAPH_SCHEMA = json.loads((ROOT / "schemas" / "tsmm-graph.schema.json").read_text())
PACKAGE_SCHEMA = json.loads((ROOT / "schemas" / "tsmm-native-package.schema.json").read_text())

# These are the only first-class package classes in the repository.
PACKAGE_DIRS = ["profiles", "patterns", "overlays", "systems", "evidence"]
errors = []


def validate_json(path: Path, schema: dict):
    """Load a JSON file and validate it against the supplied schema."""
    data = json.loads(path.read_text())
    jsonschema.Draft202012Validator(schema).validate(data)
    return data


for base in PACKAGE_DIRS:
    package_root = ROOT / base
    for pkg in sorted(package_root.glob("*")):
        if not pkg.is_dir():
            continue
        try:
            # The package contract is small but explicit. Every package must expose
            # metadata, a primary graph, and a valid example that passes.
            validate_json(pkg / "package.json", PACKAGE_SCHEMA)
            validate_json(pkg / "graph.json", GRAPH_SCHEMA)
            validate_json(pkg / "examples" / "valid-graph.json", GRAPH_SCHEMA)
        except Exception as exc:
            errors.append(f"{pkg}: expected pass but failed: {exc}")
        try:
            # Invalid examples are deliberate negative tests. If one passes, the
            # package is no longer teaching the failure boundary clearly enough.
            validate_json(pkg / "examples" / "invalid-graph.json", GRAPH_SCHEMA)
            errors.append(f"{pkg}: invalid example unexpectedly passed")
        except Exception:
            pass

if errors:
    print("TSMM-native validation failed:")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print("TSMM-native validation passed for all packages.")
