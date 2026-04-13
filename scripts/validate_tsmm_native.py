#!/usr/bin/env python3
import json, sys
from pathlib import Path
import jsonschema

ROOT = Path(__file__).resolve().parents[1]
GRAPH_SCHEMA = json.loads((ROOT / "schemas" / "tsmm-graph.schema.json").read_text())
PACKAGE_SCHEMA = json.loads((ROOT / "schemas" / "tsmm-native-package.schema.json").read_text())
PACKAGE_DIRS = ["profiles", "patterns", "overlays", "systems", "evidence"]
errors = []

def validate_json(path: Path, schema: dict):
    data = json.loads(path.read_text())
    jsonschema.Draft202012Validator(schema).validate(data)
    return data

for base in PACKAGE_DIRS:
    for pkg in sorted((ROOT / base).glob("*")):
        if not pkg.is_dir():
            continue
        try:
            validate_json(pkg / "package.json", PACKAGE_SCHEMA)
            validate_json(pkg / "graph.json", GRAPH_SCHEMA)
            validate_json(pkg / "examples" / "valid-graph.json", GRAPH_SCHEMA)
        except Exception as exc:
            errors.append(f"{pkg}: expected pass but failed: {exc}")
        try:
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
