import pygame
from os import sys
from Constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE, BLACK
from Game import Game
from Algorithm import get_random_move

FPS = 60

#window display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')

#get the square clicked from mouse
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def set_text(string, coordx, coordy, fontSize): #Function to set text
    pygame.font.init()
    font = pygame.font.Font(pygame.font.get_default_font(), fontSize) 
    text = font.render(string, True, WHITE) 
    textRect = text.get_rect()
    textRect.center = (coordx, coordy) 
    return (text, textRect)

def writeGame(game):
    games = open("games.txt", "a", encoding='utf-8')
    games.write("\n \n \n")
    games.write(game.printGame())
    games.close()
    

def main():
    run = True
    clock = pygame.time.Clock()
    #board = Board()
    game = Game(WIN)

    pause = False

    while run:
        clock.tick(FPS)
        

        if game.winner() != None:
            #Print who has won and wait for the user to press any key for new game
            output = game.winner() + " won the game! Press any key or quit!"
            totalText = set_text(output, HEIGHT // 2, WIDTH // 2 , 30)
            WIN.blit(totalText[0], totalText[1])
            pause = True
            pygame.display.update()
            writeGame(game) #add the game in the games.txt file
            pygame.event.clear()
            while pause:
                pygame.init()
                event = pygame.event.wait()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYUP:
                    main()

        if game.turn == WHITE:
            new_board = get_random_move(game.get_board(), WHITE, game)
            game.ai_move(new_board)
  

        #Check if any event has happened
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        if(not pause):
            game.update()

    pygame.quit()
    sys.exit()
    

main()