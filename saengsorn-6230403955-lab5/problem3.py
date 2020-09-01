import math


def hypotenuse(a, b):
    if a and b:
        try:
            apow = math.pow(a, 2)
            bpow = math.pow(b, 2)
            sum = apow + bpow
            sum_sqrt = math.sqrt(sum)
            return sum_sqrt
        except TypeError:
            return None
    else:
        return None


print("Sqrt({}^2 + {}^2) = {}".format(3, 4, hypotenuse(3, 4)))
print("Sqrt({}^2 + {}^2) = {}".format("3", "4", hypotenuse("3", "4")))
print("Sqrt({}^2 + {}^2) = {}".format(3, "4.0", hypotenuse(3, "4.0")))
