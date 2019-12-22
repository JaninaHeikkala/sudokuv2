import os, sys
import pygame as pg
from pygame.locals import *

white = (255, 255, 255)
black = (0, 0, 0)
grey = (180, 180, 180)

def drawButton(screen, text, y):
    pg.draw.rect(screen, grey, (45, y, 250, 40), 0)
    screen.blit(text, (55, y+10))


def mainWindow():

    pg.init()
    screen = pg.display.set_mode((350, 300))

    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        screen.fill(white)

        font = pg.font.SysFont("Arial", 75, True, False)
        sudokuText = font.render("SUDOKU", True, black)
        screen.blit(sudokuText, (45, 30))

        font2 = pg.font.SysFont("Arial", 25, False, False)
        drawButton(screen, font2.render("easy", True, black), 100)
        drawButton(screen, font2.render("medium", True, black), 160)
        drawButton(screen, font2.render("hard", True, black), 220)

        pg.display.flip()
