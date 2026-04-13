# Systemic Controller Registry Entry

**Kind:** pattern  
**Path:** `patterns/systemic-controllers`  
**Source essay:** Systemic Controllers: How Hidden Levers in Digital Infrastructure Create Real-World Risk  
**Published:** 2025-12-09  
**Signal tier:** C (8.33% engagement)

## Purpose

TSMM-native pattern for identifying hidden control surfaces, institutional leverage, and downstream risk effects.

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
- **Primary profile or graph:** `ttg.pattern.systemic-controllers`
- **Control count:** 3
- **Evidence artifact count:** 1
- **Decision count:** 1

## Validation

This package participates in repository-wide validation through:

- `scripts/validate_tsmm_native.py`
- `schemas/tsmm-graph.schema.json`
- `schemas/tsmm-native-package.schema.json`

## Source provenance

- Essay URL: `https://thetrustgraph.substack.com/p/systemic-controllers-how-hidden-levers`
