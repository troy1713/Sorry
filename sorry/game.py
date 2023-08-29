import pygame as pg
from .board import Board
from .constants import *

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = YELLOW
    
    def reset(self):
        self._init()
    
    def change_turn(self):
        if self.turn == YELLOW:
            self.turn = GREEN
        elif self.turn == GREEN:
            self.turn = RED
        elif self.turn == RED:
            self.turn = BLUE
        else:
            self.turn = YELLOW

