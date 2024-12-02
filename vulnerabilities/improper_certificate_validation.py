def detect_improper_certificate_validation(code):
    issues = []
    # Detect disabling of certificate validation
    if "verify=False" in code or "ssl.SSLContext()" in code:
        issues.append({
            "type": "Improper Certificate Validation",
            "description": "Improper certificate validation detected. Ensure certificates are properly validated."
        })
    return issues
