---
title: Home
layout: home
nav_order: 0
permalink: /
---

# Trust Graph Artifacts

<p class="tga-lede">Executable governance patterns, portable assurance evidence, and implementation guidance for governed trust systems.</p>

<div class="tga-release-strip" role="note">
  <strong>Current baseline</strong><br>
  TGA v0.12.1 · TSMM v0.24.0 semantic authority · TIS v0.14.1 portable-contract authority
</div>

Trust Graph Artifacts turns high-signal governance arguments from *The Trust Graph* into reusable, testable trust-system artifacts. The authority boundary is deliberate: **essays create design pressure; TSMM defines canonical semantics; TIS defines portable assurance contracts; TGA packages the implementation and evidence patterns.**

## Choose your path

<div class="tga-path-grid">
  <div class="tga-path-card">
    <h3>Understand the model</h3>
    <p>Start with the architectural layers, authority boundaries, and the relationship between essays, TSMM, TIS, packages, and evidence.</p>
    <p><a href="{% link docs/architecture.md %}">Architecture →</a><br><a href="{% link docs/tsmm-and-the-trust-graph.md %}">TSMM and The Trust Graph →</a></p>
  </div>
  <div class="tga-path-card">
    <h3>Implement a pattern</h3>
    <p>Use the developer-facing quickstart, inspect package anatomy, and move from an implementation problem to a reusable governance package.</p>
    <p><a href="{% link docs/quickstart.md %}">Quickstart →</a><br><a href="{% link docs/package-anatomy.md %}">Package anatomy →</a></p>
  </div>
  <div class="tga-path-card">
    <h3>Assure a system</h3>
    <p>Follow authority, delegation, enforcement, revocation, decision receipts, and portable assurance mappings into machine-verifiable evidence.</p>
    <p><a href="{% link docs/assurance.md %}">Assurance →</a><br><a href="{% link docs/crosswalks/tga-tsmm-tis-runtime-assurance.md %}">Runtime assurance →</a></p>
  </div>
  <div class="tga-path-card">
    <h3>Trace provenance</h3>
    <p>Move from a source essay through interpretation, artifact families, TSMM semantics, TIS contracts, validation, and release publication evidence.</p>
    <p><a href="{% link essays/index.md %}">Essay-to-artifact index →</a><br><a href="{% link docs/release-publication.md %}">Release publication →</a></p>
  </div>
</div>

## What this repository contains

| Layer | Purpose | Primary evidence |
| --- | --- | --- |
| **Source pressure** | Governance arguments and design constraints derived from *The Trust Graph* | Essay catalog and provenance maps |
| **Reusable artifacts** | Profiles, patterns, overlays, systems, evidence packages, and controls | Package metadata, graphs, constraints, examples |
| **Semantic alignment** | Mapping to canonical TSMM concepts and relationships | TSMM bindings and crosswalks |
| **Portable assurance** | Projection into reusable TIS contracts and assurance expectations | TIS bindings, assurance cases, receipts |
| **Repository assurance** | Machine-verifiable conformance of the corpus itself | `make validate`, CI evidence, release ledger |

[Explore the documentation hub →]({% link docs/index.md %})

## Current artifact train

The active release train includes executable governance for:

- provenance-backed reputation;
- context-bound identifier use and correlation authority;
- verifiable cross-border trade;
- agent capability accreditation;
- issuer incentive inversion and lifecycle accountability;
- autonomy-native institutional composition.

For machine-readable discovery, use the three synchronized publication surfaces:

- [`essays/current-release-catalog.yaml`]({% link essays/current-release-catalog.yaml %}) — current source catalog;
- [`provenance/current-release-map.yaml`]({% link provenance/current-release-map.yaml %}) — interpretation and evidence mapping;
- [`crosswalks/current-release-essay-to-artifact.yaml`]({% link crosswalks/current-release-essay-to-artifact.yaml %}) — essay → artifact → TSMM → TIS composition.

## Assurance contract

The canonical repository gate is:

```bash
make validate
```

It exercises package conformance, authority envelopes, delegation lineage, receipts, TIS alignment, artifact assurance cases, publication/provenance consistency, documentation integrity, repository governance, and portfolio relationships. CI emits `artifacts/validation/latest.json`; GitHub Pages publication is gated on the same assurance contract.

{: .assurance }
> **Evidence rule:** a merged release is not fully published until its merge commit, validation evidence, Git tag, and GitHub Release are recorded in the publication ledger.

See [Release publication]({% link docs/release-publication.md %}) and [`governance/release-publication-ledger.yaml`]({% link governance/release-publication-ledger.yaml %}).
