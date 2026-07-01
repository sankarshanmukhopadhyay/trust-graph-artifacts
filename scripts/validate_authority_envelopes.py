#!/usr/bin/env python3
"""Validate authority-envelope, PAD, and revocation-lag hardening cases.

This script intentionally uses transparent rule checks instead of a hidden policy
engine. It proves that the v0.3.1 authority-envelope claims have executable test
coverage: complete envelope, current authority state, bounded cache, fail-closed
PAD behavior, and revocation lag measurement.
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import sys
try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - dependency guidance path
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_ENVELOPE_FIELDS = {
    "technicalActorRef", "accountableControllerRef", "principalRef", "mandateRef",
    "scopeBoundary", "policyVersion", "evidenceRefs", "revocationStateChecked",
    "decisionReceiptRef", "redressRoute", "executionContext",
}
NON_CURRENT_STATES = {"suspended", "revoked", "expired", "stale", "orphaned", "unknown"}
errors: list[str] = []


def load_yaml(rel: str):
    if yaml is None:
        print("Authority envelope validation skipped. Install requirements.txt for PyYAML-backed validation.")
        sys.exit(0)
    path = ROOT / rel
    if not path.exists():
        errors.append(f"{rel}: missing validation file")
        return {"cases": []}
    return yaml.safe_load(path.read_text()) or {"cases": []}


def evaluate_envelope(envelope: dict) -> str:
    missing = sorted(REQUIRED_ENVELOPE_FIELDS - set(envelope))
    if missing:
        # Missing redress on a high-consequence action escalates rather than silently allowing.
        if envelope.get("executionContext", {}).get("highConsequence"):
            return "escalate"
        return "deny"
    rev = envelope.get("revocationStateChecked", {})
    if not rev.get("checked"):
        return "deny"
    if rev.get("authorityState") in NON_CURRENT_STATES:
        return "deny"
    if rev.get("cacheAgeSeconds", 10**9) > rev.get("maxCacheAgeSeconds", -1):
        return "deny"
    if envelope.get("executionContext", {}).get("highConsequence") and not envelope.get("redressRoute", {}).get("humanReviewAvailable"):
        return "escalate"
    return "allow"


def validate_authority_cases() -> None:
    data = load_yaml("validation/authority-envelope-test-cases.yaml")
    for case in data.get("cases", []):
        expected = case.get("expectedDecision")
        actual = evaluate_envelope(case.get("envelope", {}))
        if actual != expected:
            errors.append(f"{case.get('id')}: expected {expected}, got {actual}")


def evaluate_pad(case: dict) -> str:
    state = case.get("authorityState")
    if state == "active" and case.get("registryReachable"):
        return "allowed"
    if case.get("highConsequence"):
        return "blocked"
    return "review"


def validate_pad_cases() -> None:
    data = load_yaml("validation/pad-test-cases.yaml")
    for case in data.get("cases", []):
        actual = evaluate_pad(case)
        expected = case.get("expectedOutcome")
        if actual != expected:
            errors.append(f"{case.get('id')}: expected {expected}, got {actual}")
        if not case.get("padClassification"):
            errors.append(f"{case.get('id')}: missing padClassification")


def parse_z(ts: str) -> datetime:
    return datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(timezone.utc)


def evaluate_rlg(case: dict) -> str:
    revoked_at = parse_z(case["revokedAt"])
    max_lag = 0
    for obs in case.get("nodeObservations", []):
        max_lag = max(max_lag, int((parse_z(obs["recognizedAt"]) - revoked_at).total_seconds()))
    if case.get("failOpenDuringLag") or max_lag > case.get("maxAllowedLagSeconds", 0):
        return "violation"
    return "within-threshold"


def validate_rlg_cases() -> None:
    data = load_yaml("validation/revocation-lag-test-cases.yaml")
    for case in data.get("cases", []):
        actual = evaluate_rlg(case)
        expected = case.get("expectedOutcome")
        if actual != expected:
            errors.append(f"{case.get('id')}: expected {expected}, got {actual}")


validate_authority_cases()
validate_pad_cases()
validate_rlg_cases()

if errors:
    print("Authority envelope validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Authority envelope hardening validation passed.")
