---
layout: default
title: Agentic Systems Architecture and Governance
nav_order: 20
has_children: true
---

# Agentic Systems Architecture and Governance Implementation Guide

**A cross-repository method for designing bounded, verifiable, and governable multi-agent systems.**

This guide helps enterprise architects, solution architects, governance engineers, assurance leads, security architects, consultants, and product teams use three coordinated bodies of work:

- **Trust Systems Meta-Model (TSMM)** for the canonical semantics of actors, roles, authority, policy, decisions, evidence, effects, lifecycle, and delegation topology.
- **Trust Infrastructure Schemas (TIS)** for portable machine-readable contracts, validation rules, evidence structures, and cross-system exchange.
- **Trust Graph Artifacts (TGA)** for executable governance patterns, controls, threats, assurance cases, negative tests, and adoption guidance.

The delivery objective is not to create a generally autonomous agent. It is to build a **bounded job** whose consequential effects enter the world only through legitimate authority, constrained delegation, least-privilege capabilities, governed execution, and verifiable evidence.

> **Design objective:** Every consequential effect should be attributable to an identifiable role, produced under current and bounded authority, through an intact delegation chain, using a least-privilege capability, after applicable policy checks, with evidence sufficient for audit, challenge, revocation, and remediation.

## How to use this guide

Work through the material in this order:

1. Read the [implementation guide](implementation-guide.md) and select one bounded job.
2. Use the [repository crosswalk](repository-crosswalk.md) to locate the relevant TSMM, TIS, and TGA artifacts.
3. Record the design choices using the [architecture decision set](architecture-decisions.md).
4. Implement positive and negative controls using [assurance and testing](assurance-and-testing.md).
5. Apply the [adoption checklist](adoption-checklist.md) before pilot and production release.
6. Compare the design with the [supplier assessment worked example](examples/supplier-assessment-system.md).

The machine-readable [crosswalk](crosswalk.yaml) connects each implementation stage to repository inputs, delivery outputs, evidence, and exit gates.

## Governing principle

```text
Principal or authority source
        ↓
Mandate and policy
        ↓
Persistent agent role
        ↓
Delegation lineage
        ↓
Candidate action
        ↓
Policy evaluation
        ↓
Least-privilege capability
        ↓
Policy enforcement point
        ↓
Effect
        ↓
Receipt, status, challenge, revocation, and remediation
```

Agents propose. Governed workflows decide. Enforcement points permit. Evidence services record. Challenge and remediation remain available.

## Repository authority boundaries

| Repository | Authority in this guide | Architect's use |
|---|---|---|
| TSMM | Semantic and structural model | Define principals, roles, authority, delegation, policies, decisions, evidence, effects, and lifecycle. |
| TIS | Portable schema and validation contract | Define messages, records, receipts, validation behaviour, and interoperability boundaries. |
| TGA | Executable governance and assurance patterns | Select controls, threat cases, runtime patterns, failure tests, and implementation guidance. |

This guide integrates the three layers but does not replace their respective artifacts.

## Guide status

This is implementation guidance. Teams should record the exact repository revisions they adopt in their own architecture baseline and evidence bundle rather than relying on versions embedded in this guide.
