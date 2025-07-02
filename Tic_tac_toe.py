board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Initial board display
print_board()

# Symbol selection
while True:
    symbol = input("Player 1, choose your symbol ['X' or 'O']: ").upper()
    if symbol in ["X", "O"]:
        symbol_2 = "O" if symbol == "X" else "X"
        break
    else:
        print("Invalid symbol. Please choose 'X' or 'O'.")

# Game setup
current_player = "Player 1"
current_symbol = symbol
moves = 0

# Win combinations
win_combos = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

# Game loop
while True:
    print_board()
    try:
        move = int(input(f"{current_player}, choose a spot (1-9): ")) - 1
        if move < 0 or move >= 9:
            print("Enter a number between 1 and 9.")
            continue
        if board[move] in ["X", "O"]:
            print("That spot is already taken. Try again.")
            continue
        board[move] = current_symbol
        moves += 1
    except ValueError:
        print("Invalid input. Enter a number.")
        continue

    # Check for win
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == current_symbol:
            print_board()
            print(f"{current_player} wins the match! 🎉")
            exit()

    # Check for draw
    if moves == 9:
        print_board()
        print("It's a draw! 🤝")
        break

    # Switch turns
    if current_player == "Player 1":
        current_player = "Player 2"
        current_symbol = symbol_2
    else:
        current_player = "Player 1"
        current_symbol = symbol
