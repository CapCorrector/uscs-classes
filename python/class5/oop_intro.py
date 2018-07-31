import math

### non oop
#def move(p, x, y):
#	p[0] = x
#	p[1] = y

#def distance(p):
#	return math.sqrt(p[0]**2 + p[1]**2)

#p = [3, 5]
#move(p, 10, 3)
#print(p)
#print(distance(p))

# still non oop

#class Point:
#	pass

#def move(p, x, y):
#	p.x = x
#	p.y = y

#def distance(p):
#	return math.sqrt(p.x**2 + p.y**2)

# oop (self could be named different way but self is best practice)

class Point:
	def move(self, x, y):
		self.x = x
		self.y = y
	
	def distance(self):
		return math.sqrt(self.x**2 + self.y**2)

#p = Point()
#Point.move(p, 3, 5)
#print(Point.distance(p))
#Point.move(p, 10, 3)
#print(Point.distance(p))

p = Point()
p.move(3, 5)
print(p.distance())
p.move(10, 3)
print(p.distance())
