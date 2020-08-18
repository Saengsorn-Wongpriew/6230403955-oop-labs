input_99 = False

while not input_99:
    n = int(input("Enter an integer: "))
    if n == 99:
        input_99 = True
    elif n % 2 == 0:
        print(n)
