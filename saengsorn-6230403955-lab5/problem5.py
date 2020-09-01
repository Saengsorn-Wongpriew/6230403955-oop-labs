def calculate(n1, n2, op):
    n1, n2 = float(n1), float(n2)
    if n2 == 0 and op == "/":
        return "Cannot devide by zero"
    elif op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        return n1 / n2


def int_float(a):
    if a == "" or a == "float":
        return 1, 1
    elif a == "int":
        return 2, 1
    else:
        return 0, 0


def input_op(a):
    if a.lower() == "q":
        return a, 2
    try:
        a = float(a)
        return a, 1
    except ValueError:
        print("Please enter a number")
        return 0, 0


def check_operator(a):
    if a.lower() == "q":
        return a, 2
    elif a == "":
        return "+", 1
    elif a == "+" or a == "-" or a == "*" or a == "/":
        return a, 1
    else:
        print("Operation must be ADD, SUB, MUL, or DIV")
        if a == "(":
            return 0, 3
        else:
            return 0, 0


def robust_calculator():
    while True:
        correct = 0
        while not correct:
            operand1 = input("Please enter the first operand ('q' to quit):")
            op1 = input_op(operand1)
            correct = op1[1]
        if op1[1] == 2:
            break

        correct = 0
        while not correct:
            operand2 = input("Please enter the second operand:")
            op2 = input_op(operand2)
            correct = op2[1]
        if op2[1] == 2:
            break

        correct = 0
        while not correct:
            operator = input("Enter an operation ('+', '-', '*', '/'):")
            op3 = check_operator(operator)
            correct = op3[1]
        retry = 0
        if op3[1] == 2:
            break
        elif op3[1] == 3:
            retry = 1
        if not retry:

            correct = 0
            while not correct:
                output_format = input("Enter output format (float, int):")
                opt_format = int_float(output_format)
                correct = opt_format[1]

            ans = calculate(op1[0], op2[0], op3[0])
            if ans == "Cannot devide by zero":
                print("We cannot perform your requested calculation")
                print(ans)
            else:
                if opt_format[0] == 1:
                    print("{} {} {} = {}".format(
                        op1[0], op3[0], op2[0], float(ans)
                        )
                    )
                else:
                    print("{} {} {} = {}".format(
                        op1[0], op3[0], op2[0], int(round(ans))
                        )
                    )


if __name__ == "__main__":
    robust_calculator()
