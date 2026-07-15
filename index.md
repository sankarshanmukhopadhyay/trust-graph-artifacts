---
title: Home
layout: home
nav_order: 0
permalink: /
---

# Trust Graph Artifacts

**A TSMM-native corpus for turning essay-derived governance failures into reusable, testable trust-system packages.**

This site is the Just the Docs/Jekyll publication surface for the repository. It exposes the active documentation, package methodology, TSMM alignment, executable governance receipts, and the active authority-governance corpus in a navigable form.

## Start here

1. [Agentic Systems Architecture and Governance]({% link guides/agentic-systems-architecture-and-governance/README.md %})

2. [Quickstart]({% link docs/quickstart.md %})
3. [Architecture]({% link docs/architecture.md %})
4. [Package anatomy]({% link docs/package-anatomy.md %})
5. [TSMM and The Trust Graph]({% link docs/tsmm-and-the-trust-graph.md %})
6. [Executable governance]({% link docs/executable-governance.md %})

## Flagship entry points

- [Repository status]({% link docs/repository-status.md %})
- [Adoption]({% link docs/adoption.md %})
- [Assurance]({% link docs/assurance.md %})
- [Interoperability]({% link docs/interoperability.md %})

## Repository control surfaces

- **Authority and delegation:** packages model who can act, on whose behalf, within which scope, and under what revocation conditions.
- **Enforcement and revocation:** receipts and constraints make execution-time governance observable.
- **Evidence and auditability:** examples, schemas, and validation matrices provide machine-verifiable assurance hooks.

## Local validation

```bash
python3 scripts/validate_tsmm_native.py
```

## Local documentation preview

```bash
bundle install
bundle exec jekyll serve
```
