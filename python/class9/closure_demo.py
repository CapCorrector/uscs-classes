#def make_adder(base):
#	def adder(value):
#		return base + value
#	return adder
#
#adder5 = make_adder(5)
#print(adder5(10))
#print(adder5(20))
#
#def calculator(add_base, multi_base):
#	def adder(value):
#		return add_base + value
#	def multiplier(factor):
#		return multi_base * factor
#	return adder, multiplier
#
#adder5, multi3 = calculator(5,3)
#print(adder5(10))
#print(multi3(4))

def make_presenter(start_tag, close_tag):
	def presenter(text):
		return start_tag + text + close_tag
	return presenter

h1_printer = make_presenter('<h1>', '</h1>')
print(h1_printer('Hello'))
print(h1_printer('Bye'))
span_printer = make_presenter('<span>', '</span>')
print(span_printer('Java'))
print(span_printer('Python'))

