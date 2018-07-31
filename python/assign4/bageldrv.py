import sys
from bagel import BagelsGame

if __name__ == '__main__':
	game = BagelsGame()
	print('\n'.join(game.get_instruction()))
	while game.tries > 0:
		print(game.prompt())
		guess = input('What is my 3-digit number?')
		try:
			cguess = game.check_input(guess)
			hint = game.evaluate(cguess)
			if hint:
				if game.tries > 0:
					print(" ".join(hint))
				else:
					print('Sorry, you\'ve lost. The number was ' + str(game.secret_number) + '.')
			else:
				print('Congratulations you\'ve won')
				break
		except:
			print('Invalid guess. Try again.')
