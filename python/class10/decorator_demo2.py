from functools import wraps

def trace(func):
	@wraps(func) ### will wrap squares name and docstring into call_func)
	def call_func(*args, **kwargs):
		print('Calling {}: {} {}'.format(func.__name__, args, kwargs))
		r = func(*args, **kwargs)
		print('{} returns {}'. format(func.__name__, r))
		return r
	return call_func

#@trace
def square_nodecor(x):
	return x*x

print(trace(square_nodecor)(10))

@trace
def square(x):
	'''do a square function'''
	return x*x

@trace
def quadratic(x, a, b, c):
	return a*x*x + b*x +c

print(square(10))
print(quadratic(15, a=2, b=3, c=1))
#print(square.__name__) ### returns call_func if there is no @wraps
#print(square.__doc__)
print(square.__wrapped__(10)) ### needs @wraps calls function without decorator
