import re

def detect_weak_random_seeds(code):
    issues = []
    if re.search(r"seed\(1\)", code) or re.search(r"seed\(0\)", code):
        issues.append({
            "type": "Use of Weak Random Seeds",
            "description": "Weak random seed detected. Use a more secure seed."
        })
    return issues
