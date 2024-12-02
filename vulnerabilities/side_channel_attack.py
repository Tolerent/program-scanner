def detect_side_channel_attack(code):
    issues = []
    if "time.sleep(" in code or "response.time" in code:
        issues.append({
            "type": "Side-Channel Attack",
            "description": "Potential side-channel vulnerability detected. Avoid using time-based responses."
        })
    return issues
