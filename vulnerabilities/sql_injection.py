import re

def detect_sql_injection(code):
    sql_patterns = [
        r"SELECT .* FROM .* WHERE .*=[^\s]*",  # Basic SQL Injection pattern
        r"\" OR \"1\"=\"1\"",  # Common SQL Injection test pattern
    ]
    issues = []
    for pattern in sql_patterns:
        if re.search(pattern, code, re.IGNORECASE):
            issues.append({"type": "SQL Injection", "description": "Possible SQL injection detected."})
    return issues
