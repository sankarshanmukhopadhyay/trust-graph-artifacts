---
layout: default
title: Architecture Decisions
parent: Agentic Systems Architecture and Governance
nav_order: 3
---

# Architecture Decision Set

Complete these Architecture Decision Records before production deployment. Each ADR should state the decision, authority source, alternatives, trade-offs, testability, evidence, revocation implications, and migration impact.

| ADR | Decision topic | Minimum evidence |
|---|---|---|
| ADR-001 | Persistent roles and ephemeral workload instances | Role catalog and workload lifecycle test |
| ADR-002 | Principal and authority-source model | Authority map and non-self-authorization test |
| ADR-003 | Mandate format and lifecycle | Valid, expired, suspended, and revoked fixtures |
| ADR-004 | Effect-admission and policy decision architecture | Effect matrix and decision receipts |
| ADR-005 | Delegation topology and lineage representation | Topology model and lineage verification |
| ADR-006 | Scope attenuation and authority expansion | Formal invariant and negative tests |
| ADR-007 | Capability issuance and enforcement points | Enforcement map and bypass test |
| ADR-008 | Transaction and intent binding | Binding fields and replay test |
| ADR-009 | Fan-out, convergence, and dissent handling | Branch manifest and aggregate-effect test |
| ADR-010 | Evidence, receipts, custody, and selective disclosure | Evidence chain and access test |
| ADR-011 | Status, revocation, interruption, and remediation | Live propagation and recovery exercise |
| ADR-012 | Human approval and escalation | Exact-action approval binding test |
| ADR-013 | Trust-domain translation | Translation record and non-expansion proof |
| ADR-014 | Local policy admission | Accept, narrow, deny, and escalate tests |
| ADR-015 | Conformance target and release gates | CI evidence and release checklist |
| ADR-016 | Model, tool, and vendor substitution boundaries | Substitution test preserving governance controls |

## ADR template

```markdown
# ADR-NNN: Decision title

## Status
Proposed | Accepted | Superseded | Retired

## Context
Describe the bounded job, affected effects, authority relationships, and operational constraints.

## Decision
State the selected architecture and the responsible authority for approving it.

## TSMM basis
Identify the semantic concepts and instance elements used.

## TGA basis
Identify the governance patterns, threats, assurance cases, and test vectors used.

## TIS basis
Identify the schemas, required fields, and validation boundaries used.

## Alternatives considered
Document viable alternatives and why they were rejected.

## Enforcement
Identify the policy decision and policy enforcement points.

## Testability
List positive, negative, lifecycle, and adversarial tests.

## Evidence
Identify the receipts and records produced during operation.

## Revocation and failure behaviour
Explain suspension, propagation, interruption, remediation, and safe degradation.

## Migration impact
State how implementations and evidence remain valid if models, tools, schemas, or policies change.
```

## Decision quality gate

An ADR is incomplete when it describes only software components. It must also answer:

- Who has authority to make or change the decision?
- What system effect is controlled?
- What is enforced at runtime?
- What can be tested?
- What evidence is produced?
- How can the control be revoked or superseded?
- What happens when evidence is missing or state is unknown?
