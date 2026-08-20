---
title: Documentation
layout: default
nav_order: 1
permalink: /docs/
---

# Documentation

Trust Graph Artifacts is currently **v0.12.1**, aligned to **TSMM v0.24.0** as canonical semantic authority and **TIS v0.14.1** as portable-contract authority.

## Start here

- [Quickstart]({% link docs/quickstart.md %}) — fastest path to the repository.
- [Architecture]({% link docs/architecture.md %}) — repository layers and authority boundaries.
- [TSMM and The Trust Graph]({% link docs/tsmm-and-the-trust-graph.md %}) — source pressure versus canonical semantics.
- [Package anatomy]({% link docs/package-anatomy.md %}) — structure of reusable TSMM-native packages.
- [Adoption]({% link docs/adoption.md %}) — implementation and adoption guidance.

## Current release surfaces

The v0.6–v0.11 artifact train and v0.12 assurance consolidation are represented through three current machine-readable publication surfaces:

- [`essays/current-release-catalog.yaml`]({% link essays/current-release-catalog.yaml %}) — canonical source metadata for the current essay-derived artifact families.
- [`provenance/current-release-map.yaml`]({% link provenance/current-release-map.yaml %}) — source interpretation, artifact mapping, and assurance evidence paths.
- [`crosswalks/current-release-essay-to-artifact.yaml`]({% link crosswalks/current-release-essay-to-artifact.yaml %}) — essay → TGA artifact → TSMM semantics → TIS portable contracts.

The current artifact families cover provenance-backed reputation, context-bound identifier use, verifiable trade, agent capability accreditation, issuer incentive inversion, and autonomy-native institutional composition.

## Runtime assurance and interoperability

- [TSMM binding]({% link docs/bindings/tsmm-binding.md %})
- [TGA / TSMM / TIS runtime assurance]({% link docs/crosswalks/tga-tsmm-tis-runtime-assurance.md %})
- [Portfolio alignment]({% link docs/crosswalks/tga-portfolio-alignment.md %})
- [TGA ↔ TSMM alignment crosswalk]({% link docs/crosswalks/tsmm-alignment-crosswalk.md %})
- [TSMM / TIS / TGA layering]({% link docs/crosswalks/tsmm-tis-tga-layering.md %})
- [TSMM decision receipt profile]({% link docs/crosswalks/tsmm-decision-receipt-profile.md %})
- [Assurance posture]({% link docs/crosswalks/assurance-posture.md %})
- [TGA → TSMM → TIS composition]({% link docs/crosswalks/tga-tsmm-tis-composition.md %})

> Historical references to earlier TSMM/TIS versions in release-specific documentation describe those releases only. The active repository compatibility baseline is TSMM v0.24.0 / TIS v0.14.1.

## Executable governance

- [Artifact methodology]({% link docs/artifact-methodology.md %})
- [Execution model]({% link docs/execution-model.md %})
- [Governance model]({% link docs/governance-model.md %})
- [Receipts]({% link docs/receipts.md %})
- [Decision provenance]({% link docs/decision-provenance.md %})
- [Walkthrough]({% link docs/walkthrough.md %})
- [Runtime authority envelopes]({% link docs/authority-envelope.md %})
- [Public agent contestability]({% link docs/public-agent-contestability.md %})
- [Revocation dynamics]({% link docs/revocation-dynamics.md %})

## Epistemic governance

- [Guided learning path]({% link docs/epistemic-governance/index.md %}) — situated knowledge, epistemic adequacy, challenge, suspension, and override.
- [TSMM extension candidate]({% link docs/incubation/epistemic-governance-tsmm-extension-candidate.md %}) — explicitly non-normative incubation boundary.

## Method and authoring

- [Methodology]({% link docs/methodology.md %})
- [Essay-to-TSMM method]({% link docs/essay-to-tsmm-method.md %})
- [Profile taxonomy]({% link docs/profile-taxonomy.md %})
- [Authoring model]({% link docs/authoring-model.md %})
- [Developer guide]({% link docs/developer-guide.md %})
- [Release process]({% link docs/release-process.md %})
- [Release publication]({% link docs/release-publication.md %}) — merge, validation, tag, and GitHub Release publication discipline.

## Validation

The canonical repository assurance contract is:

```bash
make validate
```

It validates active packages, authority envelopes, delegation lineage, receipts, TIS alignment, artifact assurance cases, documentation integrity, repository governance, portfolio relationships, and current-release publication/provenance surfaces. CI emits `artifacts/validation/latest.json` as machine-readable evidence and GitHub Pages publication is gated on the same validation contract.

## Release history

Current release notes are under `docs/release-notes/`. The machine-readable release publication state is maintained in [`governance/release-publication-ledger.yaml`]({% link governance/release-publication-ledger.yaml %}). Older architecture and transition material remains available for auditability, but should not be interpreted as the current compatibility baseline.

## Historical material

See [`archive/README.md`]({% link archive/README.md %}) for archived models and transition material that are no longer active authority surfaces.
