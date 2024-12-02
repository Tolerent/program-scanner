def detect_weak_encryption_algorithms(code):
    issues = []
    if "DES" in code or "RC4" in code:
        issues.append({
            "type": "Weak Encryption Algorithm",
            "description": "Weak encryption algorithm (DES, RC4) detected. Use stronger algorithms like AES."
        })
    return issues
