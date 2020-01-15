import pygame as pg
from sudokuGenerator import checkIfWorks, findEmpty
from endgameWindow import endgameWindow

white = (255, 255, 255)
black = (0, 0, 0)
grey = (180, 180, 180)
lightgrey = (230, 230, 230)
darkgrey = (100, 100, 100)
red = (255, 0, 0)

def drawLines(screen):
    for i in range(50, 500, 50):
        pg.draw.line(screen, black, (i, 0), (i, 450), 1)
        pg.draw.line(screen, black, (0, i), (450, i), 1)
        if (i % 150 == 0):
            pg.draw.line(screen, black, (i, 0), (i, 450), 3)
            pg.draw.line(screen, black, (0, i), (450, i), 3)

def drawNumbers(screen, board, ownInput, smallNumbers):
    font = pg.font.SysFont("Arial", 40)
    smallfont = pg.font.SysFont("Arial", 20)
    for y in range(0,9):
        for x in range(0,9):
            if (ownInput[y][x] != 'x'):
                color = darkgrey
                numText = font.render(str(ownInput[y][x]), True, color)
                screen.blit(numText, (x * 50 + 17, y * 50 + 13))
            elif (smallNumbers[y][x] != ['x']*9):
                color = darkgrey
                for i in range(0,9):
                    if (smallNumbers[y][x][i] != 'x'):
                        numText = smallfont.render(str(smallNumbers[y][x][i]), True, color)
                        xp = x*50 + 6
                        yp = y*50 + 6
                        if i == 1:
                            xp += 15
                        elif i == 2:
                            xp += 30
                        elif i == 3:
                            yp += 15
                        elif i == 4:
                            xp += 15
                            yp += 15
                        elif i == 5:
                            xp += 30
                            yp += 15
                        elif i == 6:
                            yp += 30
                        elif i == 7:
                            yp += 30
                            xp += 15
                        elif i == 8:
                            yp += 30
                            xp += 30
                        screen.blit(numText, (xp, yp))
            elif (board[y][x] != 'x'):
                '''if (checkIfWorks(board, board[y][x], x, y)):
                    color = black
                else:
                    color = red'''
                color = black
                numText = font.render(str(board[y][x]), True, color)
                screen.blit(numText, (x*50+17, y*50+13))


def checkPos(pos):
    xC = pos[0]
    yC = pos[1]

    #print(str(xC) + " " + str(yC))

    #x
    if (xC <= 50):
        x = 0
    elif (xC <= 100):
        x = 1
    elif (xC <= 150):
        x = 2
    elif (xC <= 200):
        x = 3
    elif (xC <= 250):
        x = 4
    elif (xC <= 300):
        x = 5
    elif (xC <= 350):
        x = 6
    elif (xC <= 400):
        x = 7
    else:
        x = 8

    #y
    if (yC <= 50):
        y = 0
    elif (yC <= 100):
        y = 1
    elif (yC <= 150):
        y = 2
    elif (yC <= 200):
        y = 3
    elif (yC <= 250):
        y = 4
    elif (yC <= 300):
        y = 5
    elif (yC <= 350):
        y = 6
    elif (yC <= 400):
        y = 7
    else:
        y = 8

    return x, y

def drawSelectBox(screen, x, y):
    pg.draw.rect(screen, lightgrey, (x*50+1, y*50+1, 48, 48), 0)

def getInput(event):
    if (event.key == pg.K_1):
        num = '1'
    elif (event.key == pg.K_2):
        num = '2'
    elif (event.key == pg.K_3):
        num = '3'
    elif (event.key == pg.K_4):
        num = '4'
    elif (event.key == pg.K_5):
        num = '5'
    elif (event.key == pg.K_6):
        num = '6'
    elif (event.key == pg.K_7):
        num = '7'
    elif (event.key == pg.K_8):
        num = '8'
    elif (event.key == pg.K_9):
        num = '9'
    else:
        num = False
    return num

def drawBigNumbers(board, ownInput, smallNumbers, num, x, y):
    if (board[y][x] == 'x'):
        ownInput[y][x] = num
        board[y][x] = num
        smallNumbers[y][x] = ['x']*9
        #print("drawn")
    elif ownInput[y][x] == num:
        board[y][x] = 'x'
        ownInput[y][x] = 'x'

def removeNumber(board, ownInput, smallNumbers, x, y):
    smallNumbers[y][x] = ['x'] * 9
    if (board[y][x] != 'x' and ownInput[y][x] != 'x'):
        board[y][x] = 'x'
        ownInput[y][x] = 'x'

def drawSmallNumbers(smallNumbers, ownInput, board, num, x, y):
    if ownInput[y][x] != 'x':
        ownInput[y][x] = 'x'
        board[y][x] = 'x'
    if (smallNumbers[y][x][int(num)-1] != 'x'):
        smallNumbers[y][x][int(num) - 1] = 'x'
    else:
        smallNumbers[y][x][int(num)-1] = num

def checkIfCorrect(board, solution):
    errors = 0
    for y in range(0,9):
        for x in range(0,9):
            if (int(board[y][x]) != int(solution[y][x])):
                #print(str(board[y][x]) + " " + str(solution[y][x]))
                errors += 1
    if (errors != 0):
        return False, errors
    else:
        return True, errors

def sudokuWindow(board, solution):
    pg.init()
    screen = pg.display.set_mode((450, 450))

    ownInput = ['x']*9
    for i in range(0, 9):
        ownInput[i] = ['x']*9

    smallNumbers = ['x']*9
    for i in range(0,9):
        smallNumbers[i] = ['x']*9
        for j in range(0,9):
            smallNumbers[i][j] = ['x']*9

    x = 66
    y = 66

    bigNumbers = True

    run = True
    while run:
        screen.fill(white)
        for event in pg.event.get():
            pos = pg.mouse.get_pos()
            if (event.type == pg.QUIT):
                run = False
            if (event.type == pg.MOUSEBUTTONDOWN):
                x, y = checkPos(pos)
                #print(str(x) + " " + str(y))
                #drawSelectBox(screen, x, y)
            if (event.type == pg.KEYDOWN):
                if (event.key == pg.K_TAB):
                    if (bigNumbers):
                        bigNumbers = False
                    else:
                        bigNumbers = True
                if (x != 66 and y != 66):
                    if (event.key == pg.K_BACKSPACE):
                        removeNumber(board, ownInput, smallNumbers, x, y)
                    else:
                        num = getInput(event)
                        if (num != False):
                            #print(num)
                            if bigNumbers:
                                drawBigNumbers(board, ownInput, smallNumbers, num, x, y)
                            else:
                                drawSmallNumbers(smallNumbers, ownInput, board, num, x, y)


        drawLines(screen)
        drawNumbers(screen, board, ownInput, smallNumbers)

        if not findEmpty(board):
            win, errors = checkIfCorrect(board, solution)
            if win:
                run = False
                endgameWindow(win)
            else:
                print("You have " + str(errors) + " errors!")

        pg.display.flip()