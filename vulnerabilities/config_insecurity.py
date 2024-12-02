import re

def detect_insecure_default_config(code):
    insecure_patterns = [
        r"debug\s*=\s*True",  # Common pattern for insecure config
        r"allow_insecure_ssl\s*=\s*True",  # Example of insecure SSL setting
    ]
    issues = []
    for pattern in insecure_patterns:
        if re.search(pattern, code, re.IGNORECASE):
            issues.append({"type": "Insecure Default Configuration", "description": "Potential insecure configuration detected."})
    return issues
