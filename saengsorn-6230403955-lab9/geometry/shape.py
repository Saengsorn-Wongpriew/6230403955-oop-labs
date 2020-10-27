import abc
import random


class Shape(abc.ABC):
    @abc.abstractmethod
    def __init__(self, color):
        self.color = color

    @abc.abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    num_circles = 0

    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
        Circle.num_circles += 1

    def set_radius(self, radius):
        self.radius = radius

    def draw(self):
        print("Drawing a circle with radius", self.radius)

    @classmethod
    def get_num_circles(cls):
        return cls.num_circles


class Rectangle(Shape):
    num_rectangles = 0

    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
        Rectangle.num_rectangles += 1

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def draw(self):
        print("Drawing a rectangle with "
              "width", self.width, "height", self.height)

    def print_area(self):
        print("Rectangle width", self.width, "height", self.height,
              "has area as", self.width * self.height)

    @classmethod
    def get_num_rectangles(cls):
        return cls.num_rectangles


if __name__ == "__main__":
    circles = []
    rectangles = []
    NUM_OBJECTS = 3
    MIN = 10
    MAX = 20
    colors = ["green", "yellow", "blue", "red", "pink"]
    for i in range(NUM_OBJECTS):
        color = random.choice(colors)
        radius = random.randint(MIN, MAX)
        circles.append(Circle(color, radius))
        circles[i].draw()
    print("Num circles is {}".format(Circle.get_num_circles()))

    for i in range(NUM_OBJECTS):
        color = random.choice(colors)
        width = random.randint(MIN, MAX)
        height = random.randint(MIN, MAX)
        rectangles.append(Rectangle(color, width, height))
        rectangles[i].draw()
        rectangles[i].print_area()
    print("Num rectangle is {}".format(Rectangle.get_num_rectangles()))
