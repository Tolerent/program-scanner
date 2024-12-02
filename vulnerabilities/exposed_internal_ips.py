import re

def detect_exposed_internal_ips(code):
    issues = []
    if re.search(r"(192\.168|10\.\d+|172\.(1[6-9]|2[0-9]|3[0-1]))\.\d+\.\d+", code):
        issues.append({
            "type": "Exposed Private/Internal IPs",
            "description": "Detected exposed private or internal IP address. Avoid exposing internal network information."
        })
    return issues
