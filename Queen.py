from Constants import WHITE_QUEEN, BLACK_QUEEN, WHITE
from Piece import Piece
from Bishop import Bishop
from Rook import Rook
class Queen(Piece):
    def __init__(self, col, row, color):
        Piece.__init__(self,col, row, color)
        if color == WHITE:
            self.image = WHITE_QUEEN
        else:
            self.image = BLACK_QUEEN
    
    def draw(self, win):
            win.blit(self.image, (self.x - self.image.get_width()//2, self.y - self.image.get_height()//2))
    
    def valid_moves(self, board):
        moves = []
        row = self.getRow()
        col = self.getCol()
        
        bishop = Bishop(row, col, self.color)
        moves.extend(bishop.valid_moves(board))
        rook = Rook(row, col, self.color)
        moves.extend(rook.valid_moves(board))

        return moves

    def __repr__(self):
        if self.color == WHITE:
            return u'\u2655'
        else:
            return u'\u265B'   
    
