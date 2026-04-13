# Execution Delegation Control Receipt

**Kind:** evidence-model  
**Path:** `evidence/execution-time-delegation`  
**Source essay:** Execution-Time Delegation: Legitimacy After Transparency  
**Published:** 2026-03-05  
**Signal tier:** C (2.44% engagement)

## Purpose

TSMM-native evidence model for runtime delegation receipts, legitimacy checks, and contestability signals.

This package is authored directly in TSMM-native form. The essay provides the conceptual stance and problem framing. The package provides the machine-readable structure that can be validated, compared, and reused.

## Package contents

- `package.json` — package metadata and source essay provenance
- `graph.json` — TSMM graph instance
- `constraints.json` — package-local controls, policy rules, threats, and lifecycle
- `evidence.json` — required evidence artifacts, verification expectations, and decision receipts
- `examples/` — valid and invalid TSMM graph examples
- `tests/test-vector.json` — expected validation outcomes

## Core modeling choices

- **Primary TSMM object kind:** evidence-model
- **Primary profile or graph:** `ttg.evidence-model.execution-time-delegation`
- **Control count:** 3
- **Evidence artifact count:** 1
- **Decision count:** 1

## Validation

This package participates in repository-wide validation through:

- `scripts/validate_tsmm_native.py`
- `schemas/tsmm-graph.schema.json`
- `schemas/tsmm-native-package.schema.json`

## Source provenance

- Essay URL: `https://thetrustgraph.substack.com/p/execution-time-delegation-legitimacy`
