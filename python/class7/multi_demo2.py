class Drawable:
	def __init__(self, color, **kwargs):
		super().__init__(**kwargs)
		self.color = color

	def draw(self):
		print('Draw ' + self.color + ' stuff.')

class Shape:
	def __init__(self, name = '', **kwargs):
		super().__init__(**kwargs)
		self.name = name

	def __str__(self):
		return self.name

	def get_perimeter(self):
		return NotImplemented

class Polygon(Shape, Drawable):
	def __init__(self, sides, length, **kwargs):
		super().__init__(**kwargs)
		self.sides = sides
		self.length = length

	def get_perimeter(self):
		return self.sides * self.length

	def draw(self):
		print('Draw ' + self.color + ' ' + self.name + '.')


if __name__ == '__main__':
	p = Polygon(sides = 3, length = 50, name = 'Triangle', color = 'yellow')
	print(p.get_perimeter())
	p.draw()
