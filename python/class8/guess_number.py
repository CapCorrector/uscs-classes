import math
import random

from interactive_game import InteractiveGame, InvalidInputException

class GuessNumber(InteractiveGame):
	def __init__(self, low, high):
		self._low = low
		self._high = high
		self._tries = math.ceil(math.log2(high - low +1))
		self._secret_number = random.randint(low, high)

	def get_instruction(self):
		return [
			'I am thinking of a number between {} and {}'.format(self._low, self._high)
		]

	def get_status(self):
		chances = 'chances' if self._tries > 1 else 'chance'
		return [
			'You have {} {} to guess my number.'.format(self._tries, chances)
		]

	def get_prompt(self):
		return 'Take a guess:'

	def validate(self, guess):
		try:
			guess_number = int(guess)
		except:
			raise InvalidInputException('Invalid guess. Try again.')
		
		self._tries -= 1
		return guess_number

	def evaluate(self, guess):
		if guess == self._secret_number:
			return True, None

		if guess < self._secret_number:
			return False, ['Your guess is too low.']
		else:
			return False, ['Your guess is too high.']

	def can_continue(self):
		return self._tries > 0

	def say_congratulations(self):
		return 'Congratulations! You have guessed my number {}.'.format(self._secret_number)

	def say_sorry(self):
		return 'You\'ve lost. My number was {}.'.format(self._secret_number)
		

g = GuessNumber(10, 100)
