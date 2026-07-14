---
layout: default
title: Implementation Guide
parent: Agentic Systems Architecture and Governance
nav_order: 1
---

# Implementation Guide

## 1. Executive orientation

A production agentic system is not merely a collection of models that call tools. It is an authority-bearing system that can produce effects in the world.

The primary design question is therefore not how autonomous an agent should be. It is:

> Which effects may be admitted, under whose authority, through which delegation path, using which technical capability, with what evidence, and under what revocation and remediation arrangements?

The core architectural shift is to design around **effect admission**, not agent autonomy. Model output is a candidate action. A governed workflow evaluates it. An enforcement point controls technical execution. Evidence services preserve what happened and why the effect was permitted or denied.

### 1.1 What this guide enables

An implementation team can use this guide to:

- decompose a business job into bounded roles and governed effects;
- model principals, mandates, authority relationships, policies, evidence, decisions, and lifecycle states with TSMM;
- apply TGA patterns and negative tests to authority, delegation, execution, revocation, and contestability;
- use TIS schemas as API, message, storage, and verification contracts;
- implement multi-hop and fan-out delegation without silent scope expansion;
- separate valid delegated authority from the receiving system's local policy decision;
- produce evidence supporting conformance, audit, challenge, correction, and operational improvement.

### 1.2 End-state test

For every consequential effect, the system should answer:

1. Which persistent role acted?
2. Which principal or authority source empowered that role?
3. Which mandate and policy were current?
4. How did authority reach the executing workload?
5. Did scope remain constant or narrow at every hop?
6. Which technical capability was granted?
7. Which checks and approvals occurred?
8. What effect was produced?
9. How can the effect be challenged, revoked, interrupted, corrected, or remediated?
10. Which machine-verifiable evidence supports these answers?

## 2. The three repositories as an architecture kit

The repositories have distinct authority and should not be flattened into one specification.

| Repository | Architectural role | How an architect uses it |
|---|---|---|
| TSMM | Canonical semantic and structural model | Define entities, roles, authority, policies, decisions, effects, evidence, lifecycle, and delegation topology. |
| TIS | Portable machine-readable contracts | Validate authority boundaries, delegation lineage, verification results, execution evidence, and cross-system exchange. |
| TGA | Executable governance pattern and assurance corpus | Select mandate, delegation, runtime, receipt, revocation, threat, and adoption patterns. |

The intended design flow is:

```text
Governance problem or operational failure
        ↓
TGA pattern, control, threat, assurance case, and test vector
        ↓
TSMM semantic model and architecture instance
        ↓
TIS portable schema and verification contract
        ↓
Implementation profile, conformance tests, and operational evidence
```

Use **TSMM to define what the system means**, **TIS to define what implementations exchange and validate**, and **TGA to define what must be governed and tested**.

### 2.1 Priority reading path

1. TSMM implementer guidance and core model.
2. TSMM effect-centred decision and delegation patterns.
3. TGA quickstart and delegation governance guidance.
4. TGA agent mandate, runtime authority, and delegation lineage artifacts.
5. TIS authority-boundary and delegation-lineage schemas.
6. TGA receipt, lifecycle, revocation, and assurance artifacts.

Use the [repository crosswalk](repository-crosswalk.md) for the detailed path map.

## 3. Governing model: effect admission

### 3.1 Five objects that must remain distinct

| Object | Question answered | Failure if collapsed |
|---|---|---|
| Identity | Who or what is participating? | Authentication is mistaken for authority. |
| Authority | What may legitimately be done, for whom, and why? | Role membership or tool possession becomes presumed permission. |
| Capability | What can technically be done now? | Broad credentials create excessive blast radius. |
| Decision | What does the governed workflow conclude should happen? | Model output is mistaken for approved action. |
| Execution or effect | What actually happened in the world? | Intent and outcome cannot be reconciled, challenged, or remediated. |

### 3.2 Two independent gates

| Gate | Core question | Typical outcomes |
|---|---|---|
| Delegation assurance | Is the requester authentic, authorized, in scope, current, unrevoked, and connected to an intact lineage? | Pass, fail, indeterminate, escalate. |
| Local policy admission | May this receiving system cooperate under its own policies, approvals, agreements, data limits, and risk constraints? | Accept, narrow, request evidence, request approval, refuse, escalate. |

A valid delegation creates a legitimate request surface. It does not create an obligation to comply and does not override local governance.

## 4. Reference architecture

A scalable design places governance in a model-neutral control plane. Model invocations remain behind governed workflows and policy enforcement points.

