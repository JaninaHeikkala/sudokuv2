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

def drawNumbers(screen, board):
    font = pg.font.SysFont("Arial", 40)
    for y in range(0,9):
        for x in range(0,9):
            if (board[y][x] != 'x'):
                numText = font.render(str(board[y][x]), True, black)
                screen.blit(numText, (x*50+17, y*50+13))

def checkPos(pos):
    xC = pos[0]
    yC = pos[1]

    #x
    if (xC >= 50):
        x = 0
    elif (xC >= 100):
        x = 1
    elif (xC >= 150):
        x = 2
    elif (xC >= 200):
        x = 3
    elif (xC >= 250):
        x = 4
    elif (xC >= 300):
        x = 5
    elif (xC >= 350):
        x = 6
    elif (xC >= 400):
        x = 7
    else:
        x = 8

    #y
    if (yC >= 50):
        y = 0
    elif (yC >= 100):
        y = 1
    elif (yC >= 150):
        y = 2
    elif (yC >= 200):
        y = 3
    elif (yC >= 250):
        y = 4
    elif (yC >= 300):
        y = 5
    elif (yC >= 350):
        y = 6
    elif (yC >= 400):
        y = 7
    else:
        y = 8

    return x, y

def sudokuWindow(board):
    pg.init()
    screen = pg.display.set_mode((450, 450))

    run = True
    while run:
        for event in pg.event.get():
            pos = pg.mouse.get_pos()
            if (event.type == pg.QUIT):
                run = False
            if (event.type == pg.MOUSEBUTTONDOWN):
                click = checkPos(pos)

        screen.fill(white)
        drawLines(screen)
        drawNumbers(screen, board)

        pg.display.flip()