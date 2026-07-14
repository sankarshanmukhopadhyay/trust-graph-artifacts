---
layout: default
title: Supplier Assessment Example
parent: Agentic Systems Architecture and Governance
nav_order: 6
---

# Worked Example: Multi-Agent Supplier Assessment

This example shows how multiple agents can deliver a useful procurement-support job without granting any agent general procurement authority. The system assesses one supplier and produces a non-binding recommendation for a human procurement committee.

## 1. Job definition

| Dimension | Definition |
|---|---|
| Principal | Enterprise procurement function |
| Persistent coordinator role | Supplier Assessment Coordinator |
| Outcome | Signed recommendation record with evidence, confidence, dissent, and unresolved risks |
| Explicit non-outcomes | No contract signature, purchase order, payment, or supplier commitment |
| Risk tier | Medium by default; high when sensitive data, security exceptions, sanctions, or material financial exposure are involved |
| Completion condition | Recommendation stored, evidence complete, committee notified, temporary capabilities revoked |

## 2. Agent topology

```text
Procurement Principal
        ↓ mandate
Supplier Assessment Coordinator
        ├── Financial Analysis Agent
        ├── Security and Privacy Review Agent
        ├── Legal Terms Review Agent
        └── Sustainability Evidence Agent
                    ↓
            Convergence Review
                    ↓
         Non-binding Recommendation
                    ↓
        Human Procurement Committee
```

## 3. Authority allocation

| Role | Authority received | Capability granted | Prohibited effect |
|---|---|---|---|
| Coordinator | Delegate bounded analyses and compose recommendation | Create branch tasks; read approved branch outputs; write draft recommendation | Cannot commit funds or bind the enterprise |
| Financial agent | Evaluate named supplier financial evidence | Read specified reports; calculate bounded indicators | Cannot retrieve unrelated company data or contact supplier |
| Security agent | Evaluate supplied security and privacy evidence | Read named attestations; query approved control catalog | Cannot access production systems |
| Legal agent | Identify clause deviations from approved template | Read contract draft and clause library | Cannot accept or alter terms |
| Sustainability agent | Assess provided sustainability evidence | Read named disclosures and approved public sources | Cannot issue public claims |
| Convergence workflow | Compare outputs and produce candidate recommendation | Read branch receipts and write candidate action object | Cannot execute commercial action |

## 4. Execution sequence

| Step | System behaviour | Evidence |
|---|---|---|
| 1. Job activation | Authorized requester creates the job and binds supplier, purpose, risk tier, and deadline. | Job activation receipt |
| 2. Mandate verification | Coordinator resolves mandate, status, permitted effects, and delegation depth. | Mandate verification receipt |
| 3. Branch creation | Four child delegations receive distinct scopes, data boundaries, and expiry. | Four lineage hop records |
| 4. Capability issuance | Each branch receives only required read or compute capabilities. | Capability grant receipts |
| 5. Branch execution | Each branch returns result, evidence, confidence, limitations, and execution receipt. | Branch execution receipts |
| 6. Return review | Coordinator verifies lineage, schema validity, evidence sufficiency, and dissent. | Return-review record |
| 7. Convergence check | Workflow confirms combined recommendation remains non-binding and creates no prohibited inference. | Aggregate-effect decision receipt |
| 8. Candidate action | Recommendation object is created with unresolved risks and approval routing. | Candidate action digest |
| 9. Effect admission | Policy permits writing the recommendation but denies procurement commitment. | Policy decision receipt |
| 10. Evidence closure | Receipts are linked, capabilities revoked, and committee receives authorized view. | Evidence bundle and revocation receipts |
| 11. Challenge and correction | Reviewer may challenge evidence or rerun a branch without reopening unrelated authority. | Challenge and correction records |

## 5. Evidence bundle

- Root mandate and status proof.
- Four child delegation hop records.
- Four capability grant receipts.
- Four branch execution receipts.
- Branch evidence references, confidence statements, and limitations.
- Convergence and aggregate-authority result.
- Policy decision receipt for the recommendation effect.
- Final execution receipt and committee notification.
- Capability revocation receipts.
- Challenge endpoint and retention policy.

## 6. Failure demonstrations

| Injected failure | Expected control result |
|---|---|
| Financial agent requests raw access to unrelated supplier records | Capability broker denies resource expansion |
| Legal agent attempts to delegate contract acceptance | Lineage verifier rejects scope expansion and prohibited subdelegation |
| Security evidence expires during execution | Effect admission pauses and requires re-verification |
| Two branches disclose fields that together reveal a prohibited profile | Convergence review blocks aggregate disclosure |
| Coordinator mandate is revoked after branches begin | Propagation service interrupts branches and prevents final recommendation write |
| Requester changes purpose from assessment to negotiation | System requires a new mandate or explicit amendment; refresh cannot broaden purpose |

## 7. TSMM, TGA, and TIS trace

| Concern | TSMM | TGA | TIS |
|---|---|---|---|
| Principal, roles, effects | Instance model and effect-centred decision model | Job and runtime governance guidance | Boundary records |
| Root mandate | Authority and policy concepts | Agent mandate envelope | Authority-boundary schema |
| Four branches | Fan-out delegation pattern | Delegation lineage envelope and tests | Delegation-lineage schema |
| Capability grants | Authority/capability distinction | Execution-time delegation | Execution and authority records |
| Convergence | Fan-out and effect semantics | Aggregate-effect negative tests | Verification result fields |
| Evidence closure | Evidence and lifecycle concepts | Proof-carrying receipts | Portable receipts and lifecycle records |

## 8. Acceptance criteria

The example is successfully implemented when:

- a valid recommendation can be produced end to end;
- no agent can commit funds, sign a contract, or contact a supplier;
- every branch is reconstructable from the root mandate;
- every capability is narrower than its authority;
- aggregate disclosure and inference are evaluated;
- revocation prevents final effect admission;
- an independent verifier can reconstruct the recommendation from the evidence bundle.
