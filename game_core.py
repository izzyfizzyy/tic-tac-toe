import re
import sys

import numpy as np

from exception import OccupationError


class GameCore:

    def __init__(self):
        self.size = 3
        self.row_mapping = {
            'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
            'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
            'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
            's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
            'y': 25, 'z': 26
        }
        self._reset()

    def _reset(self):
        self.turn_counter = 0
        self.max_turns = self.size ** 2
        self.board_state = np.zeros(shape=(self.size, self.size))

    def set_size(self, new_size):
        self.size = new_size
        print(self.size)
        self._reset()

    def _check_for_winning_conditions(self, player):
        win = 0

        # checking per each row
        for x in range(self.size):
            if np.all(self.board_state[x, :] == player):
                print(f"Player number {player} won.")
                sys.exit()

        # checking per each column
        for y in range(self.size):
            if np.all(self.board_state[y, :] == player):
                print(f"Player number {player} won.")
                sys.exit()

        # checking skew
        for c in range(self.size):
            if int(self.board_state[c][c]) == player:
                win += 1
        if win == self.size:
            print(f"Player number {player} won.")
            sys.exit()
        else:
            win = 0


        # checking skew 2
        counter_x = self.size - 1
        counter_y = 0

        while counter_x >= 0:
            if int(self.board_state[counter_x][counter_y]) == player:
                win += 1
            counter_x -= 1
            counter_y += 1

        if win == self.size:
                print(f"Player number {player} won.")
                sys.exit()
        else:
                win = 0

    def _is_not_occupied(self, player_input):
        row = player_input[0]
        row = self.row_mapping[row.lower()] - 1
        col = int(player_input[1:]) - 1
        return self.board_state[row][col] == 0

    def is_grid_size_ok(self, input):
        return input <= self.size

    def validate_input_fits_on_board(self, player_input):
        row = player_input[0]
        row = self.row_mapping[row.lower()] - 1
        col = int(player_input[1:]) - 1
        return self.is_grid_size_ok(row) and self.is_grid_size_ok(col)

    def _get_current_player(self):
        if self.turn_counter % 2 == 0:
            return 1
        else:
            return 2

    def validate_input_format(self, player_input):
        match_found = re.search("^[A-Za-z](?:[0-9]|1[0-9]|2[0-6])$", player_input)

        if not match_found:
            raise TypeError(f"Input: {player_input} does not match required format.")

        if not self.validate_input_fits_on_board(player_input):
            raise ValueError(f"Input: {player_input} exceeds the grid size.")

        if not self._is_not_occupied(player_input):
            raise OccupationError(f"Position {player_input} is already occupied.", 000)

    def display_board(self):
        print("    " + "   ".join(str(i + 1) for i in range(self.size)))
        symbols = {0: " ", 1: "X", 2: "O"}

        for i in range(self.size):
            row_label = chr(ord("A") + i)
            row = " | ".join(symbols.get(v, "?") for v in self.board_state[i])
            print(f"{row_label} | {row} |")

    def play_game(self):

        while self.turn_counter < self.max_turns:
            player = self._get_current_player()
            print(f"Player {player} turn: ")

            player_input = input()  # input with coordinates

            try:
                self.validate_input_format(player_input)
            except TypeError as e:
                print(e)
                continue
            except ValueError as v:
                print(v)
                continue
            except OccupationError as o:
                print(o)
                continue

            row = player_input[0]
            row = self.row_mapping[row.lower()] - 1
            col = int(player_input[1:]) - 1

            self.board_state[row][col] = player
            self._check_for_winning_conditions(player)
            self.display_board()
            self.turn_counter += 1

        sys.exit()
