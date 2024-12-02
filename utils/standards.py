def map_to_standard(vuln_type):
    standards = {
        "SQL Injection": "OWASP A1:2017",
        "TOCTOU": "CWE-367",
        # Add mappings as needed
    }
    return standards.get(vuln_type, "Unknown Standard")
