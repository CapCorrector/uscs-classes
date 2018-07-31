import time

def tracer(cls):
	class Wrapper:
		def __init__(self, *args, **kwargs):
			self._wrapped = cls(*args, **kwargs)

		def __getattr__(self, attrname):
			print('Call {} at {}'.format(attrname, time.strftime('%Y-%m-%d %H:%M:%S')))
			return getattr(self._wrapped, attrname)

	return Wrapper

@tracer
class Employee:
	def  __init__(self, name, hours, rate):
		self._name = name
		self._hours = hours
		self._rate = rate

	def pay(self):
		return self._hours * self._rate

	def update_rate(self, r):
		self._rate = r

	def update_hours(self, h):
		self._hours = h

john = Employee('John', 8, 25)

print(john.pay())
john.update_rate(40)
print(john.pay())
john.update_hours(6)
print(john.pay())
