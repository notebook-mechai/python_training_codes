file_name = "core_code.txt"
file = open("core_code.txt", "r")
code_calc = file.read()
exec(code_calc)
file.close()




