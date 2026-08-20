#!/usr/bin/env python3
"""Execute TGA YAML assurance cases as deterministic admission tests."""
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
CASE_FILES = sorted(ROOT.glob('artifacts/*/tests/assurance-cases.yaml'))
PROHIBITED_WHEN_TRUE = {'aggregate_score_only', 'intermediary_only_assertion'}
errors = []
executed = 0


def evaluate(given: dict) -> str:
    if not given:
        return 'reject'
    for key, value in given.items():
        if not isinstance(value, bool):
            return 'reject'
        if key in PROHIBITED_WHEN_TRUE:
            if value is True:
                return 'reject'
        elif value is not True:
            return 'reject'
    return 'admit'

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
        actual = evaluate(given)
        if actual != expected:
            errors.append(f'{suite}/{case_id}: expected {expected}, evaluated {actual}')

if not CASE_FILES:
    errors.append('no artifacts/*/tests/assurance-cases.yaml files found')
if errors:
    print('Assurance case validation failed:')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)
print(f'Assurance case validation passed: {executed} cases across {len(CASE_FILES)} suites.')
