import pygame as pg
from sys import exit

# Predefined colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
AQUA = (0, 255, 255)

pg.init()

FPS = 10
clock = pg.time.Clock()

# set dimensions
S = 15  # Length of a unit grid cell
W, H = 900, 600  # SCREEN WIDTH, SCREEN HEIGHT
mx, my = W // S, H // S  # workable coordinates

# set color according to theme
darkmode = True  # use dark mode?
surfcolor = WHITE if not darkmode else BLACK  # display surface color
snakecolor = BLACK if not darkmode else AQUA  # snake body color
foodcolor = BLUE if not darkmode else YELLOW  # food color

DSURF = pg.display.set_mode((W, H))  # set the display
DSURF.fill(surfcolor)  # fill display surface with surfcolor
pg.display.set_caption('dev')  # set display caption


# class declaration for the food object
class food:
    # constructor
    def __init__(self, fx: int, fy: int):
        self.x, self.y = fx, fy
        self.rec = pg.rect.Rect(self.x * S, self.y * S, S, S)

    # function for returning food object as string
    def __str__(self):
        return f"Food at (left, top) = ({self.x}, {self.y}) in color {foodcolor}"

    # draw food object on display surface
    def drawfood(self):
        pg.draw.rect(DSURF, foodcolor, self.rec)


f = food(2, 3)
f.drawfood()

while 1:
    eset = pg.event.get()
    for event in eset:
        if event.type == pg.QUIT:
            pg.quit()
            exit()
