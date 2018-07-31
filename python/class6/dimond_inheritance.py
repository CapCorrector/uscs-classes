class Animal:
	number_of_animals = 0
	number_of_cute_animals = 0

	def __init__(self, name, cute):
		self.name = name
		Animal.number_of_animals += 1
		if cute:
			Animal.number_of_cute_animals += 1

class Dog(Animal):
	def __init__(self, breed, age, **args):
		super().__init__(**args)
		self.breed = breed
		self.age = age

class Domestic(Animal):
	def __init__(self, address, **args):
		super().__init__(**args)
		self.address = address

class HomePuppy(Dog, Domestic):
	def __init__(self, rating, **args):
		super().__init__(**args)
		self.rating = rating

	def __str__(self):
		return self.name + '\n' + self.breed + '\n' + self.address

if __name__ == '__main__':
	p = HomePuppy(name = 'Max', breed = 'Chihuahua', age = 3, address = 'San Jose', cute = True, rating = 5)
	q = HomePuppy(name = 'John', breed = 'Bulldog', age = 4, address = 'LA', cute = False, rating = 3)

	print(p)
	print(q)
	
	print(Animal.number_of_animals)
	print(Animal.number_of_cute_animals)

	print(HomePuppy.__mro__)
