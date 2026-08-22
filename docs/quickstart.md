---
title: Quickstart
layout: default
nav_order: 2
---

# Quickstart

This repository is easiest to use as a **developer-facing library of executable governance packages and assurance evidence**, aligned to TSMM semantics and portable TIS contracts.

If you only do three things, do these:

1. run the canonical validation gate;
2. choose a reader tour based on your task;
3. inspect one package from intent through evidence and tests.

## 1. Validate the repository

```bash
make validate
```

This is the canonical repository assurance contract. It exercises active package conformance, authority envelopes, delegation lineage, receipts, TIS alignment, artifact assurance cases, publication/provenance consistency, documentation integrity, repository governance, and portfolio relationships.

For focused development, individual validators remain available under `scripts/`, but `make validate` is the authoritative aggregate gate used by CI and GitHub Pages publication.

## 2. Choose the right first tour

### Authority and legitimate control

Use this when your question is **who may do what, under which scope, and what proves that authority was legitimate**:

- `patterns/authority-legitimacy-validation/`
- `overlays/legitimate-control-enforcement/`
- `evidence/legitimate-control-decision-receipt/`
- [Runtime authority envelopes]({% link docs/authority-envelope.md %})
- [Decision provenance]({% link docs/decision-provenance.md %})

### Delegation, revocation, and temporal governance

Use this when your question is **how authority moves, expires, is revoked, or becomes unsafe when system state lags governance state**:

- `patterns/delegation-lineage-envelope/`
- `validation/authority-envelope-test-cases.yaml`
- `validation/pad-test-cases.yaml`
- `validation/revocation-lag-test-cases.yaml`
- [Delegated authority assurance flow]({% link docs/delegated-authority-assurance-flow.md %})
- [Revocation dynamics]({% link docs/revocation-dynamics.md %})

### Runtime assurance and interoperability

Use this when your question is **how a TGA implementation maps into canonical semantics and portable assurance contracts**:

- `bindings/tis/tga-tis-binding.json`
- `examples/composition/runtime-assurance-v0.4/`
- `systems/executable-trust-governance-stack/`
- `patterns/agent-accountability-edge/`
- `evidence/proof-first-market-decision-receipt/`
- [TGA / TSMM / TIS runtime assurance]({% link docs/crosswalks/tga-tsmm-tis-runtime-assurance.md %})

The `runtime-assurance-v0.4` directory name is retained as release provenance; interpret its semantics through the repository's current compatibility baseline rather than treating the directory name as the current release version.

### Cross-type package anatomy

Use this when your question is **how the repository's different artifact classes are structurally expressed**:

- `profiles/first-person-credentials/`
- `patterns/delegation-after-identity/`
- `overlays/consent-not-data-structure/`
- `systems/wallet-to-agent-identity/`
- `evidence/the-proof-gap/`
- [Package anatomy]({% link docs/package-anatomy.md %})

These tours are intentionally different. Pick the one matching the governance or assurance question you need to answer; do not try to read the repository directory-by-directory.

## 3. Read one package in evidence order

For a representative package, inspect files in this order:

1. `README.md` — intent and governance problem;
2. `package.json` — classification and metadata;
3. `graph.json` — actors, relationships, and structural semantics;
4. `constraints.json` — enforceable requirements and boundaries;
5. `evidence.json` — evidence expectations and traceability;
6. `tests/test-vector.json` — machine-verifiable conformance expectations.

This order moves from **claim → structure → constraint → evidence → test**, which is the core reading pattern for executable governance.

## 4. Keep the authority layers distinct

| Layer | Role | What it must not become |
| --- | --- | --- |
| **Essay** | Explains why a governance problem matters and creates design pressure | Normative semantic authority |
| **TSMM** | Defines canonical system semantics | Essay-specific implementation policy |
| **TIS** | Defines portable assurance contracts | Repository-specific package logic |
| **TGA package** | Encodes a reusable implementation and evidence pattern | A replacement for canonical semantics |
| **Receipt / evidence** | Records what happened, under what authority, and with which result | Mere narrative documentation |

The adoption rule is simple: **do not flatten concept, semantic authority, implementation package, and evidence into one layer.**

## 5. Trace the current release

For current-release provenance and automated discovery, use:

- [`essays/current-release-catalog.yaml`]({% link essays/current-release-catalog.yaml %})
- [`provenance/current-release-map.yaml`]({% link provenance/current-release-map.yaml %})
- [`crosswalks/current-release-essay-to-artifact.yaml`]({% link crosswalks/current-release-essay-to-artifact.yaml %})

Then use [Release publication]({% link docs/release-publication.md %}) when you need to verify that merge, validation, tag, GitHub Release, and ledger evidence are complete.

## Next step

- Need the conceptual model? Read [Architecture]({% link docs/architecture.md %}).
- Need to build or extend a package? Read [Developer guide]({% link docs/developer-guide.md %}).
- Need assurance evidence? Read [Assurance]({% link docs/assurance.md %}).
- Need to trace an essay into artifacts? Open the [Essay-to-artifact index]({% link essays/index.md %}).
