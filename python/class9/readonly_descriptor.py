class ReadOnlyDescryptor:
	def __get__(self, instance, owner):
		return instance._name

	def __set__(self, instance, value):
		raise AttributeError('cannot set')

class Student:
	name = ReadOnlyDescryptor()

	def __init__(self, name):
		self._name = name

if __name__ == '__main__':
	bob = Student('Bob')
	print(bob.name) #bob
	try:
		bob.name = 'William' #attributeerror
	except:
		print('name is read-only.')
	print(bob.name) #bob
