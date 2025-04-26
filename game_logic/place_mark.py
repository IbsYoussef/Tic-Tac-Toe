
def place_mark(board, position, player):
    """
    Places a player's mark ('X' or 'O') at the specified position on the board.
    
    Args:
        board: A list of 9 elements representing the board state
        position: An integer from 1-9 representing the position on the board
                 (1 is top-left, 9 is bottom-right)
        player: The player's mark ('X' or 'O')
        
    Returns:
        bool: True if the mark was placed successfully, False if the position was invalid or already taken
    """

    # Convert from 1-9 position to 0-8 index
    index = position - 1

    # Check if the position is valid
    if index < 0 or index > 8:
        print("Invalid position! Please choose a number between 1 and 9.")
        return False
    
    # Check if the position is already taken
    if board[index] != ' ':
        print(f"Position {position} is already taken! Choose another position.")
        return False
    
    # Place the mark and return success
    board[index] = player
    return True
