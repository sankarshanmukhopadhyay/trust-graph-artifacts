# Proof Requirement Profile

## Overview

Defines what proof a system requires before it can admit a claim, distinguishing truth-held-by-institutions from proof-usable-by-machines.

---

## Source

- Essay: *The Proof Gap*
- Published: 2026-03-16
- Canonical link: https://thetrustgraph.substack.com/p/the-proof-gap

---

## Problem

- Facts can exist without portable proof.
- Subjects often cannot present machine-verifiable evidence independently.
- Agentic systems need proof at execution speed.

---

## Model

- Claim class and accepted proof forms.
- Issuer legitimacy requirements.
- Freshness and revocation rules.
- Reason codes for proof insufficiency.

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

---

## TSMM Binding

This artifact now includes a TSMM projection at `bindings/tsmm/projections/the-proof-gap.yaml`. The binding externalizes entities, relationships, controls, evidence, trust decisions, effects, and lifecycle semantics so the artifact can be compared as part of a wider trust-system model.
