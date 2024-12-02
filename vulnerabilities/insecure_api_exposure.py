import re

def detect_insecure_api_exposure(code):
    issues = []
    if re.search(r"@app.route\('/api/.+public", code) or "public" in code.lower():
        issues.append({
            "type": "Insecure API Exposure",
            "description": "Detected public API exposure. Ensure API endpoints are properly secured."
        })
    return issues
