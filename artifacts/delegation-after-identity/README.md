# Delegation Chain Policy

## Overview

Separates identity from authority transfer by formalizing delegation as a bounded chain with scope, conditions, and revocation checks.

---

## Source

- Essay: *Delegation After Identity*
- Published: 2026-02-18
- Canonical link: https://thetrustgraph.substack.com/p/delegation-after-identity

---

## Problem

- Identity proof does not express usable authority.
- Delegation chains become opaque as agent systems compose.
- Revocation propagation is often underspecified.

---

## Model

- Principal-to-agent chain structure.
- Scope and condition constraints at each hop.
- Subdelegation limits.
- Live revocation and challenge hooks.

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
