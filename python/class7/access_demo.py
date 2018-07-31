class LoginRecord:
	def __init__(self, username, password, expiry):
		self._username = username
		self.__password = password
		self.expiry = expiry


if __name__ == '__main__':
	record = LoginRecord('John', 'top_secret', 10)
	print(record._username)
	print(record._LoginRecord__password)
