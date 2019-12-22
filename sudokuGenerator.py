from random import randint


def generateBoard(diff):

    board = ['x']*9
    i = 0
    while (i < 9):
        board[i] = ['x']*9
        i += 1

    inRow = 0

    for y in range(0,9):
        for x in range(0,9):
            do = randint(0,1)
            if (do == 1):
                inRow += 1
                if (inRow <= diff):
                    tried = []
                    tries = 0
                    while (len(tried) <= 9):
                        tries += 1
                        num = randint(1,9)
                        if num not in tried:
                            works = checkIfWorks(board, num, x, y)
                            if (works):
                                board[y][x] = num
                                break
                            else:
                                tried.append(num)
                        if (tries >= 100):
                            return False
        inRow = 0

    return board

def checkIfWorks(board, num, x, y):

    #row
    if (num in board[y]):
        return False

    #column
    for i in range(0,9):
        if (num == board[i][x]):
            return False

    #boxes

    #top row
    if ((x % 3 == 0 or x == 0) and (y % 3 == 0 or y == 0)):
        if (board[y+1][x+1] == num or board[y+1][x+2] == num or board[y+2][x+1] == num or board[y+2][x+2] == num):
            return False
    elif ((x == 1 or x == 4 or x == 7) and (y % 3 == 0 or y == 0)):
        if (board[y+1][x-1] == num or board[y+1][x+1] == num or board[y+2][x-1] == num or board[y+2][x+1] == num):
            return False
    elif ((x == 2 or x == 5 or x == 8) and (y % 3 == 0 or y == 0)):
        if (board[y+1][x-2] == num or board[y+1][x-1] == num or board[y+2][x-2] == num or board[y+2][x-1] == num):
            return False

    #middle row
    elif ((x % 3 == 0 or x == 0) and (y == 1 or y == 4 or y == 7)):
        if (board[y-1][x+1] == num or board[y-1][x+2] == num or board[y+1][x+1] == num or board[y+1][x+2] == num):
            return False
    elif ((x == 1 or x == 4 or x == 7) and (y == 1 or y == 4 or y == 7)):
        if (board[y-1][x-1] == num or board[y-1][x+1] == num or board[y+1][x-1] == num or board[y+1][x+1] == num):
            return False
    elif ((x == 2 or x == 5 or x == 8) and (y == 1 or y == 4 or y == 7)):
        if (board[y-1][x-2] == num or board[y-1][x-1] == num or board[y+1][x-2] == num or board[y+1][x-1] == num):
            return False

    #bottom row
    elif ((x % 3 == 0 or x == 0) and (y == 2 or y == 5 or y == 8)):
        if (board[y-2][x+1] == num or board[y-2][x+2] == num or board[y-1][x+1] == num or board[y-1][x+2] == num):
            return False
    elif ((x == 1 or x == 4 or x == 7) and (y == 2 or y == 5 or y == 8)):
        if (board[y-2][x-1] == num or board[y-2][x+1] == num or board[y-1][x-1] == num or board[y-1][x+1] == num):
            return False
    elif ((x == 2 or x == 5 or x == 8) and (y == 2 or y == 5 or y == 8)):
        if (board[y-2][x-2] == num or board[y-2][x-1] == num or board[y-1][x-2] == num or board[y-1][x-1] == num):
            return False

    #else
    return True

def findEmpty(board):
    for y in range(0,9):
        for x in range(0,9):
            if (board[y][x] == 'x'):
                return [x, y]
    return False


def solveable(board):
    pos = findEmpty(board)
    if not pos:
        return True
    x = pos[0]
    y = pos[1]
    for num in range(1,10):
        if checkIfWorks(board, num, x, y):
            board[y][x] = num
            solv = solveable(board)
            if solv:
                return True
            board[y][x] = 'x'
    return False




def printBoard(board):
    for j in range(0, 9):
        if j % 3 == 0 and j != 0:
            for k in range(0, 9):
                if k % 3 == 0 and k != 0:
                    print(" ", end='')
                print(" ─ ", end='')
            print()
        for i in range(0, 9):
            if i % 3 == 0 and i != 0:
                print("|", end='')
            print(" {} ".format(board[j][i]), end='')
        print()

def main():
    diff = 5
    board = generateBoard(diff)
    while (board == False):
        board = generateBoard(diff)
    print("Board generated:")
    printBoard(board)
    print("solving...")
    solved = solveable(board)
    while not solved:
        print("Could not solve")
        board = generateBoard(diff)
        while (board == False):
            board = generateBoard(diff)
        print("\nBoard generated:")
        printBoard(board)
        print("solving...")
        solved = solveable(board)
    print("\nBoard solved:")
    printBoard(board)
main()