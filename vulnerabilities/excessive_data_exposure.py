def detect_excessive_data_exposure(code):
    issues = []
    if "SELECT *" in code:
        issues.append({
            "type": "Excessive Data Exposure",
            "description": "Detected excessive data exposure. Avoid using SELECT * in database queries."
        })
    return issues
