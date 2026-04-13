# Consent Enforcement Schema

## Overview

This artifact formalizes the claim that consent is not meaningful when stored as static record alone. Consent only becomes governance when it constrains what may happen at execution time.

The artifact binds subject, controller, purpose, permitted actions, contextual constraints, revocation, and audit into a single governed structure.

---

## Source

- Essay: *Consent Is Not a Data Structure*
- Published: 2026-01-09
- Canonical link: pending external link

---

## Problem

Many systems treat consent as a flag or receipt captured once and reused indefinitely. That breaks because the operational question is not whether consent once existed. It is whether the current action remains authorized under current purpose, scope, actor, and context.

Without a stronger model, systems retain a record of apparent permission while continuing to act beyond legitimate authority.

---

## Model

This artifact defines a consent object with:

- a **subject** whose authority is at stake
- a **controller** requesting or exercising permission
- a **purpose binding** that narrows legitimate use
- an explicit set of **permitted actions**
- **constraints** for time, jurisdiction, and data category
- **enforcement and revocation endpoints**
- an **audit reference** to make use visible and contestable

The point is not only representation. The point is runtime admissibility.

---

## Governance Impact

### Authority

Authority remains with the subject and only extends to the controller within explicit scope.

### Delegation

Delegated processing must inherit the same constraints or fail validation.

### Enforcement

Actions can be evaluated against purpose, actor, and context before execution.

### Revocation

Revocation is explicit and must propagate to downstream use.

### Redress

Audit and challenge are required to contest improper action.

---

## Status

Draft

---

## Next Steps

- add downstream processor inheritance semantics
- define revocation propagation behavior
- add invalid examples for purpose drift and expired consent
