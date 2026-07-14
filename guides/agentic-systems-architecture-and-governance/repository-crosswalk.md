---
layout: default
title: Repository Crosswalk
parent: Agentic Systems Architecture and Governance
nav_order: 2
permalink: /guides/agentic-systems-architecture-and-governance/repository-crosswalk/
---

# Repository Crosswalk

Use the crosswalk to trace each design decision from semantics to governance controls, portable contracts, implementation components, tests, and runtime evidence.

| Design need | TSMM | TGA | TIS | Implementation output | Evidence |
|---|---|---|---|---|---|
| define actors and effects | core entity, relationship, decision and effect model | quickstart and governance packages | authority and runtime projections | instance model and effect catalog | architecture baseline |
| define root authority | authority source and policy concepts | agent mandate envelope | authority-boundary schema | mandate service and policy rules | mandate receipt |
| govern direct delegation | delegated-agent pattern | delegation-after-identity | artifact references | delegated task contract | delegation receipt |
| govern multi-hop authority | chained-delegation pattern | delegation-lineage envelope | lineage and verification schemas | lineage service | lineage verification |
| govern parallel work | fan-out pattern | lineage tests and delegation-first controls | branch and convergence fields | branch manager and convergence gate | convergence receipt |
| mediate technical power | authority/effect separation | runtime authority and execution-time delegation | capability and execution contracts | broker and enforcement points | grant and execution receipts |
| handle lifecycle | lifecycle and authority graph | revocation dynamics and lifecycle mediation | status and lifecycle events | revocation service | propagation receipt |
| preserve evidence | evidence and decision concepts | proof-carrying receipts | receipt schemas | evidence store | evidence bundle |

## Architect reading order

1. TSMM implementer guidance and core model.
2. TSMM effect-centred decision and delegation patterns.
3. TGA quickstart and delegation governance guidance.
4. TGA mandate, runtime authority, delegation lineage, receipt, and revocation packages.
5. TIS authority-boundary, delegation-lineage, verification, and execution schemas.
6. This guide's templates, examples, and negative test suite.

## Traceability rule

For every consequential control, record:

```text
TSMM concept
  → TGA pattern or assurance case
  → TIS schema or validation contract
  → implementation component
  → positive and negative tests
  → runtime evidence
```

The machine-readable form is maintained in [crosswalk.yaml]({% link guides/agentic-systems-architecture-and-governance/crosswalk.yaml %}).
