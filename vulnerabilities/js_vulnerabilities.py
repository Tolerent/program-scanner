import re

def detect_js_vulnerabilities(code):
    issues = []
    
    # Detect usage of eval (dangerous function in JavaScript)
    if "eval(" in code:
        issues.append({"type": "JavaScript Eval Usage", "description": "Found usage of eval(), which can lead to security vulnerabilities."})

    # Detect document.write (another dangerous function in JavaScript)
    if "document.write(" in code:
        issues.append({"type": "JavaScript Document Write", "description": "Found usage of document.write(), which can lead to security vulnerabilities."})

    # Detect inline event handlers (e.g., onclick, onmouseover)
    inline_events = ["onclick", "onmouseover", "onerror"]
    for event in inline_events:
        if re.search(rf"{event}\s*=", code, re.IGNORECASE):
            issues.append({"type": "JavaScript Inline Event Handler", "description": f"Found inline event handler '{event}'."})

    return issues
