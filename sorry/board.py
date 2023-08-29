import pygame as pg
from .constants import *
from .peg import Peg

class Board:
    def __init__(self):
        self.edge = []
        self.yellow_start = 4
        self.red_start = 4
        self.green_start = 4
        self.blue_start = 4
        for i in range(60):
            self.edge.append(0)
    
    def draw_board(self, win):
        win.fill(GRAY)

        # Draw outer grid (60 tiles)
        pg.draw.rect(win, LIGHT_GRAY, (0, 15 * SQUARE_EDGE, SQUARE_EDGE * 15, SQUARE_EDGE)) # bottom
        pg.draw.rect(win, LIGHT_GRAY, (15 * SQUARE_EDGE, 0, SQUARE_EDGE, SQUARE_EDGE * 15)) # right
        pg.draw.rect(win, LIGHT_GRAY, (0, 0, SQUARE_EDGE * 15, SQUARE_EDGE)) # top
        pg.draw.rect(win, LIGHT_GRAY, (0, 0, SQUARE_EDGE, SQUARE_EDGE * 15)) # left
        pg.draw.rect(win, LIGHT_GRAY, (15 * SQUARE_EDGE, 15 * SQUARE_EDGE, SQUARE_EDGE, SQUARE_EDGE)) # bottom right

        for i in range(15):
            pg.draw.rect(win, WHITE, (2.5, i * SQUARE_EDGE+2.5, SQUARE_EDGE-5, SQUARE_EDGE-5), 0, 3) # Left edge
            pg.draw.rect(win, WHITE, (i * SQUARE_EDGE+2.5, 2.5, SQUARE_EDGE-5, SQUARE_EDGE-5), 0, 3) # Top edge
            pg.draw.rect(win, WHITE, (15 * SQUARE_EDGE+2.5, i * SQUARE_EDGE+2.5, SQUARE_EDGE-5, SQUARE_EDGE-5), 0, 3) # Right edge
            pg.draw.rect(win, WHITE, (i * SQUARE_EDGE+2.5, 15 * SQUARE_EDGE+2.5, SQUARE_EDGE-5, SQUARE_EDGE-5), 0, 3) # Bottom edge
        
        pg.draw.rect(win, WHITE, (15 * SQUARE_EDGE+2.5, 15 * SQUARE_EDGE+2.5, SQUARE_EDGE-5, SQUARE_EDGE-5), 0, 3)

        # Draw safety zones
        pg.draw.rect(win, LIGHT_GRAY, (2*SQUARE_EDGE, SQUARE_EDGE, SQUARE_EDGE, SQUARE_EDGE*5)) #y
        pg.draw.rect(win, LIGHT_GRAY, (10*SQUARE_EDGE, 2*SQUARE_EDGE, SQUARE_EDGE*5, SQUARE_EDGE)) #g
        pg.draw.rect(win, LIGHT_GRAY, (SQUARE_EDGE, 13*SQUARE_EDGE, SQUARE_EDGE*5, SQUARE_EDGE), 0, 3) #b
        pg.draw.rect(win, LIGHT_GRAY, (13*SQUARE_EDGE, 10*SQUARE_EDGE, SQUARE_EDGE, SQUARE_EDGE*5), 0, 3) #r
        for i in range(1, 6):
            pg.draw.rect(win, WHITE, ((2 * SQUARE_EDGE) + 2.5, i * SQUARE_EDGE+2.5, SQUARE_EDGE-5, SQUARE_EDGE-5), 0, 3) #y
            pg.draw.rect(win, WHITE, (((i+9) * SQUARE_EDGE) + 2.5, 2 * SQUARE_EDGE+2.5, SQUARE_EDGE-5, SQUARE_EDGE-5), 0, 3) #g
            pg.draw.rect(win, WHITE, ((i * SQUARE_EDGE) + 2.5, 13 * SQUARE_EDGE+2.5, SQUARE_EDGE-5, SQUARE_EDGE-5), 0, 3) #b
            pg.draw.rect(win, WHITE, ((13 * SQUARE_EDGE) + 2.5, (i+9) * SQUARE_EDGE+2.5, SQUARE_EDGE-5, SQUARE_EDGE-5), 0, 3) #r

        # Starting circles
        pg.draw.circle(win, YELLOW, ((4 * SQUARE_EDGE) + (SQUARE_EDGE / 2) + 1.25, (SQUARE_EDGE/3) + 2 * SQUARE_EDGE+2.5), (1.5*SQUARE_EDGE))
        pg.draw.circle(win, GREEN, (SCREEN_WIDTH-((SQUARE_EDGE/3) + 2 * SQUARE_EDGE+2.5), (4 * SQUARE_EDGE) + (SQUARE_EDGE / 2) + 1.25), (1.5*SQUARE_EDGE))
        pg.draw.circle(win, BLUE, (((SQUARE_EDGE/3) + 2 * SQUARE_EDGE+2.5), SCREEN_HEIGHT-((4 * SQUARE_EDGE) + (SQUARE_EDGE / 2) + 1.25)), (1.5*SQUARE_EDGE))
        pg.draw.circle(win, RED, (SCREEN_WIDTH-((4 * SQUARE_EDGE) + (SQUARE_EDGE / 2) + 1.25), SCREEN_HEIGHT-((SQUARE_EDGE/3) + 2 * SQUARE_EDGE+2.5)), (1.5*SQUARE_EDGE))

        # Home circles
        pg.draw.circle(win, YELLOW, ((2 * SQUARE_EDGE) + (SQUARE_EDGE / 2) + 1.25, (SQUARE_EDGE/3) + 7 * SQUARE_EDGE+2.5), (1.5*SQUARE_EDGE))
        pg.draw.circle(win, GREEN, (SCREEN_WIDTH-((SQUARE_EDGE/3) + 7 * SQUARE_EDGE+2.5), (2 * SQUARE_EDGE) + (SQUARE_EDGE / 2) + 1.25), (1.5*SQUARE_EDGE))
        pg.draw.circle(win, BLUE, ((SQUARE_EDGE/3) + 7 * SQUARE_EDGE+2.5, SCREEN_HEIGHT-((2 * SQUARE_EDGE) + (SQUARE_EDGE / 2) + 1.25)), (1.5*SQUARE_EDGE))
        pg.draw.circle(win, RED, (SCREEN_WIDTH-((2 * SQUARE_EDGE) + (SQUARE_EDGE / 2) + 1.25), SCREEN_HEIGHT-((SQUARE_EDGE/3) + 7 * SQUARE_EDGE+2.5)), (1.5*SQUARE_EDGE))

        # Yellow triangle polygon coords
        #ylw_triangle = [((2*sqr_edge) + 2.5, 6 * sqr_edge+2.5), ]
        #pg.draw.polygon(screen, white, ylw_triangle) 

    def add_peg(self, value, Peg):
        self.edge[value] = Peg
    
    def find_x_y(self, val):
        half_sqr = (SQUARE_EDGE-5) / 2
        if val < 16: # top
            x = half_sqr + val*SQUARE_EDGE + 2.5
            y = 2.5 + half_sqr
            return x, y
        elif val >= 16 and val < 30: # right
            val -= 16
            x = 15 * SQUARE_EDGE + 2.5 + half_sqr
            y = val * SQUARE_EDGE + 2.5 + half_sqr + SQUARE_EDGE
            return x, y
        elif val >= 30 and val <= 44: # bottom
            new_pos = ((37 - val) * 2) + val
            new_pos -= 30
            val = new_pos
            x = val*SQUARE_EDGE + 2.5 + half_sqr + SQUARE_EDGE
            y = 15 * SQUARE_EDGE + 2.5 + half_sqr
            return x, y
        else: # left
            new_pos = ((52 - val) * 2) + val
            new_pos -= 45
            val = new_pos
            x = 2.5 + half_sqr
            y = 2.5 + val*SQUARE_EDGE + half_sqr + SQUARE_EDGE
            return x, y
    
    def draw_edge(self, win):
        for i in range(60):
            if self.edge[i] != 0:
                piece = self.edge[i]
                x, y = self.find_x_y(i)
                piece.draw(win, x, y)

