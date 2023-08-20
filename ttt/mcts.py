from .board import Board
from .player import Player
from math import inf, log, sqrt
from operator import contains
from random import choice


class Node:
    def __init__(self, board: Board, parent=None):
        self.board = board
        self.parent = parent

        self.visits = 0
        self.score = 0
        self.children = []
        self.is_terminal = board.is_terminal_state()
        self.fully_expanded = board.is_terminal_state()


def mcts(initial_state: Board, num_iterations=1500, exp_constant=0):
    root = Node(initial_state)
    for i in range(num_iterations):
        node = select(root)
        score = rollout(node.board)
        backpropagate(node, score)

    # Return the board, containing the best move.
    return get_best_move(root, exp_constant).board


def select(node) -> Node:
    while not node.is_terminal:
        if node.fully_expanded:
            node = get_best_move(node, 2)
        else:
            return expand(node)

    return node


def expand(node: Node):
    states = node.board.generate_states()  # generate_states - could be memoized?
    xs = [n.board for n in node.children]  # existing states.

    # if we haven't come across a node, expand it.
    for state in states:
        if not contains(xs, state):
            new_node = Node(state, node)
            node.children.append(new_node)
            if len(states) == len(node.children):
                node.fully_expanded = True
            return new_node


def rollout(board: Board) -> float:
    # board.has_won - could return Naughts/Crosses/None and the return code used?
    while not (board.has_won(Player.NAUGHTS) or board.has_won(Player.CROSSES)):
        possible_states = board.generate_states()
        if len(possible_states) == 0:
            break
        board = choice(possible_states)

    if board.has_won(Player.NAUGHTS):
        return 1
    elif board.has_won(Player.CROSSES):
        return -1

    return 0


def backpropagate(node, score):
    while node:
        node.visits += 1
        node.score += score
        node = node.parent


def get_best_move(node, exploration_constant):
    best_so_far = -inf
    best_moves = []

    for child in node.children:
        player = 1 if child.board.player_2 == Player.NAUGHTS else -1

        # UCB1.
        score = player * child.score / child.visits + exploration_constant * sqrt(log(node.visits / child.visits))

        if score > best_so_far:
            best_so_far = score
            best_moves = [child]

        elif score == best_so_far:
            best_moves.append(child)

    return choice(best_moves)
