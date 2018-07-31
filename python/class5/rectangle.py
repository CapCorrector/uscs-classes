from point import Point

class Rectangle:
	def __init__(self, bottom_left, length, height):
		self.bottom_left = bottom_left
		self.height = height
		self.length = length
	
	def top_right_corner(self):
		return Point(self.bottom_left.x + self.length, self.bottom_left.y + self.height)

if __name__ == '__main__':
	pt = Point (3, 4)
	rect = Rectangle(pt, 10, 20)
	print(rect.top_right_corner())
