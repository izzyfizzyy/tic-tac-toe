import sys

from game_core import GameCore


class App:
    def __init__(self):
        pass

    @staticmethod
    def _display_welcome_screen():
        print("Welcome to tic-tac-toe game!")
        print("*********")
        print(" |TIC|   |   |\n |   |TAC|   |\n |   |   |TOC|")
        print("Select:")
        print("(N) New Game\n(O) Options\n(H) Help\n(Q) Quit")

    @staticmethod
    def _display_rules():
        print(
            "Quick instructions> \n Put coordinates in nxn matrix starting with letter pointing row, followed by number of column."
            " \n Example: \n Putting A3 meaning 1 row and 3 column:")
        print("     1   2   3   \n A |   |   |   |\n B |   |   | X |\n C |   |   |   |"
              "\nPlease find more detailed rule of the game in the Help tab"
              "\n********************************************")

    @staticmethod
    def _display_help_screen():
        print("Tic-tac-toe is a two-player game played on a 3x3 grid.\n" +
              "Players take turns placing their symbols (X or O) in empty squares, " +
              "aiming to be the first to get three in a row (horizontally, vertically, or diagonally).\n" +
              "If all squares are filled and no one has three in a row, the game is a draw."
              "\n. In this app you can change the size of the grid and play in matrix size up to 676 fields!.")

    def _display_options(self):
        pass

    def run(self):
        self._display_welcome_screen()
        game = GameCore()  # tworzenie instancji klasy GameCoreCopy

        while True:
            user_input = input()
            if user_input.lower() == "n":
                self._display_rules()
                game.play_game()  #
                break

            elif user_input.lower() == "o":
                print(
                    "Set grid size by entering size of wall. Please note: limit is 26.")  # czy nie calosci, ze 64 zamiast 8?
                matrix_size = int(input())
                game.set_size(matrix_size)

            elif user_input.lower() == "h":
                self._display_help_screen()

            elif user_input.lower() == "q":
                sys.exit()
