class Balance:
	def __get__(self, instance, owner):
		return instance._balance

	def __set__(self, instance, value):
		if value >= 0:
			instance._balance = value
		else:
			raise VallueError('Invalid amount')


class Account:
	balance = Balance()
	
	def __init__(self, amount):
		self._balance = amount

	def withdraw(self, amount):
		self.balance -= amount

	def deposit(self, amount):
		self.balance += amount


if __name__ == '__main__':
	acct = Account(1000)
	print(acct.balance)
	acct.withdraw(1300)
	print(acct.balance)
	acct.deposit(800)
	print(acct.balance)
