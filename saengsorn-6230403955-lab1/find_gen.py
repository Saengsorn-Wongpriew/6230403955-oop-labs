import datetime

name = input("Enter your name: ")
year_of_birth = int(input("Enter the year you were born: "))

now = datetime.datetime.now()
current_year = now.year
age = current_year - year_of_birth

if age >= 73:
    gen = '"Builder"'
elif age >= 55 and age <= 72:
    gen = '"Baby Boomer"'
elif age >= 40 and age <= 54:
    gen = '"X"'
elif age >= 25 and age <= 39:
    gen = '"Y"'
elif age >= 10 and age <= 24:
    gen = '"Z"'
elif age >= 1 and age <= 9:
    gen = '"Alpha"'
else:
    gen = '"unknown"'
print(name, "is", age, "years old. You are generation", gen)
