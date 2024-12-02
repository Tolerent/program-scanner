import ast

def parse_code(code):
    return ast.parse(code)

def analyze_ast(tree):
    vulnerabilities = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and getattr(node.func, 'id', '') == 'exec':
            vulnerabilities.append({"type": "Dynamic Execution", "description": "Detected use of exec, which may be unsafe."})
    return vulnerabilities
