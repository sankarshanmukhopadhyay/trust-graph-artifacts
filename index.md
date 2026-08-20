---
title: Home
layout: home
nav_order: 0
permalink: /
---

# Trust Graph Artifacts

**v0.12.1 · TSMM v0.24.0 semantic authority · TIS v0.14.1 portable-contract authority**

Trust Graph Artifacts converts high-signal governance arguments from The Trust Graph into reusable, testable trust-system artifacts while preserving a strict authority boundary: essays provide design pressure, TSMM provides canonical semantics, and TIS provides portable assurance contracts.

## Start here

1. [Documentation]({% link docs/index.md %})
2. [Quickstart]({% link docs/quickstart.md %})
3. [Architecture]({% link docs/architecture.md %})
4. [Adoption]({% link docs/adoption.md %})
5. [Essay to artifact index]({% link essays/index.md %})
6. [Release publication]({% link docs/release-publication.md %})

## Current artifact train

The active release train adds executable governance for:

- provenance-backed reputation;
- context-bound identifier use and correlation authority;
- verifiable cross-border trade;
- agent capability accreditation;
- issuer incentive inversion and lifecycle accountability;
- autonomy-native institutional composition.

The machine-readable source, provenance, and interoperability views are available in:

- [`essays/current-release-catalog.yaml`]({% link essays/current-release-catalog.yaml %})
- [`provenance/current-release-map.yaml`]({% link provenance/current-release-map.yaml %})
- [`crosswalks/current-release-essay-to-artifact.yaml`]({% link crosswalks/current-release-essay-to-artifact.yaml %})

## Assurance

The canonical repository gate is:

```bash
make validate
```

It exercises package conformance, authority envelopes, delegation lineage, receipts, TIS alignment, artifact assurance cases, publication/provenance consistency, documentation integrity, repository governance, and portfolio relationships. CI emits `artifacts/validation/latest.json`, and GitHub Pages publication is gated on the same assurance contract.

## Release integrity

A merged release is not considered fully published until its merge commit, validation evidence, Git tag, and GitHub Release are all recorded. See [Release publication]({% link docs/release-publication.md %}) and the machine-readable [`governance/release-publication-ledger.yaml`]({% link governance/release-publication-ledger.yaml %}).
