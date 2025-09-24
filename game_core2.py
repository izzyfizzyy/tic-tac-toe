import sys

import numpy as np


class GameCoreCopy:

    def __init__(self):
        self.board_state = np.zeros(shape=(3, 3))
        self.turn_counter = 0

    # def check_for_winning_conditions(self):
    #     pass

    def add_marker(self):

        while self.turn_counter < 9:
            response = (input())
            row = int(response[1]) - 1
            col = int(response[2]) - 1
            player = int(response[0])
            self.board_state[row][col] = player
            print(self.board_state)
            self.turn_counter += 1

        sys.exit()

    def _play_board_status(self):
        pass