def detect_environment_variable_exposure(code):
    issues = []
    if "os.environ" in code:
        issues.append({
            "type": "Environment Variable Exposure",
            "description": "Environment variable exposure detected. Avoid exposing environment variables in code."
        })
    return issues
