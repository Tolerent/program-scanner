def detect_improper_access_token_usage(code):
    issues = []
    if "access_token" in code and "secure" not in code:
        issues.append({
            "type": "Improper Usage of Access Tokens",
            "description": "Improper usage of access tokens detected. Ensure tokens are stored securely."
        })
    return issues
