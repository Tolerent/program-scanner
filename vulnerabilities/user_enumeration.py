def detect_user_enumeration(code):
    issues = []
    if "User not found" in code or "Incorrect password" in code:
        issues.append({
            "type": "User Enumeration",
            "description": "Potential user enumeration vulnerability detected. Avoid revealing specific error messages."
        })
    return issues
