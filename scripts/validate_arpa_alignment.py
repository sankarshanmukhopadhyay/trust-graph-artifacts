#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "bindings" / "arpa" / "tga-arpa-agentic-governance-alignment.json"
data = json.loads(path.read_text())
errors = []

if data.get("relationship") != "informative-implementation-alignment":
    errors.append("ARPA alignment must remain informative implementation alignment")
if data.get("semanticAuthority", {}).get("repository") != "trust-systems-meta-model":
    errors.append("TSMM must remain semantic authority")
if data.get("semanticAuthority", {}).get("version") != "v0.24.0":
    errors.append("ARPA alignment must use reviewed TSMM v0.24.0 baseline")
if data.get("portableContractAuthority", {}).get("repository") != "trust-infrastructure-schemas":
    errors.append("TIS must remain portable contract authority")
required_modules = {"ARPA-Core", "ARPA-Relations", "ARPA-Assurance", "ARPA-Authority", "ARPA-Evidence", "ARPA-Federation"}
seen_modules = {m for mapping in data.get("mappings", []) for m in mapping.get("arpaModules", [])}
missing_modules = sorted(required_modules - seen_modules)
if missing_modules:
    errors.append("missing ARPA module coverage: " + ", ".join(missing_modules))
required_rules = {
    "discovery != authorization",
    "registration != permission_to_act",
    "capability != legitimate_authority",
    "relationship != delegated_authority",
    "technical_federation != governance_recognition"
}
missing_rules = sorted(required_rules - set(data.get("nonImplications", [])))
if missing_rules:
    errors.append("missing non-implication rules: " + ", ".join(missing_rules))
if len(data.get("requiredNegativeTests", [])) < 8:
    errors.append("alignment profile must retain the minimum negative-test corpus")
for mapping in data.get("mappings", []):
    for concept in mapping.get("tsmmConceptIds", []):
        if not concept.startswith("urn:tsmm:concept:"):
            errors.append(f"non-canonical TSMM identifier: {concept}")

if errors:
    print("ARPA alignment validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print(f"ARPA alignment validation passed ({len(data.get('mappings', []))} mappings, {len(data.get('requiredNegativeTests', []))} negative tests).")
