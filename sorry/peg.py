import pygame as pg
from .constants import GOLD, GREEN, RED, BLUE, SQUARE_EDGE

class Peg:
    PIECE_RADIUS = (SQUARE_EDGE) * 0.35
    
    def __init__(self, color=GOLD, value=-1, x=0, y=0):
        self.color = color
        self.value = value
        self.safe = True
        self.home = False
    
    def draw(self, win, x, y):
        pg.draw.circle(win, self.color, (x, y), self.PIECE_RADIUS)
    
    def move(self, value):
        self.value = value
        if value == -1:
            self.safe = True
        elif value > 99:
            self.safe = True
    
    def __repr__(self):
        return str(self.color) + " peg at " + str(self.value)
    