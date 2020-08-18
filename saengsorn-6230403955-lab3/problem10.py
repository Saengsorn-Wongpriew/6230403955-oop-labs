possitive = 1
n_list = []

while possitive:
    n = int(input("Enter an integer: "))
    if n >= 0:
        n_list.append(n)
    else:
        possitive = 0

if n_list:
    average = sum(n_list) / len(n_list)
    print(average)
else:
    print("empty integers")
