import re

def detect_unrestricted_command_execution(code):
    issues = []
    if re.search(r"(exec|system)\(", code):
        issues.append({
            "type": "Unrestricted Command Execution",
            "description": "Unrestricted command execution detected. Avoid using exec or system calls directly."
        })
    return issues
