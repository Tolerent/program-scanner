def detect_sensitive_data_leak(code):
    issues = []
    if "Referer" in code and "Authorization" in code:
        issues.append({
            "type": "Sensitive Data Leak via Referrers",
            "description": "Potential sensitive data leak detected through referrer headers."
        })
    return issues
