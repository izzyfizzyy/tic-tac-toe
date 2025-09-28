import sys

import numpy as np


class GameCore:

    def __init__(self):
        self.board_state = np.zeros(shape=(3, 3))
        self.turn_counter = 0
        self.shape = 3

    def _check_for_winning_conditions(self, player):
        win = 0

        for x in range(self.shape):
            for y in range(self.shape):
                if int(self.board_state[x][y]) == player:
                    win += 1
            if win == 3:
                print(f"Player number {player} won.")
                sys.exit()
            else:
                win = 0

        for y in range(self.shape):
            for x in range(self.shape):
                if int(self.board_state[x][y]) == player:
                    win += 1
            if win == 3:
                print(f"Player number {player} won.")
                sys.exit()
            else:
                win = 0

    def _is_not_occupied(self, row, col):
        if self.board_state[row][col] == 0:
            return True
        else:
            return False

    def _is_input_valid(self, input):
        if input >= 3:
            return False  # try catch
        else:
            return True

    def _player_recognition(self):
        if self.turn_counter % 2 == 0:
            return 1
        elif self.turn_counter % 2 != 0:
            return 2
        return None

    def add_marker(self):

        while self.turn_counter < 9:
            response = input()  # input with coordinates
            row = int(response[0]) - 1
            col = int(response[1]) - 1

            if self._is_input_valid(row) and self._is_input_valid(col) and self._is_not_occupied(row,
                                                                                                 col):  # check whether coordinates don't exceed the grid size
                player = self._player_recognition()  # which player's turn is it currently
                self.board_state[row][col] = player
                self._check_for_winning_conditions(player)
                print(self.board_state)
                self.turn_counter += 1
            elif not self._is_not_occupied(row, col):
                print("This place is occupied by your opponent. Please change your input.")
            else:
                print("Your coordinates exceed the matrix size. Please change your input.")

        sys.exit()

    def _play_board_status(self):
        pass
