def detect_dead_code(code):
    # Placeholder: Could be extended with AST analysis for unreachable code
    if "if False:" in code:
        return [{"type": "Dead Code", "description": "Detected dead code that will never execute."}]
    return []
