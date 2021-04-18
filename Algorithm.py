import pygame
import random

def get_random_move(board, color, game):
    move = None

    pieces = board.get_all_pieces(color)
    rand = random.randint(0, len(pieces)-1)
    randomPiece = pieces[rand]
    valid_moves = board.get_valid_moves(randomPiece)
    while len(valid_moves) == 0:  #sometimes it chooses a piece that does not have valid moves
        pieces = board.get_all_pieces(color) #so choose a different piece until a piece that has valid moves is chosen
        rand = random.randint(0, len(pieces)-1)
        randomPiece = pieces[rand]
        valid_moves = board.get_valid_moves(randomPiece)
    rand = random.randint(0, len(valid_moves)-1)
    randMove = valid_moves[rand]

    draw_moves(game, board, randomPiece)

    temp_piece = board.get_piece(randomPiece.row, randomPiece.col)
    if game.winner() != "BLACK":
        move = make_move(temp_piece, randMove, board, game) 
    
    return move

def make_move(piece, move, board, game):
    board.move(piece, move[0], move[1])
    return board

def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    pygame.display.update()
    pygame.time.delay(500)