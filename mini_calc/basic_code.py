def calculator(a, b, op_char):
    if (op_char == '+'):
        result = int(a) + int(b)
    elif (op_char == '-'):
        result = int(a) - int(b)
    elif (op_char == '*'):
        result = int(a) * int(b)
    elif(op_char == '/'):
        if int(b) == 0 :
            result= 'Cannot divide by zero'
        else:
            result = int(a) / int(b)
    print("a = {} , b = {} , with operators = {} ,result = {}".format(a, b, op_char, result))

def fetch_numbers():
    print(" __ please enter your data then show result __")
    check_a_var = False
    check_b_var = False
    check_op_char = False
    while( (check_a_var != True) and (check_b_var != True) and (check_op_char != True)):
        a = input("a = ") #a = input("")
        b = input("b = ") #b = input("")
        op_char = input("operation character( + - * / ): ") #op_char = input("")
        check_a_var  = a.isnumeric()
        check_b_var  = b.isnumeric()
        for item in op_characters:
            if op_char == item:
                check_op_char = True
    calculator(a,b, op_char)

def defination_global_variables():
    if ('a' not in globals()) and ('b' not in globals()) and ('op_char' not in globals()):
        global a
        global b
        global op_characters
    a = 0
    b = 0 
    op_characters = ('+', '-', '*' , '/')
    fetch_numbers()

# start calculator
defination_global_variables()  