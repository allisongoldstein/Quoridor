import pygame
from quoridor.constants import *
from quoridor.board import Board


FPS = 60

WIN = pygame.display.set_mode((TOTAL_WIDTH, TOTAL_HEIGHT))
pygame.display.set_caption('Quoridor')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = (y // SQUARE_SIZE) - 1
    col = (x // SQUARE_SIZE) - 1
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
                            pass
                    else:
                        board.move_pawn(row, col)
                else:
                    button = board.is_button(pos)
                    if button:
                        board.set_selected_button(button)

        board.draw(WIN)
        
        pygame.display.update()

    pygame.quit()


main()
