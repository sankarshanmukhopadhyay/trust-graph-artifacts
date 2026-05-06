---
title: From inference to verification
layout: default
parent: Authority, commitments, and high-risk governance
nav_order: 4
---

# From inference to verification

## Purpose

The inference-to-verification cluster captures the failure mode where institutions substitute behavioral estimation for verifiable identity, claims, provenance, or authority.

This is not merely a data-quality problem. It is a governance control-plane problem. When inference becomes the basis for institutional action, accountability becomes harder to reconstruct, contestability weakens, and future governance data may be polluted by prior unverified outputs.

## Package surface

- `patterns/inference-substitution-gap`
- `patterns/legibility-trap-detector`
- `patterns/control-plane-shift-detection`
- `patterns/legitimacy-gap-evaluator`

## Inference substitution checks

Every material decision input should be classified as one of:

- inferred
- asserted
- verified
- authoritative

Authority-sensitive effects should not proceed when an inferred signal is being used as a substitute for delegated mandate, issuer authorization, registry evidence, or provenance.

## Legibility trap checks

The legibility trap appears when a system responds to inference failure by expanding proxy collection, intensifying behavioral monitoring, shifting burden to users, or suppressing context instead of replacing inference with verification.

## Assurance posture

The desired migration is not from weak inference to stronger inference. The desired migration is from inference-dependent governance to verification-capable infrastructure with explicit accountability and redress.
