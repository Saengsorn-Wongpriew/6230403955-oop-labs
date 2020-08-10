numbers = {
    "Jane Doe": "+27 555 5367",
    "John Smith": "+27 555 6254",
    "Bob Stone": "+27 555 5689"
    }

numbers["Jane Doe"] = "+27 555 1024"
numbers["Anna Cooper"] = "+27 555 3237"

print(numbers["Bob Stone"])

if "Bob Stone" in numbers:
    print(numbers["Bob Stone"])
else:
    print("None")

print(numbers.keys())
print(numbers.values())
