from Constants import WHITE_KNIGHT, BLACK_KNIGHT, WHITE
from Piece import Piece
import pygame
class Knight(Piece):
    def __init__(self, col, row, color):
        Piece.__init__(self,col, row, color)
        if color == WHITE:
            self.image = WHITE_KNIGHT
        else:
            self.image = BLACK_KNIGHT
    
    def draw(self, win):
                win.blit(self.image, (self.x - self.image.get_width()//2, self.y - self.image.get_height()//2))

    def valid_moves(self, board):
        moves = []

        row = self.getRow()
        col = self.getCol()

        if row+2 < 8 and col+1 < 8 and (board.get_piece(row+2, col+1) == 0 or board.get_piece(row+2, col+1).getColor() != self.color):
            moves.append((row+2, col+1))
        if row+2 < 8 and col-1 > -1 and (board.get_piece(row+2, col-1) == 0 or board.get_piece(row+2, col-1).getColor() != self.color):
            moves.append((row+2, col-1))
        if row+1 < 8 and col+2 < 8 and (board.get_piece(row+1, col+2) == 0 or board.get_piece(row+1, col+2).getColor() != self.color):
            moves.append((row+1, col+2))
        if row+1 < 8 and col-2 > -1 and (board.get_piece(row+1, col-2) == 0 or board.get_piece(row+1, col-2).getColor() != self.color):
            moves.append((row+1, col-2))
        if row-1 > -1 and col+2 < 8 and (board.get_piece(row-1, col+2) == 0 or board.get_piece(row-1, col+2).getColor() != self.color):
            moves.append((row-1, col+2))
        if row-1 > -1 and col-2 > -1 and (board.get_piece(row-1, col-2) == 0 or board.get_piece(row-1, col-2).getColor() != self.color):
            moves.append((row-1, col-2))
        if row-2 > -1 and col+1 < 8 and (board.get_piece(row-2, col+1) == 0 or board.get_piece(row-2, col+1).getColor() != self.color):
            moves.append((row-2, col+1))
        if row-2 > -1 and col-1 < 8 and (board.get_piece(row-2, col-1) == 0 or board.get_piece(row-2, col-1).getColor() != self.color):
            moves.append((row-2, col-1))
        
        return moves
        
    def __repr__(self):
        if self.color == WHITE:
            return u'\u2658'
        else:
            return u'\u265E'
