# Consent Enforcement Schema

**Kind:** overlay  
**Path:** `overlays/consent-not-data-structure`  
**Source essay:** Consent Is Not a Data Structure  
**Published:** 2026-01-09  
**Signal tier:** A (20.00% engagement)

## Purpose

TSMM-native overlay for consent execution, propagation, and revocation across actors and systems.

This package is authored directly in TSMM-native form. The essay provides the conceptual stance and problem framing. The package provides the machine-readable structure that can be validated, compared, and reused.

## Package contents

- `package.json` — package metadata and source essay provenance
- `graph.json` — TSMM graph instance
- `constraints.json` — package-local controls, policy rules, threats, and lifecycle
- `evidence.json` — required evidence artifacts, verification expectations, and decision receipts
- `examples/` — valid and invalid TSMM graph examples
- `tests/test-vector.json` — expected validation outcomes

## Core modeling choices

- **Primary TSMM object kind:** overlay
- **Primary profile or graph:** `ttg.overlay.consent-not-data-structure`
- **Control count:** 4
- **Evidence artifact count:** 2
- **Decision count:** 1

## Validation

This package participates in repository-wide validation through:

- `scripts/validate_tsmm_native.py`
- `schemas/tsmm-graph.schema.json`
- `schemas/tsmm-native-package.schema.json`

## Source provenance

- Essay URL: `https://thetrustgraph.substack.com/p/consent-is-not-a-data-structure`
