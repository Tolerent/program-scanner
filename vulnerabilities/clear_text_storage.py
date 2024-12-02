import re

def detect_clear_text_storage(code):
    issues = []
    if re.search(r"(password|secret|token) ?= ?['\"]", code):
        issues.append({
            "type": "Clear Text Storage of Sensitive Information",
            "description": "Sensitive information detected in clear text storage. Store securely using encryption."
        })
    return issues
