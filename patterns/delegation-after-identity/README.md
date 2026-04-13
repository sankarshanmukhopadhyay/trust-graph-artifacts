# Delegation Chain Policy

**Kind:** pattern  
**Path:** `patterns/delegation-after-identity`  
**Source essay:** Delegation After Identity  
**Published:** 2026-02-18  
**Signal tier:** B (18.18% engagement)

## Purpose

TSMM-native delegation pattern for bounded authority, scope inheritance, and revocation-aware chains.

This package is authored directly in TSMM-native form. The essay provides the conceptual stance and problem framing. The package provides the machine-readable structure that can be validated, compared, and reused.

## Package contents

- `package.json` — package metadata and source essay provenance
- `graph.json` — TSMM graph instance
- `constraints.json` — package-local controls, policy rules, threats, and lifecycle
- `evidence.json` — required evidence outputs, verification expectations, and decision receipts
- `examples/` — valid and invalid TSMM graph examples
- `tests/test-vector.json` — expected validation outcomes

## Core modeling choices

- **Primary TSMM object kind:** pattern
- **Primary profile or graph:** `ttg.pattern.delegation-after-identity`
- **Control count:** 3
- **Evidence artifact count:** 1
- **Decision count:** 1

## Validation

This package participates in repository-wide validation through:

- `scripts/validate_tsmm_native.py`
- `schemas/tsmm-graph.schema.json`
- `schemas/tsmm-native-package.schema.json`

## Source provenance

- Essay URL: `https://thetrustgraph.substack.com/p/delegation-after-identity`
