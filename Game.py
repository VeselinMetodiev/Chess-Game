import pygame
from Constants import BLACK, WHITE, SQUARE_SIZE, BLUE
from Board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
    
    def reset(self):
        self._init()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = []
    
    def winner(self):
        return self.board.winner()

    def get_board(self):
        return self.board

     #determines whether or not we should move sth
    def select(self, row, col): #when you select sth, select a piece - you may want to move it, or select different piece
        if self.selected:
            result = self._move(row, col) #try to move what we selected to whatever row and col we pass
            if not result: #invalid move - reselect
                self.selected = None 
                self.valid_moves = {} #delete the valid moves since the user has to click again to move a piece
                self.select(row, col) #try to reselect different piece
        else:
            piece = self.board.get_piece(row, col) #get the piece on that row, col
            if piece != 0 and piece.color == self.turn: #select the piece if it's your turn
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece) #each piece should have a method to compute the valid moves
                #print(self.valid_moves)
                return True #selection was valid
            
        return False #selection is not valid

    def _move(self, row, col):
        piece = self.board.get_piece(row, col) #get the piece
        #print((row, col) in self.valid_moves)
        if self.selected and (piece == 0 or piece.getColor() != self.turn) and (row, col) in self.valid_moves: #we can't move to a square that is already occupied by our piece
            if piece != 0 and piece.getColor() != self.turn:
                self.board.remove(piece)
            self.board.move(self.selected, row, col) #move the piece
            self.change_turn()
            #print(self.board.printBoard())
        else:
            return False

        return True
    
    def printGame(self):
        return self.board.notation
    
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)
    
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

    def ai_move(self, board):
        self.board = board
        self.change_turn()