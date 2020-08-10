valid_value = False

while not valid_value:
    try:
        t_f = float(input("Value of temperature in Fahrenheit: "))
        valid_value = True
    except ValueError:
        print("Error reading temperature value.")

t_c = (5 / 9) * (t_f - 32)

print(f"temperature in Celsius is {t_c:.4g}")
