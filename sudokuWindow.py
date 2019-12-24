import pygame as pg

white = (255, 255, 255)
black = (0, 0, 0)
grey = (180, 180, 180)

def drawLines(screen):
    for i in range(50, 500, 50):
        pg.draw.line(screen, black, (i, 0), (i, 450), 1)
        pg.draw.line(screen, black, (0, i), (450, i), 1)
        if (i % 150 == 0):
            pg.draw.line(screen, black, (i, 0), (i, 450), 3)
            pg.draw.line(screen, black, (0, i), (450, i), 3)

def sudokuWindow():
    pg.init()
    screen = pg.display.set_mode((450, 450))

    run = True
    while run:
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                run = False

        screen.fill(white)
        drawLines(screen)

        pg.display.flip()