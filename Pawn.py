from Constants import WHITE_PAWN, BLACK_PAWN, WHITE
from Piece import Piece
from Queen import Queen
import pygame
class Pawn(Piece):
    def __init__(self, col, row, color):
        Piece.__init__(self,col, row, color)
        if color == WHITE:
            self.image = WHITE_PAWN
        else:
            self.image = BLACK_PAWN
    
    def draw(self, win):
            win.blit(self.image, (self.x - self.image.get_width()//2, self.y - self.image.get_height()//2))

    
    def valid_moves(self, board):
        moves = [] 
        if 0 == 0:
            row = self.getRow()
            col = self.getCol()
            piece1, piece2 = None, None
            if self.color == WHITE:
                if board.get_piece(row+1, col) == 0:
                    moves.append((row+1, col))
                    if row == 1 and board.get_piece(row+2, col) == 0:
                        moves.append((row+2, col))
            
                if col > 0:
                    piece1 = board.get_piece(row+1, col-1)
                if col < 7:
                    piece2 = board.get_piece(row+1, col+1)
                if piece1 != 0 and col > 0 and piece1.getColor() != self.color:
                    moves.append((row+1, col-1))
                if piece2 != 0 and col < 7 and piece2.getColor() != self.color:
                    moves.append((row+1, col+1))
            else:
                if board.get_piece(row-1, col) == 0:
                    moves.append((row-1, col))
                    if row == 6 and board.get_piece(row-2, col) == 0:
                        moves.append((row-2, col))

                if col > 0:
                    piece1 = board.get_piece(row-1, col-1)
                if col < 7 and row:
                    piece2 = board.get_piece(row-1, col+1)
                if piece1 != 0 and col > 0 and piece1.getColor() != self.color:
                    moves.append((row-1, col-1))
                if piece2 != 0 and col < 7 and piece2.getColor() != self.color:
                    moves.append((row-1, col+1))
        return moves

    def __repr__(self):
        if self.color == WHITE:
            return u'\u2659'
        else:
            return u'\u265F'
    
