# Execution Delegation Control Receipt

**Kind:** evidence-model  
**Path:** `evidence/execution-time-delegation`  
**Source essay:** Execution-Time Delegation: Legitimacy After Transparency  
**Published:** 2026-03-05  
**Signal tier:** C (2.44% engagement)

## Why this package exists

This package exists because the source essay identifies a trust problem that should not remain only at the level of commentary.
The essay contributes the **problem framing**. This package contributes the **TSMM-native structure** required to reason about that problem as a developer or software architect.

## What the essay contributes

The source essay contributes the motivating pressure: why this problem matters, where current systems break, and what kind of governance claim needs to become structurally legible.

In this repository, the essay is the conceptual input. It is not the schema.

## What TSMM contributes

An evidence model captures what proof, receipt, verification output, or audit surface a governed system must emit.

In this package, TSMM is used to express:

- explicit actors and roles
- explicit trust decisions and effects
- explicit control and evidence surfaces
- a structure that can be validated and compared

## What this package gives a developer

Use this package when you want a concrete, inspectable example of how an essay-derived trust problem can be represented as a machine-readable package.

Start with:

1. `package.json` for classification and provenance
2. `graph.json` for the primary system structure
3. `constraints.json` for operational boundaries
4. `evidence.json` for proof outputs
5. `tests/test-vector.json` for validation expectations

## Package contents

- `package.json` — package metadata and source essay provenance
- `graph.json` — TSMM-native graph instance
- `constraints.json` — package-local controls, policy rules, threats, and lifecycle
- `evidence.json` — required evidence outputs, verification expectations, and decision receipts
- `examples/` — valid and invalid TSMM graph examples
- `tests/test-vector.json` — expected validation outcomes

## Package snapshot

- **Primary TSMM object kind:** evidence-model
- **Graph identifier:** `ttg.evidence-model.execution-time-delegation`
- **Node count:** 13
- **Edge count:** 13

## Design reading note

To understand the line between The Trust Graph and TSMM in this package:

- read the package README for intent
- inspect `graph.json` for the structural expression
- inspect `constraints.json` and `evidence.json` for what the package insists on at execution time

That sequence separates **conceptual stance** from **system grammar** from **implementation surface**.

## Validation

This package participates in repository-wide validation through:

- `scripts/validate_tsmm_native.py`
- `schemas/tsmm-graph.schema.json`
- `schemas/tsmm-native-package.schema.json`

## Source provenance

- Essay URL: `https://thetrustgraph.substack.com/p/execution-time-delegation-legitimacy`
