#!/usr/bin/env python3
"""Repository-wide validator for TSMM-native packages and executable artifacts.

This script is the repo's primary integrity gate. It intentionally favors
small, readable checks over a hidden framework so contributors can understand
which governance claims are machine-enforced today and which remain planned.

Implemented scope:
- validate package metadata against the package schema
- validate graph surfaces against the TSMM graph schema
- confirm valid graph examples pass and invalid examples fail
- validate provenance coverage for every active package directory
- run three lightweight semantic gates tied to the public test matrix
- validate canonical artifact YAML files and crosswalk references

Declared-but-not-yet-evaluated scope:
- free-text evidenceChecks in test vectors are treated as requirements backlog;
  they are parsed by humans but not machine-evaluated by this validator yet.
"""

import json
import sys
from pathlib import Path
from typing import Any

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]
GRAPH_SCHEMA = json.loads((ROOT / "schemas" / "tsmm-graph.schema.json").read_text())
PACKAGE_SCHEMA = json.loads((ROOT / "schemas" / "tsmm-native-package.schema.json").read_text())
PACKAGE_DIRS = ["profiles", "patterns", "overlays", "systems", "evidence"]
SEMANTIC_CHECKS = {
    "patterns/authority-legitimacy-validation": {
        "id": "legitimacy-gap-detection",
        "all_terms": ["revocation"],
        "any_terms": ["contestability", "contestable", "redress", "appeal"],
    },
    "overlays/intermediary-governance-overlay": {
        "id": "intermediary-traceability",
        "all_terms": ["provenance"],
        "any_terms": ["trace", "source", "attribution"],
    },
    "profiles/coalition-legitimacy-model": {
        "id": "coalition-capture-risk",
        "all_terms": ["capture"],
        "any_terms": ["appeal", "redress", "contest"],
    },
}

errors: list[str] = []


def validate_json(path: Path, schema: dict[str, Any]) -> dict[str, Any]:
    """Load a JSON file and validate it against the supplied schema."""
    data = json.loads(path.read_text())
    jsonschema.Draft202012Validator(schema).validate(data)
    return data


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text())


def package_paths() -> list[Path]:
    paths: list[Path] = []
    for base in PACKAGE_DIRS:
        package_root = ROOT / base
        for pkg in sorted(package_root.glob("*")):
            if pkg.is_dir() and not pkg.name.startswith("_"):
                paths.append(pkg)
    return paths


def validate_package(pkg: Path) -> None:
    try:
        validate_json(pkg / "package.json", PACKAGE_SCHEMA)
        validate_json(pkg / "graph.json", GRAPH_SCHEMA)
        validate_json(pkg / "examples" / "valid-graph.json", GRAPH_SCHEMA)
    except Exception as exc:  # noqa: BLE001 - developer-facing aggregate report
        errors.append(f"{pkg.relative_to(ROOT)}: expected pass but failed: {exc}")

    try:
        validate_json(pkg / "examples" / "invalid-graph.json", GRAPH_SCHEMA)
        errors.append(f"{pkg.relative_to(ROOT)}: invalid example unexpectedly passed")
    except Exception:
        pass


def validate_semantic_gate(pkg: Path) -> None:
    rel = pkg.relative_to(ROOT).as_posix()
    spec = SEMANTIC_CHECKS.get(rel)
    if not spec:
        return
    try:
        constraints = json.loads((pkg / "constraints.json").read_text())
        graph = json.loads((pkg / "graph.json").read_text())
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{rel}: {spec['id']} could not load inputs: {exc}")
        return

    haystack = json.dumps({"constraints": constraints, "graph": graph}, sort_keys=True).lower()
    missing_all = [term for term in spec["all_terms"] if term not in haystack]
    has_any = any(term in haystack for term in spec["any_terms"])
    if missing_all or not has_any:
        missing = missing_all + ([] if has_any else ["one of: " + ", ".join(spec["any_terms"])])
        errors.append(f"{rel}: {spec['id']} missing semantic signal(s): {', '.join(missing)}")


