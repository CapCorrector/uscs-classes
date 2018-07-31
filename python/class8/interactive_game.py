import abc

class InvalidInputException(Exception):
	pass

class InteractiveGame(abc.ABC):
	@abc.abstractmethod
	def get_instruction(self):
		pass

	@abc.abstractmethod
	def get_status(self):
		pass

	@abc.abstractmethod
	def get_prompt(self):
		pass

	@abc.abstractmethod
	def validate(self, guess):
		pass

	@abc.abstractmethod
	def evaluate(self, guess):
		pass

	@abc.abstractmethod
	def can_continue(self):
		pass

	@abc.abstractmethod
	def say_congratulations(self):
		pass

	@abc.abstractmethod
	def say_sorry(self):
		pass
