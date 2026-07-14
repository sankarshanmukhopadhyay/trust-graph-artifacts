---
layout: default
title: Assurance and Testing
parent: Agentic Systems Architecture and Governance
nav_order: 5
---

# Assurance and Testing Strategy

Testing must demonstrate both useful execution and governance failure behaviour. A system that shows only successful agent operation has not demonstrated governed operation.

## 1. Test layers

| Layer | What is tested | Evidence |
|---|---|---|
| Schema conformance | Mandates, hops, receipts, lifecycle records, and examples validate against TIS contracts. | Validator output and versioned fixtures |
| Semantic invariants | Principal continuity, attenuation, transaction binding, status freshness, and branch authority conform to TSMM. | Invariant test report |
| Governance behaviour | Allow, deny, narrow, downgrade, and escalation paths implement TGA controls. | Decision receipts and policy coverage |
| Enforcement | Workloads cannot bypass capability brokers or exceed resource boundaries. | Integration and penetration-test evidence |
| Lifecycle | Expiry, suspension, revocation, interruption, correction, and remediation work. | Lifecycle event chain |
| Adversarial behaviour | Prompt injection, forged lineage, stale evidence, replay, missing parent, and aggregation amplification fail safely. | Negative test corpus |
| Operational assurance | Evidence availability, selective disclosure, audit reconstruction, and challenge handling work under realistic conditions. | Assurance review and incident exercise |

## 2. Minimum negative test suite

- Authenticated actor with no valid mandate.
- Expired mandate with a still-valid technical token.
- Missing intermediate delegation hop.
- Changed originating principal.
- Scope expansion at a child hop.
- Refresh that changes purpose or removes constraints.
- Trust-domain translation that broadens access.
- Fan-out branches that aggregate into an unauthorized effect.
- Revocation reaching only some descendants.
- Capability request broader than the approved action.
- Model output attempting direct tool invocation.
- Receipt with unavailable or unverifiable evidence.
- Human approval reused for a different action digest.
- Local policy denial despite valid delegated authority.
- Stale evidence becoming invalid between decision and execution.
- Replay of a capability against another transaction.
- Revoked parent mandate while descendants remain active.
- Aggregate disclosure assembled from individually permitted fields.

## 3. Test case format

```yaml
id: NEG-DELEGATION-003
title: child delegation expands authority
objective: prove monotonic attenuation is enforced
preconditions:
  - root mandate is active
  - parent hop permits read-only access to supplier-442
injection:
  child_hop:
    permitted_actions:
      - read_supplier_442
      - write_supplier_442
expected:
  lineage_verification: fail
  effect_admission: deny
  capability_issued: false
  evidence:
    - failed_invariant: scope_attenuation
    - parent_hop_ref
    - child_hop_ref
    - decision_receipt
```

## 4. Assurance cases

For each consequential effect, create an assurance case with:

- **Claim:** the effect can occur only under bounded and current authority.
- **Argument:** authority, lineage, policy, capability, enforcement, evidence, and lifecycle controls jointly support the claim.
- **Evidence:** schemas, validated fixtures, test reports, receipts, integration exercises, and operational monitoring.
- **Defeaters:** stale status, missing evidence, bypass paths, partial revocation, ambiguous translation, or aggregate amplification.
- **Response:** deny, suspend, narrow, escalate, re-verify, interrupt, correct, or remediate.

## 5. Release gates

A release is ready when:

1. TSMM instance changes have been reviewed for semantic impact.
2. TIS schemas and examples validate.
3. TGA assurance cases and negative fixtures are mapped to implementation tests.
4. Authority-sensitive changes have explicit migration and revocation treatment.
5. Documentation and relative links resolve.
6. A complete evidence bundle exists for at least one end-to-end job execution.
7. A revocation and recovery exercise has passed.
8. Known limitations and unsupported effect classes are documented.

## 6. Adoption metrics

| Metric | Target direction |
|---|---|
| Consequential effects with valid mandate and lineage | 100% |
| Consequential tool calls mediated by enforcement points | 100% |
| Evidence bundle completeness | 100% |
| Human approval reuse errors | Zero |
| Mandatory negative test coverage | Complete |
| Revocation propagation completion | Within declared risk-tier objective |
| Time to reconstruct one effect for audit | Measured and decreasing |
| Unknown authority state reaching execution | Zero |
