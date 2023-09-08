import pygame as pg
import sys
from random import randint as rint

pg.init()

FPS = 2
FramePerSec = pg.time.Clock()

# Predefined colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# width = 900
# height = 600

sqSize = 10  # side length of squares

# UCS =

# Screen information
SCREEN_W = 900  # 900/15=60
SCREEN_H = 600  # 600/15=40

DISPLAYSURF = pg.display.set_mode((SCREEN_W, SCREEN_H))
DISPLAYSURF.fill(WHITE)
pg.display.set_caption("Classic Snake")

bodylist = [((SCREEN_W // sqSize) // 2, (SCREEN_H // sqSize) // 2)]


# bodylist =set()

# print (bodylist[0][0], bodylist[0][1])

# pg.draw.rect(DISPLAYSURF, GREEN, pg.rect.Rect((bodylist[0][0] * sqSize, bodylist[0][1] * sqSize), (sqSize, sqSize)))


def foodspawn():
    left = rint(0, SCREEN_W // sqSize - 1)
    top = rint(0, SCREEN_H // sqSize - 1)
    # print(left, top)
    while tuple((left, top)) in bodylist:
        left = rint(0, SCREEN_W // sqSize - 1)
        top = rint(0, SCREEN_H // sqSize - 1)
        # if tuple((left, top)) in bodylist:
        #     left = rint(0, SCREEN_W // sqSize - 1)
        #     top = rint(0, SCREEN_H // sqSize - 1)
        #     print(left, top)
        # else:
        #     break
    # print(left, top)
    # bodylist.append(tuple((left, top)))
    # print(bodylist)
    return tuple((left, top))

score = [0,]

def eat(foodpos, lastu, sc: list):
    if bodylist[-1] == foodpos:
        sc[0] += 1
        foodpos = pg.rect.Rect(0, 0, 0, 0)
        pg.draw.rect(DISPLAYSURF, WHITE, foodpos)
        storefood(foodp)
        bodylist.append(lastu)
        pg.display.update()


def storefood(v):
    v[0] = foodspawn()


foodp = [0]

storefood(foodp)

def movesnake(ikey, sbody):
    try:
        lastunit = sbody[-2]
    except IndexError:
        prevunit = sbody[-1]
    lastunit = sbody[-1]
    if ikey == 'UP':
        if prevunit != (sbody[-1][0], sbody[-1][1] + 1):
            sbody.append((sbody[-1][0], sbody[-1][1] + 1))
            lastunit=sbody.pop(0)
    if ikey == 'DOWN':
        if prevunit != (sbody[-1][0], sbody[-1][1] - 1):
            sbody.append((sbody[-1][0], sbody[-1][1] - 1))
            lastunit=sbody.pop(0)
    if ikey == 'RIGHT':
        if prevunit != (sbody[-1][0] + 1, sbody[-1][1]):
            sbody.append((sbody[-1][0] + 1, sbody[-1][1]))
            lastunit=sbody.pop(0)
    if ikey == 'LEFT':
        if prevunit != (sbody[-1][0] - 1, sbody[-1][1]):
            sbody.append((sbody[-1][0] - 1, sbody[-1][1]))
            lastunit=sbody.pop(0)
    return lastunit

keyp = ['UP',]

def getKey(k, eset):
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if e.key == pg.K_w:
            k[0] = 'UP'
        if e.key == pg.K_s:
            k[0] = 'DOWN'
        if e.key == pg.K_d:
            k[0] = 'RIGHT'
        if e.key == pg.K_a:
            k[0] = 'LEFT'

while True:
    #for event in pg.event.get():
    #    if event.type == pg.QUIT:
    #        pg.quit()
    #        sys.exit()
    eventset = pg.event.get()
    getKey(keyp, eventset)
    ltpos = foodp[0]
    # print(ltpos, len(bodylist))
    pg.draw.rect(DISPLAYSURF, BLUE, pg.rect.Rect((ltpos[0] * sqSize, ltpos[1] * sqSize), (sqSize, sqSize)))
    pg.display.update()
    FramePerSec.tick(FPS)
    skey = keyp[0]
#    getKey(keyp)
    l = movesnake(skey, bodylist)
    for u in bodylist:
        pg.draw.rect(DISPLAYSURF, GREEN, pg.rect.Rect(u[0]*sqSize, u[1]*sqSize, sqSize, sqSize))
    pg.display.update()
    eat(ltpos, l, score)
    FramePerSec.tick(FPS)
