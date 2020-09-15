def append_to_new_txt(filename, new_filename, newlines):
    
    textfile = open(filename,"r", encoding="utf-8")
    text = textfile.readlines()
    textfile.close()
    
    textfile = open(new_filename,"w",  encoding="utf-8")
    for i in text:
        textfile.write(i)
    textfile.close()
    
    textfile = open(new_filename,"a+",  encoding="utf-8")
    for l in newlines:
        textfile.write(l)
    textfile.close()


def read_from_txt(filename):
    textfile = open(filename,"r", encoding="utf-8")
    text = textfile.readlines()
    textfile.close()
    
    for i in text:
        print(i, end="")


if __name__ == "__main__":
    
    line1 = "\nMotto: วิทยา จริยา ปัญญา"
    line2 = "\nMotto in English: Knowledge, Virtues, Wisdom"
    
    append_to_new_txt("kku.txt", "kku2.txt", [line1, line2])
    read_from_txt("kku2.txt")
