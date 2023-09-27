#!usr/bin/env python
from .constants import *
from .card import Card
import random
import pygame as pg

class Deck:
    def __init__(self):
        self.cards = []
        self.flipped_cards = []
        for k in range(1, 13, 1):
            if k == 1:
                for i in range(5):
                    self.cards.append(Card(1))
            elif k == 6 or k == 9:
                continue
            else:
                for i in range(4):
                    self.cards.append(Card(k))
        for i in range(4):
            self.cards.append(Card(-1))
        self.shuffle()
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self, win):
        if len(self.cards) > 0:
            pg.draw.rect(win, ORANGE, (5*SQUARE_EDGE, 5*SQUARE_EDGE, 2*SQUARE_EDGE, 3*SQUARE_EDGE), 0, 10)
        if len(self.flipped_cards) > 0:
            self.flipped_cards[-1].draw(win)
    
    def flip_card(self, win):
        card_flipped = self.cards.pop()
        self.flipped_cards.append(card_flipped)
    
    def __repr__(self):
        return "Flipped cards: " + str(self.flipped_cards) + "\n" + "Remaining deck: " + str(self.cards)
    
