import re

def detect_password_in_url(code):
    issues = []
    if re.search(r"(http|https)://.*password=.*", code):
        issues.append({
            "type": "Password in URL",
            "description": "Password detected in URL, which could expose sensitive information in logs and browser history."
        })
    return issues
