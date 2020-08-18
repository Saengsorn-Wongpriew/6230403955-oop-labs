months = (
    'January', 'February', 'March',
    'April', 'May', 'June',
    'July', 'August', 'September',
    'October', 'November', 'December'
    )

days = (
    31, 28, 31,
    30, 31, 30,
    31, 31, 30,
    31, 30, 31
    )

dict_date = {}

for d in range(12):
    dict_date[months[d]] = days[d]

print(dict_date.items())

select_month = input("Enter month: ")

if select_month in dict_date:
    print("Number of days in", select_month, "is", dict_date[select_month])
else:
    print("No matched.")
