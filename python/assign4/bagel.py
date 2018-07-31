import random

class InvalidInputException(Exception):
	pass

class BagelsGame:
	def __init__(self):
		self.tries = 10
		self.secret_number = self._generate_secret_number()

	def _generate_secret_number(self):
		digits = list(map(str, range(10)))
		random.shuffle(digits)
		while digits[0] == '0':
			random.shuffle(digits)
		return digits[:3]
		
	def get_instruction(self):
		return [
			'Instruction: ',
			'Bagel: no digit is correct.',
			'Pico: one digit is correct but in wrong position.',
			'Fermi: one digit is correct and in the correct position.'
		];

	def prompt(self):
		chances = 'chances' if self.tries > 1 else 'chance'
		return 'You have ' + str(self.tries) + ' ' + chances + ' to guess my 3-digit number.'

	def evaluate(self, guess):
		#guess is an int
		guess_digits = list(str(guess))
		
		hint = []
		
		if guess_digits == self.secret_number:
			return hint

		for i in range(len(guess_digits)):
			if guess_digits[i] == self.secret_number[i]:
				hint.append('Fermi')
			elif guess_digits[i] in self.secret_number:
				hint.append('Pico')
		
		if len(hint) == 0:
			hint.append('Bagels')
		else:
			hint.sort()
		return hint
				

	def check_input(self, user_input):
		try:
			guess = int(user_input)
			guess_str = str(guess)
			if len(guess_str) != 3:
				raise InvalidInputException()
			if len(set(guess_str)) != 3:
				raise InvalidInputException()
		except:
			raise InvalidInputException()

		self.tries -= 1
		return guess
