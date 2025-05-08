import sys

def split_entries(line):
    return line.split(" ")

def print_board(nested_list):
    ''' Prints out sudoku board when given in nested list format '''
    for y in nested_list:
        for x in y:
            print(x, end=' ')
        print()

def is_valid(board, row, col, num):
    ''' Check if it's valid to place num at position (row, col) '''
    # Check row
    if num in board[row]:
        return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def check_if_board_valid(board):
    ''' Checks if the board in nested list format is a valid board and returns True, else False '''
    # Check if board is not empty
    if len(board) == 0:
        return False
    # Checks if board has 9 rows
    if len(board) != 9:
        return False

    for row in board:
        if len(row) != 9:  # checks if each row has 9 columns
            return False
        for element in row:
            try:
                num = int(element)  # Convert string to integer
                if num < 0 or num > 9:  # Valid range is 0–9
                    return False
            except ValueError:
                return False
    return True

def txt_output(nested_board):
    ''' Takes in a solved nested board [[][]] and write to a txt file in named solved.txt '''
    f=open('solved.txt','w') #open or create file called solved.txt
    for line in nested_board:
        new_line=''
        for entry in line:
            new_line+=entry+' ' #append string to create row
        new_line=new_line.strip()+'\n'
        f.write(new_line)
    f.close


def is_solved(nested_board):
    ''' Check if the board is solved (all cells are filled and valid) '''
    for line in nested_board:
        for entry in line:
            if entry == '0':  # Check if there is any empty cell
                return False
    return True

def find_empty_cell(board):
    ''' Find the next empty cell in the board (returns None if no empty cells) '''
    for i in range(9):
        for j in range(9):
            if board[i][j] == '0':  # Empty cells are marked with '0'
                return i, j
    return None

def solve(board):
    ''' Solve the sudoku puzzle using backtracking '''
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # Puzzle solved

    row, col = empty_cell

    for num in range(1, 10):
        num_str = str(num)  # Convert number to string for comparison
        if is_valid(board, row, col, num_str):
            board[row][col] = num_str  # Place the number as a string

            if solve(board):
                return True

            # Backtrack
            board[row][col] = '0'

    return False  # Trigger backtracking

def print_sudoku_instructions():
    print("Welcome to Sudoku!")
    print("\nObjective:")
    print("The goal is to fill a 9x9 grid with digits from 1 to 9, so that each row, each column, and each of the nine 3x3 subgrids contain every number from 1 to 9 without repetition.")
    
    print("\nRules:")
    print("1. Each row must contain the numbers 1 to 9, without repetition.")
    print("2. Each column must contain the numbers 1 to 9, without repetition.")
    print("3. Each of the nine 3x3 subgrids must contain the numbers 1 to 9, without repetition.")
    print("4. Some numbers may already be placed in the grid; these are known as 'given' numbers.")
    print("5. Use logic to fill in the missing numbers.")
    
    print("\nTips:")
    print("1. Start by looking for rows, columns, or subgrids that are almost complete.")
    print("2. Use the process of elimination to determine which numbers can go where.")
    print("3. Work methodically and don't guess, as there is usually only one solution to a Sudoku puzzle.")
    print("4. If stuck, take a break and return with a fresh mind!")
    
    print("\nGood luck and have fun solving!")

def main():
    # Opens file with error handling
    try:
        with open(sys.argv[1], 'r') as puzzle:
            puzzle = puzzle.read().split('\n')  
    except FileNotFoundError as e:
        sys.exit(f"Error: {e}")
    except IndexError:
        sys.exit("Usage: python3 solve.py <filename>")
    
    # Format the board to nested list [['9', '6', '2', '0', '7', '8', '5', '0', '0'], ['1', '0', '5', '0', '0', '9', '3', '0', '0']]
    puzzle = list(map(split_entries, puzzle))
    
    # Check the board validity
    if check_if_board_valid(puzzle):
        print('Valid board\n')
        print_board(puzzle)
        if solve(puzzle):
            print("\nSolved Sudoku Board:")
            txt_output(puzzle)
            print_board(puzzle)
        else:
            print("\nNo solution exists.")
    else:
        sys.exit('Invalid Sudoku Board size')

if __name__ == "__main__":
    main()

 