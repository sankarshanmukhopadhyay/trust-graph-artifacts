---
layout: default
title: Repository Crosswalk
parent: Agentic Systems Architecture and Governance
nav_order: 2
permalink: /guides/agentic-systems-architecture-and-governance/repository-crosswalk/
---

# Repository Crosswalk

Use the crosswalk to trace each design decision from semantics to governance controls, portable contracts, optional protocol realization, implementation components, tests, and runtime evidence.

| Design need | TSMM | TGA | TIS | Optional ARPA realization | Implementation output | Evidence |
|---|---|---|---|---|---|---|
| define actors and effects | core entity, relationship, decision and effect model | quickstart and governance packages | authority and runtime projections | ARPA-Core identifies persistent agents; ARPA-Authority records authority decisions | instance model and effect catalog | architecture baseline |
| define root authority | authority source and policy concepts | agent mandate envelope | authority-boundary schema | ARPA-Relations + ARPA-Authority | mandate service and policy rules | mandate receipt |
| govern direct delegation | delegated-agent pattern | delegation-after-identity | artifact references | ARPA-Authority Authority Envelope | delegated task contract | delegation receipt |
| govern multi-hop authority | chained-delegation pattern | delegation-lineage envelope | lineage and verification schemas | ARPA-Authority scoped delegation with relationship context | lineage service | lineage verification |
| govern parallel work | fan-out pattern | lineage tests and delegation-first controls | branch and convergence fields | ARPA may carry per-branch authority state; convergence remains a guide/runtime responsibility | branch manager and convergence gate | convergence receipt |
| mediate technical power | authority/effect separation | runtime authority and execution-time delegation | capability and execution contracts | ARPA-Assurance can verify capability claims; ARPA-Authority determines permission | broker and enforcement points | grant and execution receipts |
| handle lifecycle | lifecycle and authority graph | revocation dynamics and lifecycle mediation | status and lifecycle events | ARPA-Core lifecycle + ARPA-Authority revocation + ARPA-Evidence convergence evidence | revocation service | propagation receipt |
| preserve evidence | evidence and decision concepts | proof-carrying receipts | receipt schemas | ARPA-Evidence reconstruction and retention | evidence store | evidence bundle |
| cross governance domains | trust registry and authority concepts | trust-boundary and recognition patterns | registry / portable references | ARPA-Federation | federation/recognition policy | recognition decision evidence |
| contest and repair outcomes | redress | contestability and remediation patterns | decision/evidence references | ARPA authority/evidence redress surfaces | review and remediation service | challenge/remediation record |

## Authority direction

The crosswalk is intentionally asymmetric:

```text
TSMM semantic concept
  → TGA governance pattern / assurance requirement
  → TIS portable contract when needed
  → optional ARPA protocol realization for registry/control-plane responsibilities
  → implementation component
  → positive and negative tests
  → runtime evidence
```

ARPA is not the semantic authority for the guide and is not required for guide adoption. Where ARPA is used, its own specification remains authoritative for ARPA module semantics and conformance.

## Non-implication rules

Any ARPA-aligned implementation of this guide must preserve these invariants:

1. discovery != authorization;
2. authentication != authority;
3. registration != permission to act;
4. capability != legitimate authority;
5. relationship != delegated authority;
6. technical federation != governance recognition;
7. successful execution != legitimate effect.

These rules should be represented as negative tests, not merely architecture prose.

## Architect reading order

1. TSMM implementer guidance and core model.
2. TSMM effect-centred decision and delegation patterns.
3. TGA quickstart and delegation governance guidance.
4. TGA mandate, runtime authority, delegation lineage, receipt, and revocation packages.
5. TIS authority-boundary, delegation-lineage, verification, and execution schemas.
6. If an agent registry/control plane is required, ARPA design principles and protocol modules.
7. This guide's templates, examples, and negative test suite.

## Traceability rule

For every consequential control, record:

```text
TSMM concept
  → TGA pattern or assurance case
  → TIS schema or validation contract
  → optional protocol realization such as ARPA
  → implementation component
  → positive and negative tests
  → runtime evidence
```

The machine-readable guide form is maintained in [crosswalk.yaml]({% link guides/agentic-systems-architecture-and-governance/crosswalk.yaml %}); the ARPA-specific alignment is maintained in [`bindings/arpa/tga-arpa-agentic-governance-alignment.json`]({% link bindings/arpa/tga-arpa-agentic-governance-alignment.json %}).
