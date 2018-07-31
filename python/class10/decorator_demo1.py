def decor(func):
	print('decor')
	return func

@decor #decor(foo)()
def foo():
	print('foo')

foo()
