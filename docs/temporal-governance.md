# Temporal Governance

Temporal governance treats authority as a time-sensitive execution condition rather than a static property of a credential, license, delegation, or archived artifact.

The repository now distinguishes between three states that are often collapsed in conventional verification flows:

1. **Artifact persistence** — the record still exists and can be resolved.
2. **Technical validity** — the record may still parse, verify, or chain to an issuer.
3. **Executable legitimacy** — the record is still admissible for action under current authority, revocation, scope, and freshness conditions.

The core assurance rule is simple: a preserved artifact MUST NOT be treated as executable authority unless current authority state can be verified at the moment of use.

## Artifact packages

- `patterns/persistence-trap-detector`
- `patterns/revocation-lag-analyzer`
- `patterns/gradient-exploitation-surface`
- `profiles/compositional-revocation-profile`
- `overlays/execution-bound-revocation`

## Evidence model

Temporal governance produces machine-verifiable receipts rather than narrative assertions:

- `revocation-propagation-receipt`
- `execution-authority-state-receipt`
- `gradient-exploitation-signal-receipt`

These receipts make time, propagation, enforcement, and evidence limits explicit.
