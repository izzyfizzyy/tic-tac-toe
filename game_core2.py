import sys

import numpy as np


class GameCoreCopy:

    def __init__(self):
        self.board_state = np.zeros(shape=(3, 3))
        self.i = 0

    # def check_for_winning_conditions(self):
    #     pass

    def add_marker(self):

        while self.i < 9:
            response = (input())
            x = int(response[1]) -1
            print(x, type(x))
            y = int(response[2]) - 1
            player = int(response[0])
            self.board_state[x][y] = player
            print(self.board_state)
            self.i += 1

        sys.exit()
