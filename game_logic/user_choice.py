def user_choice(board):
    """""
    
    Asks the player to choose a place on the board that is valid and not taken

    """""

    # Initial Variables
    choice = 'WRONG'
    acceptable_range = range(1,10)
    within_range = False

    # Core game loop to ask for player choice
    while choice.isdigit() == False or within_range == False or board[int(choice) - 1] != ' ':

        # Asks user for input choice
        choice = input("Please enter a number (1-9): ")

        # Digit check
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
        
        # Check number is within valid range
        if int(choice) not in acceptable_range:
            print("Sorry you are out of acceptable range.")
            continue

        if board[int(choice)-1] != ' ':
            print("Sorry spot already taken. Please choose another.")
            continue

        within_range = True

    # Returns player choice
    return int(choice)