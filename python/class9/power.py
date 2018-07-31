class Power:
	def __call__(self, x, n):
		result = 1
		for i in range(n):
			result *= x	
		return result

if __name__ == '__main__':
	p = Power()
	print(p(5,3))
