```python
"""
Architecture validation script.
Ensures the core remains pure and extensions don't violate principles.
"""

import ast
import importlib.util
from pathlib import Path

def validate_core_purity():
    """Validate that core files contain no implementations"""
    core_path = Path("core_formal/operators_axiomatic.py")
    
    with open(core_path, 'r') as f:
        content = f.read()
    
    # Parse AST
    tree = ast.parse(content)
    
    violations = []
    
    # Check for function definitions (except property methods)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # Allow property methods (they're structural)
            if not node.name.startswith('is_') and not node.name == '__str__':
                violations.append(f"Function definition found: {node.name}")
        
        # Check for if statements
        if isinstance(node, ast.If):
            violations.append("If statement found in core")
        
        # Check for arithmetic operations
        if isinstance(node, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
            violations.append(f"Arithmetic operation found: {type(node).__name__}")
    
    return violations

def validate_dependencies():
    """Validate unidirectional dependencies"""
    # Core should not import from extensions
    core_path = Path("core_formal/operators_axiomatic.py")
    
    with open(core_path, 'r') as f:
        content = f.read()
    
    if "from extensions" in content or "import extensions" in content:
        return ["Core imports from extensions - VIOLATION"]
    
    return []

def validate_extensions():
    """Validate extensions import core correctly"""
    extensions_dir = Path("extensions")
    violations = []
    
    for ext_file in extensions_dir.glob("*.py"):
        with open(ext_file, 'r') as f:
            content = f.read()
        
        # Extensions should import from core
        if "from core_formal" not in content and "import core_formal" not in content:
            violations.append(f"{ext_file.name} doesn't import from core")
    
    return violations

def main():
    print("=== ARCHITECTURAL VALIDATION ===\n")
    
    # Validate core purity
    print("1. Validating core purity...")
    core_violations = validate_core_purity()
    if core_violations:
        print("   ❌ VIOLATIONS FOUND:")
        for v in core_violations:
            print(f"      - {v}")
    else:
        print("   ✅ Core is pure (no implementations)")
    
    # Validate dependencies
    print("\n2. Validating dependencies...")
    dep_violations = validate_dependencies()
    if dep_violations:
        print("   ❌ VIOLATIONS FOUND:")
        for v in dep_violations:
            print(f"      - {v}")
    else:
        print("   ✅ Dependencies are unidirectional")
    
    # Validate extensions
    print("\n3. Validating extensions...")
    ext_violations = validate_extensions()
    if ext_violations:
        print("   ⚠️  WARNINGS:")
        for v in ext_violations:
            print(f"      - {v}")
    else:
        print("   ✅ Extensions properly import core")
    
    # Summary
    print("\n=== VALIDATION SUMMARY ===")
    total_violations = len(core_violations) + len(dep_violations)
    
    if total_violations == 0:
        print("✅ ARCHITECTURE IS SOUND")
        print("Core remains incontrovertible, extensions are clean.")
    else:
        print(f"❌ {total_violations} ARCHITECTURAL VIOLATIONS")
        print("The system's philosophical integrity is compromised.")
    
    return total_violations == 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
