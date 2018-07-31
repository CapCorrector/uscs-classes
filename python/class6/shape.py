import math

class Shape:
    def __init__(self, name):
        self.name = name

    def get_circumference(self):
        return NotImplemented

    def get_size(self):
        return NotImplemented

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def get_circumference(self):
        return 2 * (self.length + self.width)

    def get_size(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.radius

    def get_size(self):
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    r = Rectangle('rect', 10, 5)
    print(r.get_circumference())
    print(r.get_size())

    c = Circle('circle', 20)
    print(c.get_circumference())
    print(c.get_size())
