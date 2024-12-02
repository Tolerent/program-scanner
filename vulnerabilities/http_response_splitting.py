import re

def detect_http_response_splitting(code):
    issues = []
    # Pattern to detect headers with unvalidated user input
    if re.search(r"Set\-Cookie|Location|Content\-Type", code) and "\r\n" in code:
        issues.append({
            "type": "HTTP Response Splitting",
            "description": "Potential HTTP Response Splitting detected. Avoid including newline characters in headers."
        })
    return issues
