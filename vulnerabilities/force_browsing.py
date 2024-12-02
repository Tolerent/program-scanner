def detect_forced_browsing(code):
    if "/admin" in code or "/config" in code:
        return [{"type": "Forced Browsing", "description": "Forced browsing vulnerability suspected. Sensitive directories found in code."}]
    return []
