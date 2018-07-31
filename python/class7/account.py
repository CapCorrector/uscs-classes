class InvalidWithdrawalException(Exception):
	pass

class InvalidDepositException(Exception):
	pass
	
class BankAccount:
	def __init__(self, balance = 0):
		self._balance = balance

	def __str__(self):
		return str(self._balance)

	def deposit(self, amount):
		if amount > 0:
			self._balance += amount
		else:
			raise InvalidDepositException()

	def withdraw(self, amount):
		if amount <= self.balance:
			self._balance -= amount
		else:
			raise InvalidWithdrawalException()	

	def _get_balance(self):
		return self._balance

	balance = property(_get_balance)

if __name__ == '__main__':
	acct = BankAccount(1000)
	try:
		acct.withdraw(800)
	except Exception as err:
		if str(err) == 'Invalid withdraw':
			print('You do not have enough money in your bank account')
		elif str(err) == 'Invalid deposit':
			print('Your deposit operation is not allowed')
		else:
			print('Invalid operation')
	print(acct.balance)
	try:
		acct.withdraw(500) # -> exception is thrown
	except InvalidWithdrawalException:
		print('You do not have enough money in your bank account')
	except InvalidDepositException:
		print('Your deposit operation is not allowed')
	except Exception:
		print('Invalid operation')
	print(acct.balance)
	try:
		acct.deposit(1000) 
		print(acct.balance)
	except Exception as err:
		# exception is caught <-
		print(err)
