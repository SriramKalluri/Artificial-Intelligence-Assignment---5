# montecarlo.py
# Tic-Tac-Toe using Monte Carlo Simulation


import random


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


# Simulate random game
def simulate_game(board, current_player):

    temp_board = board[:]

    while not is_terminal(temp_board):

        empty = get_empty_cells(temp_board)

        move = random.choice(empty)

        temp_board[move] = current_player

        # Switch player
        if current_player == 'X':
            current_player = 'O'

        else:
            current_player = 'X'

    if check_winner(temp_board, 'O'):
        return 'O'

    elif check_winner(temp_board, 'X'):
        return 'X'

    else:
        return 'Draw'


def monte_carlo_move(board, simulations=300):

    empty = get_empty_cells(board)

    best_move = None
    best_score = -1

    for cell in empty:

        wins = 0

        for _ in range(simulations):

            temp_board = board[:]

            temp_board[cell] = 'O'

            result = simulate_game(
                temp_board,
                'X'
            )

            if result == 'O':
                wins += 1

        if wins > best_score:

            best_score = wins
            best_move = cell

    return best_move


def play_game():

    board = [' '] * 9

    print("Tic-Tac-Toe using Monte Carlo Search")
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
        print("AI is simulating games...")

        ai_move = monte_carlo_move(board)

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
