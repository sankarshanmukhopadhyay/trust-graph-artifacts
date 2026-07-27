# Prior-Incident Retrieval

## Purpose

Requires comparable institutional incidents and outcomes to be retrieved and assessed before a consequential decision.

## Source essay

- Essay: *The Edge Knows First*
- URL: https://thetrustgraph.substack.com/p/the-edge-knows-first
- Published: 2026-07-22

## Authority boundary

This package is an implementation-draft governance artifact. It uses existing TSMM entities and TIS-aligned evidence conventions. It does not create canonical TSMM semantics, redefine TIS contracts, certify an institution, or establish universal thresholds.

## Core controls

- `control.incident-corpus-declared` — Declare the incident corpus and its authority.
- `control.search-reproducible` — Record reproducible search terms, filters, and time bounds.
- `control.precedent-relevance-assessed` — Assess the relevance and distinguishing facts of retrieved precedents.
- `control.limitations-visible` — Record search limitations and unresolved precedent conflicts.

## Required evidence fields

- `incident_corpus`
- `search_terms`
- `retrieved_precedents`
- `relevance_assessment`
- `distinction_rationale`
- `search_limitations`

## Assurance interpretation

A passing result means that the declared discovery, challenge, authority, and evidence conditions were met for the assessed scope and validity period. It does not prove that every relevant fact was discovered or that the resulting decision is correct.

## Validation posture

The package includes a TSMM-native graph, constraints, evidence requirements, positive and negative graph examples, and a repository test vector.
