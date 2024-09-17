from math import ceil
from random import shuffle, choices

class Sudoku:
    def __init__(self, size=9, square=3):
        self.size = size
        self.square = square
        self.p_nums = [str(i + 1) for i in range(size)]  # Initialize p_nums here
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.generate_board()

    def generate_board(self):
        if not self._generate_board(0, 0):
            raise Exception("Failed to generate a board")

    def _generate_board(self, x, y):
        if y == self.size:
            return True
        next_x, next_y = (x + 1, y) if x < self.size - 1 else (0, y + 1)
        if self.board[y][x] != '.':
            return self._generate_board(next_x, next_y)

        shuffle(self.p_nums)
        for num in self.p_nums:
            if self._is_valid(x, y, num):
                self.board[y][x] = num
                if self._generate_board(next_x, next_y):
                    return True
                self.board[y][x] = '.'
        return False

    def _is_valid(self, x, y, num):
        sq_index = (x // self.square) + ((y // self.square) * self.square)
        # Check if the number is in the same row, column, or square
        row_valid = num not in self.board[y]
        col_valid = num not in (self.board[i][x] for i in range(self.size))
        sq_valid = num not in (self.board[i][j] for i in range((y // self.square) * self.square, (y // self.square + 1) * self.square)
                                         for j in range((x // self.square) * self.square, (x // self.square + 1) * self.square))
        return row_valid and col_valid and sq_valid

    def mask_board(self, i_choice=[2, 3], hints=17):
        for y in range(self.size):
            i_amt = choices(i_choice, k=1)[0]
            if i_amt > hints:
                i_amt = hints
            hints -= i_amt
            positions = list(range(self.size))
            shuffle(positions)
            for i in positions[:i_amt]:
                self.board[y][i] = '.'
            if hints <= 0:
                break
