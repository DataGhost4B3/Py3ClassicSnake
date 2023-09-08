import pygame as pg
import sys
from random import randint as rint
from tkinter import *
from tkinter import ttk


# loadscr = Tk()
# lf=ttk.Frame(loadscr, padding=10)
# lf.grid()
# ttk.Label(lf, text='Loading...').grid(column=0, row=0)
# loadscr.mainloop()
# loadscr.destroy()


def showscore(s: int, r: str):
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    sh = 'Why you pegged out:\n' + r + '\nYou scored: ' + str(s)
    ttk.Label(frm, text=sh, font=('Poppins bold', 15)).grid(column=0, row=0)
    ttk.Button(frm, text='Quit', command=root.destroy).grid(column=0, row=1)
    root.mainloop()


pg.init()


def exitcall():
    pg.quit()
    sys.exit()


# def menuexitcall(r):
#     r.destroy()
#     exitcall()

darktheme = False


def sel():
    global darktheme
    darktheme = bool(var.get())


toor = Tk()
fram = ttk.Frame(toor, padding=10)
fram.pack()
label = ttk.Label(fram, text='Navigate using arrow keys.\n'
                             'Press Space Bar anytime to quit the game.\n'
                             'Press T to toggle theme in-game.\n'
                             'Live score will be counted on the title bar.', font=('Poppins bold', 12))
label.pack(side=TOP)
var = IntVar()
R1 = Radiobutton(toor, text="Light Mode", variable=var, value=0, command=sel)
R1.pack(side=TOP)
R2 = Radiobutton(toor, text="Dark Mode", variable=var, value=1, command=sel)
R2.pack(side=TOP)
ttk.Button(fram, text='Play', command=toor.destroy).pack(side=LEFT)
ttk.Button(fram, text='Exit', command=exitcall).pack(side=RIGHT)
toor.protocol("WM_DELETE_WINDOW", exitcall)
# darktheme = (var.get())
toor.mainloop()

FPS = 10
FramePerSec = pg.time.Clock()

# Predefined colors
BLACK = (0, 0, 0) if not darktheme else (255, 255, 255)
BLUE = (255, 0, 0) if darktheme else (0, 255, 0)
WHITE = (255, 255, 255) if not darktheme else (0, 0, 0)
GREEN = (0, 255, 0) if darktheme else (255, 0, 0)

# def togmode():
# global BLACK
# global WHITE
# global BLUE
# global GREEN
# tempcol = BLACK
# BLACK = WHITE
# WHITE = tempcol
# tempcol = BLUE
# BLUE = GREEN
# GREEN = tempcol
# DISPLAYSURF.fill(WHITE)

SCREEN_W = 900  # 900/15=60
SCREEN_H = 600  # 600/15=40

DISPLAYSURF = pg.display.set_mode((SCREEN_W, SCREEN_H))
DISPLAYSURF.fill(WHITE)
pg.display.set_caption("Snake!")

SIDE = 15

kpressed = ['UP']

x, y = SCREEN_W // SIDE // 2, SCREEN_H // SIDE // 2

bodylist = [(x, y)]


