def checknumber(num):
    try:
        num = int(num)
    except ValueError:
        print("Please Enter a number")
        return 0, 0
    else:
        return num, 1


def checkop(op):
    if op == "+" or op == "-" or op == "*" or op == "/":
        return op, 1
    else:
        print("Please Enter an operator (+, -, *, /)")
        return 0, 0


def calculate(a, b, op):
    if b == 0 and op == "/":
        print("Unknown value!")
        return 0, 0
    elif op == "+":
        return a + b, 1
    elif op == "-":
        return a - b, 1
    elif op == "*":
        return a * b, 1
    elif op == "/":
        return a / b, 1


valid_input = 0
while not valid_input:
    operade1 = input("Please enter the first operade: ")
    valid_input = checknumber(operade1)[1]

valid_input = 0
while not valid_input:
    operade2 = input("Please enter the second operade: ")
    valid_input = checknumber(operade2)[1]

valid_input = 0
while not valid_input:
    operade3 = input("Please enter an operator (+, -, *, /): ")
    valid_input = checkop(operade3)[1]

result = calculate(int(operade1), int(operade2), operade3)

if result[1]:
    print("The answer is:", result[0])
