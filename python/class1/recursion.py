def fib(n):
	if n <= 0:
		return -1
	elif n == 1 or n == 2:
		return n-1
	else:
		return fib(n-1) + fib(n-2)

print('fib({}) = {}'.format(20, fib(20)))
