---
title: Documentation
layout: default
nav_order: 1
permalink: /docs/
---

# Documentation

<p class="tga-lede">Navigate Trust Graph Artifacts by the question you are trying to answer, not by the repository directory tree.</p>

**Current compatibility baseline:** TGA **v0.12.1**, TSMM **v0.24.0** as canonical semantic authority, and TIS **v0.14.1** as portable-contract authority.

## Four reader journeys

<div class="tga-path-grid">
  <div class="tga-path-card">
    <h3>1. I need the mental model</h3>
    <p>Understand what authority lives where and how narrative pressure becomes executable governance without turning essays into normative specifications.</p>
    <p><a href="{% link docs/architecture.md %}">Architecture →</a><br><a href="{% link docs/tsmm-and-the-trust-graph.md %}">TSMM and The Trust Graph →</a><br><a href="{% link docs/crosswalks/tsmm-tis-tga-layering.md %}">TSMM / TIS / TGA layering →</a></p>
  </div>
  <div class="tga-path-card">
    <h3>2. I need to build</h3>
    <p>Start from an implementation problem, choose an artifact class, inspect a representative package, and apply the authoring and validation model.</p>
    <p><a href="{% link docs/quickstart.md %}">Quickstart →</a><br><a href="{% link docs/package-anatomy.md %}">Package anatomy →</a><br><a href="{% link docs/developer-guide.md %}">Developer guide →</a></p>
  </div>
  <div class="tga-path-card">
    <h3>3. I need assurance evidence</h3>
    <p>Trace authority, delegation, enforcement, revocation, decision state, and interoperability into receipts and machine-verifiable gates.</p>
    <p><a href="{% link docs/assurance.md %}">Assurance →</a><br><a href="{% link docs/receipts.md %}">Receipts →</a><br><a href="{% link docs/crosswalks/tga-tsmm-tis-runtime-assurance.md %}">Runtime assurance →</a></p>
  </div>
  <div class="tga-path-card">
    <h3>4. I need provenance or auditability</h3>
    <p>Trace a claim from source essay to artifact, canonical semantics, portable contract, validation evidence, and published release state.</p>
    <p><a href="{% link essays/index.md %}">Essay-to-artifact index →</a><br><a href="{% link docs/decision-provenance.md %}">Decision provenance →</a><br><a href="{% link docs/release-publication.md %}">Release publication →</a></p>
  </div>
</div>

## Core concepts

Read these when you need the vocabulary and architectural boundary conditions rather than a specific implementation recipe.

| Topic | Read this | Question answered |
| --- | --- | --- |
| Authority boundaries | [Architecture]({% link docs/architecture.md %}) | Which layer is authoritative for what? |
| Essay relationship | [TSMM and The Trust Graph]({% link docs/tsmm-and-the-trust-graph.md %}) | How does narrative design pressure become structured semantics? |
| Artifact structure | [Package anatomy]({% link docs/package-anatomy.md %}) | What is inside a reusable package? |
| Executable governance | [Artifact methodology]({% link docs/artifact-methodology.md %}) | How do governance claims become enforceable/testable artifacts? |
| Runtime authority | [Runtime authority envelopes]({% link docs/authority-envelope.md %}) | How is delegated authority bounded at execution time? |
| Temporal control | [Revocation dynamics]({% link docs/revocation-dynamics.md %}) | What happens when authority changes faster than system state? |
| Epistemic adequacy | [Epistemic governance]({% link docs/epistemic-governance/index.md %}) | How are situated knowledge, challenge, suspension, and override represented? |

## Build and adoption

Use these surfaces when moving from understanding to implementation.

1. [Quickstart]({% link docs/quickstart.md %}) — validate the repository and choose a first tour.
2. [Package anatomy]({% link docs/package-anatomy.md %}) — understand package files and their roles.
3. [Profile taxonomy]({% link docs/profile-taxonomy.md %}) — choose the right artifact type.
4. [Authoring model]({% link docs/authoring-model.md %}) — create or extend artifacts consistently.
5. [Developer guide]({% link docs/developer-guide.md %}) — work with repository tooling and conventions.
6. [Adoption]({% link docs/adoption.md %}) — integrate patterns into another system or repository.

## Assurance and interoperability

The assurance path is intentionally evidence-first:

**authority → delegation → permitted effect → enforcement/revocation → receipt → semantic alignment → portable assurance → repository validation**

Key references:

- [Assurance]({% link docs/assurance.md %})
- [TSMM binding]({% link docs/bindings/tsmm-binding.md %})
- [TGA / TSMM / TIS runtime assurance]({% link docs/crosswalks/tga-tsmm-tis-runtime-assurance.md %})
- [TGA ↔ TSMM alignment crosswalk]({% link docs/crosswalks/tsmm-alignment-crosswalk.md %})
- [TSMM / TIS / TGA layering]({% link docs/crosswalks/tsmm-tis-tga-layering.md %})
- [TSMM decision receipt profile]({% link docs/crosswalks/tsmm-decision-receipt-profile.md %})
- [Assurance posture]({% link docs/crosswalks/assurance-posture.md %})
- [TGA → TSMM → TIS composition]({% link docs/crosswalks/tga-tsmm-tis-composition.md %})
- [Portfolio alignment]({% link docs/crosswalks/tga-portfolio-alignment.md %})

{: .governance }
> **Authority boundary:** historical release documents can cite older TSMM/TIS baselines. They are evidence of their release state, not current semantic authority. The active compatibility baseline is TSMM v0.24.0 / TIS v0.14.1.

## Provenance and machine-readable discovery

Three synchronized current-release surfaces support automated discovery and audit:

- [`essays/current-release-catalog.yaml`]({% link essays/current-release-catalog.yaml %}) — canonical source metadata;
- [`provenance/current-release-map.yaml`]({% link provenance/current-release-map.yaml %}) — source interpretation, artifact mapping, and evidence paths;
- [`crosswalks/current-release-essay-to-artifact.yaml`]({% link crosswalks/current-release-essay-to-artifact.yaml %}) — essay → TGA artifact → TSMM semantics → TIS portable contracts.

The current artifact families cover provenance-backed reputation, context-bound identifier use, verifiable trade, agent capability accreditation, issuer incentive inversion, and autonomy-native institutional composition.

## Repository assurance contract

```bash
make validate
```

This is the canonical conformance gate. It validates active packages, authority envelopes, delegation lineage, receipts, TIS alignment, artifact assurance cases, documentation integrity, repository governance, portfolio relationships, and current-release publication/provenance surfaces. CI emits `artifacts/validation/latest.json`, and GitHub Pages publication is gated on the same contract.

## Release and historical material

- [Release process]({% link docs/release-process.md %}) — how a release is prepared.
- [Release publication]({% link docs/release-publication.md %}) — merge, validation, tag, GitHub Release, and ledger completion.
- `docs/release-notes/` — release-specific change and impact records.
- [`governance/release-publication-ledger.yaml`]({% link governance/release-publication-ledger.yaml %}) — machine-readable publication state.
- [`archive/README.md`]({% link archive/README.md %}) — superseded models and transition material retained for auditability.
