import random

class Ticket:
	def __init__(self):
		self.number =  random.randint(1000, 9999)

	def __str__(self):
		return str(self.number) + ': ' + str(self.get_price())

	def get_price(self):
		return NotImplemented

class ShowTicket(Ticket):
	def __init__(self, adv):
		super().__init__()
		self.advanced = adv

	def get_price(self):
		if self.advanced >= 10:
			return 30
		else:
			return 40

class StudentTicket(ShowTicket):
	def get_price(self):
		return super().get_price() // 2	

	def __str__(self):
		return super().__str__() + '\n (Student ID required.)'

if __name__ == '__main__':
	t1 = ShowTicket(13)
	print(t1)
	t2 = ShowTicket(5)
	print(t2)
	s1 = StudentTicket(20)
	print(s1)
	s2 = StudentTicket(1)
	print(s2)
