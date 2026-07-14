---
layout: default
title: Adoption Checklist
parent: Agentic Systems Architecture and Governance
nav_order: 4
---

# Adoption Checklist

## Architecture readiness

- [ ] One bounded job and explicit definition of done are approved.
- [ ] Consequential effects and prohibited effects are enumerated.
- [ ] Every persistent role resolves to a principal or recognized authority source.
- [ ] Persistent roles and ephemeral workload instances are distinct.
- [ ] Mandates are machine-readable, versioned, status-checkable, and testable.
- [ ] Delegation topology and maximum depth are explicit.
- [ ] Monotonic attenuation is enforced.
- [ ] Trust-domain translation has a non-expansion rule.
- [ ] Capability broker and enforcement points are identified.
- [ ] Candidate action schemas are defined.
- [ ] Fan-out convergence and dissent policies are defined.
- [ ] Evidence bundle and receipt chain are defined.
- [ ] Challenge, correction, and remediation owners are assigned.
- [ ] ADRs are current.

## Implementation readiness

- [ ] No consequential tool is directly reachable by a model or ungoverned workflow.
- [ ] Every consequential action passes mandate, lineage, policy, status, and capability checks.
- [ ] Technical capabilities are narrower than or equal to supporting authority.
- [ ] Capabilities are transaction-bound, time-bound, and revocable.
- [ ] Human approvals bind to exact action or content digests.
- [ ] Model output cannot directly trigger execution.
- [ ] Evidence references are resolvable by authorized verifiers.
- [ ] Unknown or stale authority state causes safe suspension.
- [ ] Branch data and capabilities are minimized.
- [ ] Aggregate effects are checked independently of branch validity.

## Assurance readiness

- [ ] TSMM instance and semantic invariants are reviewed.
- [ ] TIS schemas validate all boundary artifacts and examples.
- [ ] TGA positive and negative tests are mapped to implementation tests.
- [ ] Mandatory negative tests pass.
- [ ] Revocation propagation is demonstrated in an integration environment.
- [ ] In-flight interruption and post-effect remediation are exercised.
- [ ] An independent reviewer can reconstruct one effect from evidence.
- [ ] Selective-disclosure and access-control behaviour are tested.
- [ ] Documentation links and repository references resolve.
- [ ] Release notes identify authority, policy, schema, and evidence changes.

## Production readiness

- [ ] Status and revocation services are monitored.
- [ ] Evidence availability and retention objectives are monitored.
- [ ] Operational metrics and alerts are active.
- [ ] Runbooks cover stale evidence, unknown lineage, partial propagation, and unavailable dependencies.
- [ ] Incident exercises include revocation, interruption, correction, and remediation.
- [ ] Third-party and trust-domain dependencies are documented.
- [ ] Control owners and escalation paths are current.
- [ ] Model, tool, and vendor replacement cannot bypass governance controls.
- [ ] The implementation baseline records the exact TSMM, TIS, and TGA revisions adopted.

## Minimum implementation profile

A system should not claim governed consequential agent operation unless it can demonstrate all of the following:

1. Every consequential workload executes under a persistent role.
2. Every persistent role resolves to a principal or recognized authority source.
3. Every consequential effect is declared in an effect catalog.
4. Every effect requires a current mandate and policy result.
5. Every delegated action has a reconstructable lineage.
6. Authority remains equal or narrower at each delegation hop.
7. Capabilities are narrower than or equal to supporting authority.
8. Workloads cannot directly reach consequential tools outside enforcement points.
9. Model output is treated as a candidate action and validated before execution.
10. Fan-out branches are evaluated individually and collectively.
11. Trust-domain translations prove preservation or attenuation of meaning.
12. Refresh preserves principal, intent, scope, lineage, and revocation relationships.
13. Revocation propagates to known descendants and in-flight work.
14. Every consequential effect produces signed or otherwise verifiable evidence.
15. Valid delegation remains separate from local policy admission.
16. Human approval thresholds and action bindings are explicit.
17. Challenge, correction, and remediation paths are discoverable.
18. Negative tests prove rejection of invalid or ambiguous authority.
19. Exact repository revisions are recorded in implementation evidence and release metadata.
