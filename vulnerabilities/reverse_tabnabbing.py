import re

def detect_reverse_tabnabbing(code):
    issues = []
    if re.search(r'<a [^>]*href=.*target="_blank"[^>]*>', code) and "noopener" not in code:
        issues.append({
            "type": "Reverse Tabnabbing",
            "description": "Anchor tag with target='_blank' detected without 'noopener noreferrer', which could lead to reverse tabnabbing."
        })
    return issues
