from guizero import App, Box, Text, TextBox, PushButton

# Predefined Sudoku puzzle (0 represents empty cells)
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Create a board for the user to input their answers
user_board = [[0 for _ in range(9)] for _ in range(9)]


def is_valid_move(board, row, col, num):
    """Check if placing num at (row, col) is valid."""
    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def check_solution():
    """Check if the user's solution is correct."""
    # Fill user board with input values
    for row in range(9):
        for col in range(9):
            value = input_boxes[row][col].value
            if value.isdigit():
                user_board[row][col] = int(value)
            else:
                user_board[row][col] = 0

    # Validate the entire Sudoku grid
    for row in range(9):
        for col in range(9):
            num = user_board[row][col]
            if num == 0 or not is_valid_move(user_board, row, col, num):
                status_text.value = "Incorrect solution. Try again!"
                return

    status_text.value = "Congratulations! You solved it!"


# GUI setup
app = App("Sudoku", width=400, height=500)
Text(app, text="Sudoku Puzzle", size=18)

# Create the Sudoku grid
grid_box = Box(app, layout="grid")
input_boxes = [[None for _ in range(9)] for _ in range(9)]

for row in range(9):
    for col in range(9):
        if puzzle[row][col] != 0:  # Pre-filled cells
            input_boxes[row][col] = Text(
                grid_box, text=str(puzzle[row][col]), grid=[col, row], size=14
            )
        else:  # Empty cells for user input
            input_boxes[row][col] = TextBox(
                grid_box,
                grid=[col, row],
                width=2,
                height=1,
                align="center",
            )

# Button to check the solution
PushButton(app, text="Check Solution", command=check_solution)

# Status text to display results
status_text = Text(app, text="", size=14)

# Run the app
app.display()