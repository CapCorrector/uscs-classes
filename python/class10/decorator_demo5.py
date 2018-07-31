class memorized:
	def __init__(self, func):
		self._func = func
		self._cache = {}

	def __call__(self, *args):
		try:
			c = self._cache.get(args)
			if c:
				return c
			else:
				r = self._func(*args)
				self._cache[args] = r
				return r
		except:
			return self._func(*args)
	
			

@memorized
def fibonacci(n):
	if n in (1, 2):
		return 1
	return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(50))
