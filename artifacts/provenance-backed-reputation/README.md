# Provenance-Backed Reputation

## Governance problem

Reputation signals become unsafe when a relying party can observe a score or rating but cannot reconstruct who issued the signal, under what authority, from which evidence, in which context, and with what lifecycle state.

This artifact turns the essay-derived claim into an executable assurance surface: consequential reliance on reputation requires provenance, context compatibility, issuer authority, and current status.

## Authority boundary

This artifact is an incubation artifact in TGA. It does not define canonical trust-system semantics or a portable reputation credential format.

- TSMM v0.24.0 supplies the semantic grammar.
- TIS v0.14.1 supplies portable authority, evidence, evaluation, decision, registry, and existing reputation credential contracts.
- TGA supplies the governance interpretation and assurance cases derived from *Why Reputation Economies Fail Without Provenance*.

## Admission rule

A consequential decision influenced by a reputation signal is admissible only when:

1. subject lineage is resolvable;
2. issuer authority for the signal class is valid;
3. origin context is recorded;
4. the target use is compatible with the origin context;
5. supporting evidence can be reconstructed;
6. status and revocation state are current at decision time; and
7. an aggregate score is not being used as a substitute for provenance.

## Evidence produced

An implementation should be capable of projecting the decision into TIS-compatible artifacts containing the authority boundary, evidence bundle, evaluation envelope, decision receipt, and any registry reference used during resolution.

## Assurance cases

See `tests/assurance-cases.yaml` for valid reliance, unverifiable issuer, context collapse, score substitution, and stale-status cases.
