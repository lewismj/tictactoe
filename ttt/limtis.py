from enum import Enum


class Limits(Enum):
    """Integer limits, for searching.
       Consider why we use integer arithmetic for static evaluation,
       used by Negamax. It isn't important for tic-tac-toe but could
       be for more complex games where speed is required.
    """
    Min: int = -100000000
    Max: int = 100000000
