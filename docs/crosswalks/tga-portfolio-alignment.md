---
owner: maintainers
last_reviewed: 2026-06-30
applicable_version: v0.4.0
title: Portfolio Alignment
layout: default
parent: TSMM alignment
nav_order: 7
---

# Portfolio Alignment

`trust-graph-artifacts` should be treated as the portfolio's research-to-executable-artifact translation layer.

It sits between research and implementation. The repository does not publish the Trust Graph essays themselves and does not define the TSMM or TIS core models. It turns essay-derived governance pressure into TSMM-native packages with evidence, validation, provenance, and runtime assurance projection paths.

## Portfolio Role

| Field | Value |
|---|---|
| Repository | `trust-graph-artifacts` |
| Layer | research-to-executable-artifact-translation |
| Role | essay-derived-governance-pattern-corpus |
| Upstream semantic dependency | `trust-systems-meta-model` |
| Upstream artifact dependency | `trust-infrastructure-schemas` |
| Evidence produced | TSMM-native packages, package graphs, constraints, evidence expectations, decision receipts, provenance maps |

## Relationship Model

| Source | Target | Relationship | Evidence |
|---|---|---|---|
| `trust-graph-artifacts` | `trust-systems-meta-model` | `extends` / `drift_sensitive_to` | `bindings/tsmm/`, package graphs, TSMM alignment docs |
| `trust-graph-artifacts` | `trust-infrastructure-schemas` | `depends_on` / `produces_evidence_for` | `bindings/tis/`, TIS projection docs, runtime assurance examples |
| `digital-governance-paper-notes` | `trust-graph-artifacts` | `informs` | research review findings that identify new governance failure patterns |
| `trust-graph-artifacts` | downstream assurance repositories | `informs` | reusable package controls, evidence expectations, and decision receipt patterns |

## Drift Triggers

Review this repository when any of the following changes occur:

- TSMM changes authority graph, runtime governance envelope, decision receipt, lifecycle, or task evidence semantics.
- TIS changes authority boundary, evidence bundle, evaluation envelope, decision receipt, registry publication, assurance, or status/revocation schemas.
- Trust Graph essays introduce a new governance failure pattern that requires package, receipt, or validation representation.
- Downstream assurance repositories adopt a TGA package as a reusable control or evidence model.

## v0.4.0 Portfolio Impact

The v0.4.0 release has artifact and assurance impact. It updates upstream alignment, adds a TIS runtime assurance projection binding, introduces new TSMM-native packages, and expands validation coverage around evidence and decision artifacts.
