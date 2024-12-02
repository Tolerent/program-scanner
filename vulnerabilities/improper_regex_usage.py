import re

def detect_improper_regex_usage(code):
    issues = []
    if re.search(r"\.\*\.\*", code):
        issues.append({
            "type": "Improper Use of Regular Expressions",
            "description": "Improper regular expression usage detected, which could lead to inefficiencies or vulnerabilities."
        })
    return issues
