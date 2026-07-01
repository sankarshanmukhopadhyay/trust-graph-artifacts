#!/usr/bin/env python3
"""Validate receipt examples against matching JSON Schemas."""
from pathlib import Path
import json
import sys
try:
    import jsonschema
except ModuleNotFoundError:  # pragma: no cover - dependency guidance path
    jsonschema = None

ROOT = Path(__file__).resolve().parents[1]
errors = []
for example_path in sorted((ROOT / "examples" / "receipts").glob("*.example.json")):
    schema_path = ROOT / "schemas" / "receipts" / example_path.name.replace(".example.json", ".schema.json")
    if not schema_path.exists():
        errors.append(f"{example_path.relative_to(ROOT)}: missing schema {schema_path.relative_to(ROOT)}")
        continue
    try:
        schema = json.loads(schema_path.read_text())
        data = json.loads(example_path.read_text())
        if jsonschema is None:
            # Lean local environments still prove the examples and schemas are
            # parseable JSON. Full JSON Schema validation is exercised when
            # requirements.txt dependencies are installed.
            if not isinstance(schema, dict) or not isinstance(data, dict):
                raise ValueError("schema and example must be JSON objects")
        else:
            jsonschema.Draft202012Validator(schema).validate(data)
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{example_path.relative_to(ROOT)}: {exc}")
if errors:
    print("Receipt validation failed:")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)
if jsonschema is None:
    print("Receipt JSON parse validation passed. Install requirements.txt for full JSON Schema validation.")
else:
    print("Receipt schema validation passed.")
