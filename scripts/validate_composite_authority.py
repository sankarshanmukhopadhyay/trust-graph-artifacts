#!/usr/bin/env python3
"""Execute TGA's project-local collective-authority pressure composition."""
from __future__ import annotations
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "validation" / "pressure-tests" / "composite_authority_invalidation.yaml"


def evaluate(case: dict) -> tuple[str, str]:
    membership = case.get("membership_state")
    rule = case.get("rule_state")

    if membership in {"missing", "unknown", "unavailable"} or rule in {"missing", "unknown", "unavailable"}:
        return "indeterminate", "preserved"
    if membership == "stale" or rule == "stale":
        return "reassessment_required", "preserved"
    if membership != "current" or rule != "current":
        return "deny", "preserved"
    if case.get("exact_action_binding") is not True:
        return "deny", "preserved"

    threshold = case.get("threshold")
    members = set(case.get("current_members") or [])
    evidence = case.get("evidence_members")
    if not isinstance(threshold, int) or threshold < 1 or not members or evidence is None:
        return "indeterminate", "preserved"
    if any(member not in members for member in evidence):
        return "deny", "preserved"
    if len(set(evidence)) < threshold:
        return "deny", "preserved"
    return "permit", "preserved"


def main() -> int:
    payload = yaml.safe_load(FIXTURE.read_text(encoding="utf-8"))
    failures = []
    for case in payload["cases"]:
        current, historical = evaluate(case)
        expected = case["expected"]
        if current != expected["current_authorization"]:
            failures.append(f"{case['id']}: expected current={expected['current_authorization']} got {current}")
        if historical != expected["historical_verification"]:
            failures.append(f"{case['id']}: expected history={expected['historical_verification']} got {historical}")
    if failures:
        print("\n".join(failures))
        return 1
    print(f"collective-authority-invalidation: {len(payload['cases'])}/{len(payload['cases'])} OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
