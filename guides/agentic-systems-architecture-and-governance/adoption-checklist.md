---
layout: default
title: Adoption Checklist
parent: Agentic Systems Architecture and Governance
nav_order: 4
permalink: /guides/agentic-systems-architecture-and-governance/adoption-checklist/
---

# Adoption and Production-Readiness Checklist

## Discovery and scope

- [ ] Bounded job and business owner are named.
- [ ] Consequential effects and prohibited effects are catalogued.
- [ ] Human or institutional fallback is defined.
- [ ] Risk tier and affected parties are recorded.

## Authority architecture

- [ ] Every persistent role resolves to a principal or authority source.
- [ ] Mandates are machine-readable, current, testable, and revocable.
- [ ] Delegation depth and subdelegation rights are explicit.
- [ ] Trust-domain boundaries are documented.

## Execution controls

- [ ] Model output is a candidate action, not a tool instruction.
- [ ] Policy decision and enforcement are separate.
- [ ] Consequential tools are reachable only through enforcement points.
- [ ] Capability grants are resource-, operation-, parameter-, purpose-, and time-bound.
- [ ] Human approval is bound to the exact action digest.

## Multi-agent controls

- [ ] Every child delegation has a parent reference and attenuated scope.
- [ ] Branches receive only necessary data and capability.
- [ ] Convergence checks combined authority, data exposure, inference, and dissent.
- [ ] Refresh cannot alter principal, purpose, scope, or revocation relationships.

## Evidence and lifecycle

- [ ] Mandate, lineage, policy, capability, and execution receipts are produced.
- [ ] Evidence is retrievable by authorized reviewers.
- [ ] Retention and selective disclosure are implemented.
- [ ] Revocation reaches known descendants.
- [ ] In-flight interruption and completed-effect remediation are exercised.
- [ ] Challenge and correction routes are discoverable.

## Jekyll and publication readiness

- [ ] Every documentation page has valid YAML front matter.
- [ ] Permalinks are stable and unique.
- [ ] Internal links and anchors validate.
- [ ] Mermaid diagrams have text alternatives or surrounding explanation.
- [ ] Tables are usable on narrow screens.
- [ ] Site builds with strict front matter.
- [ ] Raw Markdown remains understandable outside the generated site.

## Production gate

- [ ] All required schemas validate.
- [ ] All mandatory negative tests pass.
- [ ] No consequential tool bypass exists.
- [ ] Operational metrics and alerts are active.
- [ ] ADRs, runbooks, and ownership are current.
- [ ] An independent reviewer can reconstruct one effect end to end.
