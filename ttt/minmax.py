"""
algorithm;
Implementation of algorithm(s) for tic-tac-toe play.
"""

from .square import Square
from .board import Board
from .limtis import Limits


def negamax(depth: int, alpha: int, beta: int, board_state: Board) -> [Square, int]:
    # check terminal states.

    if board_state.has_won(board_state.player_1):
        # this 'if' illustrates the algorithm, but do we really need it?
        # e.g. think about this if writing code to output the game tree.
        return None, 1000 * max(1, depth)

    if board_state.has_won(board_state.player_2):
        return None, -1000 * max(1, depth)

    if depth == 0:
        return None, 0

    best_so_far = (None, Limits.Min.value)
    moves = board_state.generate_moves()

    # if no moves left and nobody won, then the game state is draw.
    if len(moves) == 0:
        return None, 0

    for move in moves:
        copy_board = board_state.make_move(move)
        score = -negamax(depth - 1, -beta, -alpha, copy_board)[1]

        if score > best_so_far[1]:
            best_so_far = (move, score)

        # Read up on alpha/beta pruning, this has a *very big* impact
        # on timing, even for simple games like tic-tac-toe.
        alpha = max(alpha, score)

        if alpha >= beta:
            break

    return best_so_far
