def detect_exposed_debug_info(code):
    if "debug" in code and "True" in code:
        return [{"type": "Exposed Debug Information", "description": "Debug mode is enabled, which exposes sensitive information."}]
    return []
