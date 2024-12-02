def detect_leaking_stack_traces(code):
    if "Exception" in code and "print" in code:
        return [{"type": "Leaking Stack Traces", "description": "Detected exception print statements, which may leak stack traces."}]
    return []
