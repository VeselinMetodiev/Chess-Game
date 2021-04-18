import pygame
from Constants import BLACK, ROWS, SQUARE_SIZE, COLS, WHITE, GREY, BLACK
from Piece import Piece
from King import King
from Queen import Queen
from Knight import Knight
from Bishop import Bishop
from Rook import Rook
from Pawn import Pawn

class Board:
    def __init__(self):
        self.board = []
        self.notation = ""
        self.numberOfMoves = 0
        self.black_pieces_left = self.white_pieces_left = 16
        self.create_board_fisher()
    
    def printBoard(self):
        return self.board
    
    def getBoard(self):
        return self.board

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, GREY, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) #x,y, width, height of the rect
    
    def evaluate(self):
        return self.white_pieces_left - self.black_pieces_left + 10
    
    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces


    def move(self, piece, row, col):
        #delete the piece from where it is and move its position
        if self.board[row][col] != 0 and self.board[row][col].getColor() != piece.getColor():
            self.remove(self.board[row][col])
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col] #swap positions
        piece.move(row, col)
        if isinstance(piece, King): #for castling
            if piece.getColor() == BLACK and piece.getRow() == 7 and col == 1: #black
                #short castle
                if self.board[7][0].moved == False:
                    self.board[7][0].move(7,2)
                    self.board[7][0], self.board[7][2] = self.board[7][2], self.board[7][0] #swap positions
            elif piece.getColor() == BLACK and piece.getRow() == 7 and col == 5:
                #long castle
                if self.board[7][7].moved == False:
                    self.board[7][7].move(7,4)
                    self.board[7][7], self.board[7][4] = self.board[7][4], self.board[7][7] #swap positions
            if piece.getColor == WHITE and piece.getRow() == 0 and col == 1: #white
                #short castle
                if self.board[0][0].moved == False:
                    self.board[0][0].move(0,2)
                    self.board[0][0], self.board[0][2] = self.board[0][2], self.board[0][0] #swap positions
            elif piece.getColor == WHITE and piece.getRow() == 0 and col == 5:
                #long castle
                if self.board[0][7].moved == False:
                    self.board[0][7].move(0,4)
                    self.board[0][7], self.board[0][4] = self.board[0][4], self.board[0][7] #swap positions
                piece.moved = True
        if isinstance(piece, Rook) or isinstance(piece, King): #for castling
            piece.moved = True
        letter = ord('h') - col

        if(self.numberOfMoves % 2 == 0):
            moving = str((self.numberOfMoves // 2) + 1) + "." + str(piece) + chr(letter) + str(row+1) + " "
        else:
            moving = ", " + str(piece) + chr(letter) + str(row+1) + "\n"
        self.notation += moving
        self.numberOfMoves += 1
    
    def get_piece(self, row, col):
        return self.board[row][col]


    #add the pieces - the normal starting position
    def create_board(self):
        for row in range(ROWS):
            self.board.append([]) #list represents what each row has
            for col in range(COLS):
                    if row == 0:
                        if col == 0 or col == COLS-1:
                            self.board[row].append(Rook(row, col, WHITE))
                        elif col == 1 or col == COLS-2:
                            self.board[row].append(Knight(row, col, WHITE))
                        elif col == 2 or col == COLS-3:
                            self.board[row].append(Bishop(row, col, WHITE))
                        elif col == 3:
                            self.board[row].append(King(row, col, WHITE))
                        elif col == 4:
                            self.board[row].append(Queen(row, col, WHITE))
                    elif row == 1:
                        self.board[row].append(Pawn(row, col, WHITE))
                    elif row == ROWS-2:
                        self.board[row].append(Pawn(row, col, BLACK))
                    elif row == ROWS-1:
                        if col == 0 or col == COLS-1:
                            self.board[row].append(Rook(row, col, BLACK))
                        elif col == 1 or col == COLS-2:
                            self.board[row].append(Knight(row, col, BLACK))
                        elif col == 2 or col == COLS-3:
                            self.board[row].append(Bishop(row, col, BLACK))
                        elif col == 3:
                            self.board[row].append(King(row, col, BLACK))
                        elif col == 4:
                            self.board[row].append(Queen(row, col, BLACK))
                    else:
                        self.board[row].append(0)

    def appendPiece(self, row, col, color, listPieces):
        if listPieces[col] == "Rook":
            if(color == "White"):
                self.board[row].append(Rook(row, col, WHITE))
            else:
                self.board[row].append(Rook(row, col, BLACK))
        elif listPieces[col] == "Knight":
            if(color == "White"):
                self.board[row].append(Knight(row, col, WHITE))
            else:
                self.board[row].append(Knight(row, col, BLACK))
        elif listPieces[col] == "Bishop":
            if(color == "White"):
                self.board[row].append(Bishop(row, col, WHITE))
            else:
                self.board[row].append(Bishop(row, col, BLACK))
        elif listPieces[col] == "King":
            if(color == "White"):
                self.board[row].append(King(row, col, WHITE))
            else:
                self.board[row].append(King(row, col, BLACK))
        elif listPieces[col] == "Queen":
            if(color == "White"):
                self.board[row].append(Queen(row, col, WHITE))
            else:
                self.board[row].append(Queen(row, col, BLACK))

        #add the pieces from the text file
    def create_board_fisher(self):
        pieces = open("start.txt", 'r')
        listPieces = pieces.read().split(' ')
        
        for row in range(ROWS):
            self.board.append([]) #list represents what each row has
            for col in range(COLS):
                    if row == 0:
                        self.appendPiece(row, col, "White", listPieces)
                    elif row == 1:
                        self.board[row].append(Pawn(row, col, WHITE))
                    elif row == ROWS-2:
                        self.board[row].append(Pawn(row, col, BLACK))
                    elif row == ROWS-1:
                        self.appendPiece(row, col, "Black", listPieces)
                    else:
                        self.board[row].append(0)
        
        #draw all of the pieces and squares
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    if isinstance(piece, Pawn):
                        if row == 7 and piece.color == WHITE:
                            self.board[row][col] = Queen(row, col, WHITE)
                            piece = Queen(row, col, WHITE)
                        elif row == 0 and piece.color == BLACK:
                            self.board[row][col] = Queen(row, col, BLACK)
                            piece = Queen(row, col, BLACK)
                    piece.draw(win)
    
    #Removes a piece from the board when it is captured
    def remove(self, piece):
        if piece.color == BLACK:
            self.black_pieces_left -= 1
            if(isinstance(piece, King)):
                self.black_pieces_left = 0
                print(self.black_pieces_left)
        else:
            self.white_pieces_left -= 1
            if(isinstance(piece, King)):
                self.white_pieces_left = 0
                print(self.white_pieces_left)
        self.board[piece.row][piece.col] = 0
    
    def winner(self):
        if self.black_pieces_left <= 0:
            self.notation += "   1 :    0" #print result in text file
            return "WHITE"
        elif self.white_pieces_left <= 0:
            self.notation += "   0 :    1" 
            return "BLACK"
        
        return None

    def get_valid_moves(self, piece):
        moves = [] 
        moves = piece.valid_moves(self)
        return moves