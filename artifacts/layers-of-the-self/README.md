# Contextual Identity Projection

## Overview

This artifact formalizes the idea that identity should not be treated as a monolith. Systems need bounded projections of self that reveal only the role, attributes, and linkage semantics required for the current interaction.

The artifact defines a governed projection model for contextual disclosure.

---

## Source

- Essay: *Layers of the Self*
- Published: 2026-01-12
- Canonical link: pending external link

---

## Problem

When systems demand a full identity where only a role or narrow attribute set is required, they create unnecessary disclosure, mis-scoped authority, and durable linkage that the interaction did not justify.

Without explicit projection structure, privacy and governance degrade together.

---

## Model

This artifact defines an identity projection with:

- a **base identity** from which projection is derived
- an **active role** for the current interaction
- a **context** describing where the projection is valid
- an **attribute subset** governing what is disclosed
- a **disclosure policy** describing when and to whom it may be presented
- **linkage rules** that determine whether the projection can be correlated back to the base identity
- lifecycle controls such as expiry and invalidation

---

## Governance Impact

### Authority

Authority is bound to the active role and context, not inferred from full identity disclosure.

### Delegation

Projection may be issued or carried by a wallet or agent, but only within declared policy.

### Enforcement

Systems can check whether requested disclosure exceeds the allowed projection.

### Revocation

A projection can be withdrawn, expired, or narrowed without destroying the base identity.

### Redress

Improper linkage or over-disclosure can be contested against the declared policy.

---

## Status

Draft

---

## Next Steps

- define correlation resistance levels
- add projection composition rules for multi-role interactions
- add invalid examples for over-disclosure and wrong-context use
