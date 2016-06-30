class Board(object):
    """Board class contains """

    def __init__(self):
        board = []
        for y in xrange(8):
            row = []
            for x in xrange(8):
                row.append(None)
            board.append(row)
        self.board = board

    def is_in_check(color):
        pass

    def setup_board(self):
        colors = ["white", "black"]
        pieces = [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook]
        for color in colors:
            # Sets up rows of pawns in appropriate spaces
            if color == "white":
                y = 1
            else:
                y = 6
            for x in xrange(8):
                pawn = Pawn(color)
                pawn.place_on_board(self, (y, x))
            # Place rows 0 and 7
            if color == "white":
                y = 0
            else:
                y = 7
            for x, piece in enumerate(pieces):
                curr_piece = piece(color)
                curr_piece.place_on_board(self, (y, x))


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
        return self.name


class Pawn(Piece):
    """Inherits from Piece. Represents a Pawn"""
    name =


class Knight(Piece):
    """Inherits from Piece. Represents a Knight."""


class Bishop(Piece):
    """Inherits from Piece. Represents a Bishop."""


class Rook(Piece):
    """Inherits from Piece. Represents a Rook."""


class Queen(Piece):
    """Inherits from Piece. Represents a Queen."""


class King(Piece):
    """Inherits from Piece. Represents a King."""
