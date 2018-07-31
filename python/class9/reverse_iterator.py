class ReverseIterable:
	def __init__(self, iterables):
		self._iterables = iterables
		self._currentindex = len(iterables)

	def __iter__(self):
		return self

	def __next__(self):
		self._currentindex -= 1

		if self._currentindex <0:
			raise StopIteration()
		return self._iterables[self._currentindex]

if __name__ == '__main__':
	rt = ReverseIterable([10, 3, 56, 190])

	for n in rt:
		print(n)
