import pygame as pg
from .peg import Peg

class Player:
    def __init__(self, color):
        self.color = color
        self.pegs = []
        for i in range(4):
            peg = Peg(color, -1)
            self.pegs.append(peg)