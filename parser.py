import ast
import os

def parse_file(filepath):
    """Extract all imports from a single Python file."""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        source = f.read()
    
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []
    
    imports = []
    for node in ast.walk(tree):
        # import os, sys
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name.split('.')[0])
        # from os.path import join
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module.split('.')[0])
    
    return list(set(imports))


def parse_project(directory):
    """Walk a directory and parse all Python files."""
    project = {}  # {module_name: [dependencies]}
    
    # First pass: collect all module names in the project
    local_modules = set()
    for root, dirs, files in os.walk(directory):
        # Skip hidden folders and __pycache__
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for file in files:
            if file.endswith('.py'):
                module = file[:-3]  # strip .py
                local_modules.add(module)
    
    # Second pass: parse imports, keep only local ones
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                module = file[:-3]
                all_imports = parse_file(filepath)
                # Only keep imports that are local to this project
                local_deps = [i for i in all_imports if i in local_modules and i != module]
                project[module] = local_deps
    
    return project