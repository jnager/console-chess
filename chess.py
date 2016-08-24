from pprint import pprint
from copy import deepcopy
from pandas import DataFrame


class Board(object):
    """Board class contains """
    empty_board = []
    for y in xrange(8):
        for x in xrange(8):
            if y % 2 == 0:
                color = "black"

    def __init__(self):
        board = []
        for y in xrange(8):
            row = []
            for x in xrange(8):
                row.append(None)
            board.append(row)
        self.board = board

    def print_board(self):
        print DataFrame(self.board)

    def is_in_check(color):
        pass

    def setup_board(self):
        colors = ["white", "black"]
        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for color in colors:
            # Sets up rows of pawns in appropriate spaces
            if color == "black":
                y = 1
            else:
                y = 6
            for x in xrange(8):
                pawn = Pawn(color)
                pawn.place_on_board(self, (y, x))
            # Place rows 0 and 7
            if color == "black":
                y = 0
            else:
                y = 7
            for x, piece in enumerate(pieces):
                curr_piece = piece(color)
                curr_piece.place_on_board(self, (y, x))

    def move_piece(self, loc1, loc2, color):
        """Rearranges the board per passed in parameters.
           Loc1 and loc2 should be tuples.

           Will return True if move is allowable or False
           if that is not a valid move.

        """
        # Check to make sure loc1 contains a piece of the player's color
        # Also check that loc2 is a valid spot
        try:
            piece = self.board[loc1[0]][loc1[1]]
            for num in loc2:
                num = int(num)
                if num < 0 or num > 7:
                    return False
        except (TypeError, IndexError, ValueError):
            return False
        if not isinstance(piece, Piece):
            return False
        if not piece.color == color:
            return False
        # Check to make sure the move is valid
        if not piece.check_move(loc1, loc2):
            return False
        # Now that all checks have been passed, move piece
        self.board[loc2[0]][loc2[1]] = piece
        self.board[loc1[0]][loc1[1]] = None
        return True


class Piece(object):
    """Piece class contains universal methods for each type of piece"""

    def __init__(self, color):
        self.color = color

    def place_on_board(self, board, location):
        """
           board should be the actual Board object for modification
           location should be a tuple indicating (y, x)
        """
        board.board[location[0]][location[1]] = self

    def __repr__(self):
        """Prints out the piece name with color"""
        return "{}-{}".format(self.color[0], self.name[0:2])

    def check_move(self, loc1, loc2):
        """Skeleton function as a placeholder"""
        return True


class Pawn(Piece):
    """Inherits from Piece. Represents a Pawn"""
    name = "Pawn"


class Knight(Piece):
    """Inherits from Piece. Represents a Knight."""
    name = "Knight"


class Bishop(Piece):
    """Inherits from Piece. Represents a Bishop."""
    name = "Bishop"


class Rook(Piece):
    """Inherits from Piece. Represents a Rook."""
    name = "Rook"


class Queen(Piece):
    """Inherits from Piece. Represents a Queen."""
    name = "Queen"


class King(Piece):
    """Inherits from Piece. Represents a King."""
    name = "King"
