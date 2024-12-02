def detect_binary_planting(code):
    issues = []
    if "LoadLibrary(" in code or "dlopen(" in code:
        issues.append({
            "type": "Binary Planting",
            "description": "Potential binary planting vulnerability detected. Ensure safe library loading."
        })
    return issues
