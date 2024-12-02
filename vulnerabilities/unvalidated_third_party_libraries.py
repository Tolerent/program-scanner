import re

def detect_unvalidated_third_party_libraries(code):
    issues = []
    # Pattern to detect import statements without validation comments
    if re.search(r"import", code) and "validate" not in code.lower():
        issues.append({
            "type": "Unvalidated Third-Party Libraries",
            "description": "Third-party library imported without validation. Ensure libraries are from trusted sources."
        })
    return issues
