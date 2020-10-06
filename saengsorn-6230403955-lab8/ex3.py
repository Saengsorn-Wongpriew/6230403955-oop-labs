class Pet:
    def __init__(self, args):
        self.args = args

    def show_info(self):
        print("I'm" + self.args)

    def move(self):
        print("moving ...")


class Cat(Pet):
    def __init__(self, *args):
        super().__init__(args)

    def show_info(self):
        name = self.args[0]
        belong = self.args[1]
        color = self.args[2]
        print(f"I'm {name} and is {color} belonging to {belong}")

    def move(self):
        print("Cat likes to walk more than run")


class Dog(Pet):
    def __init__(self, *args):
        super().__init__(args)

    def show_info(self):
        name = self.args[0]
        belong = self.args[1]
        color = self.args[2]
        print(f"I'm {name} and is {color} belonging to {belong}")

    def move(self):
        print("Dog likes to run more than walk")

    def eat_cat(self, animal):
        name = self.args[0]
        animal_name = animal.args[0]
        print(f"Dog {name} eats cat {animal_name}")


if __name__ == "__main__":
    pet1 = Pet("Thongdaeng")
    pet1.show_info()
    pet1.move()
    cat1 = Cat("Thongdee", "Manee", "white")
    cat1.show_info()
    cat1.move()
    dog1 = Dog("Thongdum", "Mana", "black")
    dog1.show_info()
    dog1.move()
    dog1.eat_cat(cat1)
