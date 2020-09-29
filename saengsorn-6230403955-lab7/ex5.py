class Numbers:

    def __init__(self, n1, n2):
        self.x = n1
        self.y = n2

    def add(self):
        return "{} + {} = {}".format(self.x, self.y, (self.x + self.y))

    @classmethod
    def display_factors(cls, number):
        if number % 2 == 0:
            cls.display = number
            return "Factors of {} is {} and {}".format(
                cls.display, cls.display/2, cls.display - cls.display/2
            )
        else:
            cls.display = number
            return "Factors of {} is {} and {}".format(
                cls.display,
                (cls.display - 1) / 2,
                cls.display - (cls.display + 1) / 2
            )

    @staticmethod
    def is_valid_divisor(number):
        if number == 0:
            return "{} is not a valid devisor".format(number)
        else:
            return "{} is a valid devisor".format(number)


if __name__ == "__main__":
    print(Numbers(3, 5).add())
    print(Numbers.display_factors(6))
    print(Numbers.display_factors(8))
    print(Numbers.is_valid_divisor(2))
    print(Numbers.is_valid_divisor(0))
