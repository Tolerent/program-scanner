def detect_weak_hash_functions(code):
    issues = []
    if "md5(" in code or "sha1(" in code:
        issues.append({
            "type": "Weak Hash Function",
            "description": "Weak hash function (MD5 or SHA-1) detected. Consider using SHA-256 or stronger."
        })
    return issues
