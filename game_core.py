import sys
import numpy as np


class GameCore:

    def __init__(self):
        self.input = []
        self.input2 = []
        self.i = 0

    def add_input(self):
        while self.i < 9:
            user_input = int(input())
            if self.i % 2 == 0:
                self.input.append(user_input)
            elif self.i % 2 != 0:
                self.input2.append(user_input)
            if self.win_condition_check:
                if self.i % 2 == 0:
                    print("Wygral gracz numer 1")
                else:
                    print("Wygral gracz numer 2")
                break
            self.i += 1
            print(self.input)
            print(self.input2)

        sys.exit()

    @property
    def win_condition_check(self):
        winning_combos = [
            [1, 2, 3],
            [1, 4, 7],
            [1, 5, 9],
            [2, 5, 8],
            [4, 5, 6],
            [3, 5, 7],
            [7, 8, 9]
        ]

        if self.i >= 4:
            for player_input in [self.input, self.input2]:
                for combo in winning_combos:
                    if all(x in player_input for x in combo):
                        return True
        return False
