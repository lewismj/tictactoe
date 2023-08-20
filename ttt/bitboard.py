"""
BitBoard;
We use a single integer to represent a bit-board for representing
either naughts, crosses or both etc. Used by 'Board' to represent
game state.
"""

from .square import Square


class BitBoard:
    """
    A single integer is used to create a bitset for a 3x3
    tic-tac-toe board.
    """
    def __init__(self, value: int = None):
        """
        Initialize a bitboard, if a value is give, use that; otherwise
        set value to zero (empty bit set).
        :param value: optional value used to initialize the
        bitset.
        """
        if not value:
            self.value = 0
        elif value < 0:
            # note, when converting this to C# don't bother with this step,
            # just use and unsigned integer type.
            # if we have -ve number, then: val =  - (val ^ 1 0 0000 0000)
            self.value = value + 512
        else:
            self.value = value

    def set_bit(self, square: Square):
        """
        Given a square, set the bit in the underlying bitset corresponding
        to the square.
        :param square: the square to set.
        """
        if not isinstance(square, Square):
            raise TypeError("BitBoard::set_bit, expecting Square parameter.")
        self.value |= (1 << square.value)

    def get_bit(self, square: Square):
        """
        Test that a given square is set or not.
        :param square: the square to test 'has been set'.
        :return: zero, if the bit corresponding to the square is not set;
         i.e. value & (1 << square.value) otherwise.
        """
        if not isinstance(square, Square):
            raise TypeError("BitBoard::set_bit, expecting Square parameter.")
        return self.value & (1 << square.value)

    def pop_bit(self, square: Square):
        """
        Given a square, if the corresponding bit is set, set it to zero.
        :param square: the square to 'pop'.
        """
        if not isinstance(square, Square):
            raise TypeError("BitBoard::set_bit, expecting Square parameter.")
        self.value &= ~(1 << square.value)

    def square_lsb(self):
        """
        Returns the square corresponding to the least significant bit of
        the bitboard, or none if no bits set.
        :return: square of lsb, none if no bits set.
        """
        if self.value == 0:
            return None

        return Square(((self.value & (-self.value)) - 1).bit_count())

    def is_empty(self):
        """
        Return true if the bitboard is 'empty', that is, has zero value.
        :return: True if value is zero; false otherwise.
        """
        return self.value == 0

    def __str__(self):
        """
        Return a string representation of the bitboard.
        :return: a string representation of the bitboard.
        """
        tmp = ""
        for rank in range(3):
            for file in range(3):
                square = Square(rank * 3 + file)
                if self.get_bit(square):
                    tmp += " 1 "
                else:
                    tmp += " O "
            tmp += "\n"
        tmp += f"value {self.value}\n"
        tmp += "\n"
        return tmp