def foodspawn():
    foox = rint(0, SCREEN_W // SIDE - 1)
    fooy = rint(0, SCREEN_H // SIDE - 1)
    while tuple((foox, fooy)) in bodylist:
        foox = rint(0, SCREEN_W // SIDE - 1)
        fooy = rint(0, SCREEN_H // SIDE - 1)
    return tuple((foox, fooy))


foodpos = foodspawn()
fx, fy = foodpos[0], foodpos[1]
pg.draw.rect(DISPLAYSURF, GREEN, pg.rect.Rect(fx * SIDE, fy * SIDE, SIDE, SIDE))

# pg.draw.rect(DISPLAYSURF, GREEN, pg.rect.Rect(fx * SIDE, fy * SIDE, SIDE, SIDE))

# def intsec(lst1, lst2):
#     lst3 = [v for v in lst1 if v in lst2]
#     return lst3

realscore = 0
score = 0
lastunit = bodylist[0]

while not (x == -1 or y == -1 or x == SCREEN_W // SIDE or y == SCREEN_H // SIDE):
    score = len(bodylist) - 1
    # lastunit = bodylist.pop(0)
    # pg.draw.rect(DISPLAYSURF, WHITE, pg.rect.Rect(lastunit[0] * SIDE, lastunit[1] * SIDE, SIDE, SIDE))
    # fx, fy = foodpos[0], foodpos[1]
    if x == fx and y == fy:
        realscore += 1
        pg.display.set_caption('Snake!  |   Score: ' + str(realscore))
        bodylist.insert(0, lastunit)
        # pg.draw.rect(DISPLAYSURF, WHITE, pg.rect.Rect(fx * SIDE, fy * SIDE, SIDE, SIDE))
        print('*')
        foodpos = foodspawn()
        fx, fy = foodpos[0], foodpos[1]
        pg.draw.rect(DISPLAYSURF, GREEN, pg.rect.Rect(fx * SIDE, fy * SIDE, SIDE, SIDE))
    fx, fy = foodpos[0], foodpos[1]
    # pg.draw.rect(DISPLAYSURF, GREEN, pg.rect.Rect(fx * SIDE, fy * SIDE, SIDE, SIDE))
    pressed = False
    allevent = pg.event.get()
    # try:
    #     if allevent[0].type == pg.QUIT:
    #         # pg.display.quit()
    #         pg.quit()
    #         print("score =", score, "realscore =", realscore)
    #         reason = "You didn't. You quit."
    #         showscore(realscore, reason)
    #         sys.exit()
    # except IndexError:
    #     pass
    try:
        if (allevent[0].key in {pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN, pg.K_SPACE}) or (allevent[0].type==pg.QUIT):
            eset = [allevent[0], ]
        else:
            eset = []
    except (IndexError, AttributeError):
        eset = []
    c = False
    for k in allevent:
        if not c:
            if k.type == pg.KEYDOWN:
                if k.key == pg.K_t:
                    tempcol = BLACK
                    BLACK = WHITE
                    WHITE = tempcol
                    tempcol = BLUE
                    BLUE = GREEN
                    GREEN = tempcol
                    DISPLAYSURF.fill(WHITE)
                    pg.draw.rect(DISPLAYSURF, GREEN, pg.rect.Rect(fx * SIDE, fy * SIDE, SIDE, SIDE))
                    # pg.display.update()
                    for uc in bodylist:
                        pg.draw.rect(DISPLAYSURF, BLACK, pg.rect.Rect(uc[0] * SIDE, uc[1] * SIDE, SIDE, SIDE))
                    c = True
    print('eset=', eset, '\nevents=', allevent)
    lastunit = bodylist.pop(0)
    pg.draw.rect(DISPLAYSURF, WHITE, pg.rect.Rect(lastunit[0] * SIDE, lastunit[1] * SIDE, SIDE, SIDE))
    for event in eset:
        if event.type == pg.QUIT:
            # pg.display.quit()
            pg.quit()
            print("score =", score, "realscore =", realscore)
            reason = "You didn't. You quit."
            showscore(realscore, reason)
            sys.exit()
        if event.type == pg.KEYDOWN:
            pressed = True
            # bodylist.pop(0)
            # pg.draw.rect(DISPLAYSURF, WHITE, pg.rect.Rect(lastunit[0] * SIDE, lastunit[1] * SIDE, SIDE, SIDE))
            if event.key == pg.K_SPACE:
                pg.quit()
                print("score =", score, "realscore =", realscore)
                reason = "You didn't. You quit."
                showscore(realscore, reason)
                sys.exit()
            if realscore == 0:
                if event.key == pg.K_UP:
                    kpressed[0] = 'UP'
                    y -= 1
                if event.key == pg.K_DOWN:
                    kpressed[0] = 'DOWN'
                    y += 1
                if event.key == pg.K_LEFT:
                    kpressed[0] = 'LEFT'
                    x -= 1
                if event.key == pg.K_RIGHT:
                    kpressed[0] = 'RIGHT'
                    x += 1
            if realscore > 0:
                if event.key == pg.K_UP:
                    if kpressed[0] != 'DOWN':
                        kpressed[0] = 'UP'
                        y -= 1
                    else:
                        y += 1
                if event.key == pg.K_DOWN:
                    if kpressed[0] != 'UP':
                        kpressed[0] = 'DOWN'
                        y += 1
                    else:
                        y -= 1
                if event.key == pg.K_LEFT:
                    if kpressed[0] != 'RIGHT':
                        kpressed[0] = 'LEFT'
                        x -= 1
                    else:
                        x += 1
                if event.key == pg.K_RIGHT:
                    if kpressed[0] != 'LEFT':
                        kpressed[0] = 'RIGHT'
                        x += 1
                    else:
                        x -= 1
            if tuple((x, y)) in bodylist:
                pg.quit()
                print('YOU BIT YOURSELF! Score =', score, 'realscore =', realscore)
                reason = 'Autosarcophagy'
                showscore(realscore, reason)
                sys.exit()
            bodylist.append(tuple((x, y)))
    if not pressed:
        # bodylist.pop(0)
        # pg.draw.rect(DISPLAYSURF, WHITE, pg.rect.Rect(lastunit[0] * SIDE, lastunit[1] * SIDE, SIDE, SIDE))
        if kpressed[0] == 'UP':
            y -= 1
        if kpressed[0] == 'DOWN':
            y += 1
        if kpressed[0] == 'LEFT':
            x -= 1
        if kpressed[0] == 'RIGHT':
            x += 1
        if tuple((x, y)) in bodylist:
            pg.quit()
            print('YOU BIT YOURSELF! Score =', score, 'realscore =', realscore)
            reason = 'Autosarcophagy'
            showscore(realscore, reason)
            sys.exit()
        bodylist.append(tuple((x, y)))

    # il = intsec(tuple((x, y)), bodylist)
    #
    # if len(il) > 1:
    #     pg.quit()
    #     print('STOP BITING YOURSELF!', 'Score =', score)
    #     sys.exit()
    testSq = pg.rect.Rect(x * SIDE, y * SIDE, SIDE, SIDE)
    print(x, y, score, realscore)
    pg.draw.rect(DISPLAYSURF, BLACK, testSq)
    # lastunit = bodylist.pop(0)
    # pg.draw.rect(DISPLAYSURF, WHITE, pg.rect.Rect(lastunit[0] * SIDE, lastunit[1] * SIDE, SIDE, SIDE))
    # print(kpressed, c)
    # if x == fx and y == fy:
    #     bodylist.insert(0, lastunit)
    #     # pg.draw.rect(DISPLAYSURF, WHITE, pg.rect.Rect(fx * SIDE, fy * SIDE, SIDE, SIDE))
    #     foodpos = foodspawn()
    pg.display.flip()
    FramePerSec.tick(FPS)
    # time.sleep(1)

pg.quit()
print("CRASHED HEAD ON WALL!")
print("GAME OVER!", "Score =", score, "realscore =", realscore)
reason = 'Crashed your head on the wall LMAO.'
showscore(realscore, reason)
sys.exit()
