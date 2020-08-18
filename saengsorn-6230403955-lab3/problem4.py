n = int(input("Enter a number to find the factorial: "))
fact_n = 1

for i in range(n):
    fact_n = fact_n * (i+1)

print("Factorial of", n, "is", fact_n)
