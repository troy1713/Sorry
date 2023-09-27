#!usr/bin/env python
import pygame as pg
from .constants import *

class Card:
    def __init__(self, val=1):
        self.val = val
    
    def draw(self, win):
        pg.draw.rect(win, WHITE, (9*SQUARE_EDGE, 5*SQUARE_EDGE, 2*SQUARE_EDGE, 3*SQUARE_EDGE), 0, 10)
        card_font = pg.font.Font(None, 64)
        if self.val != -1:
            card_txt = card_font.render(str(self.val), False, BLACK, None)
        else:
            card_txt = card_font.render('SRY', False, BLACK, None)
        card_txt_rect = card_txt.get_rect()
        card_txt_rect.center = (10*SQUARE_EDGE, 6.5*SQUARE_EDGE)
        win.blit(card_txt, card_txt_rect)
    
    def __repr__(self):
        return "Card of value " + str(self.val)