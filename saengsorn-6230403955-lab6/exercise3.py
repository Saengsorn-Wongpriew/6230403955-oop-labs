filename = input("Enter a filename:")

textfile = open(filename, "r", encoding="utf-8")
text = textfile.readlines()
textfile.close()

for x in text:
    print(x, end="")
