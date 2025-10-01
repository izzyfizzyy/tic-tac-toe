import sys

from game_core import GameCore


class App:
    def __init__(self):
        pass

    @staticmethod
    def _display_welcome_screen():
        print("Welcome to tic-tac-toe")
        print("*********")
        print(" |TIC|   |   |\n |   |TAC|   |\n |   |   |TOC|")
        print("Select:")
        print("(N) New Game\n(O) Options\n(H) Help\n(Q) Quit")

    @staticmethod
    def _display_rules():
        print(
            "Quick instructions> \n Put coordinates in 3x3 matrix starting with number of row, followed by number of column."
            " \n Example: \n Putting A3 meaning 1 row and 3 column:")
        print("     A   B   C   \n 1 |   |   |   |\n 2 |   |   | X |\n 3 |   |   |   |"
              "\nPlease find more information in the Help tab"
              "\n********************************************")

    @staticmethod
    def _display_help_screen():
        print("Tic-tac-toe is a two-player game played on a 3x3 grid.\n" +
              "Players take turns placing their symbols (X or O) in empty squares, " +
              "aiming to be the first to get three in a row (horizontally, vertically, or diagonally).\n" +
              "If all squares are filled and no one has three in a row, the game is a draw")

    def _display_options(self):
        pass

    def run(self):
        self._display_welcome_screen()
        game = GameCore()  # tworzenie instancji klasy GameCoreCopy

        while True:
            user_input = input()
            if user_input.lower() == "n":
                self._display_rules()
                game.play_game() #
                break

            elif user_input.lower() == "o":
                # select game options , user can change size of matrix
                pass

            elif user_input.lower() == "h":
                self._display_help_screen()

            elif user_input.lower() == "q":
                sys.exit()

