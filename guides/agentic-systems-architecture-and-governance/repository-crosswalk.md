---
layout: default
title: Repository Crosswalk
parent: Agentic Systems Architecture and Governance
nav_order: 2
---

# Repository Crosswalk

This crosswalk identifies the primary TSMM, TIS, and TGA inputs for each design need. Repository paths may evolve; implementation baselines should pin the exact revision used.

| Design need | TSMM | TGA | TIS |
|---|---|---|---|
| Define the system and effects | Core model; effect-centred trust-decision model | Quickstart; executable-governance packages | Artifact and evidence contracts used by the selected profile |
| Model persistent agent participation | Agentic extension; entity and relationship model | Agent-accountability and runtime-authority patterns | Authority-boundary and runtime projection schemas |
| Define root authority | Authority and policy concepts | `artifacts/agent-mandate-envelope/`; `patterns/agent-mandate-envelope/` | `governance/authority-boundary.schema.json` |
| Govern direct delegation | Delegated-agent pattern | `patterns/delegation-after-identity/` | Authority-boundary and artifact references |
| Govern multi-hop delegation | Chained-delegation pattern | `patterns/delegation-lineage-envelope/` | `delegation/delegation-lineage.schema.json` |
| Govern parallel branches | Fan-out delegation pattern | Delegation lineage tests; delegation-first profile | Delegation verification and branch/convergence fields |
| Evaluate runtime authority | Trust-decision and effect model | `patterns/runtime-authority-envelope/` | Runtime governance projection and verification records |
| Record execution | Effect and evidence model | `artifacts/execution-time-delegation/`; proof-carrying receipts | Trust-task execution receipt |
| Handle revocation | Lifecycle and authority graph | Revocation dynamics; commitment-lifecycle mediation | Lifecycle events and lineage verification |
| Validate adoption | Conformance guidance | Validation scripts, assurance cases, and negative fixtures | Schema validators and examples |

## Reading sequence

### Step 1: Establish semantics in TSMM

Read the implementer guide, core model, authority and policy concepts, effect-centred decision model, and delegation patterns. Produce a TSMM instance describing the job, principals, roles, authority edges, decisions, evidence, effects, and lifecycle.

### Step 2: Select governance patterns in TGA

Start with:

- [`../../docs/quickstart.md`](../../docs/quickstart.md)
- [`../../docs/delegation-governance.md`](../../docs/delegation-governance.md)
- [`../../artifacts/agent-mandate-envelope/`](../../artifacts/agent-mandate-envelope/)
- [`../../patterns/runtime-authority-envelope/`](../../patterns/runtime-authority-envelope/)
- [`../../patterns/delegation-lineage-envelope/`](../../patterns/delegation-lineage-envelope/)
- [`../../profiles/delegation-first-governance-profile/`](../../profiles/delegation-first-governance-profile/)
- [`../../artifacts/execution-time-delegation/`](../../artifacts/execution-time-delegation/)
- [`../../evidence/proof-carrying-commitment-receipt/`](../../evidence/proof-carrying-commitment-receipt/)

Select the smallest set of patterns that covers the job's effects and failure modes.

### Step 3: Adopt TIS contracts

Use TIS schemas for authority boundaries, delegation lineage, lineage verification, lifecycle records, and execution receipts. Validate every stored and exchanged artifact at system boundaries, not only in unit tests.

### Step 4: Trace design decisions

For every implementation control, maintain a trace to:

1. the TSMM semantic concept;
2. the TGA governance pattern or assurance case;
3. the TIS schema or validation rule;
4. the implementation component;
5. the positive and negative tests;
6. the evidence produced in operation.

## Traceability record template

```yaml
control_id: CTRL-DELEGATION-001
objective: prevent authority expansion across agent delegation
semantic_basis:
  repository: TSMM
  concept: chained delegation and authority attenuation
governance_basis:
  repository: TGA
  artifact: patterns/delegation-lineage-envelope
contract_basis:
  repository: TIS
  artifact: delegation/delegation-lineage.schema.json
implementation:
  component: lineage-verifier
  enforcement_point: delegation-admission-api
tests:
  positive:
    - valid-linear-chain
  negative:
    - invalid-scope-expansion
    - invalid-principal-substitution
evidence:
  - delegation-lineage-verification
owner: authority-platform-team
```
