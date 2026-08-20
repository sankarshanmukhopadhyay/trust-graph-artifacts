#!/usr/bin/env python3
from pathlib import Path
import yaml

status = Path('PROJECT-STATUS.yaml')
if not status.exists():
    raise SystemExit('missing PROJECT-STATUS.yaml required by portfolio governance')
sd = yaml.safe_load(status.read_text()) or {}
project = sd.get('project') or {}
authority = sd.get('authority') or {}
evidence = sd.get('evidence') or {}
release = sd.get('release') or {}
for field in ['name', 'maturity', 'lifecycle', 'operational_status', 'intended_use', 'not_asserted']:
    if field not in project:
        raise SystemExit('PROJECT-STATUS.yaml project missing field: ' + field)
if project['name'] != 'trust-graph-artifacts' or project['lifecycle'] != 'active':
    raise SystemExit('invalid PROJECT-STATUS.yaml project identity or lifecycle')
for field in ['normative_scope', 'does_not_own', 'delegation', 'revocation_or_supersession']:
    if field not in authority:
        raise SystemExit('PROJECT-STATUS.yaml authority missing field: ' + field)
if 'validation_commands' not in evidence or 'evidence_outputs' not in evidence:
    raise SystemExit('PROJECT-STATUS.yaml evidence contract incomplete')
if not release.get('current_version'):
    raise SystemExit('PROJECT-STATUS.yaml release.current_version missing')

p = Path('governance/repository-authority.yaml')
if not p.exists():
    raise SystemExit('missing authority declaration')
d = yaml.safe_load(p.read_text()) or {}
required = ['repository','portfolio_tier','lifecycle','role','authority','dependencies','supersession_policy','revocation_or_withdrawal_policy','current_version']
missing = [x for x in required if x not in d]
if missing:
    raise SystemExit('missing authority fields: ' + ', '.join(missing))
if d['repository'] != 'trust-graph-artifacts' or d['portfolio_tier'] != 'flagship' or d['lifecycle'] != 'active':
    raise SystemExit('invalid flagship authority declaration')
own = set(d['authority'].get('owns', [])); no = set(d['authority'].get('does_not_own', []))
if own & no:
    raise SystemExit('conflicting authority claims: ' + ', '.join(sorted(own & no)))
version = Path('VERSION').read_text().strip()
versions = {version, str(release['current_version']), str(d['current_version'])}
if len(versions) != 1:
    raise SystemExit('release version drift: VERSION, PROJECT-STATUS.yaml, and repository-authority.yaml must agree')
print('Repository governance declaration: PASS')
