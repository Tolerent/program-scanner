def detect_insecure_http_methods(code):
    issues = []
    insecure_methods = ["TRACE", "PUT", "DELETE"]
    for method in insecure_methods:
        if method in code:
            issues.append({
                "type": "Allowing Insecure HTTP Methods",
                "description": f"Detected use of insecure HTTP method: {method}. Avoid using these methods in production."
            })
    return issues
