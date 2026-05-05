import ast

def analyze_code(code: str):
    tree = ast.parse(code)

    functions = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
    loops = len([n for n in ast.walk(tree) if isinstance(n, (ast.For, ast.While))])

    return {
        "functions": functions,
        "loops": loops
    }
