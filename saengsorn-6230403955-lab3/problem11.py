def checkvalue(value):
    if value == "quit":
        return True, True
    elif value.isdigit():
        return False, True
    else:
        return False, False


def checkop(value):
    if value == "quit":
        return True, True
    elif value == "+" or value == "-" or value == "*" or value == "/":
        return False, True
    else:
        print("Unknown Operator")
        return False, False


def calculate(a, b, in_op):
    if in_op == "+":
        return float(a) + float(b), True
    elif in_op == "-":
        return float(a) - float(b), True
    elif in_op == "*":
        return float(a) * float(b), True
    elif in_op == "/":
        if b == "0":
            print("Cannot devide a number by 0")
            return None, False
        else:
            return float(a) / float(b), True
    else:
        return None, False


End = False
while not End:
    if not End:
        correct = 0
        while not correct:
            n_1 = input("Enter the fisrt number: ")
            correct = checkvalue(n_1)[1]
        End = checkvalue(n_1)[0]
        if not End:
            correct = 0
            while not correct:
                n_2 = input("Enter the second number: ")
                correct = checkvalue(n_2)[1]
            End = checkvalue(n_2)[0]
            if not End:
                correct = 0
                while not correct:
                    op = input("Enter the operator: ")
                    correct = checkop(op)[1]
    if not End:
        End = checkop(op)[0]
        output = calculate(n_1, n_2, op)
        if output[1]:
            print(n_1, op, n_2, "=", output[0])
