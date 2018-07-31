import math

class Shape:
    def __init__(self, name):
        self.name = name

    def get_circumference(self):
        return NotImplemented

    def get_size(self):
        return NotImplemented

    def draw(self):
        print('draw shape')

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.radius

    def get_size(self):
        return math.pi * self.radius ** 2

class Picture:
    def __init__(self, background_color, color):
        self.background_color = background_color
        self.color = color

    def draw(self):
        print('Draw a picture in ' + self.color + ' on ' + self.background_color)

class Art(Circle, Picture):
    def __init__(self, name, radius, back_color, color, rating):
        Circle.__init__(self, name, radius)
        Picture.__init__(self, back_color, color)
        self.rating = rating

if __name__ == '__main__':
    a = Art('landscape', 10, 'yellow', 'red', 6)
    print(a.get_size())
    a.draw()
    print(a.rating)
        
