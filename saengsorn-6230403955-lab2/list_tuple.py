a = (1), (2, 2), (3, 3, 3)

print(a[1][1])

w = []
v = []

for i in range(5):
    for k in range(10):
        v.append(k+((i-1)*10))
    v = []
    if i < 4:
        w.append(v)
print([w[0][-2] , w[0][-1]])
