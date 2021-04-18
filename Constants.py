import pygame
#pixels
WIDTH, HEIGHT = 700, 700

#matrix
ROWS, COLS = 8, 8

#How big is each square of the chessboard
SQUARE_SIZE = WIDTH//COLS

#RGB
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0,0,0)
GREY = (128,128,128)
RED = (255, 0, 0)
BLUE = (0,0,255)

#pieces
BLACK_BISHOP = pygame.transform.scale(pygame.image.load(r'pieces\bb.png'), (80,80))
BLACK_ROOK = pygame.transform.scale(pygame.image.load(r'pieces\br.png'), (80,80))
BLACK_KNIGHT = pygame.transform.scale(pygame.image.load(r'pieces\bn.png'), (80,80))
BLACK_QUEEN = pygame.transform.scale(pygame.image.load(r'pieces\bq.png'), (80,80))
BLACK_PAWN = pygame.transform.scale(pygame.image.load(r'pieces\bp.png'), (80,80))
BLACK_KING = pygame.transform.scale(pygame.image.load(r'pieces\bk.png'), (80,80))
WHITE_BISHOP = pygame.transform.scale(pygame.image.load(r'pieces\wb.png'), (80,80))
WHITE_ROOK = pygame.transform.scale(pygame.image.load(r'pieces\wr.png'), (80,80))
WHITE_KNIGHT = pygame.transform.scale(pygame.image.load(r'pieces\wn.png'), (80,80))
WHITE_QUEEN = pygame.transform.scale(pygame.image.load(r'pieces\wq.png'), (80,80))
WHITE_PAWN = pygame.transform.scale(pygame.image.load(r'pieces\wp.png'), (80,80))
WHITE_KING = pygame.transform.scale(pygame.image.load(r'pieces\wk.png'), (80,80))