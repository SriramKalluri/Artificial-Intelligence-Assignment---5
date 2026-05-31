# minimax.py
# Tic-Tac-Toe using the Minimax algorithm

def print_board(board):
    # Print the board
    print()

    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")

        if i < 6:
            print("---|---|---")

    print()


def get_empty_cells(board):
    # Return all empty positions
    return [i for i in range(9) if board[i] == ' ']


def check_winner(board, player):

    wins = [
        [0,1,2],
        [3,4,5],
        [6,7,8],

        [0,3,6],
        [1,4,7],
        [2,5,8],

        [0,4,8],
        [2,4,6]
    ]

    for combo in wins:

        if all(board[i] == player for i in combo):
            return True

    return False


def is_terminal(board):

    return (
        check_winner(board, 'X') or
        check_winner(board, 'O') or
        len(get_empty_cells(board)) == 0
    )


def minimax(board, is_maximizing):

    # Base cases
    if check_winner(board, 'O'):
        return 1

    if check_winner(board, 'X'):
        return -1

    if not get_empty_cells(board):
        return 0

    # AI turn
    if is_maximizing:

        best_score = -float('inf')

        for cell in get_empty_cells(board):

            board[cell] = 'O'

            score = minimax(board, False)

            board[cell] = ' '

            best_score = max(best_score, score)

        return best_score

    # Human turn
    else:

        best_score = float('inf')

        for cell in get_empty_cells(board):

            board[cell] = 'X'

            score = minimax(board, True)

            board[cell] = ' '

            best_score = min(best_score, score)

        return best_score


def get_best_move(board):

    best_score = -float('inf')
    best_move = None

    for cell in get_empty_cells(board):

        board[cell] = 'O'

        score = minimax(board, False)

        board[cell] = ' '

        if score > best_score:

            best_score = score
            best_move = cell

    return best_move


def play_game():

    board = [' '] * 9

    print("Tic-Tac-Toe using Minimax")
    print("You are X")
    print("AI is O")

    while not is_terminal(board):

        print_board(board)

        # User move
        while True:

            try:
                move = int(input("Enter position (1-9): ")) - 1

                if move in get_empty_cells(board):
                    break

                else:
                    print("Invalid move")

            except ValueError:
                print("Enter a number from 1-9")

        board[move] = 'X'

        if is_terminal(board):
            break

        # AI move
        print("AI is thinking...")

        ai_move = get_best_move(board)

        board[ai_move] = 'O'

        print(f"AI chose position {ai_move + 1}")

    # Final board
    print_board(board)

    if check_winner(board, 'X'):
        print("You win!")

    elif check_winner(board, 'O'):
        print("AI wins!")

    else:
        print("Draw!")


if __name__ == "__main__":
    play_game()
