import re

def detect_insecure_websocket(code):
    issues = []
    if re.search(r"new WebSocket\('ws://", code):
        issues.append({
            "type": "Insecure WebSocket Implementation",
            "description": "Insecure WebSocket connection ('ws://' detected). Use 'wss://' for secure connections."
        })
    return issues
