#!/usr/bin/env python3
"""TGA implementation-owned decision-resolution consumer; TSMM owns semantics."""
import copy
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ADMISSIBLE={"authority_change","evidence_change","policy_change","lifecycle_change","correction"}
DIMENSION={"authority_change":"authority","evidence_change":"evidence","policy_change":"policy","lifecycle_change":"lifecycle","correction":"proposition"}

def consume(record):
    """Classify evidence; this is NOT authority verification or effect authorization."""
    if not isinstance(record,dict): return "indeterminate"
    c=record.get("condition"); b=record.get("transition_basis"); p=record.get("provenance")
    if not all(isinstance(x,dict) for x in (c,b,p)): return "indeterminate"
    if p.get("semantic_profile")!="TSMM decision-resolution semantics" or not p.get("producer"): return "indeterminate"
    if not record.get("event_id") or not record.get("observed_at") or not c.get("condition_id") or not c.get("established_at"): return "indeterminate"
    category=b.get("primary_category"); dims=b.get("changed_dimensions"); evidence=b.get("evidence_refs")
    if not isinstance(dims,list) or not isinstance(evidence,list) or not isinstance(b.get("authority_changed"),bool): return "indeterminate"
    if len(dims)!=len(set(dims)) or len(evidence)!=len(set(evidence)): return "indeterminate"
    if c.get("state")=="unresolved":
        return "unresolved" if category=="none" and not dims and b["authority_changed"] is False and not c.get("resolved_at") else "indeterminate"
    if c.get("state")!="resolved" or not c.get("resolved_at") or category not in ADMISSIBLE: return "indeterminate"
    if not record.get("previous_decision_ref") or not record.get("current_decision_ref"): return "indeterminate"
    if DIMENSION[category] not in dims or not evidence or len(b.get("rationale",""))<10: return "indeterminate"
    if category=="authority_change":
        if b["authority_changed"] is not True or "authority" not in dims or not b.get("authority_ref"): return "indeterminate"
    elif b["authority_changed"] is not False or "authority" in dims: return "indeterminate"
    if category=="policy_change" and not b.get("policy_ref"): return "indeterminate"
    if category=="lifecycle_change" and not b.get("lifecycle_ref"): return "indeterminate"
    if category=="correction" and not p.get("source_event_ref"): return "indeterminate"
    return "resolved"

def falsify(resolved,unresolved):
    assert consume(resolved)=="resolved"
    assert consume(unresolved)=="unresolved"
    mutations=[
        (resolved,("transition_basis","primary_category"),"peer_pressure"),
        (resolved,("transition_basis","primary_category"),"evaluation_context_change"),
        (resolved,("transition_basis","authority_changed"),True),
        (resolved,("transition_basis","changed_dimensions"),["authority"]),
        (resolved,("transition_basis","evidence_refs"),[]),
        (resolved,("provenance","producer"),""),
        (resolved,("provenance","semantic_profile"),"unknown"),
        (resolved,("previous_decision_ref",),None),
        (resolved,("condition","resolved_at"),None),
        (unresolved,("condition","state"),"resolved"),
        (unresolved,("transition_basis","primary_category"),"evidence_change"),
        (unresolved,("transition_basis","authority_changed"),True)]
    for idx,(base,path,value) in enumerate(mutations):
        record=copy.deepcopy(base); target=record
        for key in path[:-1]: target=target[key]
        target[path[-1]]=value
        if consume(record)=="resolved": raise AssertionError(f"false resolution: {idx}")
    print(f"Decision-resolution consumer: 2 canonical, {len(mutations)} false-success mutations PASS")

if __name__=="__main__":
    fixture=json.loads((ROOT/"validation/tsms/decision-resolution-consumer.json").read_text())
    falsify(fixture["resolved"],fixture["unresolved"])
