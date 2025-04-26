def initialise_board():
    """"
    Creates and returns a new empty tic-tac-toe board.

    Returns:
        list: A list of 9 empty spaces representing an empty board
    """""

    return [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def displayBoard(board):
    """
    Displays a tic-tac-toe board in a visually appealing format.
    
    Args:
        board: A list of 9 elements representing the board state
              (empty spaces, 'X's, and 'O's)
    """

    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
    print("-----+-----+-----")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
    print("-----+-----+-----")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")

def showPositionGuide():
    print("Position Guide:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()