# heuristicalphabeta.py
# Tic-Tac-Toe using Heuristic Alpha-Beta Pruning

def print_board(board):

    print()

    for i in range(0, 9, 3):

        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")

        if i < 6:
            print("---|---|---")

    print()


def get_empty_cells(board):

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


# Heuristic evaluation function
def heuristic(board):

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

    score = 0

    for combo in wins:

        line = [board[i] for i in combo]

        o_count = line.count('O')
        x_count = line.count('X')

        # Favor AI positions
        if o_count > 0 and x_count == 0:
            score += o_count

        # Penalize human positions
        if x_count > 0 and o_count == 0:
            score -= x_count

    return score


def alphabeta(board, depth, is_maximizing, alpha, beta):

    # Base cases
    if check_winner(board, 'O'):
        return 100

    if check_winner(board, 'X'):
        return -100

    if not get_empty_cells(board):
        return 0

    # Depth limit reached
    if depth == 0:
        return heuristic(board)

    # AI turn
    if is_maximizing:

        best_score = -float('inf')

        for cell in get_empty_cells(board):

            board[cell] = 'O'

            score = alphabeta(
                board,
                depth - 1,
                False,
                alpha,
                beta
            )

            board[cell] = ' '

            best_score = max(best_score, score)

            alpha = max(alpha, best_score)

            # Pruning
            if beta <= alpha:
                break

        return best_score

    # Human turn
    else:

        best_score = float('inf')

        for cell in get_empty_cells(board):

            board[cell] = 'X'

            score = alphabeta(
                board,
                depth - 1,
                True,
                alpha,
                beta
            )

            board[cell] = ' '

            best_score = min(best_score, score)

            beta = min(beta, best_score)

            # Pruning
            if beta <= alpha:
                break

        return best_score


def get_best_move(board, depth=4):

    best_score = -float('inf')
    best_move = None

    for cell in get_empty_cells(board):

        board[cell] = 'O'

        score = alphabeta(
            board,
            depth,
            False,
            -float('inf'),
            float('inf')
        )

        board[cell] = ' '

        if score > best_score:

            best_score = score
            best_move = cell

    return best_move


def play_game():

    board = [' '] * 9

    print("Tic-Tac-Toe using Heuristic Alpha-Beta")
    print("You are X")
    print("AI is O")

    while not is_terminal(board):

        print_board(board)

        # User move
        while True:

            try:

                move = int(
                    input("Enter position (1-9): ")
                ) - 1

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

    # Final result
    print_board(board)

    if check_winner(board, 'X'):
        print("You win!")

    elif check_winner(board, 'O'):
        print("AI wins!")

    else:
        print("Draw!")


if __name__ == "__main__":
    play_game()
