# Walkthrough: Commons Moderation Decision

A content input is submitted to a commons ingestion pipeline. The system resolves authority, checks delegation, checks revocation state, evaluates policy, executes enforcement, and emits a decision receipt. A reviewer can then replay the decision from the receipt chain and determine whether authority was exercised legitimately.


## TSMM v0.20 alignment checklist

Before merging a new or revised package, verify that:

1. The package has a clear Trust Graph source or governance pressure.
2. The graph models authority, evidence, policy, decision, and effect using TSMM-native concepts where applicable.
3. Any local Trust Graph vocabulary is mapped through `registries/outcome-vocabulary.yaml` or documented as narrative-only.
4. `assuranceLevel` is not treated as a TIS AL1-AL4 claim unless an explicit assurance artifact is referenced.
5. Runtime evidence is represented separately from essay provenance.
6. `python3 scripts/validate_tsmm_native.py` passes.
