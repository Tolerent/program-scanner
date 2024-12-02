import re

def detect_cookie_overflow(code):
    issues = []
    # Pattern to identify large cookie values being set
    if re.search(r"Set\-Cookie", code) and len(code) > 4096:
        issues.append({
            "type": "Cookie Overflow",
            "description": "Potential cookie overflow detected. Cookies should be under 4096 bytes."
        })
    return issues
