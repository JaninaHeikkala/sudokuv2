def generateBoard():
    board = ['x']*9
    i = 0
    while (i < 9):
        board[i] = ['x']*9
        i += 1
    return board

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
    board = generateBoard()
    printBoard(board)
main()