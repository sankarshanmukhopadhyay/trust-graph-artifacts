# Preservation–Authority Divergence

Preservation is not legitimacy.

A record can remain available, discoverable, and cryptographically intact while no longer being authorized for execution. This divergence is the persistence trap: durability preserves the artifact, but governance must decide whether the artifact still carries live authority.

## Divergence indicators

- issuer no longer trusted;
- authority revoked after artifact creation;
- scope changed after issuance;
- downstream delegation survived revoked upstream authority;
- relying party used a stale cache;
- execution occurred after the authority validity window.

## Required control

Execution MUST require an execution authority state receipt when artifact preservation and current authority may diverge.
