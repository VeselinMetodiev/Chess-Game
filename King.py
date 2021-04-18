from Constants import WHITE_KING, BLACK_KING, WHITE
from Piece import Piece
from Rook import Rook
import pygame

class King(Piece):
    def __init__(self, col, row, color):
        Piece.__init__(self,col, row, color)
        self.moved = False
        if color == WHITE:
            self.image = WHITE_KING
        else:
            self.image = BLACK_KING
    
    def draw(self, win):
        if self.image != None:
            win.blit(self.image, (self.x - self.image.get_width()//2, self.y - self.image.get_height()//2))
        
    def valid_moves(self, board):
        moves = []

        row = self.getRow()
        col = self.getCol()

        if row+1 < 8 and col+1 < 8 and (board.get_piece(row+1, col+1) == 0 or board.get_piece(row+1, col+1).getColor() != self.color):
            moves.append((row+1, col+1))
        if row+1 < 8 and (board.get_piece(row+1, col) == 0 or board.get_piece(row+1, col).getColor() != self.color):
            moves.append((row+1, col))
        if col+1 < 8 and (board.get_piece(row, col+1) == 0 or board.get_piece(row, col+1).getColor() != self.color):
            moves.append((row, col+1))
        if row-1 > -1 and col-1 > -1 and (board.get_piece(row-1, col-1) == 0 or board.get_piece(row-1, col-1).getColor() != self.color):
            moves.append((row-1, col-1))
        if row-1 > -1 and (board.get_piece(row-1, col) == 0 or board.get_piece(row-1, col).getColor() != self.color):
            moves.append((row-1, col))
        if col-1 > -1 and (board.get_piece(row, col-1) == 0 or board.get_piece(row, col-1).getColor() != self.color):
            moves.append((row, col-1))
        if row+1 < 8 and col-1 > -1 and (board.get_piece(row+1, col-1) == 0 or board.get_piece(row+1, col-1).getColor() != self.color):
            moves.append((row+1, col-1))
        if row-1 > -1 and col+1 < 8 and (board.get_piece(row-1, col+1) == 0 or board.get_piece(row-1, col+1).getColor() != self.color):
            moves.append((row-1, col+1))
        
        #short castle
        if not self.moved and isinstance(board.get_piece(self.row,self.col-3), Rook) and board.get_piece(self.row,self.col-3) != 0 and not board.get_piece(self.row,self.col-3).moved and (board.get_piece(row, col-1) == 0 and board.get_piece(row, col-2) == 0): 
            moves.append((row, col-2))

        #long castle
        if not self.moved and isinstance(board.get_piece(self.row,self.col-3), Rook) and board.get_piece(self.row,self.col+4) != 0 and not board.get_piece(self.row,self.col+4).moved and (board.get_piece(row, col+1) == 0 and board.get_piece(row, col+2) == 0 and board.get_piece(row, col+3) == 0):
            moves.append((row, col+2))
        

        return moves
    def __repr__(self):
        if self.color == WHITE:
            return u'\u2654'
        else:
            return u'\u265A'
