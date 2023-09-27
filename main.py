#!usr/bin/env python
"""
The board game Sorry!

"""

import pygame as pg
from sorry.constants import *
from sorry.board import Board
from sorry.peg import Peg
from sorry.deck import Deck
from sorry.card import Card

WIN = pg.display.set_mode((720, 720), pg.SCALED)
FPS = 60

def main():
    pg.display.set_caption("Sorry! game")

    clock = pg.time.Clock()
    playing = True
    board = Board()
    deck= Deck()

    while playing:
        clock.tick(FPS)

        # Handle input events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                playing = False
            
            if event.type == pg.MOUSEBUTTONDOWN:
                deck.flip_card(WIN)
        
        board.draw_board(WIN)
        x = (SQUARE_EDGE-5)/2 +2.5
        y = (SQUARE_EDGE-5)/2 +2.5
        peg = Peg(DARK_RED)
        board.edge[20] = peg
        #board.edge[58] = peg
        #peg.draw(WIN, x, y)
        board.draw_pegs(WIN)
        deck.draw(WIN)

        pg.display.update()

    pg.quit()

if __name__ == "__main__":
    main()
