class Note:
	def __init__(self, cont, cat):
		self.cont = cont
		self.cat = cat
	
	def __str__(self):
		return self.cont + ' (' + self.cat + ')'

	def match_content(self, cont):
		if cont in self.cont:
			return True
		return False
		

if __name__ == '__main__':
	pass	
