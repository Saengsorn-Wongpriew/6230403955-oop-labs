class Student:
    def __init__(self, name, *course_ids):
        self.name = name
        self.course_ids = course_ids


if __name__ == "__main__":
    manee = Student("Manee", "842004")
    mana = Student("Mana", "842004", "842005", "813701")
    chujai = Student("Chujai", "842004", "842005")
    print("{} registered courses {}".format(manee.name, manee.course_ids))
    print("{} registered courses {}".format(mana.name, mana.course_ids))
    print("{} registered courses {}".format(chujai.name, chujai.course_ids))
