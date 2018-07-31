import math

class SmartPoint:
	def __init__(self, x = 0, y = 0):
		self.move(x, y)

	def __str__(self):
		return '(' + str(self.x) + ', ' + str(self.y) + ')'

	def __eq__(self, other):
		return isinstance(other, SmartPoint) and self.x == other.x and self.y == other. y

	def __add__(self, other):
		if isinstance(other, SmartPoint):
			return SmartPoint(self.x + other.x, self.y + other.y)
		else:
			return NotImplemented
	
	def __mul__(self, factor):
		return SmartPoint(self.x * factor, self.y * factor)

	def move(self, x, y):
		self.x = x
		self.y = y

	def distance(self):
		return math.sqrt(self.x**2 + self.y**2)

sp1 = SmartPoint(3, 4)
sp2 = SmartPoint(10, 3)
spsum = sp1 + sp2

print(spsum)
print (sum([SmartPoint(1, 2), SmartPoint(3, 4), SmartPoint(5, 6)], SmartPoint()))

sp3 = SmartPoint(10, 20)
sp4 = sp3 * 2
print(sp4)
