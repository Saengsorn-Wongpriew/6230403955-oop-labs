num_lst =
input("Enter the list of numbers(delimited by a comma): ").split(",")

print(num_lst)

try:
    index_lst = int(input("Enter an index: "))
    print(num_lst[index_lst])
except IndexError:
    print("The list has no element at index", index_lst)
