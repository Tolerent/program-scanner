def detect_overly_broad_permissions(code):
    issues = []
    if "chmod 777" in code or "setPermissions('ALL')" in code:
        issues.append({
            "type": "Overly Broad Permissions",
            "description": "Overly broad permissions detected. Use restrictive permissions to limit access."
        })
    return issues
