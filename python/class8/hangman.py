from interactive_game import InteractiveGame, InvalidInputException
from random_word import RandomWordGenerator
from hangman_drawing_basic import HangmanDrawer

class Hangman(InteractiveGame):
    def __init__(self):
        self._tries = 8
        self._secret_word = RandomWordGenerator().get_random_word()
        self._used_letters = []
        self._guessed_word_so_far = list('_' * len(self._secret_word))
        self._drawer = HangmanDrawer()

    def get_instruction(self):
        return [
            'Guess my secret word.'
        ]

    def get_status(self):
        chances = 'chances' if self._tries > 1 else 'chance'
        return [
            'You have {} {} to guess my secret word.'.format(self._tries, chances),
            'Used letters: {}'.format(' '.join(self._used_letters)),
            ' '.join(self._guessed_word_so_far)
        ]

    def get_prompt(self):
        return 'Take a guess: '

    def validate(self, guess):
        if len(guess) != 1:
            raise InvalidInputException('Invalid guess. Try again')

        self._tries -= 1
        return guess

    def evaluate(self, guess):
        self._used_letters.append(guess)
        for i in range(len(self._guessed_word_so_far)):
            if self._secret_word[i] == guess:
                self._guessed_word_so_far[i] = guess

        if self._guessed_word_so_far.count('_') == 0:
            return True, None
        else:
            if hasattr(self, '_drawer'):
                self._drawer.next()
            return False, None

    def can_continue(self):
        return self._tries > 0

    def say_congratulations(self):
        return 'Congratulations! You have guessed my secret word {}.'.format(self._secret_word)

    def say_sorry(self):
        return 'Sorry that you lost! My secret word is {}.'.format(self._secret_word)
