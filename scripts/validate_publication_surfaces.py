#!/usr/bin/env python3
"""Validate current publication, provenance, and release-ledger consistency."""
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
errors = []


def load_yaml(path: str):
    p = ROOT / path
    if not p.exists():
        errors.append(f'missing required publication surface: {path}')
        return {}
    try:
        return yaml.safe_load(p.read_text(encoding='utf-8')) or {}
    except Exception as exc:
        errors.append(f'{path}: invalid YAML: {exc}')
        return {}

version = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
status = load_yaml('PROJECT-STATUS.yaml')
authority = load_yaml('governance/repository-authority.yaml')
ledger = load_yaml('governance/release-publication-ledger.yaml')
catalog = load_yaml('essays/current-release-catalog.yaml')
provenance = load_yaml('provenance/current-release-map.yaml')
crosswalk = load_yaml('crosswalks/current-release-essay-to-artifact.yaml')

status_version = str((status.get('release') or {}).get('current_version', ''))
authority_version = str(authority.get('current_version', ''))
for surface, value in [('PROJECT-STATUS.yaml', status_version), ('repository-authority.yaml', authority_version)]:
    if value != version:
        errors.append(f'{surface} version {value!r} does not match VERSION {version!r}')

for path, data in [
    ('essays/current-release-catalog.yaml', catalog),
    ('provenance/current-release-map.yaml', provenance),
    ('crosswalks/current-release-essay-to-artifact.yaml', crosswalk),
]:
    if str(data.get('release', '')) != version:
        errors.append(f'{path}: release must match VERSION {version}')

expected_artifacts = {
    'artifacts/provenance-backed-reputation/artifact.yaml',
    'artifacts/context-bound-identifier-use/artifact.yaml',
    'artifacts/verifiable-trade-corridor/artifact.yaml',
    'artifacts/agent-capability-accreditation/artifact.yaml',
    'artifacts/issuer-incentive-inversion/artifact.yaml',
    'artifacts/autonomy-native-institution/artifact.yaml',
}

catalog_paths = {entry.get('artifact_path') for entry in catalog.get('entries', [])}
provenance_paths = {entry.get('artifact') for entry in provenance.get('mappings', [])}
crosswalk_paths = {entry.get('artifact_path') for entry in crosswalk.get('entries', [])}
for name, paths in [('catalog', catalog_paths), ('provenance', provenance_paths), ('crosswalk', crosswalk_paths)]:
    missing = expected_artifacts - paths
    extra_missing_files = {p for p in paths if p and not (ROOT / p).exists()}
    if missing:
        errors.append(f'{name}: missing current artifact mappings: {sorted(missing)}')
    if extra_missing_files:
        errors.append(f'{name}: references missing artifact files: {sorted(extra_missing_files)}')

releases = ledger.get('releases') or []
versions = [str(entry.get('version')) for entry in releases]
if not versions or versions[-1] != version:
    errors.append(f'release ledger latest version must be {version}')
if len(versions) != len(set(versions)):
    errors.append('release ledger contains duplicate versions')

sha = re.compile(r'^[0-9a-f]{40}$')
allowed_status = {'pending-publication', 'published'}
for entry in releases:
    v = str(entry.get('version', ''))
    notes = entry.get('release_notes')
    commit = str(entry.get('merge_commit', ''))
    if not notes or not (ROOT / notes).exists():
        errors.append(f'v{v}: missing canonical release notes file')
    if v == version:
        if commit != 'pending-pr-merge' and not sha.fullmatch(commit):
            errors.append(f'v{v}: current merge_commit must be pending-pr-merge or a 40-character SHA')
    elif not sha.fullmatch(commit):
        errors.append(f'v{v}: historical merge_commit must be a 40-character SHA')
    for key in ('tag_status', 'github_release_status'):
        if entry.get(key) not in allowed_status:
            errors.append(f'v{v}: {key} must explicitly be pending-publication or published')
    if not entry.get('validation_evidence'):
        errors.append(f'v{v}: validation_evidence must be explicit')

readme = (ROOT / 'README.md').read_text(encoding='utf-8')
docs_index = (ROOT / 'docs/index.md').read_text(encoding='utf-8')
for surface, text in [('README.md', readme), ('docs/index.md', docs_index)]:
    for marker in (f'v{version}', 'TSMM v0.24.0', 'TIS v0.14.1'):
        if marker not in text:
            errors.append(f'{surface}: missing current publication marker {marker!r}')

if errors:
    print('Publication/provenance validation failed:')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)

pending = sum(
    1 for entry in releases
    if entry.get('tag_status') != 'published' or entry.get('github_release_status') != 'published'
)
print(
    f'Publication/provenance validation passed: {len(releases)} release ledger entries, '
    f'{len(expected_artifacts)} current artifact mappings, {pending} releases pending publication.'
)
