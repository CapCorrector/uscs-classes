class Square:
	def __init__(self, length):
		super().__setattr__('length', length)
	
	def __getattr__(self, attrname):
		if attrname == 'area':
			return self.length ** 2
		else:
			raise AttributeError(attrname)

	def __setattr__(self, attrname, value):
		raise AttributeError('Cannot set ' + attrname)
		

if __name__ == '__main__':
	s = Square(10)
	print(s.length)
	print(s.area)
	
#	s.perimeter = 50
#	super(Square, s).__setattr__('perimeter', 50)
	s.__dict__['perimeter'] = 50
	print(s.perimeter)
