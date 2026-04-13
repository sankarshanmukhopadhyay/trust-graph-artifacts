# Agent Mandate Envelope

**Kind:** pattern  
**Path:** `patterns/your-agents-are-not-failing-your`  
**Source essay:** Your Agents Are Not Failing. Your Mandates Are  
**Published:** 2026-02-26  
**Signal tier:** B (13.64% engagement)

## Purpose

TSMM-native mandate pattern for translating human intent into executable and contestable agent authority.

This package is authored directly in TSMM-native form. The essay provides the conceptual stance and problem framing. The package provides the machine-readable structure that can be validated, compared, and reused.

## Package contents

- `package.json` — package metadata and source essay provenance
- `graph.json` — TSMM graph instance
- `constraints.json` — package-local controls, policy rules, threats, and lifecycle
- `evidence.json` — required evidence artifacts, verification expectations, and decision receipts
- `examples/` — valid and invalid TSMM graph examples
- `tests/test-vector.json` — expected validation outcomes

## Core modeling choices

- **Primary TSMM object kind:** pattern
- **Primary profile or graph:** `ttg.pattern.your-agents-are-not-failing-your`
- **Control count:** 3
- **Evidence artifact count:** 1
- **Decision count:** 1

## Validation

This package participates in repository-wide validation through:

- `scripts/validate_tsmm_native.py`
- `schemas/tsmm-graph.schema.json`
- `schemas/tsmm-native-package.schema.json`

## Source provenance

- Essay URL: `https://thetrustgraph.substack.com/p/your-agents-are-not-failing-your`
