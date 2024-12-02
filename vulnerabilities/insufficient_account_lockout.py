def detect_insufficient_account_lockout(code):
    issues = []
    if "account.lockout" not in code.lower() and "attempts" in code.lower():
        issues.append({
            "type": "Insufficient Account Lockout Mechanism",
            "description": "Account lockout mechanism not detected. Implement account lockout to prevent brute-force attacks."
        })
    return issues
