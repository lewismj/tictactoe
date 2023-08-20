"""
mask;
Define bitmasks for testing board state, e.g. all squares,
first rank, first file etc.
"""

from enum import Enum


class Mask(Enum):
    """
    Masks of the form; e.g. A file:

   0   1 0 0
   1   1 0 0
   2   1 0 0

       a b c

     Used to evaluate Board.
    """
    RANK_0 = 7
    RANK_1 = 56
    RANK_2 = 448
    A_FILE = 73
    B_FILE = 146
    C_FILE = 292
    LR_DIAGONAL = 273
    RL_DIAGONAL = 84
