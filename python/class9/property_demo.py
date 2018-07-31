class DescriptorProperty:
	def __init__(self, getter=None, setter=None):
		self._getter = getter
		self._setter = setter

	def __get__(self, instance, owner):
		if self._getter:
			return self._getter(instance)
		else:
			raise AttributeError('can\'t get attribute')

	def __set__(self, instance, value):
		if self._setter:
			self._setter(instance, value)
		else:
			raise AttributeError('can\'t set attribute')

class Person:
	def __init__(self, name, age):
		self._name = name
		self._age = age

	def _get_name(self):
		return self._name

	def _get_age(self):
		return self._age

	def _set_age(self, value):
		if value >= 0:
			self._age = value
		else:
			raise ValueError('Invalid age to set')

	#name = property(fget=_get_name)
	#age = property(fget = _get_age, fset = _set_age)

	name = DescriptorProperty(getter=_get_name)
	age = DescriptorProperty(getter=_get_age, setter=_set_age)

if __name__ == '__main__':
	john = Person('John', 18)
	print(john.name)
	print(john.age)
	john.age = 20
	print(john.age)
	john.name = 'Johnny'
	john.age = -5
