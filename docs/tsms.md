---
title: TSMS executable golden path
---
# TGA in the Trust Systems Modelling Stack (TSMS)

TGA is the **executable governance and implementation layer** of TSMS.

The original stack-qualified golden path remains `examples/tsms/golden-path.json`. It makes the dependency chain inspectable:

```text
TSMM canonical concepts
        ↓
TIS portable contracts
        ↓
TGA executable governance
        ↓
positive and negative execution evidence
```

## Historical accepted baseline

The immutable first stack release remains **`tsms-stack-2026.1 — Cashew-Nut`** at its exact accepted commits:

- TSMM `v0.24.0` — `2867010121e8a61971184d8fe7d3306b985e5884`
- TIS `v0.14.1` — `d25539932181e6d883f5bec261daaf011f740059`
- TGA `v0.12.1` — `f0bdc309a691a7be8dca3b48fed8ac1555219bec`

TGA v0.13.0 does not retroactively alter that receipt.

## v0.13.0 executable authority posture

The current TGA release consumes:

- **TSMM v0.25.0** as canonical semantic authority;
- **TIS v0.15.0** as portable-contract authority.

It adds executable evidence for two post-2026.1 propositions.

### Authority at material commitment

A material action is permitted only when current action-specific authority supports the exact attempted transition. Deterministic negative cases reject:

- valid identity with absent commitment authority;
- valid signature with insufficient or out-of-scope authority;
- expired or revoked authority;
- missing required approval evidence;
- reputation or runtime success used to expand mandate authority.

### Composite-authority lifecycle invalidation

Executable cases distinguish a collective authority principal from participating controllers and reject stale authority evidence after material governance change, including:

- member added or removed;
- threshold changed;
- exercise rule changed;
- collective authority suspended or revoked.

Historical verification can remain available where the governing semantics permit it, but historical validity does not imply current authorization.

## Stack qualification

A TGA artifact may claim `stackQualified: true` only when it:

1. identifies the TSMM semantic authority and concepts actually consumed;
2. identifies the TIS contracts actually consumed;
3. identifies its TGA version and executable artifact identity;
4. survives positive and meaningful negative cases;
5. treats unknown or incompatible semantic/contract state as non-success;
6. does not imply external certification or compatibility with unreviewed future versions.

A green local TGA gate cannot override `REVIEW_REQUIRED`, `UNSUPPORTED`, or `INDETERMINATE` at stack level.

## Run it

```bash
make validate
```

The canonical gate includes the TSMS golden path, authority-at-commitment execution, composite-authority lifecycle pressure tests, documentation integrity and publication/provenance checks.

## Successor stack relationship

TGA v0.13.0 is an independently versioned component input to the separately governed TSMS Stack 2026.2 renewal. The successor stack becomes accepted only when TSMM records exact component commits in a new immutable receipt, executes the cross-stack release gate, and records explicit human acceptance.

Complete-stack adopters should use:

https://qbf-consulting.github.io/trust-systems-meta-model/tsms-adopter-guide.html

## Non-claims

A passing TGA result is repository conformance evidence. It is not external certification, does not establish principal authority absent from the governed system, does not prove remote repositories are unchanged, and does not transfer TSMM semantic or TIS portable-contract authority into TGA.
