def solve_sudoku(grid):
    """
    Solves a Sudoku puzzle using backtracking.

    :param grid: A 2D list representing an unsolved Sudoku puzzle.
    :return: A 2D list representing the solved Sudoku puzzle.
    """
    row, col = find_empty(grid)

    if row is None and col is None:
        return grid

    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return grid

            grid[row][col] = 0

    return None

def is_valid(grid, row, col, num):
    """
    Checks if a given number can be placed at a given position in the Sudoku grid.

    :param grid: A 2D list representing a Sudoku puzzle.
    :param row: The row index of the position to check.
    :param col: The column index of the position to check.
    :param num: The number to check.
    :return: True if the number can be placed at the given position, False otherwise.
    """
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False

    box_row = row - row % 3
    box_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[i + box_row][j + box_col] == num:
                return False

    return True

def find_empty(grid):
    """
    Finds the next empty position in the Sudoku grid.

    :param grid: A 2D list representing a Sudoku puzzle.
    :return: A tuple of the row and column indices of the next empty position, or None if there are no empty positions.
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col

    return None, None

def print_grid(grid):
    """
    Prints a Sudoku grid in a human-readable format.

    :param grid: A 2D list representing a Sudoku puzzle.
    """
    for row in range(9):
        for col in range(9):
            if col == 3 or col == 6:
                print("|", end="")
            print(f" {grid[row][col]:2}", end="")
        print("")
    print("-" * 21)

# Example usage:

grid = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

solved_grid = solve_sudoku(grid)

if solved_grid is not None:
    print_grid(solved_grid)
else:
    print("No solution found.")