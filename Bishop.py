from Constants import WHITE_BISHOP, BLACK_BISHOP, WHITE
from Piece import Piece
class Bishop(Piece):
    def __init__(self, col, row, color):
        Piece.__init__(self,col, row, color)
        if color == WHITE:
            self.image = WHITE_BISHOP
        else:
            self.image = BLACK_BISHOP
    
    def draw(self, win):
            win.blit(self.image, (self.x - self.image.get_width()//2, self.y - self.image.get_height()//2))
    
    def valid_moves(self, board):
        moves = [] 
        
        row = self.getRow()
        col = self.getCol()
        
        count = 1
        for i in range(row+1,8):
            if col - count > -1 and board.get_piece(i, col-count) == 0:
               moves.append((i, col-count))
               count += 1
            elif col - count > -1 and board.get_piece(i, col-count).getColor() != self.color: #take a piece from the opponent
                moves.append((i, col-count))
                break
            else:
                break
            
        count = 1
        for j in range(row-1, -1, -1):
            if col + count < 8 and board.get_piece(j, col+count) == 0:
               moves.append((j, col + count))
               count +=1
            elif col + count < 8 and board.get_piece(j, col+count).getColor() != self.color: #take a piece from the opponent
                moves.append((j, col+count))
                break
            else:
               break
        
        count = 1
        for l in range(row-1, -1, -1):
            if col - count > -1 and board.get_piece(l, col-count) == 0:
               moves.append((l, col - count))
               count +=1
            elif col - count > -1 and board.get_piece(l, col-count).getColor() != self.color: #take a piece from the opponent
                moves.append((l, col-count))
                break
            else:
               break
        
        count = 1
        for k in range(row+1, 8):
            if col + count < 8 and board.get_piece(k, col+count) == 0:
                moves.append((k, col + count))
                count += 1
            elif col + count < 8 and board.get_piece(k, col+count).getColor() != self.color: #take a piece from the opponent
                moves.append((k, col + count))
                break
            else:
                break


        return moves

    def __repr__(self):
        if self.color == WHITE:
            return u'\u2657'
        else:
            return u'\u265D'
    
    
