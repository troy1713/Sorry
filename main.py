#!usr/bin/env python
"""
The board game Sorry!

"""

import pygame as pg
from sorry.constants import *
from sorry.board import Board
from sorry.peg import Peg

WIN = pg.display.set_mode((720, 720), pg.SCALED)
FPS = 60

def main():
    pg.display.set_caption("Sorry! game")

    clock = pg.time.Clock()
    playing = True
    board = Board()

    while playing:
        clock.tick(FPS)

        # Handle input events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                playing = False
            
            if event.type == pg.MOUSEBUTTONDOWN:
                pass
        
        board.draw_board(WIN)
        x = (SQUARE_EDGE-5)/2 +2.5
        y = (SQUARE_EDGE-5)/2 +2.5
        peg = Peg()
        board.edge[59] = peg
        #board.edge[58] = peg
        #peg.draw(WIN, x, y)
        board.draw_edge(WIN)

        pg.display.update()

    pg.quit()

if __name__ == "__main__":
    main()
