from sudokuGenerator import generator
from MainWindow import mainWindow
from sudokuWindow import sudokuWindow
#from endgameWindow import endgameWindow

def main():
    diff = mainWindow()
    print(diff)
    preSolved, board = generator(diff)
    sudokuWindow(preSolved, board)
main()