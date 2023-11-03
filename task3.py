import random

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

# Function to get a valid player move
def get_player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Please try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

# Main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    
    print("Tic Tac Toe Game")
    print_board(board)

    for _ in range(9):
        print(f"Player {player}'s turn")
        if player == "X":
            row, col = get_player_move(board)
        else:
            # Implement AI here (e.g., random moves)
            while True:
                row, col = random.randint(0, 2), random.randint(0, 2)
                if board[row][col] == " ":
                    break
        board[row][col] = player
        print_board(board)
        if check_win(board, player):
            print(f"Player {player} wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    play_game()
