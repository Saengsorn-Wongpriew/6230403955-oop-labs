import random

a = random.randint(1, 10)
b = random.randint(1, 10)

a, b = int(a), int(b)

avg = (a + b)/2

std = (((a-avg)**2 + (b-avg)**2)/2)**0.5

print("The average of", a, "and", b, "is", avg)

print("The standard deviation of", a, "and", b, "is", std)
