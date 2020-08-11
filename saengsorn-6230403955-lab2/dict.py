numbers = {
    "Jane Doe": "+27 555 5367",
    "John Smith": "+27 555 6254",
    "Bob Stone": "+27 555 5689"
    }

numbers["Jane Doe"] = "+27 555 1024"
numbers["Anna Cooper"] = "+27 555 3237"

print(numbers["Bob Stone"])

print(numbers.get("Bob Stone"))

print(numbers.keys())
print(numbers.values())
