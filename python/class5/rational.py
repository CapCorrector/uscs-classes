import math
class Rational:
	def __init__(self, num, den):
		self.num = num
		self.den = den
		self.reduce()
	
	def __add__(self, other):
		sumnum = self.num * other.den + self.den * other.num
		sumden = self.den * other.den
		return(Rational(sumnum, sumden))
	
	def __mul__(self, other):
		mulnum = self.num * other.num
		mulden = self.den * other.den
		return(Rational(mulnum, mulden))

	def __str__(self):
		return '(' + str(self.num) + '/' + str(self.den) + ')'
	
	def reduce(self):
		gcd = math.gcd(self.num, self.den)
		self.num //= gcd
		self.den //= gcd
		



r1 = Rational(3, 4)
r2 = Rational(2, 5)
r3 = r1 + r2
r4 = r1 * r2

print(r1)
print(r2)
print(r3)
print(r4)
