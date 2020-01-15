import pygame as pg

white = (255, 255, 255)
black = (0, 0, 0)
grey = (180, 180, 180)

def drawButton(screen, text, y):
    pg.draw.rect(screen, grey, (45, y, 250, 40), 0)
    screen.blit(text, (55, y+10))

def pressedButton(pos):
    x = pos[0]
    y = pos[1]
    if (x >= 45 and x <= 295):
        if (y >= 100 and y <= 140):
            return 1
        elif (y >= 160 and y <= 200):
            return 2
        elif (y>= 220 and y <= 260):
            return 3
    return False

def checkDifficulty(pressed):
    if (pressed == 1):
        diff = 6
    elif (pressed == 2):
        diff = 5
    elif (pressed == 3):
        diff = 4
    return diff

def mainWindow():

    pg.init()
    screen = pg.display.set_mode((350, 300))

    run = True
    while run:
        for event in pg.event.get():
            pos = pg.mouse.get_pos()
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                pressed = pressedButton(pos)
                if (pressed != False):
                    diff = checkDifficulty(pressed)
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

    return diff