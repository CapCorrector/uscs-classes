class NumberIterable:
	def __init__(self, start, end, step):
		self._start = start
		self._end = end
		self._step = step

	def __iter__(self):
		return NumberIterator(self._start, self._end, self._step) 	

class NumberIterator:
	def __init__(self, start, end, step):
		self._start = start
		self._end = end
		self._step = step
		self._current = start - step

	def __iter__(self):
		return self

	def __next__(self):
		self._current += self._step

		if self._current >= self._end:
			raise StopIteration()
		return self._current

if __name__ == '__main__':
	numbers = NumberIterable(10, 58, 4)

	for n in numbers:
		print(n)
