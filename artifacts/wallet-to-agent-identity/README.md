# Wallet-Agent Binding Contract

## Overview

Makes the wallet-to-agent binding explicit so that identity context becomes a bounded execution interface rather than an ambient permission source.

---

## Source

- Essay: *Wallet-to-Agent Identity: When Identity Becomes an Execution Interface*
- Published: 2026-02-11
- Canonical link: https://thetrustgraph.substack.com/p/wallet-to-agent-identity

---

## Problem

- Wallet identity often stops at authentication rather than execution control.
- Agents can inherit wallet context without binding rules.
- Session revocation is often too coarse or too late.

---

## Model

- Wallet principal and bound agent instance.
- Presentable credential classes and request types.
- Session controls and revocation endpoint.
- Evidence fields for each request.

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
