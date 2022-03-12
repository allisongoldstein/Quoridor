import pygame
from quoridor.constants import *
from quoridor.board import Board


FPS = 60

WIN = pygame.display.set_mode((ALL_SIZE+200, ALL_SIZE))
pygame.display.set_caption('Quoridor')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = (y // SQUARE_SIZE) - 1
    col = (x // SQUARE_SIZE) - 1
    print("x", x, "y", y)
    print(row, col)
    return row, col


def main():
    run = True
    pygame.init()
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if board.on_board(pos):
                    row, col = get_row_col_from_mouse(pos)
                    if board.selected_pawn is None:
                        if board.set_selected_pawn(row, col) is False:
                            print("invalid selection")
                    else:
                        board.move_pawn(row, col)
                else:
                    
                    # if button
                    pass

        board.draw(WIN)
        
        pygame.display.update()

    pygame.quit()


main()
