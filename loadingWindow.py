from time import sleep

import pygame as pg

def loadingWindow():
    pg.init()
    screen = pg.display.set_mode((200, 70))
    run = True
    while run:
        font = pg.font.SysFont("Arial", 50)
        loadingText = font.render("Loading", True, (0, 0, 0))
        screen.blit(loadingText, (20, 20))
        for i in range(1,4):
            if i%3 == 0:
                screen.fill((255, 255, 255))
            dotText = font.render(".", True, (0, 0, 0))
            screen.blit(dotText, (50 + i*20, 20))
            sleep(1000)

        pg.display.flip()