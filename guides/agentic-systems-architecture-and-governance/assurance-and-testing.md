---
layout: default
title: Assurance and Testing
parent: Agentic Systems Architecture and Governance
nav_order: 5
permalink: /guides/agentic-systems-architecture-and-governance/assurance-and-testing/
---

# Assurance and Testing Strategy

A system that demonstrates only successful agent execution has not demonstrated governance. Testing must prove that valid work succeeds and invalid authority fails safely.

## Test layers

| Layer | What is tested | Evidence |
|---|---|---|
| Schema conformance | mandates, hops, receipts, status events, examples | validator output and fixtures |
| Semantic invariants | principal continuity, attenuation, transaction binding, freshness | invariant report |
| Policy behavior | permit, deny, narrow, downgrade, escalate | policy coverage and receipts |
| Enforcement | broker bypass, resource and parameter boundaries, replay | integration and penetration evidence |
| Lifecycle | expiry, suspension, revocation, interruption, remediation | lifecycle event chain |
| Adversarial | prompt injection, forged lineage, stale evidence, aggregation amplification | negative corpus |
| Operational assurance | evidence availability, selective disclosure, reconstruction, challenge | exercise report |

## Mandatory negative tests

1. authenticated actor with no mandate;
2. expired mandate with still-valid technical token;
3. missing intermediate delegation hop;
4. changed originating principal;
5. scope expansion at a child hop;
6. refresh changing purpose or removing constraints;
7. trust-domain translation broadening access;
8. valid branches aggregating into an unauthorized effect;
9. revocation reaching only some descendants;
10. capability request broader than the approved action;
11. model attempting direct tool invocation;
12. receipt with unavailable evidence;
13. human approval reused for a different digest;
14. valid delegation failing local policy admission;
15. replay of a previously valid capability;
16. branch dissent omitted from convergence evidence.

## Assurance evidence bundle

A release evidence bundle should include:

- architecture baseline and repository revisions;
- TSMM instance model;
- TIS validation output;
- TGA control and threat mappings;
- positive and negative fixture results;
- policy and enforcement coverage;
- revocation and remediation exercise;
- evidence reconstruction report;
- known limitations and residual risk;
- migration and rollback plan.
