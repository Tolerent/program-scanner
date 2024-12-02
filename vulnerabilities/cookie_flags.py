import re

def detect_cookie_flags(code):
    issues = []
    if re.search(r"Set-Cookie", code) and "Secure" not in code and "HttpOnly" not in code:
        issues.append({
            "type": "Lack of Secure Cookie Flags",
            "description": "Cookie is set without 'Secure' and 'HttpOnly' flags, which could lead to security vulnerabilities."
        })
    return issues
