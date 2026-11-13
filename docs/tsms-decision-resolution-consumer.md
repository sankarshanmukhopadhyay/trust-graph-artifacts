---
title: TSMS Decision-Resolution Consumer
---
# TSMS Decision-Resolution Consumer

TGA's decision-resolution consumer is an additive executable test of TSMM v0.26.0 semantics using TIS v0.16.0 portable record shapes. It does not alter the previously accepted golden path, TGA v0.13.0 release, or authority boundaries.

Run `python3 scripts/validate_decision_resolution_consumer.py` or `make validate`. The canonical gate checks two positive states and twelve adversarial mutations through the exact `consume` function. Unsupported change categories, inconsistent authority-change declarations, missing provenance, missing evidence, and peer/workflow progression cannot produce `resolved`.

**Crucial limitation:** `resolved` classifies modeled evidence only. It does not authenticate an authoritative source, verify historical completeness, establish valid authorization or admit a material effect. A producer string, evidence URI, or `observed_at` is not cryptographic proof or competent authoritative recording. Runtime authority and external policy remain separately enforceable.

The coordinating TSMS gate must fetch and validate canonical TSMM invariants, the TIS schema, and this actual consumer from pinned commits, including negative cases. Local fixtures cannot assert independent interoperability. This research-implementation increment alone does not authorize a TGA or TSMS release.
