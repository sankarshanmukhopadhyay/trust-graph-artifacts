---
layout: default
title: Architecture Decisions
parent: Agentic Systems Architecture and Governance
nav_order: 3
permalink: /guides/agentic-systems-architecture-and-governance/architecture-decisions/
---

# Architecture Decision Record Set

Every ADR should state the decision, authority, alternatives, trade-offs, testability, evidence produced, revocation implications, migration impact, and repository mappings.

| ADR | Decision topic | Minimum acceptance evidence |
|---|---|---|
| ADR-001 | Persistent roles and ephemeral workloads | role lifecycle diagram and attribution test |
| ADR-002 | Principal and authority-source model | TSMM instance and authority map |
| ADR-003 | Mandate format and lifecycle | valid, expired, revoked, and amended fixtures |
| ADR-004 | Effect admission and policy decision architecture | state machine and decision receipts |
| ADR-005 | Delegation topology and lineage | valid and invalid lineage corpus |
| ADR-006 | Scope attenuation and authority expansion | formal comparison rule and tests |
| ADR-007 | Capability issuance and enforcement | broker contract and bypass test |
| ADR-008 | Transaction and intent binding | replay and substitution tests |
| ADR-009 | Fan-out, convergence, and dissent | aggregate-effect and dissent tests |
| ADR-010 | Evidence, custody, and selective disclosure | evidence manifest and authorized-view test |
| ADR-011 | Status, revocation, interruption, remediation | lifecycle exercise results |
| ADR-012 | Human approval and escalation | exact-digest binding test |
| ADR-013 | Trust-domain translation | no-expansion translation receipt |
| ADR-014 | Local policy admission | accept, narrow, refuse, and escalate cases |
| ADR-015 | Conformance target and release gates | CI workflow and release evidence |
| ADR-016 | Model, tool, and vendor substitution | replacement test without authority-semantic change |

Use the [ADR template]({% link guides/agentic-systems-architecture-and-governance/templates/adr-template.md %}).