```text
┌──────────────────────── Governance Control Plane ────────────────────────┐
│ Role and Principal Registry     Mandate Service                         │
│ Delegation Lineage Service      Policy Decision Service                 │
│ Capability Broker               Status and Revocation Service           │
│ Evidence and Receipt Store      Approval and Escalation Service         │
│ Challenge and Remediation Service                                      │
└──────────────────────────────────────────────────────────────────────────┘
                ↑                    ↑                    ↑
         Agent Workflow A     Agent Workflow B     External Agent
                │                    │                    │
                └──────────── Policy Enforcement Points ─┘
                                      │
                                    Effects
```

### 4.1 Logical components

| Component | Responsibility | Evidence produced |
|---|---|---|
| Role registry | Resolve persistent roles, principals, policy profiles, and current status. | Role resolution receipt. |
| Mandate service | Issue, version, validate, suspend, and revoke machine-readable mandates. | Mandate verification receipt. |
| Lineage service | Record authority transfers and verify continuity, attenuation, and status. | Delegation-lineage verification. |
| Policy decision point | Evaluate authority, policy, risk, agreements, and approval conditions. | Policy decision receipt. |
| Capability broker | Issue narrow, time-bound, transaction-bound technical grants. | Capability grant receipt. |
| Policy enforcement point | Mediate access to tools, data, signing, messaging, or payment. | Execution and denial events. |
| Evidence store | Preserve linked, append-only evidence and authorized views. | Evidence bundle or root. |
| Status and revocation service | Publish current validity and propagate revocation. | Status and propagation receipts. |
| Challenge and remediation service | Support dispute, correction, compensation, and recovery. | Challenge and remediation records. |

### 4.2 Persistent roles and ephemeral workloads

Accountability attaches to the persistent role and its authority architecture. Model invocations, reasoning passes, and temporary workers are ephemeral workload instances.

| Persistent role retains | Ephemeral workload receives |
|---|---|
| Identity and principal relationship | Task-specific context |
| Mandates and agreements | Narrow delegated scope |
| Policy profile | Short-lived capability references |
| Reputation and lifecycle state | Transaction and intent bindings |
| Audit and challenge obligations | Execution identifier and termination conditions |

## 5. Sequential implementation stages

Each stage has an architecture decision, repository inputs, implementation outputs, tests, and an exit gate. A team should not progress only because code exists; it should progress when the evidence for the gate is available.

### Stage 0 — Define the job and effects

**Objective:** Select one bounded job that creates observable value. Do not begin with a general-purpose autonomous agent.

**Architecture decisions:** Define the job owner, intended outcome, prohibited outcomes, consequence classes, completion state, and fallback to a human or institutional process.

**Repository inputs:** TSMM effect-centred decision model; TGA quickstart and governance profiles.

**Outputs:** Job charter, effect catalog, risk tier, effect-admission matrix, definition of done.

**Tests:** Every external effect is named. Each effect has allow, deny, downgrade, and escalation handling where applicable.

**Exit gate:** The team can describe the system without referring to a model vendor or orchestration framework.

| Effect | Risk tier | Required authority | Evidence before effect | Failure route |
|---|---|---|---|---|
| Read protected record | Medium | Role mandate and transaction scope | Identity, mandate, resource scope, status | Deny or request narrower scope |
| Send external message | Medium | Communication mandate | Recipient, purpose, approved content version | Queue for review |
| Commit funds | High | Financial mandate and approval threshold | Lineage, amount, payee, approval, fraud checks | Deny or human approval |
| Sign agreement | High | Binding authority | Exact agreement digest, terms, duration, required review | Escalate |
| Publish or disclose data | High | Data-use authority | Purpose, recipient, minimization, agreement, provenance | Deny, narrow, or use controlled interface |

### Stage 1 — Model principals, roles, and authority

**Objective:** Define who is represented, which persistent roles exist, and where authority originates.

**Architecture decisions:** Identify principals, authority sources, beneficiaries, operators, role owners, relying parties, affected parties, and trust domains.

**Repository inputs:** TSMM core model, entity definitions, relationship model, and agentic extension.

**Outputs:** TSMM instance model, role catalog, authority-source map, trust-domain map.

**Tests:** No role is self-authorizing. Every consequential role resolves to an accountable authority source. Persistent role and live workload are distinguishable.

**Exit gate:** Every proposed action can be attributed to a persistent role and an authority source.

### Stage 2 — Define mandates and policy boundaries

