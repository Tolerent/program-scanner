import re

def detect_predictable_temp_file_names(code):
    issues = []
    # Detect hardcoded temp file paths
    if re.search(r"/tmp/|tempfile.mktemp\(", code):
        issues.append({
            "type": "Predictable Temporary File Names",
            "description": "Predictable temporary file name detected. Use secure random naming for temp files."
        })
    return issues
