import math

class Point:
	def __init__(self, x = 0, y = 0):
		self.move(x, y)
	
	def __str__(self):
		return '(' + str(self.x) + ', ' + str(self.y) + ')'
	
	def __eq__(self, other):
		return isinstance(other, Point) and self.x == other.x and self.y == other.y
	
	def move(self, x, y):
		self.x = x
		self.y = y
	
	def distance(self):
		return math.sqrt(self.x**2 + self.y**2)
	
	def distance_from(self, other):
		if not isinstance(other, Point):
			return NotImplemented

		return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

if __name__ == '__main__':
	class Car:
		pass
	
	p = Point(3, 5)
	print(p.distance())
	p.move(10, 3)
	print(p.distance())
	print(p)
	
	q = Point()
	print(q.distance())
	print(q)
	
	r = Point(10, 3)
	print(p is r)
	print(p == r)
	
	c = Car()
	c.x = 10
	c.y = 3
	print(c == p)
