import ast

file_name = "basic_code.txt"
file = open(file_name, "r")
code =  file.read()

tree = ast.parse(code)

print(ast.dump(tree, indent = 4))
file.close()
