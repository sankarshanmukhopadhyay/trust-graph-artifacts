# Wallet-Agent Binding Contract

**Kind:** system  
**Path:** `systems/wallet-to-agent-identity`  
**Source essay:** Wallet-to-Agent Identity: When Identity Becomes an Execution Interface  
**Published:** 2026-02-11  
**Signal tier:** B (13.33% engagement)

## Purpose

TSMM-native system model for wallet-to-agent bindings, execution interfaces, and accountable invocation.

This package is authored directly in TSMM-native form. The essay provides the conceptual stance and problem framing. The package provides the machine-readable structure that can be validated, compared, and reused.

## Package contents

- `package.json` — package metadata and source essay provenance
- `graph.json` — TSMM graph instance
- `constraints.json` — package-local controls, policy rules, threats, and lifecycle
- `evidence.json` — required evidence artifacts, verification expectations, and decision receipts
- `examples/` — valid and invalid TSMM graph examples
- `tests/test-vector.json` — expected validation outcomes

## Core modeling choices

- **Primary TSMM object kind:** system
- **Primary profile or graph:** `ttg.system.wallet-to-agent-identity`
- **Control count:** 3
- **Evidence artifact count:** 1
- **Decision count:** 1

## Validation

This package participates in repository-wide validation through:

- `scripts/validate_tsmm_native.py`
- `schemas/tsmm-graph.schema.json`
- `schemas/tsmm-native-package.schema.json`

## Source provenance

- Essay URL: `https://thetrustgraph.substack.com/p/wallet-to-agent-identity`
