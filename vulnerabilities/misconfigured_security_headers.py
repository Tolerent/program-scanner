def detect_misconfigured_security_headers(code):
    issues = []
    if "Content-Security-Policy" not in code or "Strict-Transport-Security" not in code:
        issues.append({
            "type": "Misconfigured Security Headers",
            "description": "Missing or misconfigured security headers. Consider adding Content-Security-Policy and Strict-Transport-Security."
        })
    return issues
