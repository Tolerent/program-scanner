import re

def detect_shell_metacharacters(code):
    issues = []
    if re.search(r"[;&|<>]", code) and ("subprocess.call(" in code or "os.system(" in code):
        issues.append({
            "type": "Improper Use of Shell Metacharacters",
            "description": "Improper use of shell metacharacters detected. Avoid unvalidated commands in shell execution."
        })
    return issues
