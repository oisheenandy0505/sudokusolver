class SolveSudoku:
    def __init__(self, board, square=3):
        self.square = square  # Size of small inner square
        self.board = board  # Game board
        self.empty = []  # List to keep track of empty squares
        self.x_hold = [set() for _ in range(9)]  # Row holds
        self.y_hold = [set() for _ in range(9)]  # Column holds
        self.s_hold = [set() for _ in range(9)]  # Subgrid holds
        self.p_nums = {str(i + 1) for i in range(9)}  # Possible numbers

        self._initialize_holds()
        self._solve()

    def _initialize_holds(self):
        for y in range(9):
            for x in range(9):
                num = self.board[y][x]
                if num != 0:
                    self.x_hold[y].add(num)
                    self.y_hold[x].add(num)
                    subgrid = (x // self.square) + ((y // self.square) * self.square)
                    self.s_hold[subgrid].add(num)
                else:
                    self.empty.append((x, y))

    def _solve(self):
        if not self.empty:
            return True  # Puzzle is solved

        x, y = self.empty.pop(0)
        subgrid = (x // self.square) + ((y // self.square) * self.square)
        
        for num in self.p_nums:
            if (num not in self.x_hold[y] and
                num not in self.y_hold[x] and
                num not in self.s_hold[subgrid]):
                
                # Place number
                self.board[y][x] = int(num)
                self.x_hold[y].add(num)
                self.y_hold[x].add(num)
                self.s_hold[subgrid].add(num)

                if self._solve():
                    return True

                # Remove number (backtrack)
                self.board[y][x] = 0
                self.x_hold[y].remove(num)
                self.y_hold[x].remove(num)
                self.s_hold[subgrid].remove(num)
        
        self.empty.insert(0, (x, y))
        return False
