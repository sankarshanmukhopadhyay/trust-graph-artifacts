# Delegation Lineage Envelope

## Purpose

Make the complete derivation of delegated authority inspectable before a downstream agent effect is admitted. The pattern covers linear chains, fan-out branches, trust-domain transitions, scope attenuation, lineage refresh, revocation propagation, and convergence-level aggregate authority.

## Adoption path

1. Begin with `examples/valid-linear-chain.json`.
2. Preserve the originating principal, original intent, and transaction across every hop.
3. Require scope to remain constant or narrow at each delegation.
4. Add domain-transition evidence whenever authority crosses a trust domain.
5. For fan-out, evaluate the combined effect at convergence.
6. Bind the chain-level verification result to the runtime authority and decision receipts.

## Normative invariants

- No hop may grant authority broader than it received.
- Every non-root hop must identify its parent.
- The originating principal and transaction may not change during refresh.
- Authentication of a local actor cannot compensate for broken lineage.
- Individually valid branches cannot authorize an aggregate effect beyond the parent mandate.
