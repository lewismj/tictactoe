"""
player;
Defines the player (NAUGHTS or CROSSES) that can exist in
a tic-tac-toe game.
"""

from enum import Enum


class Player(Enum):
    """
    Player can be either NAUGHTS or CROSSES.
    """
    NAUGHTS = 0
    CROSSES = 1

    # Note, In the board representation, I use two fields
    # player_1, player_2; rather than using a single 'player' field.

    # You could convert the code to use a single 'next_player' field
    # and use these methods.
    # Pro; uses less memory.
    # Con; the code is maybe harder to read as some statements
    # are changed?
    def next(self):
        """
        If the last player was Naughts, the next player
        will be Crosses.
        :return: Naughts if player is Crosses, Crosses otherwise.
        """
        if self == Player.NAUGHTS:
            return Player.CROSSES
        return Player.NAUGHTS

    def previous(self):
        """
        Given that there are two players, previous player equals
        the next player.
        :return: Naughts if player is Crosses, Crosses otherwise.
        """
        return self.next()
