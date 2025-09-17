from game_core2 import GameCoreCopy


class App:
    def __init__(self):
        pass

    def _display_welcome_screen(self):
        print("Welcome to tic-tac-toe")
        print("*********")
        print(" |TIC|\n |TAC|\n |TOC|")
        print("Select:")
        print("(N) New Game\n(O) Options\n(H) Help\n(Q) Quit")

    def _play_board(self):
        print("*********")
        print("Playboard:")
        print("     1   2   3   \n 1 |   |   |   |\n 2 |   |   |   |\n 3 |   |   |   |")
        print("Choose your player (1/2) and put coordinates for example 23 meaning 2 row and 3 column")
        print("Your input should look like this: X enter 2 enter 3 enter to achieve:")
        print("     1   2   3   \n 1 |   |   |   |\n 2 |   |   | X |\n 3 |   |   |   |")

    def _display_help_screen(self):
        print("Tic-tac-toe is a two-player game played on a 3x3 grid.\n" +
              "Players take turns placing their symbols (X or O) in empty squares, " +
              "aiming to be the first to get three in a row (horizontally, vertically, or diagonally).\n" +
              "If all squares are filled and no one has three in a row, the game is a draw")

    def run(self):
        self._display_welcome_screen()
        self._play_board()
        game = GameCoreCopy()  # tworzenie instancji klasy GameCoreCopy

        while True:
            user_input = input()
            if user_input.lower() == "n":
                game.add_marker()
                break

            elif user_input.lower() == "o":
                # select game options
                pass

            elif user_input.lower() == "h":
                self._display_help_screen()

            elif user_input.lower() == "q":
                break

            else:
                print("FUCK OFF")
