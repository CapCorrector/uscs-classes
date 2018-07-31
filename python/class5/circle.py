#import math

from point import Point

class Circle:
	def __init__(self, x = 0, y = 0, rad = 1):
		self.cent = Point(x, y)
		self.rad = rad

	def move(self, x, y):
		self.cent.move(x, y)

	def include(self, point):
		if not isinstance(point, Point):
			return False
#		distance = math.sqrt((self.cent.x - point.x)**2 + (self.cent.y -point.y)**2)
#		return distance <= self.rad
		return self.cent.distance_from(point) <= self.rad

if __name__ == '__main__':
	circle = Circle(1, 0, 2)
	pt = Point(1,1)
	print(circle.include(pt))
	
	circle2 = Circle()
	print(circle2.include(pt))
	circle2.move(2, 1)
	print(circle2.include(pt))
