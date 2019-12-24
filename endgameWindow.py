import pygame as pg

white = (255, 255, 255)
black = (0, 0, 0)

def endgameWindow(win):
    if (win):
        text = "You won!"
    else:
        text = "You lost!"

    run = True

    pg.init()
    screen = pg.display.set_mode((200, 70))

    while run:
        screen.fill(white)
        font = pg.font.SysFont("Arial", 50)
        textscr = font.render(text, True, black)
        screen.blit(textscr, (20, 20))

        for event in pg.event.get():
            if (event.type == pg.QUIT):
                run = False

        pg.display.flip()
