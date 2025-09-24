import sys

import numpy as np


class GameCoreCopy:

    def __init__(self):
        self.board_state = np.zeros(shape=(3, 3))
        self.turn_counter = 0

    # def check_for_winning_conditions(self):
    #     pass
    def _is_input_valid(self, input):
        if input >= 3:
            return False
        else:
            return True

    def _player_recognition(self):
        if self.turn_counter % 2 == 0:
            return 1
        elif self.turn_counter % 2 != 0:
            return 2
        return None

    def _add_marker(self):

        while self.turn_counter < 9:
            response = (input())  # input with coordinates
            row = int(response[0]) - 1
            col = int(response[1]) - 1

            if self._is_input_valid(row) and self._is_input_valid(col): # check whether coordinates don't exceed the grid size
                player = self._player_recognition()  # which player's turn is it currently
                self.board_state[row][col] = player
                print(self.board_state)
                self.turn_counter += 1
            else:
                print("Your coordinates exceed the grid size. Please change the input")



        sys.exit()

    def _play_board_status(self):
        pass
