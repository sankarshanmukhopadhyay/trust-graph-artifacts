# Artifact Manifest Schema

Each artifact must include a machine-readable manifest.

---

## Required Fields

```yaml
id: string
title: string
status: draft | experimental | stable | deprecated

source:
  essay_title: string
  essay_url: string
  published_date: date

signal:
  engagement_rate: number
  tier: A | B | C

classification:
  artifact_type: [schema | control-model | protocol | mapping]
  domain: [string]

governance:
  authority: string
  maintainers:
    - string
  maturity: experimental | stable

semantics:
  affects:
    - authority
    - delegation
    - enforcement
    - revocation
    - redress

relationships:
  supersedes: string | null
  superseded_by: string | null
  related_artifacts: [string]

validation:
  has_examples: boolean
  has_tests: boolean
  conformance_level: draft | partial | complete

lifecycle:
  created: date
  last_updated: date
```

---

## Purpose

The manifest ensures that artifacts are:

- traceable to source
- structurally classified
- governed through lifecycle
- evaluable for completeness

---

## Enforcement

When CI is introduced, it should validate:

- required fields present
- valid enum values
- linkage integrity
