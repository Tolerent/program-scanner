def detect_ui_redress_attack(code):
    issues = []
    if "<iframe" in code and "X-Frame-Options" not in code:
        issues.append({
            "type": "UI Redress Attack",
            "description": "Potential UI redress attack detected. Add X-Frame-Options to prevent clickjacking."
        })
    return issues
