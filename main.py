from game_logic.display import initialise_board, displayBoard, showPositionGuide
from game_logic.place_mark import place_mark
from game_logic.user_choice import user_choice
from game_logic.win_check import check_game_over

def main():
    # Welcome message to user
    print("Welcome to Tic Tac Toe 😊")

    # Gather player choice input
    valid_symbols = ['X', 'O']
    player_one = ''

    while place_mark not in valid_symbols:
        player_one = input("Player 1, choose your symbol (X or O): ").upper()
        if player_one not in valid_symbols:
            print("Sorry invalid choice, please pick either X or O")
        else:
            break

    # Set player two's symbol to be the opposite of player one's
    player_two = 'O' if player_one == 'X' else 'X'

    print(f"Player 1 will be {player_one} and Player 2 will be {player_two}")

    # Print board guide
    showPositionGuide()

    # Initialise board
    board = initialise_board()

    # Print initial board
    displayBoard(board)

    # Core game loop
    current_player = player_one # Player One goes first
    current_player_number = 1 # Keep track of which player's turn it is
    game_over = False

    while not game_over:
        # Display current player turn
        print(f"\nPlayer {current_player}'s turn ({current_player}).")

        # Get position choice from current player
        position = user_choice(board)

        # Place the mark
        place_mark(board, position, current_player)

        # Display updated board
        displayBoard(board)

        # Check for win/draw 
        game_over, result = check_game_over(board)

        if game_over:
            print(f"\nGame Over! {result}")
            if "wins" in result:
                print(f"Congratulations Player {current_player}!")
        else:
            # Switch players
            current_player = player_two if current_player == player_one else player_one
            current_player_number = 2 if current_player_number == 1 else 1

if __name__ == "__main__":
    main()