**Objective:** Convert authority into machine-readable, reviewable boundaries before building tool access.

**Architecture decisions:** Define purpose, permitted and prohibited actions, resource boundaries, value limits, duration, delegation depth, approval thresholds, revocation authority, and escalation.

**Repository inputs:** TGA agent mandate envelope, runtime authority envelope, and delegation-first governance profile; TIS authority-boundary schema.

**Outputs:** Mandate instance, policy rules, status endpoint, approval matrix, mandate test cases.

**Tests:** Expired, revoked, ambiguous, excessive-value, wrong-purpose, and prohibited-action requests fail or escalate.

**Exit gate:** No consequential effect can be admitted without a current mandate and applicable policy result.

```yaml
mandate_id: supplier-assessment-01
principal_ref: enterprise-procurement
agent_role_ref: supplier-assessment-coordinator
purpose: assess approved suppliers and produce a non-binding recommendation
permitted_actions:
  - request_public_supplier_information
  - request_approved_internal_risk_data
  - delegate_bounded_analysis
  - produce_recommendation
prohibited_actions:
  - execute_contract
  - commit_funds
  - disclose_unrelated_supplier_data
constraints:
  maximum_delegation_depth: 2
  human_approval_required_for:
    - recommendation_above_risk_threshold
    - use_of_nonapproved_data_source
revocation:
  authority_ref: procurement-governance-board
  status_ref: status:mandate:supplier-assessment-01
```

### Stage 3 — Design delegation and lineage

**Objective:** Model authority transfer before implementing task routing.

**Architecture decisions:** Choose direct, chained, fan-out, or cross-domain topology. Define parent references, original principal and intent, transaction binding, attenuation, refresh, and revocation propagation.

**Repository inputs:** TSMM chained and fan-out delegation patterns; TGA delegation lineage envelope; TIS delegation-lineage and verification schemas.

**Outputs:** Delegation topology, hop record format, lineage verifier, domain-translation record, negative fixtures.

**Tests:** Broken lineage, principal substitution, scope expansion, stale status, refresh renegotiation, domain-translation amplification, and partial revocation fail.

**Exit gate:** The complete authority path to every executing workload is reconstructable and machine-verifiable.

> **Monotonic attenuation:** For every non-root hop, granted authority must be equal to or narrower than the authority received from the parent. A broader grant is a new authorization event, not a valid subdelegation.

### Stage 4 — Separate authority from capability

**Objective:** Issue technical power only after authority and policy checks, and make the grant narrower than the supporting authority where possible.

**Architecture decisions:** Select enforcement points. Define resource, operation, parameter, purpose, duration, transfer, and revocation restrictions.

**Repository inputs:** TGA mandate and execution-time delegation artifacts; TIS authority-boundary and trust-task schemas.

**Outputs:** Capability broker, capability request format, grant receipt, denial reasons, secrets isolation design.

**Tests:** Broad standing credentials are unavailable to workloads. Out-of-scope resources and parameters are technically blocked.

**Exit gate:** Agents cannot bypass the broker to reach consequential tools or protected data.

| Weak pattern | Governed pattern |
|---|---|
| Database administrator credential plus prompt restraint | Read-only query capability for named records, bounded fields, transaction, and expiry |
| General payment token | Single-payee, maximum-value, one-time capability after approval |
| Unrestricted messaging account | Recipient-bound, template-bound, purpose-bound send capability |
| Raw dataset copy | Query-only or aggregate-only controlled workspace capability |
| General agent spawning | Named subtask, maximum depth, resource, time, and no-further-delegation capability |

### Stage 5 — Build the governed execution workflow

**Objective:** Treat model output as a candidate action object. Validation and policy evaluation occur before execution.

**Architecture decisions:** Define action schema, evidence requirements, risk scoring, approvals, policy checks, retry limits, escalation, and execution transaction boundaries.

**Repository inputs:** TSMM trust-decision and effect model; TGA runtime authority and execution-time delegation; TIS trust-task execution records.

**Outputs:** Candidate action schema, policy decision workflow, execution state machine, human-review packet, refusal and escalation format.

**Tests:** Prompt injection cannot invoke tools directly. Malformed or unsupported action objects fail. Approval is bound to the exact action version or digest.

**Exit gate:** The model can propose but cannot unilaterally create a consequential effect.

```json
{
  "action": "publish_supplier_recommendation",
  "job_ref": "job-017",
  "supplier_ref": "supplier-442",
  "evidence_refs": ["financial-verify-22", "security-review-19"],
  "risk_level": "medium",
  "uncertainty": "low",
  "requested_capability": "write-recommendation-record",
  "approval_required": false
}
```

