---
layout: default
title: Cross-Domain Disputed Transaction
parent: Worked Examples
grand_parent: Agentic Systems Architecture and Governance
nav_order: 3
permalink: /guides/agentic-systems-architecture-and-governance/examples/cross-domain-agent-workflow/
---

# Cross-Domain Disputed Transaction

## Job

Investigate one disputed transaction across a customer service domain, payment operations domain, and external fraud-analysis domain. Produce a recommendation; do not issue a refund without separate approval.

## Critical boundary

The original authority permits review of one transaction. The external fraud domain must not translate that into standing access to transaction history.

## Sequence

```mermaid
sequenceDiagram
  participant C as Case Coordinator
  participant P as Payment Review Agent
  participant T as Scope Translator
  participant F as External Fraud Agent
  participant V as Lineage Verifier
  C->>P: Delegate single-transaction verification
  P->>T: Request cross-domain scope translation
  T->>V: Prove translated scope is equal or narrower
  V-->>T: Pass / fail with invariant results
  T->>F: Issue transaction-bound request
  F-->>P: Risk assessment and evidence receipt
  P-->>C: Bounded result; no standing access
```

## Required translation record

- source and target trust domains;
- source and target vocabularies;
- original and translated scope;
- preserved, narrowed, dropped, and unresolved elements;
- translator identity;
- no-expansion result;
- status and revocation references.

## Negative demonstrations

- destination token grants transaction-history access: fail;
- translation cannot represent no-retention: refuse or use controlled interface;
- external agent returns a recommendation without evidence: indeterminate and escalate;
- original mandate revoked during review: interrupt and propagate status.
