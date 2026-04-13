# Legitimate Control Decision Receipt

**Kind:** evidence-model  
**Path:** `evidence/legitimate-control-decision-receipt`  
**Source essay:** Enforceable Authority Without Legitimate Control  
**Published:** 2026-04-08

## Why this package exists

This package captures the evidentiary surface implied by the essay. It specifies what a system must emit when it claims a consequential action was exercised under legitimate control.

The essay contributes the **asymmetry diagnosis**: systems increasingly carry enforceable authority, but the control-side mechanisms required to make that authority legitimate are still missing or too slow.
This package contributes the **TSMM-native structure** required to make that gap implementable and testable.

## What the essay contributes

The source essay draws a sharp line between two conditions:

- **enforceable authority** — the system can act with real-world consequence under credentialed, sanctioned authority
- **legitimate control** — the system can be revoked, audited, attributed, and remediated at execution-relevant speed

That distinction is the design pressure this package captures.

## What TSMM contributes

TSMM gives this package a repeatable structural vocabulary:

- actors, issuers, verifiers, and governance authorities as nodes
- control and decision relationships as edges
- evidence bundles as explicit outputs rather than narrative assumptions
- effects that describe what operational boundary the system actually enforces

## What to inspect first

Start with:

1. `graph.json` — the core system shape
2. `constraints.json` — the policy boundary and expected failure modes
3. `evidence.json` — what the system must emit to justify operation
4. `examples/` — the passing and failing graph surfaces

## Relationship to existing work

This package aligns most strongly with:

- `patterns/delegation-after-identity`
- `evidence/execution-time-delegation`
- `profiles/trust-registry-governance-model`
- `evidence/the-proof-gap`

Together these packages make it easier to model not only who may act, but whether that authority remains governable at the moment of action.
