import time

def trace(fd):
	def file_trace(func):
		def call_func(*args, **kwargs):
			fd.write('{} \n'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
			fd.write('Calling {}: {} {}\n'.format(func.__name__, args, kwargs))
			r = func(*args, **kwargs)
			fd.write('{} returns {}\n'. format(func.__name__, r))
			fd.flush()
			return r
		return call_func
	return file_trace

with open('debug3.log', 'a+') as fd:
	@trace(fd)
	def square(x):
		'''do a square function'''
		return x*x

	@trace(fd)
	def quadratic(x, a, b, c):
		return a*x*x + b*x +c

	#trace(fd)(square)(10)

	square(10)
	time.sleep(2)
	quadratic(15, a=2, b=3, c=1)

#print(square(10))
#print(quadratic(15, a=2, b=3, c=1))
