import re

def detect_insufficient_entropy(code):
    issues = []
    # Detect usage of weak random functions
    if re.search(r"\brand\b", code) or re.search(r"\brandom.randint\(", code):
        issues.append({
            "type": "Insufficient Entropy",
            "description": "Weak random number generation detected, which may lead to insufficient entropy."
        })
    return issues
