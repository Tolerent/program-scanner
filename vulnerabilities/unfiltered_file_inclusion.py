import re

def detect_unfiltered_file_inclusion(code):
    issues = []
    if re.search(r"(require|include)\(", code) and "sanitize" not in code:
        issues.append({
            "type": "Unfiltered File Inclusion",
            "description": "Unfiltered file inclusion detected. Ensure file paths are validated."
        })
    return issues
