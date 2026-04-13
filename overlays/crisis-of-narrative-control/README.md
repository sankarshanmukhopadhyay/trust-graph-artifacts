# Narrative Contestability Record

**Kind:** overlay  
**Path:** `overlays/crisis-of-narrative-control`  
**Source essay:** Crisis of Narrative Control  
**Published:** 2026-02-09  
**Signal tier:** B (17.07% engagement)

## Purpose

TSMM-native overlay for narrative contestability, provenance, and governance of interpretation surfaces.

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
- **Primary profile or graph:** `ttg.overlay.crisis-of-narrative-control`
- **Control count:** 3
- **Evidence artifact count:** 1
- **Decision count:** 1

## Validation

This package participates in repository-wide validation through:

- `scripts/validate_tsmm_native.py`
- `schemas/tsmm-graph.schema.json`
- `schemas/tsmm-native-package.schema.json`

## Source provenance

- Essay URL: `https://thetrustgraph.substack.com/p/crisis-of-narrative-control`
