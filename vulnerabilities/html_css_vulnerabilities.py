import re

def detect_html_css_vulnerabilities(code):
    issues = []
    
    # Detect inline JavaScript in HTML
    if re.search(r"<script.*?>.*?</script>", code, re.DOTALL | re.IGNORECASE):
        issues.append({"type": "Inline JavaScript", "description": "Found inline JavaScript, which could lead to XSS vulnerabilities."})

    # Detect dangerous HTML attributes like onerror, onclick
    dangerous_attributes = ["onerror", "onclick", "onload", "onmouseover"]
    for attr in dangerous_attributes:
        if re.search(rf"{attr}\s*=", code, re.IGNORECASE):
            issues.append({"type": "HTML Attribute Vulnerability", "description": f"Found dangerous attribute '{attr}'."})

    # Detect CSS injection (style tag or inline style with potential CSS injection)
    if re.search(r"<style.*?>.*?</style>", code, re.DOTALL | re.IGNORECASE) or 'style="' in code:
        issues.append({"type": "CSS Injection", "description": "Found potential CSS injection vulnerability."})

    return issues
