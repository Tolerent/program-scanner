def detect_client_side_caching(code):
    issues = []
    # Detect cache control headers allowing sensitive data caching
    if "Cache-Control: public" in code or "Cache-Control: max-age" in code:
        issues.append({
            "type": "Client-Side Caching of Sensitive Data",
            "description": "Sensitive data is being cached on the client side. Consider setting Cache-Control: no-store."
        })
    return issues
