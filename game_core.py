import sys
import re
import numpy as np


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
            for y in range(self.size):
                if int(self.board_state[x][y]) == player:
                    win += 1
            if win == self.size:
                print(f"Player number {player} won.")
                sys.exit()
            else:
                win = 0

        # checking per each column
        for y in range(self.size):
            for x in range(self.size):
                if int(self.board_state[x][y]) == player:
                    win += 1
            if win == self.size:
                print(f"Player number {player} won.")
                sys.exit()
            else:
                win = 0

        # checking skew
        for x in range(self.size):
            if int(self.board_state[x][x]) == player:
                win += 1
        if win == self.size:
            print(f"Player number {player} won.")
            sys.exit()
        else:
            win = 0

    def _is_not_occupied(self, row, col):
        return self.board_state[row][col] == 0

    def is_grid_size_ok(self, input):
        return input <= self.size

    def validate_input_fits_on_board(self, col, row):
        return self.is_grid_size_ok(row) and self.is_grid_size_ok(col)

    def _get_current_player(self):
        if self.turn_counter % 2 == 0:
            return 1
        else:
            return 2

    @staticmethod
    def validate_input_format(player_input):
        match_found = re.search("^[A-Za-z](?:[0-9]|1[0-9]|2[0-6])$", player_input)

        if not match_found:
            raise RuntimeError(f"Input: {player_input} does not match required format")


    def _play_board_status(self):
        pass

    def play_game(self):

        while self.turn_counter < self.max_turns:  # zmienic na max turns
            player = self._get_current_player()
            print(f"Player {player} turn: ")

            player_input = input()  # input with coordinates

            try:
                self.validate_input_format(player_input)
            except RuntimeError as e:
                print(e)
                continue

            row = player_input[0]
            row = self.row_mapping[row.lower()] - 1
            col = int(player_input[1:]) - 1

            if self.validate_input_fits_on_board(col, row) and self._is_not_occupied(row,col):

                self.board_state[row][col] = player
                self._check_for_winning_conditions(player)
                print(self.board_state)
                self.turn_counter += 1

            elif not self.validate_input_fits_on_board(col, row):
                print("Your coordinates exceed the matrix size. Please change your input.")
            else:
                print("This place is occupied by your opponent. Please change your input.")
                break


        sys.exit()

