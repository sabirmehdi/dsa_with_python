import os

# The game board, represented as a list
board = [' ' for _ in range(9)]

def clear_screen():
    """Clears the console screen."""
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS/Linux
    else:
        os.system('clear')

def display_board():
    """Prints the current state of the Tic-Tac-Toe board."""
    clear_screen()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_win(player_mark):
    """Checks if the given player has won the game."""
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player_mark:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player_mark:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player_mark:
        return True
    if board[2] == board[4] == board[6] == player_mark:
        return True
    return False

def check_tie():
    """Checks if the game is a tie."""
    return ' ' not in board

def play_game():
    """Manages the Tic-Tac-Toe game flow."""
    current_player = 'X'
    game_over = False

    while not game_over:
        display_board()
        print(f"\nPlayer {current_player}'s turn.")

        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if not (0 <= move <= 8) or board[move] != ' ':
                print("Invalid move. Please choose an empty cell between 1 and 9.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        board[move] = current_player

        if check_win(current_player):
            display_board()
            print(f"\nPlayer {current_player} wins!")
            game_over = True
        elif check_tie():
            display_board()
            print("\nIt's a tie!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

# Start the game
if __name__ == "__main__":
    play_game()