import re

def detect_local_file_inclusion(code):
    issues = []
    # Detect file inclusion without sanitizing input
    if re.search(r"(open|include|require|file_get_contents)\(", code) and "sanitize" not in code:
        issues.append({
            "type": "Local File Inclusion (LFI)",
            "description": "Potential local file inclusion vulnerability detected. Ensure file paths are validated."
        })
    return issues
