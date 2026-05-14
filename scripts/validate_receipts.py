#!/usr/bin/env python3
"""Validate receipt examples against matching JSON Schemas."""
from pathlib import Path
import json
import sys
import jsonschema

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
        jsonschema.Draft202012Validator(schema).validate(data)
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{example_path.relative_to(ROOT)}: {exc}")
if errors:
    print("Receipt validation failed:")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)
print("Receipt schema validation passed.")
