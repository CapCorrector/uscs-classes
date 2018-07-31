class SeqIter:
	def __init__(self, iterations):
		self._iterations = iterations
		self._curiter = -1
		self._current = 1

	def __iter__(self):
		return self

	def __next__(self):
		self._curiter += 1
		if self._curiter >= self._iterations:
			raise StopIteration()
		div = 0 if self._curiter == 0 else (-1) ** self._curiter
		self._current += div*(1/(3+2*(self._curiter-1)))
		return self._current

if __name__ == '__main__':
	for v in SeqIter(20):
		print(v*4)
