---
layout: default
title: Maturity Model
parent: Agentic Systems Architecture and Governance
nav_order: 6
permalink: /guides/agentic-systems-architecture-and-governance/maturity-model/
---

# Agentic Governance Maturity Model

Use this model to assess an existing system and plan a staged adoption path.

| Level | Name | Characteristics | Minimum evidence |
|---|---|---|---|
| L0 | Unmediated | model holds credentials or calls tools directly; authority is implicit | ordinary application logs only |
| L1 | Attributable | named persistent roles; structured actions; execution recorded | role catalog and execution events |
| L2 | Bounded | mandates, policy decisions, capability mediation, explicit effects | mandate and policy receipts |
| L3 | Delegation-aware | multi-hop lineage, attenuation, fan-out checks, portable evidence | lineage verification and convergence receipts |
| L4 | Recoverable | cross-domain verification, revocation propagation, interruption, remediation | lifecycle exercise and remediation evidence |
| L5 | Continuously assured | independent verification, CI conformance, operational metrics, controlled change | recurring assurance reports and release evidence |

## Assessment dimensions

Score each dimension from 0 to 5 and use the lowest consequential dimension as the effective level.

1. authority explicitness;
2. capability mediation;
3. delegation lineage;
4. effect admission;
5. evidence portability;
6. revocation and recovery;
7. cross-domain interoperability;
8. operational assurance.

## Recommended adoption path

- Move from L0 to L1 by naming roles and structuring actions.
- Move to L2 before permitting financial, legal, privacy-sensitive, or externally binding effects.
- Move to L3 before using multi-agent or cross-service delegation.
- Move to L4 before relying on external trust domains or persistent downstream effects.
- Move to L5 for regulated, rights-affecting, safety-relevant, or ecosystem-scale deployments.
