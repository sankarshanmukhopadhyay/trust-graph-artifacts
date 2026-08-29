#!/usr/bin/env python3
import json, pathlib, sys, datetime
ROOT=pathlib.Path(__file__).resolve().parents[1]
KNOWN_CONCEPTS={
"urn:tsmm:concept:authority","urn:tsmm:concept:delegation","urn:tsmm:concept:scope","urn:tsmm:concept:policy",
"urn:tsmm:concept:evidence-artifact","urn:tsmm:concept:evidence-bundle","urn:tsmm:concept:assessment",
"urn:tsmm:concept:trust-decision","urn:tsmm:concept:effect","urn:tsmm:concept:revocation",
"urn:tsmm:concept:supersession","urn:tsmm:concept:redress","urn:tsmm:concept:assurance-profile"}
KNOWN_CONTRACTS={
"governance/authority-boundary.schema.json","evidence/evidence-bundle-manifest.schema.json",
"decision/decision-receipt.schema.json","oasf/oasf-evaluation-envelope.schema.json",
"registry/registry-publication-profile.schema.json"}
EXPECTED_TSMM="v0.24.0"; EXPECTED_TIS="v0.14.1"; EXPECTED_TGA="v0.12.1"
def load(p): return json.loads((ROOT/p).read_text())
def disposition(a):
    if a.get("tgaVersion")!=EXPECTED_TGA or a.get("semanticAuthority",{}).get("version")!=EXPECTED_TSMM or a.get("portableContractAuthority",{}).get("version")!=EXPECTED_TIS: return "unsupported"
    if any(x not in KNOWN_CONCEPTS for x in a.get("semanticAuthority",{}).get("conceptIds",[])): return "reject"
    if any(x not in KNOWN_CONTRACTS for x in a.get("portableContractAuthority",{}).get("contracts",[])): return "reject"
    if a.get("stackQualified") is not True: return "reject"
    return "candidate-compatible"
cases=[
("examples/tsms/golden-path.json","candidate-compatible"),
("validation/tsms/missing-semantic.json","reject"),
("validation/tsms/missing-contract.json","reject"),
("validation/tsms/unknown-version.json","unsupported")]
results=[]; errors=[]
for path,expected in cases:
    actual=disposition(load(path)); results.append({"fixture":path,"expected":expected,"actual":actual,"status":"pass" if actual==expected else "fail"})
    if actual!=expected: errors.append(f"{path}: expected {expected}, got {actual}")
ev={"repository":"trust-graph-artifacts","repositoryVersion":"0.12.1","profile":"tsms-stack-qualified-artifact","baseline":{"tsmm":EXPECTED_TSMM,"tis":EXPECTED_TIS,"tga":EXPECTED_TGA},"results":results,"status":"fail" if errors else "pass","limitations":["Local conformance evidence does not prove remote repository state or external certification."],"executedAt":datetime.datetime.now(datetime.timezone.utc).isoformat()}
(ROOT/"artifacts/validation").mkdir(parents=True,exist_ok=True)
(ROOT/"artifacts/validation/tsms-golden-path.json").write_text(json.dumps(ev,indent=2)+"\n")
if errors:
    print("\n".join(errors)); sys.exit(1)
print("TSMS stack-qualified golden path validation passed.")
