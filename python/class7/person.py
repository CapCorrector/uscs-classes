class Person:

	bmi_underweight_threshold = 18.5
	bmi_normal_threshold = 24.9
	bmi_overweight_threshold = 29.9
	
	def __init__(self, name, age, height, weight):
		self._name = name
		self._age = age
		self._height = height
		self._weight = weight

	def __str__(self):
		return self._name + ' is ' + str(self._age) + ' years old.'

	def _get_age(self):
		return self._age

	def _set_age(self, age):
		if age > self._age:
			self._age = age

	def _calculate_bmi(self):
		return self._weight / (self._height / 100) / (self._height / 100)

	def _get_bmi_category(self):
		bmi = self._calculate_bmi()
		if bmi < Person.bmi_underweight_threshold:
			return 'Underweight'
		if bmi < Person.bmi_normal_threshold:
			return 'Normal'
		if bmi < Person.bmi_overweight_threshold:
			return 'Overweight'
		return 'Obese'
	
	age = property(_get_age, _set_age)
	bmi = property(_calculate_bmi)
	bmi_category = property (_get_bmi_category)

if __name__ == '__main__':
	john = Person('John', 18, 166, 60)
	print(john)
	#john.set_age(20)
	john.age = -20
	#print(john.get_age())
	print(john.age)
	print(john)
	print(john.bmi)
	john.bmi = 35.5 # will not work because there is no setter
	print(john.bmi_category)
