class Person:
	def __init__(self, name, age):
		self.name = name.upper()
		self.age = age

	def __str__(self):
		return self.name + ' is ' + str(self.age) + ' years old.'

class Student(Person):
	def __init__(self, name, age, school):
		super().__init__(name, age)
		self.school = school
	def __str__(self):
		return self.name + ' is a student from ' + self.school + '.'

if __name__ == '__main__':
	john = Person('John', 18)
	print(john) 
	jack = Student('Jack', 15, 'San Jose State')
	print(jack)
