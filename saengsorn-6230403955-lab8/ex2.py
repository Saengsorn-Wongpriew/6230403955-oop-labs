class Vehicle:
    def __init__(self, name, speed, mileage):
        self.name = name
        self.__speed = speed
        self.mileage = mileage

    def set_speed(self, new_speed):
        self.__speed = new_speed

    def get_speed(self):
        return self.__speed


class Car(Vehicle):
    def __init__(self, name, speed, mileage, door):
        self.door = door
        super().__init__(name, speed, mileage)

    def __str__(self):
        s = "Name: {} speed: {}, mileage: {:,} num doors: {}".format(
            self.name,
            self.get_speed(),
            self.mileage,
            self.door
        )
        return s


class Bus(Vehicle):
    def __init__(self, name, speed, mileage, cap):
        self.cap = cap
        super().__init__(name, speed, mileage)

    def __str__(self):
        s = "{} speed: {} mileage: {:,} capacity: {}".format(
            self.name,
            self.get_speed(),
            self.mileage,
            self.cap
        )
        return s


if __name__ == "__main__":
    car = Car("Toyota Vios", 90, 150000, 4)
    bus = Bus("School Volvo", 12, 200000, 100)
    print(car)
    print(bus)
    bus.set_speed(30)
    print(bus)
