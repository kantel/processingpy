# Bouncing Balls handgezeichnet
# nach einer Idee von Martin Prout
# <http://monkstone.github.io/jruby_art/update/2018/10/03/handy_library.html>

add_library('handy')
import random as r
from ball import Ball

balls = []

def setup():
    global h
    h = HandyRenderer(this)
    size(640, 480)
    h.setHachurePerturbationAngle(r.randint(15, 165))
    h.setRoughness(1)
    h.setFillWeight(r.uniform(0.1, 1.2))
    h.setFillGap(r.uniform(1.0, 1.9))
    for _ in range(10):
        balls.append(Ball(h))
    # noLoop()


def draw():
    background(235, 215, 182)
    drawBorders()
    for ball in balls:
        ball.display()
        ball.checkEdges()
        ball.update()


def drawBorders():
    h1 = HandyRenderer(this)
    fill(0, 255, 0)
    h1.rect(20, 20, width - 40, 20) # oben
    h1.rect(20, height - 40, width - 40, 20) #unten
    h1.rect(20, 40, 20, height - 80) # links
    h1.rect(width - 40, 40, 20, height - 80) #rechts
    
