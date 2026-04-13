# Execution Delegation Control Receipt

## Overview

Captures a decision receipt for delegated actions at execution time, binding authority basis, control checks, and outcome into a structured record.

---

## Source

- Essay: *Execution-Time Delegation: Legitimacy After Transparency*
- Published: 2026-03-05
- Canonical link: https://thetrustgraph.substack.com/p/execution-time-delegation-legitimacy

---

## Problem

- Transparency alone does not establish legitimate control.
- Delegated action is often logged without explaining control state.
- Revocation timing during execution is rarely captured.

---

## Model

- Authority basis and policy version.
- Pre-execution control checks.
- Outcome and reversibility class.
- Challenge reference.

---

## Governance Impact

### Authority

Authority is made explicit in the schema and manifest rather than inferred from surrounding context.

### Delegation

Delegated behavior is bounded by declared fields, conditions, and lifecycle controls.

### Enforcement

The artifact is designed to support deterministic checks rather than narrative interpretation alone.

### Revocation

The artifact includes status or lifecycle controls that can narrow, suspend, or withdraw its effect.

### Redress

A structured path exists for challenge, correction, or appeal where the concept requires it.

---

## Status

Draft

---

## Next Steps

- refine field cardinality and enum coverage
- add JSON Schema or equivalent validation form
- add richer edge-case examples
