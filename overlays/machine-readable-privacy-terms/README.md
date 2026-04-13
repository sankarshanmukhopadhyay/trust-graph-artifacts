# Privacy Term Enforcement Profile

**Kind:** overlay  
**Path:** `overlays/machine-readable-privacy-terms`  
**Source essay:** Machine-Readable Privacy Terms and the Infrastructure of Control  
**Published:** 2026-01-30  
**Signal tier:** B (18.42% engagement)

## Purpose

TSMM-native privacy policy overlay for executable terms, machine legibility, and constrained use.

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
- **Primary profile or graph:** `ttg.overlay.machine-readable-privacy-terms`
- **Control count:** 3
- **Evidence artifact count:** 1
- **Decision count:** 1

## Validation

This package participates in repository-wide validation through:

- `scripts/validate_tsmm_native.py`
- `schemas/tsmm-graph.schema.json`
- `schemas/tsmm-native-package.schema.json`

## Source provenance

- Essay URL: `https://thetrustgraph.substack.com/p/machine-readable-privacy-terms`
