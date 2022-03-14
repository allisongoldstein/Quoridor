import pygame
from quoridor.constants import *
from quoridor.board import Board


FPS = 60

WIN = pygame.display.set_mode((TOTAL_WIDTH, TOTAL_HEIGHT))
pygame.display.set_caption('Quoridor')


def pawn_row_col_from_mouse(pos):
    y, x = pos
    row = (x // SQUARE_SIZE) - 1
    col = (y // SQUARE_SIZE) - 1
    return row, col

def fence_row_col_from_mouse(pos):
    y, x = pos
    for i in range(len(F_RANGES)):
        if x in range(F_RANGES[i][0], F_RANGES[i][1]):
            x = i + 1
        if y in range(F_RANGES[i][0], F_RANGES[i][1]):
            y = i + 1
    if x > ROWS-1 and y > ROWS-1 or (x < ROWS and y < ROWS):
        print("not a fence")
        return False
    elif x > 10:
        x = (x // SQUARE_SIZE) - 1
        if x >= ROWS-1:
            return False
        orientation = "v"
    elif y > 10:
        y = (y // SQUARE_SIZE) - 1
        if y >= ROWS-1:
            return False
        orientation = "h"
    return x, y, orientation


def main():
    pygame.init()

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
                if board.game_status == "unfinished" and board.on_board(pos):
                    if board.move_type == "pawn":
                        row, col = pawn_row_col_from_mouse(pos)
                        if board.selected_pawn is None:
                            if board.set_selected_pawn(row, col) is False:
                                pass
                        else:
                            board.move_pawn(row, col)
                    elif board.move_type == "fence":
                        if fence_row_col_from_mouse(pos) is not False:
                            x, y, orientation = fence_row_col_from_mouse(pos)
                            board.place_fence(x, y, orientation)
                else:
                    if board.game_status == "unfinished":
                        button = board.is_button(pos)
                        if button:
                            board.set_selected_button(button)

        board.draw(WIN)
        
        pygame.display.update()

    pygame.quit()


main()
