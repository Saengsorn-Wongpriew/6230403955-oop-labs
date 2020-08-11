a = []
b = []

for n in range(4):
    a.append(n + 1)
    b.append((n + 1)*2 - 1)

a = set(a)
b = set(b)
c = a.union(b)
d = a.difference(b)

print("a is", a)
print("b is", b)
print("a | b is", c)
print("a - b is", d)

a = list(range(20))
print(a)

b = list(range(3, 13))
print(b)

a = list(range(2, 53, 3))
print(a)
