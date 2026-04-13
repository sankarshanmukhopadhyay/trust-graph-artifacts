# Narrative Contestability Record

## Overview

Formalizes how a person or institution contests a machine-generated narrative by supplying contextual correction, affected decision context, and requested remedy.

---

## Source

- Essay: *Crisis of Narrative Control*
- Published: 2026-02-09
- Canonical link: https://thetrustgraph.substack.com/p/crisis-of-narrative-control

---

## Problem

- Systems construct narratives from fragments without narrative competence.
- People rarely see or can correct the operative system narrative.
- Misclassification becomes durable across domains.

---

## Model

- Contested narrative claim.
- Decision context.
- Correction statement and evidence links.
- Requested remedy and review status.

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

This artifact now includes a TSMM projection at `bindings/tsmm/projections/crisis-of-narrative-control.yaml`. The binding externalizes entities, relationships, controls, evidence, trust decisions, effects, and lifecycle semantics so the artifact can be compared as part of a wider trust-system model.
