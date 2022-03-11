import pygame
from quoridor.constants import *
from quoridor.board import Board


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Quoridor')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE - 1
    col = x // SQUARE_SIZE - 1
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)

                if board.selected_pawn is None:
                    pawn = board.get_pawn(row, col)
                    if board.set_selected_pawn(pawn, row, col) is False:
                        print("invalid selection")
                else:
                    board.move_pawn(row, col)


        board.draw(WIN)
        
        pygame.display.update()

    pygame.quit()


main()
