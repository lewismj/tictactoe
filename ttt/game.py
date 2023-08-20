"""
game;
 Implementation of game loop.
"""

from .board import Board
from .square import Square
from .minmax import negamax, Limits
from .mcts import mcts


def is_win_or_draw(board: Board):
    if board.has_won(board.player_2):
        print(f"{board.player_2} has won!")
        return True
    elif board.is_full():
        print("game drawn.")
        return True

    return False


def game_loop(algorithm='negamax', max_depth=9, num_iterations=1000):
    print("tic tac toe\n")
    print("'exit' to quit\n")
    print("enter moves; rank, file format, e.g. 0,2 for C0.\n")
    board = Board()
    while True:
        print(board)
        user_input = input(">")

        if user_input == "exit":
            break

        if user_input == "":
            continue

        try:
            rank = int(user_input.split(',')[0])
            file = int(user_input.split(',')[1])
            square = Square(rank * 3 + file)

            if not board.is_square_empty(square):
                print("Illegal move, square occupied.\n")
                continue

            board = board.make_move(square)
            print(board)
            if is_win_or_draw(board):
                print(board)
                board = Board()
                continue

            # When migrating this to C# think of a better way to
            # represent algorithms as a parameter, higher order functions?
            if algorithm == 'negamax':
                move, _ = negamax(max_depth, Limits.Min.value, Limits.Max.value, board)
                board = board.make_move(move)
            else:
                board = mcts(board, num_iterations)

            if is_win_or_draw(board):
                print(board)
                board = Board()
                continue

        except ValueError as ve:
            print(f"Incorrect move format {ve}")
