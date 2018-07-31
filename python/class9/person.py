class SSN:
	def __get__(self, instance, owner):
		return '***-**-' + self._ssn[-4:]

	def __set__(self, instance, value):
		self._ssn = value

class Person:
	ssn = SSN()

	def __init__(self, name, ssn):
		self._name = name
		self.ssn = ssn


if __name__ == '__main__':
	john = Person('John', '253-57-1930')
	print(john.ssn)
	print(john.__dict__)
	print(type(john).__dict__['ssn'].__dict__)
	jack = Person('Jack', '411-41-1856')
	print(john.ssn)
	print(jack.ssn)
