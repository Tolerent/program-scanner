def detect_improper_sandbox_configuration(code):
    issues = []
    if "sandbox" not in code and "<iframe" in code:
        issues.append({
            "type": "Improper Sandbox Configuration",
            "description": "Improper sandbox configuration detected. Consider using 'sandbox' attribute in iframes."
        })
    return issues
