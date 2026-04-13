# Systemic Controller Registry Entry

## Overview

Captures hidden control levers as explicit registry entries so they can be enumerated, scoped, and audited.

---

## Source

- Essay: *Systemic Controllers: How Hidden Levers in Digital Infrastructure Create Real-World Risk*
- Published: 2025-12-09
- Canonical link: https://thetrustgraph.substack.com/p/systemic-controllers-how-hidden-levers

---

## Problem

- Power is often exercised through hidden configuration levers.
- Affected parties cannot see who can override or reclassify.
- Incident response lacks a stable control inventory.

---

## Model

- Controller identity and lever class.
- Affected systems and authority basis.
- Override conditions.
- Risk tags and redress contact.

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

This artifact now includes a TSMM projection at `bindings/tsmm/projections/systemic-controllers.yaml`. The binding externalizes entities, relationships, controls, evidence, trust decisions, effects, and lifecycle semantics so the artifact can be compared as part of a wider trust-system model.
