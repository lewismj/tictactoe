"""
board;
Representation of board state for a tic-tac-toe game.
We use two BitBoard to represent the naughts and crosses.
"""

from copy import deepcopy
from .bitboard import BitBoard
from .mask import Mask
from .player import Player
from .square import Square


class Board:
    """
    The tic-tac-toe board state is represented as naughts & crosses bitboards,
    together with 'player_to_move'.

    Note -  I use two bitboard utilising 9 bits of an integer.
    Exercise - This makes the logic easy to follow and logical.

    However, you can decide to change the BitBoard to use just one integer.
    and mask the top 9 bits for naughts and the other 9 bits for crosses.
    You would need to add in appropriate logic to handle that.

    In reality in a 'real system' you would prefer the use of two integers.
    """

    # if self.naughts.value | self.crosses.value == 511, then we know the
    # board is full, no spaces available.
    FULL_BOARD: int = 511

    def __init__(self, naughts=None, crosses=None):
        """
        Initializes board state.
        :param naughts: the bitboard representing naughts, set empty if None.
        :param crosses: the bitboard representing crosses, set empty if None.
        """
        self.naughts = naughts if naughts else BitBoard()
        self.crosses = crosses if crosses else BitBoard()
        self.player_1 = Player.NAUGHTS
        self.player_2 = Player.CROSSES

    def is_full(self):
        return True if (self.naughts.value | self.crosses.value) == self.FULL_BOARD else False

    def is_square_empty(self, square: Square) -> bool:
        if self.naughts.get_bit(square) or self.crosses.get_bit(square):
            return False
        return True

    def make_move(self, square: Square):
        """
        Return a new board, that represents the game state after apply a move.
        Notes;
        1. the moving player is self.next_player
        2. self.next_player is shifted from O -> X or X -> O as appropriate.
           (i.e. score appropriately).
        :param square: the square of the move.
        :return: the new board state.
        """
        # assume the square is validated by generate_moves function.
        # n.b. we set the next player forward.
        copy_board = deepcopy(self)

        if self.player_1 == Player.NAUGHTS:
            copy_board.naughts.set_bit(square)
            copy_board.player_1 = Player.CROSSES
            copy_board.player_2 = Player.NAUGHTS
        else:
            copy_board.crosses.set_bit(square)
            copy_board.player_1 = Player.NAUGHTS
            copy_board.player_2 = Player.CROSSES

        return copy_board

    def generate_moves(self):
        """
        Returns a list of possible 'moves', that is empty squares.
        :return: the list of empty squares on the board.
        """
        moves = []
        free_squares = BitBoard(~(self.naughts.value | self.crosses.value))
        while not free_squares.is_empty():
            square = free_squares.square_lsb()
            moves.append(square)
            free_squares.pop_bit(square)
        return moves

    def generate_states(self):
        """
        Returns a list of possible board states (i.e. applied moves) at the
        current position.
        :return: the list of board states.
        """
        states = []
        free_squares = BitBoard(~(self.naughts.value | self.crosses.value))
        while not free_squares.is_empty():
            square = free_squares.square_lsb()
            state = self.make_move(square)
            states.append(state)
            free_squares.pop_bit(square)
        return states

    def has_won(self, player: Player):
        """
        Returns true, if 'player' has won the game, i.e. 3 in some rank,
        file or diagonal.
        :param player: the player to test.
        :return: True if player won; false otherwise.
        """
        side = self.naughts if player == Player.NAUGHTS else self.crosses
        for mask in Mask:
            if side.value & mask.value == mask.value:
                return True
        return False

    def is_terminal_state(self):
        if self.has_won(self.player_1) or self.has_won(self.player_2):
            return True
        elif self.is_full():
            return True

        return False

    def __eq__(self, other):
        if isinstance(other, Board):
            return self.naughts.value == other.naughts.value and self.crosses.value == other.crosses.value
        return False

    def __str__(self):
        tmp = ""
        for rank in range(3):
            for file in range(3):
                square = Square(rank * 3 + file)
                if self.naughts.get_bit(square):
                    tmp += " O "
                elif self.crosses.get_bit(square):
                    tmp += " X "
                else:
                    tmp += " . "
            tmp += "\n"
        tmp += f"player to move: {self.player_1}"
        tmp += "\n"

        return tmp
