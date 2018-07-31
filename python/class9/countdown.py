def countdown(n):
	print('Counting down from {}'.format(n))
	while n>0:
		yield n
		n -= 1

r = countdown(10)
print(next(r))
print(next(r))
