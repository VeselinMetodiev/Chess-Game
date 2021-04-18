import pygame
#from abc import ABC, abstractmethod
from Constants import  WHITE,SQUARE_SIZE, BLACK, BLACK_BISHOP

class Piece():
    #class attributes, for the pieces
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row 
        self.col = col
        self.color = color
        if self.color == WHITE:
            self.direction = -1 #going down
        else:
            self.direction = 1 #going up

        #coordinates and position
        self.x = 0
        self.y = 0
        self.calc_pos()
    
    def getRow(self):
        return self.row
    def getCol(self):
        return self.col
    def getColor(self):
        return self.color

    #calculate the position of each piece in pixels
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    #this should be an abstract method that will be overriden by the subclasses
    def draw(self, win):
        win.blit(BLACK_BISHOP, (self.x - BLACK_BISHOP.get_width()//2, self.y - BLACK_BISHOP.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos() #updates coordinates x, y

    def __repr__(self):
        return str(self.color)

    