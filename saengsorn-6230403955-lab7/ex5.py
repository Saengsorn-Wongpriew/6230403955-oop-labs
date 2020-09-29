import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    c_circle = Circle(3)
    print(
        "The circle with radius {} "
        "has the area as {:.2f} "
        "and the perimeter as {:.2f}".format(
            c_circle.radius,
            c_circle.area(),
            c_circle.perimeter()
            )
    )

    c_circle = Circle(4)
    print(
        "The circle with radius {} "
        "has the area as {:.2f} "
        "and the perimeter as {:.2f}".format(
            c_circle.radius,
            c_circle.area(),
            c_circle.perimeter()
            )
    )
