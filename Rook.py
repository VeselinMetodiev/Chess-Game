from Constants import WHITE_ROOK, BLACK_ROOK, WHITE
from Piece import Piece
class Rook(Piece):
    def __init__(self, col, row, color):
        Piece.__init__(self, col, row, color)
        self.moved = False
        if color == WHITE:
            self.image = WHITE_ROOK
        else:
            self.image = BLACK_ROOK
    
    def draw(self, win):
            win.blit(self.image, (self.x - self.image.get_width()//2, self.y - self.image.get_height()//2))
    
    def valid_moves(self, board):
        moves = [] 
        
        row = self.getRow()
        col = self.getCol()
        
        for i in range(row+1,8):
            if board.get_piece(i, col) == 0:
               moves.append((i, col))
            elif board.get_piece(i, col).getColor() != self.color: #take a piece from the opponent
                moves.append((i, col))
                break
            else:
                break
        for j in range(row-1, -1, -1):
            if board.get_piece(j, col) == 0:
               moves.append((j, col))
            elif board.get_piece(j, col).getColor() != self.color: #take a piece from the opponent
                moves.append((j, col))
                break
            else:
               break
        
        for k in range(col+1,8):
            if board.get_piece(row, k) == 0:
               moves.append((row, k))
            elif board.get_piece(row, k).getColor() != self.color: #take a piece from the opponent
                moves.append((row, k))
                break
            elif board.get_piece(row, k) != 0:
               break

        for m in range(col-1, -1, -1):
            if board.get_piece(row, m) == 0:
               moves.append((row, m))
            elif board.get_piece(row, m).getColor() != self.color: #take a piece from the opponent
                moves.append((row, m))
                break
            elif board.get_piece(row, m) != 0:
               break
       

            
                  
        return moves
    
    def __repr__(self):
        if self.color == WHITE:
            return u'\u2656'
        else:
            return u'\u265C'
    
