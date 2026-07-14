# Trust Graph Artifacts v0.5.0

## Delegation becomes a verifiable chain

This release operationalizes three new Trust Graph essays into an adoption-ready governance increment. It separates agent identity from delegated authority, represents multi-hop and fan-out lineage, and moves governance upstream to mandates and delegation boundaries before consequential effects are admitted.

## Added

- Delegation Lineage Envelope pattern with principal continuity, attenuation, transaction and intent binding, domain-transition, convergence, and revocation controls.
- Delegation-First Governance Profile covering mandate completeness, executable constraints, escalation, interruption, compensation, and pre-effect admission.
- Essay source, provenance, and artifact crosswalk entries.
- TIS v0.11.0 binding example and TSMM v0.22.0 alignment guidance.
- Negative assurance cases for scope expansion, broken lineage, principal substitution, translation amplification, aggregation amplification, refresh renegotiation, and partial revocation.

## Adoption impact

Existing packages remain valid. Teams should adopt the lineage pattern when delegation depth exceeds one, authority crosses a trust domain, or concurrent branches converge into a consequential effect. The new profile is particularly relevant to standing authority and workflows whose effects may outlive the initiating interaction.

## Validation

Run the delegation validator together with the existing TSMM-native, TIS-alignment, authority-envelope, and receipt validators. The release is additive and does not redefine TSMM or TIS authority.
