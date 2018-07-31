class BankAccount:
	def __init__(self, balance = 0):
		self. balance = balance

	def __str__(self):
		return str(self.balance)

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		self.balance -= amount

class SavingAccount(BankAccount):
	def withdraw(self, amount):
		super().withdraw(amount)
		if self.balance < 500:
			super().withdraw(3)

if __name__ == '__main__':
	b = BankAccount(100)
	b.deposit(500)
	print(b) #600
	b.withdraw(200)
	print(b) #400
	
	c = SavingAccount(100)
	c.deposit(500)
	print(c) #600
	c.withdraw(200)
	print(c) #397
