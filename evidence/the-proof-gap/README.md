# Proof Requirement Profile

**Kind:** evidence-model  
**Path:** `evidence/the-proof-gap`  
**Source essay:** The Proof Gap  
**Published:** 2026-03-16  
**Signal tier:** B (11.11% engagement)

## Purpose

TSMM-native evidence model for proof sufficiency, subject-held proof, and evidence production requirements.

This package is authored directly in TSMM-native form. The essay provides the conceptual stance and problem framing. The package provides the machine-readable structure that can be validated, compared, and reused.

## Package contents

- `package.json` — package metadata and source essay provenance
- `graph.json` — TSMM graph instance
- `constraints.json` — package-local controls, policy rules, threats, and lifecycle
- `evidence.json` — required evidence outputs, verification expectations, and decision receipts
- `examples/` — valid and invalid TSMM graph examples
- `tests/test-vector.json` — expected validation outcomes

## Core modeling choices

- **Primary TSMM object kind:** evidence-model
- **Primary profile or graph:** `ttg.evidence-model.the-proof-gap`
- **Control count:** 3
- **Evidence artifact count:** 1
- **Decision count:** 1

## Validation

This package participates in repository-wide validation through:

- `scripts/validate_tsmm_native.py`
- `schemas/tsmm-graph.schema.json`
- `schemas/tsmm-native-package.schema.json`

## Source provenance

- Essay URL: `https://thetrustgraph.substack.com/p/the-proof-gap`
