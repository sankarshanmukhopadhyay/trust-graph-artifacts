---
owner: maintainers
last_reviewed: 2026-05-06
applicable_version: v0.2.0
---

# Receipts

Receipts are first-class artifacts and the evidence surface that proves a governance system executed as claimed. They are not narrative notes. They are machine-readable records of authority, delegation, revocation, licensing, enforcement, and decisions at execution time.

TGA receipt schemas live under `schemas/receipts/`. Examples live under `examples/receipts/`.

## Receipt classes

| Receipt | Purpose |
|---|---|
| Decision receipt | Records what decision was made, why, which authority was relied on, which policy/evidence was evaluated, which boundary was implicated, and what operational effect was admitted or blocked. |
| Authority receipt | Proves the actor held valid authority at decision time. |
| Delegation receipt | Proves how authority moved from delegator to delegatee. |
| Revocation receipt | Records revocation and propagation status. |
| Licensing receipt | Proves eligibility and issuer authority. |
| Enforcement receipt | Shows how a rule was actually enforced. |

No artifact is complete unless it emits or references receipts.

## TSMM alignment for decision receipts

The TGA decision receipt is harmonized with the TSMM decision receipt model. TGA does not maintain a competing decision representation. Instead, it uses the TSMM runtime assurance core and adds a Trust Graph provenance layer.

| TSMM field | TGA representation | Governance purpose |
|---|---|---|
| `decisionId` | `decisionId` | Stable identifier for the decision event. |
| `timestamp` | `timestamp` | Time of decision or recording. |
| `subjectRef` | `subjectRef` | Effect, artifact, claim, actor, or request being decided. |
| `requestingActorRef` | `requestingActorRef` | Actor or agent requesting the effect. |
| `authorityBasis` | `authorityBasis` | Authority source, status, scope, and optional delegation/license references. |
| `policyRefs` | `policyRefs` | Policies applied during evaluation. |
| `evidenceRefs` | `evidenceRefs` | Evidence inspected during evaluation. |
| `boundaryRef` | `boundaryRef` | Trust boundary implicated by the decision. |
| `decision` | `decision` | Runtime outcome and reason. TGA may also include `decision.decisionType` as an essay-derived interpretation class. |
| `effect` | `effect` | Effect reference and admission state. TGA may also include control-plane step and transformation metadata. |
| `revocationStateChecked` | `revocationStateChecked` | Revocation status, check time, and source. |
| `assuranceLevel` | `assuranceLevel` | Assurance posture asserted by the receipt. |
| `reviewPath` | `reviewPath` | Where the decision can be challenged, reviewed, or escalated. |

## TGA-specific extension fields

| Field | Purpose |
|---|---|
| `receiptId` | Stable identifier for the receipt object itself. |
| `receiptType` | Fixed receipt class. For decision receipts this is `decision-receipt`. |
| `sourceEssays` | Essay provenance anchors explaining which Trust Graph analysis motivated the receipt model or interpretation. |
| `signature` | Optional proof envelope for signed receipts or external verification pipelines. |

## Representation rule

Use camelCase for the active decision receipt schema. Earlier snake_case fields such as `receipt_id`, `decision_id`, `authority_basis`, `policy_evaluation`, `execution_trace`, and `revocation_state` are legacy representation terms and should not be used for new active examples.

The old terms map as follows:

| Legacy TGA field | Active TSMM-aligned field |
|---|---|
| `receipt_id` | `receiptId` |
| `decision_id` | `decisionId` |
| `actor` | `requestingActorRef` |
| `decision_type` | `decision.decisionType` |
| `authority_basis` | `authorityBasis` |
| `policy_evaluation.policies_applied` | `policyRefs` |
| `policy_evaluation.constraints_checked` | `evidenceRefs` when backed by evidence, otherwise profile constraints |
| `execution_trace.control_plane_step` | `effect.controlPlaneStep` |
| `execution_trace.transformation_applied` | `effect.transformationApplied` |
| `revocation_state` | `revocationStateChecked` |

## Conformance expectation

A TGA decision receipt is conformant when it can answer five audit questions without additional narrative:

1. Who or what requested the effect?
2. What authority made the decision valid or invalid?
3. Which policies and evidence were evaluated?
4. Was revocation checked against a named source at a specific time?
5. What effect was admitted, blocked, restricted, or routed for review?


## TSMM v0.20 profile hardening

As of v0.2.0, TGA decision receipts are explicitly treated as TSMM-profiled receipts with Trust Graph provenance extensions. The schema `schemas/receipts/decision_receipt.schema.json` remains the active receipt contract. The schema `schemas/receipts/tsmm_profiled_decision_receipt.schema.json` makes the profile boundary visible for implementers and reviewers.

A receipt should not use essay provenance as runtime evidence. `sourceEssays` explains why a governance pattern was modeled; `evidenceRefs` identifies what was actually evaluated at execution time.

For vocabulary alignment, see:

- `docs/crosswalks/outcome-vocabulary.md`
- `docs/crosswalks/assurance-posture.md`
- `docs/crosswalks/tsmm-decision-receipt-profile.md`
