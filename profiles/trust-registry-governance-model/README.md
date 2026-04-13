# Trust Registry Governance Profile

**Kind:** profile  
**Path:** `profiles/trust-registry-governance-model`  
**Source essay:** The Political Economy of Trust Registries  
**Published:** 2025-12-05  
**Signal tier:** A (25.00% engagement)

## Purpose

TSMM-native profile for trust registry governance, operator authority, plurality, and forking rights.

This package is authored directly in TSMM-native form. The essay provides the conceptual stance and problem framing. The package provides the machine-readable structure that can be validated, compared, and reused.

## Package contents

- `package.json` — package metadata and source essay provenance
- `graph.json` — TSMM graph instance
- `constraints.json` — package-local controls, policy rules, threats, and lifecycle
- `evidence.json` — required evidence outputs, verification expectations, and decision receipts
- `examples/` — valid and invalid TSMM graph examples
- `tests/test-vector.json` — expected validation outcomes

## Core modeling choices

- **Primary TSMM object kind:** profile
- **Primary profile or graph:** `ttg.profile.trust-registry-governance-model`
- **Control count:** 3
- **Evidence artifact count:** 1
- **Decision count:** 1

## Validation

This package participates in repository-wide validation through:

- `scripts/validate_tsmm_native.py`
- `schemas/tsmm-graph.schema.json`
- `schemas/tsmm-native-package.schema.json`

## Source provenance

- Essay URL: `https://thetrustgraph.substack.com/p/the-political-economy-of-trust-registries`
