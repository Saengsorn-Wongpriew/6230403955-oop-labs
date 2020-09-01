import math


def hypotenuse(a, b):
    apow = math.pow(a, 2)
    bpow = math.pow(b, 2)
    sum = apow + bpow
    sum_sqrt = math.sqrt(sum)
    print(f"Sqrt({a}^2 + {b}^2) = {sum_sqrt}")


hypotenuse(3.0, 4.0)

hypotenuse(3, 4)

hypotenuse(3, 4.0)
