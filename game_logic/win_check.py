def check_win(board):
    """
    Checks if a player has won the game.
    
    Args:
        board: A list of 9 elements representing the board state
        
    Returns:
        tuple: (bool, str) - (True if there's a winner, winner's mark ('X' or 'O'))
               If no winner, returns (False, None)
    """
    
    # Check rows
    for i in range(0, 9, 3):
        if board[i] != ' ' and board[i] == board[i+1] == board[i+2]:
            return True, board[i]
     
    # Check columns
    for i in range(3):
        if board[i] != ' ' and board[i] == board[i+3] == board[i+6]:
            return True, board[i]
    
    # Check diagonal (top-left to bottom-right)
    if board[0] != ' ' and board[0] == board[4] == board[8]:
        return True, board[0]
    
    # Check diagonal (top-right to bottom-left)
    if board[2] != ' ' and board[2] == board[4] == board[6]:
        return True, board[2]

    # No winner
    return False, None

def check_draw(board):
    '''
    Checks if the game is a draw (board is full with no winner).


    Args:
        board: A list of 9 elements, representing the board state


    Returns:
        bool: True if the game is a draw, False otherwise    
    '''

    return ' ' not in board

def check_game_over(board):
    ''' 
    Checks if the game is over (either by win or draw).

    Args:
        board: A list of 9 elements representing the board state

    Returns:
        tuple: (bool, str) - (True if game is over, result string)
               Result will be "X wins", "O wins", "Draw", or None if game isn't over 
    '''

    has_winner, winner = check_win(board)
    if has_winner:
        return True, f"{winner} wins"
    
    # Check for draw
    if check_draw(board):
        return True, "Draw"
    
    # Game is not over
    return False, None

def test_win_conditions():
    # Test row win
    board = ['X', 'X', 'X',
            'O', 'O', 'O',
            ' ', ' ', ' ']
    is_win, winner = check_win(board)
    print(f"Row win test: {is_win}, Winner: {winner}")

    # Test column win
    board = ['O', ' ', 'X',
             'O', ' ', 'X',
             'O', ' ', ' ']
    is_win, winner = check_win(board)
    print(f"Column win test: {is_win}, Winner: {winner}")
    
    # Test diagonal win
    board = ['X', 'O', ' ',
             'O', 'X', ' ',
             ' ', ' ', 'X']
    is_win, winner = check_win(board)
    print(f"Diagonal win test: {is_win}, Winner: {winner}")
    
    # Test draw
    board = ['X', 'O', 'X',
             'X', 'O', 'O',
             'O', 'X', 'X']
    is_draw = check_draw(board)
    print(f"Draw test: {is_draw}")
    
    # Test game over
    is_over, result = check_game_over(board)
    print(f"Game over test: {is_over}, Result: {result}")

if __name__ == "__main__":
    test_win_conditions()