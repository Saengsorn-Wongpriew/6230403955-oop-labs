name = input("Studen Name: ")

grade = ""


def check_valid(mark):
    if mark.isdigit():
        mark = float(mark)
        if mark >= 0 and mark <= 100:
            valid = 1
        else:
            print("Error reading value")
            valid = 0
    else:
        print("Error reading value")
        valid = 0
    return valid

correct = 0

while not correct:
    midterm_exam = input("Please enter midterm mark (0-100): ")
    correct = check_valid(midterm_exam)

correct = 0

while not correct:
    final_exam = input("Please enter final mark (0-100): ")
    correct = check_valid(final_exam)

total = (float(midterm_exam) / 2) + (float(final_exam) / 2)

if total >= 80 and total <= 100:
    grade = "A"
elif total >= 70 and total < 80:
    grade = "B"
elif total >= 60 and total < 70:
    grade = "C"
elif total >= 50 and total < 60:
    grade = "D"
elif total < 50:
    grade = "F"

print(f"{name} has total mark as {total:.4g} and grade as {grade}")
