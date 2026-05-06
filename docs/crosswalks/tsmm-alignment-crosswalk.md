---
owner: maintainers
last_reviewed: 2026-05-06
applicable_version: v0.2.0
---

# TGA ↔ TSMM Alignment Crosswalk

This crosswalk defines how active Trust Graph Artifact repository surfaces map to TSMM v0.20 concepts.

| TGA surface | TSMM concept | Harmonization rule |
|---|---|---|
| `package.json` | Package-level model declaration | Describes the bounded trust-system interpretation and package type. |
| `graph.json` | TSMM trust-system graph | Represents entities, authorities, policies, evidence, decisions, and effects as TSMM-native graph elements. |
| `constraints.json` | Policy and governance constraints | Captures constraints that shape permissible authority, effect, delegation, and review behavior. |
| `evidence.json` | EvidenceArtifact / evidence expectations | Describes evidence expected or produced by the modeled system. |
| `examples/valid-graph.json` | Positive conformance example | Demonstrates a graph that satisfies the TSMM-native schema. |
| `examples/invalid-graph.json` | Negative conformance example | Demonstrates a graph that must fail validation. |
| `examples/receipts/*.example.json` | Runtime receipt artifacts | Records authority, delegation, revocation, licensing, enforcement, or decision events. |
| `sourceEssays` | Provenance extension | Preserves Trust Graph intellectual provenance; not runtime evidence. |

## Decision receipt profile

TGA decision receipts use the TSMM runtime decision receipt core. TGA adds only provenance and interpretation extensions.

| TSMM field | TGA representation | Notes |
|---|---|---|
| `decisionId` | `decisionId` | Stable identifier for the decision event. |
| `timestamp` | `timestamp` | Recording or decision time. |
| `subjectRef` | `subjectRef` | The subject, claim, artifact, actor, or effect under decision. |
| `requestingActorRef` | `requestingActorRef` | Actor or agent requesting the effect. |
| `authorityBasis` | `authorityBasis` | Authority source, status, scope, and optional delegation or license references. |
| `policyRefs` | `policyRefs` | Policy surface applied. |
| `evidenceRefs` | `evidenceRefs` | Runtime evidence inspected. |
| `boundaryRef` | `boundaryRef` | Trust boundary crossed or implicated. |
| `decision.outcome` | `decision.outcome` | Uses TSMM canonical decision outcome vocabulary. |
| `effect.admission` | `effect.admission` | Describes operational effect admission. |
| `revocationStateChecked` | `revocationStateChecked` | Status, time, and source of revocation check. |
| `assuranceLevel` | `assuranceLevel` | TSMM posture value, not a TIS AL1-AL4 claim. |
| `reviewPath` | `reviewPath` | Contestability or escalation route. |

