import re

def detect_ssrf(code):
    issues = []
    if re.search(r"(http|https)://", code) and ("requests.get(" in code or "urllib.request.urlopen(" in code):
        issues.append({
            "type": "Server-Side Request Forgery (SSRF)",
            "description": "Potential SSRF vulnerability detected. Avoid unsanitized external requests."
        })
    return issues
