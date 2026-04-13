# First-Person Assertion Envelope

**Kind:** profile  
**Path:** `profiles/first-person-credentials`  
**Source essay:** First-Person Credentials  
**Published:** 2026-03-02  
**Signal tier:** A (20.93% engagement)

## Purpose

TSMM-native profile for first-person assertion admissibility, challenge handling, and evidence-linked self-claims.

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
- **Primary profile or graph:** `ttg.profile.first-person-credentials`
- **Control count:** 4
- **Evidence artifact count:** 2
- **Decision count:** 1

## Validation

This package participates in repository-wide validation through:

- `scripts/validate_tsmm_native.py`
- `schemas/tsmm-graph.schema.json`
- `schemas/tsmm-native-package.schema.json`

## Source provenance

- Essay URL: `https://thetrustgraph.substack.com/p/first-person-credentials`
