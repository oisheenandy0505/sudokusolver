import numpy as np
from Sudoku import Sudoku
from Solver import SolveSudoku

def print_welcome():
    print('''
------------------------------
 WELCOME TO THE SUDOKU SOLVER
------------------------------
''')

def print_menu():
    print('''
\n
----------------------------
 WHAT WOULD YOU LIKE TO DO?
----------------------------
  * Generate Puzzle [G]
  * Solve Puzzle    [P]
\n
''')

def get_user_option():
    options = {'g': 0, 'generate puzzle': 0, 'p': 1, 'solve puzzle': 1}
    while True:
        user_input = input().strip().lower()
        if user_input in options:
            return options[user_input]
        print("Invalid input, please enter 'G' for Generate or 'P' for Solve.")

def handle_generate_puzzle(game):
    game.mask_board(i_choice=[2, 3, 4], hints=45)
    print(np.array(game.board))

def handle_solve_puzzle(game):
    print("Enter the Sudoku board row by row. Use '.' for empty cells.")
    
    for y in range(9):
        while True:
            row_input = input(f"Enter row {y + 1}: ").strip()
            if len(row_input) == 9 and all(c in '123456789.' for c in row_input):
                for x in range(9):
                    value = row_input[x]
                    game.board[y][x] = int(value) if value != '.' else 0
                break
            else:
                print("Invalid input. Please enter exactly 9 characters for each row, using '.' for empty cells.")
    
    # Solve the puzzle
    solver = SolveSudoku(game.board)
    
    # Output the solved puzzle
    print("\nSolved Sudoku Puzzle:")
    print(np.array(solver.board))

def main():
    print_welcome()
    
    while True:
        print_menu()
        option = get_user_option()
        game = Sudoku()
        
        if option == 0:
            handle_generate_puzzle(game)
        elif option == 1:
            handle_solve_puzzle(game)

if __name__ == "__main__":
    main()
