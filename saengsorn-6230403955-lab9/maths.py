def sum(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def devide(a, b):
    if b == 0:
        raise ValueError("Cannot devide by zero")
    return a / b
