import pygame as pg
from .constants import *
from .peg import Peg

class Board:
    def __init__(self):
        self.edge = []
        self.yellow_start = []
        self.red_start = []
        self.green_start = []
        self.blue_start = []
        for i in range(60):
            self.edge.append(0)
        for i in range(4):
            gold_peg = Peg(GOLD, -1)
            green_peg = Peg(GREEN, -1)
            red_peg = Peg(RED, -1)
            blue_peg = Peg(BLUE, -1)
            self.yellow_start.append(gold_peg)
            self.red_start.append(red_peg)
            self.green_start.append(green_peg)
            self.blue_start.append(blue_peg)
            del gold_peg, green_peg, blue_peg, red_peg # We are NOT leaking this memory
    
    def draw_board(self, win):
        """
        Draws the game board, including the edges, circles, words.
        This took a long time to make.
        """
        win.fill(GRAY)
        pg.font.init()
        info_font = pg.font.Font(None, 34)
        start_txt = info_font.render('START', False, BLACK, None)
        start_txt_rect = start_txt.get_rect()
        home_txt = info_font.render('HOME', False, BLACK, None)
        home_txt_rect = home_txt.get_rect()

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

        # Draw the word 'START'
        start_txt_rect.center = ((4 * SQUARE_EDGE) + (SQUARE_EDGE / 2) + 1.25, (SQUARE_EDGE/3) + 2 * SQUARE_EDGE+2.5)
        win.blit(start_txt, start_txt_rect) # yellow
        start_txt_rect.center = (SCREEN_WIDTH-((SQUARE_EDGE/3) + 2 * SQUARE_EDGE+2.5), (4 * SQUARE_EDGE) + (SQUARE_EDGE / 2) + 1.25)
        win.blit(start_txt, start_txt_rect) # green
        start_txt_rect.center = (((SQUARE_EDGE/3) + 2 * SQUARE_EDGE+2.5), SCREEN_HEIGHT-((4 * SQUARE_EDGE) + (SQUARE_EDGE / 2) + 1.25))
        win.blit(start_txt, start_txt_rect) # blue
        start_txt_rect.center = (SCREEN_WIDTH-((4 * SQUARE_EDGE) + (SQUARE_EDGE / 2) + 1.25), SCREEN_HEIGHT-((SQUARE_EDGE/3) + 2 * SQUARE_EDGE+2.5))
        win.blit(start_txt, start_txt_rect) # red

        # Draw the word 'HOME'
        home_txt_rect.center = ((2 * SQUARE_EDGE) + (SQUARE_EDGE / 2) + 1.25, (SQUARE_EDGE/3) + 7 * SQUARE_EDGE+2.5)
        win.blit(home_txt, home_txt_rect) # yellow
        home_txt_rect.center = (SCREEN_WIDTH-((SQUARE_EDGE/3) + 7 * SQUARE_EDGE+2.5), (2 * SQUARE_EDGE) + (SQUARE_EDGE / 2) + 1.25)
        win.blit(home_txt, home_txt_rect) # green
        home_txt_rect.center = ((SQUARE_EDGE/3) + 7 * SQUARE_EDGE+2.5, SCREEN_HEIGHT-((2 * SQUARE_EDGE) + (SQUARE_EDGE / 2) + 1.25))
        win.blit(home_txt, home_txt_rect) # blue
        home_txt_rect.center = (SCREEN_WIDTH-((2 * SQUARE_EDGE) + (SQUARE_EDGE / 2) + 1.25), SCREEN_HEIGHT-((SQUARE_EDGE/3) + 7 * SQUARE_EDGE+2.5))
        win.blit(home_txt, home_txt_rect) # red


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
    
    def draw_pegs(self, win):
        if len(self.yellow_start) > 0:
            for i in range(len(self.yellow_start)):
                piece = self.yellow_start[i]
                match i:
                    case 0:
                        piece.draw(win, 4*SQUARE_EDGE, SQUARE_EDGE + (SQUARE_EDGE/2) + 5)
                    case 1:
                        piece.draw(win, 5*SQUARE_EDGE, SQUARE_EDGE + (SQUARE_EDGE/2) + 5)
                    case 2:
                        piece.draw(win, 4*SQUARE_EDGE, 3 * SQUARE_EDGE + 2.5)
                    case 3:
                        piece.draw(win, 5*SQUARE_EDGE, 3 * SQUARE_EDGE + 2.5)
        for i in range(60):
            if self.edge[i] != 0:
                piece = self.edge[i]
                x, y = self.find_x_y(i)
                piece.draw(win, x, y)

