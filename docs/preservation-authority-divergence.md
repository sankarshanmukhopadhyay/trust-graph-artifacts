---
title: Preservation–Authority Divergence
layout: default
parent: Temporal governance
nav_order: 3
---

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


## v0.3.1 validation

PAD is now represented as executable validation data in `validation/pad-test-cases.yaml`. The validation distinguishes current, stale, revoked, expired, orphaned, and unknown authority states. High-consequence execution is blocked when the preserved artifact cannot prove current authority state; lower-consequence unverifiable cases route to review.

Run:

```bash
python3 scripts/validate_authority_envelopes.py
```
