# tic_tac_toe_loops_start.py

def print_board(board):
    print()
    for i in range(3):
        print(" ", board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        if i < 2:
            print("---+---+---")
    print()

def check_winner(board, player):
    win_patterns = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # cols
        (0,4,8), (2,4,6)            # diagonals
    ]
    for a,b,c in win_patterns:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def board_full(board):
    for cell in board:
        if cell == " ":
            return False
    return True

def ai_move(board, ai, human):
    # 1. Can AI win this turn?
    for i in range(9):
        if board[i] == " ":
            board[i] = ai
            if check_winner(board, ai):
                return
            board[i] = " "

    # 2. Can Human win next? Block!
    for i in range(9):
        if board[i] == " ":
            board[i] = human
            if check_winner(board, human):
                board[i] = ai
                return
            board[i] = " "

    # 3. Otherwise, just pick first empty
    for i in range(9):
        if board[i] == " ":
            board[i] = ai
            return

def human_move(board, human):
    while True:
        try:
            pos = int(input("Enter your move (1-9): ")) - 1
            if pos not in range(9):
                print("Invalid. Choose 1-9.")
            elif board[pos] != " ":
                print("Cell already taken.")
            else:
                board[pos] = human
                break
        except ValueError:
            print("Enter a number, 1-9.")

def game():
    board = [" "] * 9
    human = ""
    while human not in ("X", "O"):
        human = input("Choose X or O: ").upper().strip()
    ai = "O" if human == "X" else "X"

    # Ask who begins
    first = ""
    while first not in ("H", "A"):
        first = input("Who begins? (H)uman or (A)I: ").upper().strip()
    turn = first

    print("\nBoard positions:")
    print_board([str(i+1) for i in range(9)])  # show guide

    while True:
        print_board(board)

        if check_winner(board, human):
            print("You win 🎉")
            break
        if check_winner(board, ai):
            print("AI wins 🤖")
            break
        if board_full(board):
            print("It's a tie!")
            break

        if turn == "H":
            human_move(board, human)
            turn = "A"
        else:
            print("AI is thinking...")
            ai_move(board, ai, human)
            turn = "H"

if __name__ == "__main__":
    game()