def validate_provenance_coverage() -> None:
    path = ROOT / "provenance" / "essay-source-map.yaml"
    try:
        provenance = load_yaml(path) or {}
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{path.relative_to(ROOT)}: could not parse provenance map: {exc}")
        return
    tracked = {entry.get("packagePath") for entry in provenance.get("provenance", [])}
    for pkg in package_paths():
        rel = pkg.relative_to(ROOT).as_posix()
        if rel not in tracked:
            errors.append(f"{rel}: missing provenance entry in provenance/essay-source-map.yaml")


def schema_for_artifact(path: Path, data: dict[str, Any]) -> Path | None:
    # Canonical domain artifacts live in artifacts/<domain>/<name>.yaml and map
    # directly to schemas/<domain>/artifact.schema.json. Legacy-style manifests
    # under artifacts/<slug>/artifact.yaml are intentionally scaffold records.
    rel = path.relative_to(ROOT).parts
    if len(rel) == 3 and rel[0] == "artifacts" and path.name != "artifact.yaml":
        candidate = ROOT / "schemas" / rel[1] / "artifact.schema.json"
        if candidate.exists():
            return candidate
    return None


def validate_artifacts() -> None:
    artifact_files = [p for p in (ROOT / "artifacts").glob("*/*.yaml") if "_template" not in p.parts]
    existing = {p.relative_to(ROOT).as_posix() for p in artifact_files}

    for path in sorted(artifact_files):
        try:
            data = load_yaml(path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path.relative_to(ROOT)}: invalid YAML: {exc}")
            continue
        schema_path = schema_for_artifact(path, data or {})
        if not schema_path:
            continue
        try:
            schema = json.loads(schema_path.read_text())
            jsonschema.Draft202012Validator(schema).validate(data)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path.relative_to(ROOT)}: artifact schema validation failed: {exc}")

    crosswalk_path = ROOT / "crosswalks" / "essay_to_artifact.yaml"
    try:
        crosswalk = load_yaml(crosswalk_path) or {}
        refs = []
        for entry in crosswalk.get("crosswalk", []):
            refs.extend(entry.get("artifacts", []))
        for ref in refs:
            if ref.startswith("artifacts/") and ref.endswith((".yaml", ".yml")) and ref not in existing:
                errors.append(f"crosswalks/essay_to_artifact.yaml: missing artifact reference {ref}")
            if ref.startswith(tuple(f"{base}/" for base in PACKAGE_DIRS)) and not (ROOT / ref).is_dir():
                errors.append(f"crosswalks/essay_to_artifact.yaml: missing package reference {ref}")
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{crosswalk_path.relative_to(ROOT)}: could not validate crosswalk references: {exc}")



def validate_receipts() -> None:
    """Validate receipt examples against their matching JSON Schemas."""
    schema_dir = ROOT / "schemas" / "receipts"
    example_dir = ROOT / "examples" / "receipts"
    if not schema_dir.exists() or not example_dir.exists():
        return
    for example_path in sorted(example_dir.glob("*.example.json")):
        schema_name = example_path.name.replace(".example.json", ".schema.json")
        schema_path = schema_dir / schema_name
        if not schema_path.exists():
            errors.append(f"{example_path.relative_to(ROOT)}: missing schema {schema_path.relative_to(ROOT)}")
            continue
        try:
            schema = json.loads(schema_path.read_text())
            validate_json(example_path, schema)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{example_path.relative_to(ROOT)}: receipt schema validation failed: {exc}")

for package in package_paths():
    validate_package(package)
    validate_semantic_gate(package)

validate_provenance_coverage()
validate_artifacts()
validate_receipts()

if errors:
    print("TSMM-native validation failed:")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print(f"TSMM-native validation passed for all packages and artifact crosswalks ({len(package_paths())} packages).")
