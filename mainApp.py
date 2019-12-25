from sudokuGenerator import generator
from MainWindow import mainWindow
from sudokuWindow import sudokuWindow
#from endgameWindow import endgameWindow
from loadingWindow import loadingWindow

def main():
    diff = mainWindow()
    print(diff)
    preSolved, board = generator(diff)
    #loadingWindow()
    sudokuWindow(preSolved, board)
main()