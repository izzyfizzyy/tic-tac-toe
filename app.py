import sys

from game_core2 import GameCoreCopy


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
            "Choose your player (1 or 2) and put coordinates in 3x3 matrix. For example 123 meaning player 1 choose 2 row and 3 column:")
        print("     1   2   3   \n 1 |   |   |   |\n 2 |   |   | X |\n 3 |   |   |   |")

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
        game = GameCoreCopy()  # tworzenie instancji klasy GameCoreCopy

        while True:
            user_input = input()
            if user_input.lower() == "n":
                self._display_rules()
                game._add_marker()
                break

            elif user_input.lower() == "o":
                # select game options
                pass

            elif user_input.lower() == "h":
                self._display_help_screen()

            elif user_input.lower() == "q":
                sys.exit()

            else:
                print("Exit")
