import re

def detect_unvalidated_json_input(code):
    issues = []
    if re.search(r"json.loads\(", code) and "validate" not in code:
        issues.append({
            "type": "Unvalidated JSON Input",
            "description": "Potential unvalidated JSON input detected, which could lead to injection attacks."
        })
    return issues
