def detect_session_fixation(code):
    issues = []
    if "session_id=" in code and "new session" not in code:
        issues.append({
            "type": "Session Fixation",
            "description": "Session ID is set without rotating on authentication. This could lead to session fixation attacks."
        })
    return issues
