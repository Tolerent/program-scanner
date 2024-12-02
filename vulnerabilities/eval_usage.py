import re

def detect_eval_usage(code):
    issues = []
    if re.search(r"\beval\(", code):
        issues.append({
            "type": "Dynamic Code Execution",
            "description": "Usage of eval() detected, which is dangerous and could lead to security vulnerabilities."
        })
    return issues
