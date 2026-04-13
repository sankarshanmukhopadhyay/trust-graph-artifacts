#!/usr/bin/env python3
import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
ARTIFACTS = [
    'after-consent','delegation-after-identity','your-agents-are-not-failing-your','wallet-to-agent-identity',
    'digital-credential-verification-policy-playbook','systemic-controllers','trust-registry-governance-model',
    'machine-readable-privacy-terms','portable-eligibility','the-proof-gap','execution-time-delegation','crisis-of-narrative-control'
]
REQUIRED_PROJECTION_KEYS = {'governanceContext','profile','entities','relationships','artifacts','policies','controls','threats','evidence','verifications','trustDecisions','effects','lifecycle'}
REQUIRED_STATES = {'issued','active','suspended','revoked','expired'}

def load_yaml(path: Path):
    with path.open('r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def main() -> int:
    entity_registry = load_yaml(ROOT / 'entities/registry.yaml')
    control_registry = load_yaml(ROOT / 'controls/registry.yaml')
    entity_ids = {entry['id'] for entry in entity_registry['entries']}
    control_ids = {entry['id'] for entry in control_registry['entries']}
    errors = []

    for slug in ARTIFACTS:
        manifest_path = ROOT / 'artifacts' / slug / 'artifact.yaml'
        projection_path = ROOT / 'bindings' / 'tsmm' / 'projections' / f'{slug}.yaml'
        manifest = load_yaml(manifest_path)
        if 'tsmm_binding' not in manifest:
            errors.append(f'{slug}: missing tsmm_binding in manifest')
            continue
        expected_proj = f'bindings/tsmm/projections/{slug}.yaml'
        if manifest['tsmm_binding'].get('projection') != expected_proj:
            errors.append(f'{slug}: projection path mismatch in manifest')
        if not projection_path.exists():
            errors.append(f'{slug}: missing projection file')
            continue
        proj = load_yaml(projection_path)
        if not {'bindingId','artifactRef','tsmmVersion','projection'}.issubset(proj):
            errors.append(f'{slug}: missing top-level projection keys')
            continue
        section_keys = set(proj['projection'].keys())
        missing = REQUIRED_PROJECTION_KEYS - section_keys
        if missing:
            errors.append(f'{slug}: missing projection sections: {sorted(missing)}')
        for entity in proj['projection'].get('entities', []):
            if entity['id'] not in entity_ids:
                errors.append(f"{slug}: entity not in registry: {entity['id']}")
        for control in proj['projection'].get('controls', []):
            if control['id'] not in control_ids:
                errors.append(f"{slug}: control not in registry: {control['id']}")
        effect_ids = {e['id'] for e in proj['projection'].get('effects', [])}
        for td in proj['projection'].get('trustDecisions', []):
            refs = td.get('effectRefs', [])
            if not refs:
                errors.append(f"{slug}: trust decision {td['id']} missing effectRefs")
            elif not set(refs).issubset(effect_ids):
                errors.append(f"{slug}: trust decision {td['id']} references unknown effects")
        states = {s['name'] for s in proj['projection'].get('lifecycle', {}).get('states', [])}
        if not REQUIRED_STATES.issubset(states):
            errors.append(f'{slug}: lifecycle missing required states')

    if errors:
        print('TSMM binding validation failed:')
        for err in errors:
            print(f' - {err}')
        return 1
    print(f'TSMM binding validation passed for {len(ARTIFACTS)} artifacts.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
