#!/usr/bin/env python3
"""Validate the repository-local TSMM alignment contract.

This validator intentionally does not fetch TSMM at runtime. The reviewed TSMM
release and source commit are pinned in the binding, while stable semantic URNs
make the dependency independently inspectable. The goal is to prevent local
version, authority, and mapping drift from silently weakening the published
alignment claim.
"""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
errors: list[str] = []

TGA_VERSION = "v" + (ROOT / "VERSION").read_text().strip()
EXPECTED_TSMM_VERSION = "v0.24.0"
EXPECTED_TIS_VERSION = "v0.14.1"
EXPECTED_BINDING_ID = "tga-tsmm-v0.24.0"
EXPECTED_CONCEPTS = {
    "urn:tsmm:concept:authority",
    "urn:tsmm:concept:delegation",
    "urn:tsmm:concept:scope",
    "urn:tsmm:concept:policy",
    "urn:tsmm:concept:evidence-artifact",
    "urn:tsmm:concept:evidence-bundle",
    "urn:tsmm:concept:assessment",
    "urn:tsmm:concept:trust-decision",
    "urn:tsmm:concept:effect",
    "urn:tsmm:concept:revocation",
    "urn:tsmm:concept:supersession",
    "urn:tsmm:concept:redress",
    "urn:tsmm:concept:assurance-profile",
}


def load_json(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text())


binding = load_json("bindings/tsmm/tga-tsmm-binding.json")
constraints = load_json("bindings/tsmm/constraints.json")
tis_binding = load_json("bindings/tis/tga-tis-binding.json")

if binding.get("bindingId") != EXPECTED_BINDING_ID:
    errors.append(f"TSMM binding id must be {EXPECTED_BINDING_ID}")
if binding.get("sourceVersion") != EXPECTED_TSMM_VERSION:
    errors.append(f"TSMM sourceVersion must be {EXPECTED_TSMM_VERSION}")
if binding.get("targetVersion") != TGA_VERSION:
    errors.append(f"TSMM targetVersion {binding.get('targetVersion')} does not match VERSION {TGA_VERSION}")
if binding.get("semanticRegistry") != "model/semantic-concepts.json":
    errors.append("TSMM semanticRegistry must identify the v0.24.0 canonical semantic registry path")
if not binding.get("sourceCommit"):
    errors.append("TSMM binding must pin the reviewed source commit")

mapped: set[str] = set()
for mapping in binding.get("maps", []):
    mapped.update(mapping.get("tsmmConceptIds", []))
unknown_shape = sorted(x for x in mapped if not x.startswith("urn:tsmm:concept:"))
if unknown_shape:
    errors.append("non-canonical TSMM semantic identifiers: " + ", ".join(unknown_shape))
missing = sorted(EXPECTED_CONCEPTS - mapped)
if missing:
    errors.append("required TSMM semantic mappings missing: " + ", ".join(missing))

if constraints.get("bindingId") != EXPECTED_BINDING_ID:
    errors.append("TSMM constraints bindingId does not match active binding")
if "v" + constraints.get("version", "") != TGA_VERSION:
    errors.append("TSMM constraints version does not match repository VERSION")

semantic_authority = tis_binding.get("semanticAuthority", {})
if semantic_authority.get("repository") != "trust-systems-meta-model":
    errors.append("TIS binding must preserve trust-systems-meta-model as semantic authority")
if semantic_authority.get("version") != EXPECTED_TSMM_VERSION:
    errors.append("TIS binding TSMM semantic-authority version is stale")
if tis_binding.get("sourceVersion") != TGA_VERSION:
    errors.append("TIS binding sourceVersion does not match repository VERSION")
if tis_binding.get("targetVersion") != EXPECTED_TIS_VERSION:
    errors.append(f"TIS targetVersion must be {EXPECTED_TIS_VERSION}")

binding_doc = (ROOT / "docs/bindings/tsmm-binding.md").read_text()
for stale in ("TSMM v0.21.0", "targetVersion\": \"v0.4.0", "aligned to TSMM v0.21.0"):
    if stale in binding_doc:
        errors.append(f"active TSMM binding documentation contains stale baseline: {stale}")
for required in (TGA_VERSION, EXPECTED_TSMM_VERSION, EXPECTED_TIS_VERSION):
    if required not in binding_doc:
        errors.append(f"active TSMM binding documentation does not state {required}")

if errors:
    print("TSMM alignment validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(
    "TSMM alignment validation passed: "
    f"{TGA_VERSION} -> {EXPECTED_TSMM_VERSION}, TIS {EXPECTED_TIS_VERSION}, "
    f"{len(mapped)} stable semantic identifiers mapped."
)
