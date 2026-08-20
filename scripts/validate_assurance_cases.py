#!/usr/bin/env python3
"""Execute TGA YAML assurance cases as deterministic admission tests."""
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
CASE_FILES = sorted(ROOT.glob('artifacts/*/tests/assurance-cases.yaml'))
errors = []
executed = 0


def expected_from_given(given: dict) -> str:
    return 'admit' if given and all(value is True for value in given.values()) else 'reject'

for path in CASE_FILES:
    data = yaml.safe_load(path.read_text()) or {}
    suite = data.get('suite') or path.parent.parent.name
    cases = data.get('cases') or []
    if not cases:
        errors.append(f'{path.relative_to(ROOT)}: no assurance cases declared')
        continue
    for case in cases:
        executed += 1
        case_id = case.get('id', '<missing-id>')
        expected = case.get('expected')
        given = case.get('given') or {}
        if expected not in {'admit', 'reject'}:
            errors.append(f'{suite}/{case_id}: expected must be admit or reject')
            continue
        actual = expected_from_given(given)
        if actual != expected:
            errors.append(f'{suite}/{case_id}: expected {expected}, evaluated {actual}')
        if expected == 'reject' and not case.get('reason'):
            errors.append(f'{suite}/{case_id}: rejected case must provide reason evidence')

if not CASE_FILES:
    errors.append('no artifacts/*/tests/assurance-cases.yaml files found')
if errors:
    print('Assurance case validation failed:')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)
print(f'Assurance case validation passed: {executed} cases across {len(CASE_FILES)} suites.')
