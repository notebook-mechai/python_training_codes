import ast # Abstract Syntax Tree
import re # regular expressions

class CodeVisitor(ast.NodeVisitor):
    def __init__(self):
        self.tokenized_code = []
        self.results = []

    def visit_If(self, node):
        self.tokenized_code.append(f"if L[{node.lineno}]")
        self.generic_visit(node)

    def visit_While(self, node):
        self.tokenized_code.append(f"while L[{node.lineno}]")
        self.generic_visit(node)

    def visit_For(self, node):
        self.tokenized_code.append(f"for L[{node.lineno}]")
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.tokenized_code.append(f"def L[{node.lineno}]")
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id == "print":
            self.tokenized_code.append(f"print L[{node.lineno}]")
            self.tokenized_code.append(f"( L[{node.lineno}]")
            self.generic_visit(node)
            self.tokenized_code.append(f") L[{node.lineno}]")
        else:
            self.generic_visit(node)

    def visit_BinOp(self, node):
        left = self._expr_to_source(node.left)
        op = self._op_to_source(node.op)
        right = self._expr_to_source(node.right)
        self.tokenized_code.append(f"{left} L[{node.lineno}]")
        self.tokenized_code.append(f"{op} L[{node.lineno}]")
        self.tokenized_code.append(f"{right} L[{node.lineno}]")
        self.generic_visit(node)

    def _expr_to_source(self, node):
        # """Convert an expression node into Python source code."""
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Constant):
            return repr(node.value)
        return ""

    def _op_to_source(self, op):
        # """Convert an operator node into Python source code."""
        if isinstance(op, ast.Add):
            return "+"
        elif isinstance(op, ast.Sub):
            return "-"
        elif isinstance(op, ast.Mult):
            return "*"
        elif isinstance(op, ast.Div):
            return "/"
        return ""

# Preprocess the code to fix syntax issues
def preprocess_code(code):
    # Ensure proper quotes around strings
    code = re.sub(r'print\s*\((.+?)\)', lambda m: f'print({repr(m.group(1).strip())})', code)
    return code

# Read and process the code from the file
file_name = "code.txt"
try:
    with open(file_name, 'r') as file:
        raw_code = file.read()

    # Preprocess the code
    code = preprocess_code(raw_code)

    # Parse the code into an AST
    tree = ast.parse(code)

    # Visit the AST nodes
    visitor = CodeVisitor()
    visitor.visit(tree)

    # Print the tokenized code with line numbers
    for token in visitor.tokenized_code:
        print(token)

    # Simulating Python script execution``
    print("\nResults:")
    result_globals = {}
    exec(code, {}, result_globals)

    # Extract and print numerical results
    for key, value in result_globals.items():
        if isinstance(value, (int, float)):
            print(value)

except Exception as e:
    print(f"An error occurred: {e}")
