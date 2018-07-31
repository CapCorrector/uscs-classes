import abc

class Foo(abc.ABC):
	@abc.abstractmethod
	def method1(self):
		pass
#	@abc.abstractmethod
	def method2(self):
		pass

class Bar(Foo):
	def method1(self):
		print('method1 is called')

b = Bar()
b.method1()
