fruits = ["Grapefruit", "Longan", "Orange", "Apple", "Cherry"]
emu_fruits = list(enumerate(fruits, start=1))

for i in range(len(emu_fruits)):
    print(str(emu_fruits[i][0]) + ". " + str(emu_fruits[i][1]))
