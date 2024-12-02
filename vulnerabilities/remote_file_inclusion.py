import re

def detect_remote_file_inclusion(code):
    issues = []
    # Detect URL-based file inclusion
    if re.search(r"(http|https)://", code) and ("include" in code or "require" in code):
        issues.append({
            "type": "Remote File Inclusion (RFI)",
            "description": "Potential remote file inclusion vulnerability detected. Avoid including files over HTTP/HTTPS."
        })
    return issues
