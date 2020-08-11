weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]

print(f"Weekday are {weekday}")
print(f"Weekend are {weekend}")

days = weekday + weekend
print(f"Days are {days}")

sorted_days = sorted(days)
print(f"Sorted days are {sorted_days}")

reversed_days = list(reversed(days))
print(f"Reversed days are {reversed_days}")

last_2_days = [days[-2], days[-1]]
print(f"The last two days of list days are {last_2_days}")
