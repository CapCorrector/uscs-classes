from interactive_game import InteractiveGame, InvalidInputException

class InvalidGameException(Exception):
    pass

class InteractiveGameConsoleDriver:
    def __init__(self, game):
        self._game = game
        self._win = False

    def play(self):
        if not isinstance(self._game, InteractiveGame):
            raise InvalidGameException("Invalid game")

        print('\n'.join(self._game.get_instruction()))

        while self._game.can_continue():
            print('\n'.join(self._game.get_status()))

            user_input = input(self._game.get_prompt())

            try:
                guess = self._game.validate(user_input)
                result, hint = self._game.evaluate(guess)

                if result:
                    self._win = True
                    break
                elif hint != None:
                    print('\n'.join(hint))

            except InvalidInputException as err:
                print(err)

        if self._win:
            print(self._game.say_congratulation())
        else:
            print(self._game.say_sorry())

if __name__ == '__main__':
    from guess_number import GuessNumber
    from hangman import Hangman

    #d = InteractiveGameConsoleDriver(GuessNumber(1, 100))
    d = InteractiveGameConsoleDriver(Hangman())
    d.play()
