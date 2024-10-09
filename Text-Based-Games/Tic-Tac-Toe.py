"""

    print('    😊😊😊😊😊    ')
    print('  😊            😊  ')
    print(' 😊      😊      😊 ')
    print(' 😊             😊 ')
    print('  😊  😊😊😊😊  😊  ')
    print('    😊😊😊😊😊    ')
    print('\n')
    print('      TUZOV       ')
    print('-------------------')

"""



def print_board(board):
    # Prints the Tic-Tac-Toe board
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    # Check all winning combinations
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                      (0, 4, 8), (2, 4, 6)]
    for combo in win_conditions:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_board_full(board):
    # Check if the board is full (i.e. no empty spaces)
    return all([spot != ' ' for spot in board])

def tic_tac_toe():
    # Initialize the board
    board = [' '] * 9
    current_player = 'X'  # Player 'X' starts first
    
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Get player's move
        try:
            move = int(input(f"Player {current_player}, choose your move (1-9): ")) - 1
        except ValueError:
            print("Invalid input. Please choose a number between 1 and 9.")
            continue

        if move < 0 or move > 8 or board[move] != ' ':
            print("This move is not valid. Try again.")
            continue
        
        # Make the move
        board[move] = current_player
        print_board(board)
        
        # Check if the current player has won
        if check_winner(board, current_player):
            print(f"Congratulations! Player {current_player} wins!")
            break
        
        # Check if the board is full (i.e., it's a draw)
        if is_board_full(board):
            print("It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'
        
if __name__ == "__main__":
    tic_tac_toe()

    