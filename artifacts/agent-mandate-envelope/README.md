# Agent Mandate Envelope

## Overview

Defines the mandate boundary for an agent in terms of permitted actions, prohibited actions, escalation rules, and evidence duties.

---

## Source

- Essay: *Your Agents Are Not Failing. Your Mandates Are*
- Published: 2026-02-26
- Canonical link: https://thetrustgraph.substack.com/p/your-agents-are-not-failing-your

---

## Problem

- Agent evaluation often ignores mandate quality.
- Underspecified missions create preventable autonomy failures.
- Post-hoc audits do not repair bad mandate design.

---

## Model

- Mandate issuer and accountable owner.
- Permitted and prohibited action classes.
- Escalation thresholds and evidence requirements.
- Sunset and rollback references.

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

This artifact now includes a TSMM projection at `bindings/tsmm/projections/agent-mandate-envelope.yaml`. The binding externalizes entities, relationships, controls, evidence, trust decisions, effects, and lifecycle semantics so the artifact can be compared as part of a wider trust-system model.
