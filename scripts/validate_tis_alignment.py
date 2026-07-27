#!/usr/bin/env python3
"""Validate TGA package projections into TIS v0.12 runtime assurance artifacts."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_DIRS = ["profiles", "patterns", "overlays", "systems", "evidence"]
REQUIRED_TIS_PROJECTION = {
    "authorityBoundary": "governance/authority-boundary.schema.json",
    "evidenceBundle": "evidence/evidence-bundle-manifest.schema.json",
    "evaluationEnvelope": "oasf/oasf-evaluation-envelope.schema.json",
    "decisionReceipt": "decision/decision-receipt.schema.json",
    "registryPublicationProfile": "registry/registry-publication-profile.schema.json",
}

errors: list[str] = []


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def package_paths() -> list[Path]:
    paths: list[Path] = []
    for base in PACKAGE_DIRS:
        for pkg in sorted((ROOT / base).glob("*")):
            if pkg.is_dir() and not pkg.name.startswith("_"):
                paths.append(pkg)
    return paths


def validate_tis_binding() -> None:
    binding = ROOT / "bindings" / "tis" / "tga-tis-binding.json"
    constraints = ROOT / "bindings" / "tis" / "constraints.json"
    if not binding.exists():
        errors.append("bindings/tis/tga-tis-binding.json is missing")
        return
    if not constraints.exists():
        errors.append("bindings/tis/constraints.json is missing")
        return
    data = load_json(binding)
    if data.get("targetVersion") != "v0.12.0":
        errors.append("TIS binding targetVersion must be v0.12.0")
    if "trust-infrastructure-schemas v0.12.0" not in data.get("compatibleWith", []):
        errors.append("TIS binding compatibleWith must include trust-infrastructure-schemas v0.12.0")


def validate_package_projection(pkg: Path) -> None:
    rel = pkg.relative_to(ROOT).as_posix()
    evidence_path = pkg / "evidence.json"
    constraints_path = pkg / "constraints.json"
    if not evidence_path.exists() or not constraints_path.exists():
        return
    evidence = load_json(evidence_path)
    constraints = load_json(constraints_path)
    projection = evidence.get("tisArtifactProjection")
    assurance = constraints.get("tisRuntimeAssurance")

    if assurance:
        missing_flags = [
            key for key in [
                "authorityBoundaryRequired",
                "evidenceBundleRequired",
                "decisionReceiptRequired",
                "redressRouteRequired",
            ]
            if assurance.get(key) is not True
        ]
        if missing_flags:
            errors.append(f"{rel}: TIS assurance flags are not all true: {', '.join(missing_flags)}")
        if assurance.get("registryPublicationIsAuthorization") is not False:
            errors.append(f"{rel}: registryPublicationIsAuthorization must be false")

    if projection:
        for key, expected in REQUIRED_TIS_PROJECTION.items():
            actual = projection.get(key)
            if actual != expected:
                errors.append(f"{rel}: TIS projection {key} expected {expected}, got {actual}")

    if assurance and not projection:
        errors.append(f"{rel}: declares TIS runtime assurance but lacks tisArtifactProjection")


def validate_composition_pack() -> None:
    pack = ROOT / "examples" / "composition" / "runtime-assurance-v0.4"
    required = [
        "01-tga-source-package.json",
        "02-tsmm-runtime-governance-envelope.json",
        "03-tis-authority-boundary.json",
        "04-tis-evidence-bundle.json",
        "05-tis-decision-receipt.json",
        "06-tis-registry-publication-profile.json",
        "07-tga-provenance-extension.json",
    ]
    for name in required:
        path = pack / name
        if not path.exists():
            errors.append(f"examples/composition/runtime-assurance-v0.4/{name} is missing")
            continue
        load_json(path)


validate_tis_binding()
for package in package_paths():
    validate_package_projection(package)
validate_composition_pack()

if errors:
    print("TIS alignment validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("TIS runtime assurance alignment validation passed.")
