def detect_untrusted_deserialization(code):
    if "pickle.loads" in code or "pickle.load" in code:
        return [{"type": "Untrusted Deserialization", "description": "Potential untrusted deserialization detected."}]
    return []
