---
title: Essay to artifact index
layout: default
nav_order: 2
permalink: /essays/
---

# Essay to artifact index

The Trust Graph is the source corpus for design pressure and governance failure modes. TGA does **not** treat essay prose as executable authority. Current artifacts are interpreted through **TSMM v0.24.0** semantics and projected through **TIS v0.14.1** portable contracts where interoperable assurance evidence is required.

## Current release train

| Source essay | TGA artifact | Introduced | Primary governance surface |
|---|---|---:|---|
| *Why Reputation Economies Fail Without Provenance* | `artifacts/provenance-backed-reputation` | v0.6.0 | provenance-bearing, context-bounded reputation reliance |
| *The State Learned to Recognise Us. The System Learned to Watch Us.* | `artifacts/context-bound-identifier-use` | v0.7.0 | purpose-bound identifier use and correlation authority |
| *The Coming Trust Repricing in Global Trade* | `artifacts/verifiable-trade-corridor` | v0.8.0 | cross-border authority, provenance, status and decision receipts |
| *The Labor Market for Agents* | `artifacts/agent-capability-accreditation` | v0.9.0 | task-class, configuration-bound, revocable capability accreditation |
| *The Audit Nobody Asked For* | `artifacts/issuer-incentive-inversion` | v0.10.0 | issuer lifecycle accountability and institutional legibility |
| *Delegated Intelligence: The Next Compute Paradigm* | `artifacts/autonomy-native-institution` | v0.11.0 | institutional composition of delegation, authority, accreditation, contestability and redress |

Machine-readable views:

- [`current-release-catalog.yaml`]({% link essays/current-release-catalog.yaml %}) — source metadata and artifact paths.
- [`../provenance/current-release-map.yaml`]({% link provenance/current-release-map.yaml %}) — interpretation and assurance provenance.
- [`../crosswalks/current-release-essay-to-artifact.yaml`]({% link crosswalks/current-release-essay-to-artifact.yaml %}) — TSMM/TIS interoperability crosswalk.

## Existing TSMM-native package corpus

The repository also contains earlier reusable profiles, patterns, overlays, systems, and evidence models. High-value entry points include:

- `patterns/runtime-authority-envelope`
- `patterns/delegation-lineage-envelope`
- `profiles/delegation-first-governance-profile`
- `patterns/agent-mandate-envelope`
- `patterns/agent-accountability-edge`
- `profiles/public-agent-contestability-profile`
- `overlays/redress-rails-for-machine-decisions`
- `profiles/registry-gatekeeper-risk-profile`
- `evidence/proof-first-market-decision-receipt`
- `systems/executable-trust-governance-stack`
- `patterns/epistemic-adequacy-gate`
- `evidence/epistemic-challenge-receipt`

The full historical source mapping remains in [`source-catalog.yaml`]({% link essays/source-catalog.yaml %}). The current-release catalog is the normalized view for the v0.6–v0.12 release train and should be used when evaluating the active documentation baseline.

## Admission rule

An essay should produce a TGA artifact only when it exposes a governable object that can be made testable: an authority boundary, delegation rule, enforcement or revocation condition, evidence requirement, failure mode, control surface, or system composition. Narrative duplication alone is not an artifact.
