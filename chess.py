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


class Piece(object):
    """Piece class contains universal methods for each type of piece"""

    def __init__(self, color):
        self.color = color

    def place_on_board(self, board, location):
        board.board[location[0]][location[1]] = self


