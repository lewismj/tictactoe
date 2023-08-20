"""
square;
We define the board representation as bitsets (integer) for naughts
and crosses; referenced by square enumeration:
  A0 B0 C0
  A1 B1 C1
  A2 B2 C2
"""

from enum import Enum


class Square(Enum):
    """
    Define squares used for tic-tac-toe.
    """
    A0 = 0
    B0 = 1
    C0 = 2
    A1 = 3
    B1 = 4
    C1 = 5
    A2 = 6
    B2 = 7
    C2 = 8
