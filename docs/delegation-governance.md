# Delegation Governance and Lineage

## Why this increment exists

Agent identity establishes who or what is acting. It does not establish whose authority is being exercised, whether that authority remains current, or whether it narrowed correctly through a multi-agent chain. TGA v0.5.0 addresses this gap with a delegation-lineage pattern and a delegation-first governance profile.

## Implementer route

1. Define the root mandate using `patterns/agent-mandate-envelope`.
2. Use `patterns/runtime-authority-envelope` for effect-time checks.
3. Add `patterns/delegation-lineage-envelope` when depth exceeds one, domains change, or branches fan out.
4. Apply `profiles/delegation-first-governance-profile` to consequential workflows.
5. Emit chain verification and decision evidence before effect admission.

## What can be tested

Principal continuity, parent-hop completeness, monotonic attenuation, immutable transaction and intent binding, domain translation, aggregate branch authority, status freshness, revocation propagation, interruption, and compensation.

## Cross-repository bindings

TSMM v0.22.0 supplies the canonical chained and fan-out patterns. TIS v0.11.0 supplies portable delegation-lineage and verification schemas. TGA remains the governance-pattern incubation layer and does not supersede either repository's authority.