### Stage 6 — Add fan-out, convergence, and return review

**Objective:** Govern both the authority given to each branch and the combined effect produced when branches return.

**Architecture decisions:** Define subtask boundaries, branch data minimization, branch capabilities, independence requirements, dissent handling, convergence rules, and aggregate-authority checks.

**Repository inputs:** TSMM fan-out delegation pattern; TGA delegation-lineage test vectors and delegation-first profile; TIS lineage verification and topology fields.

**Outputs:** Branch manifests, branch lineage records, convergence policy, dissent record, aggregate-effect review.

**Tests:** Each branch is valid individually. Combined outputs do not exceed parent authority, create prohibited inference, or erase material dissent.

**Exit gate:** The initiating workflow can prove what was delegated, returned, reviewed, accepted, rejected, or escalated.

> Individual branch validity does not prove aggregate validity. The initiating workflow must check combined authority, data exposure, prohibited inference, conflicts, and material dissent before admitting the final effect.

### Stage 7 — Produce evidence and receipts

**Objective:** Make evidence a first-class runtime output, not an after-the-fact log reconstruction exercise.

**Architecture decisions:** Define receipt types, signing, timestamping, evidence links, selective disclosure, custody, retention, challenge access, and schema identifiers.

**Repository inputs:** TGA receipt packages and proof-carrying commitment receipt; TIS execution, authority, and lineage schemas.

**Outputs:** Mandate, lineage, policy, capability, execution, approval, refusal, revocation, and remediation receipts.

**Tests:** An independent verifier can reconstruct authority and execution using authorized evidence without querying model memory.

**Exit gate:** Every consequential effect has a portable evidence bundle and discoverable challenge route.

```text
mandate_verification_receipt
        ↓
delegation_lineage_verification
        ↓
policy_decision_receipt
        ↓
capability_grant_receipt
        ↓
execution_receipt
        ↓
status, challenge, correction, and remediation records
```

### Stage 8 — Implement revocation, interruption, and remediation

**Objective:** Design revocation as a graph operation and operational workflow, not only as token expiry.

**Architecture decisions:** Define revokers, scope, propagation, latency, branch handling, in-flight interruption, settled effects, compensation, quarantine, and degraded-safe behaviour.

**Repository inputs:** TGA revocation dynamics, delegation-first profile, and commitment lifecycle mediation; TIS lineage verification and lifecycle records.

**Outputs:** Revocation state machine, propagation service, interruption hooks, remediation playbooks, downstream-response evidence.

**Tests:** Root revocation reaches descendants. In-flight work stops where possible. Completed effects route to remediation. Unknown state causes safe suspension.

**Exit gate:** The team can demonstrate revocation and recovery in a live integration test.

### Stage 9 — Operationalize assurance

**Objective:** Keep implementation, schemas, semantic model, documentation, and release evidence aligned as the system evolves.

**Architecture decisions:** Select conformance target, evidence owner, release gates, schema compatibility policy, threat-review cadence, control ownership, and operational metrics.

**Repository inputs:** TSMM conformance guidance; TGA validators and assurance cases; TIS validators.

**Outputs:** Conformance profile, CI validation, ADR set, control ownership matrix, operational assurance dashboard, release evidence.

**Tests:** Schemas and examples validate. Documentation links resolve. Authority-sensitive changes trigger review. Release evidence is complete.

**Exit gate:** The system can evolve without silently changing authority, evidence, or interoperability semantics.

## 6. Production design rules

1. Build a bounded job, not a general-purpose agent.
2. Make persistent roles accountable and workload instances ephemeral.
3. Require an explicit authority source for every consequential role.
4. Treat model output as a proposal.
5. Place enforcement outside the model and orchestration runtime.
6. Require monotonic attenuation across delegation.
7. Bind authority, capabilities, approvals, and evidence to the same transaction and intent.
8. Evaluate fan-out branches individually and collectively.
9. Generate receipts at every consequential control transition.
10. Make revocation, interruption, challenge, and remediation executable workflows.
11. Record exact repository revisions in each implementation baseline, but do not hard-code them into this guide.

## 7. Next steps

- Apply the [architecture decision set](architecture-decisions.md).
- Run the [assurance and testing strategy](assurance-and-testing.md).
- Use the [adoption checklist](adoption-checklist.md) for pilot and production gates.
- Study the [supplier assessment example](examples/supplier-assessment-system.md) as an end-to-end reference.
