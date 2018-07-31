class Ticket:

	next_ticket_number = 1	

	def __init__(self):
		self.number =  Ticket.next_ticket_number
		Ticket.next_ticket_number += 1

	def __str__(self):
		return str(self.number) + ': ' + str(self.get_price())

	def get_price(self):
		return NotImplemented

class ShowTicket(Ticket):
	
	minimum_advanced_days = 10
	advanced_price = 30
	full_price = 40
	
	def __init__(self, adv):
		super().__init__()
		self.advanced = adv

	def get_price(self):
		if self.advanced >= ShowTicket.minimum_advanced_days:
			return ShowTicket.advanced_price
		else:
			return ShowTicket.full_price

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
