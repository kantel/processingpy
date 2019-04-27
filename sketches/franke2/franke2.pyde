add_library('handy')
from random import randint

magenta  = color(247, 114, 205)
orange   = color(252, 188, 117)
darkgrey = color(84, 72, 74)

def setup():
    global h
    size(400, 600)
    this.surface.setTitle("2. Re-Mixing Herbert W. Franke")
    h = HandyRenderer(this)
    rectMode(CENTER)
    h.setRoughness(0.6)
    noLoop()

def draw():
    background(250, 250, 250)
    strokeWeight(2)
    noFill()
    for _ in range(100):
        margin = 25
        stroke(orange)
        x = randint(margin, width - margin)
        y = randint(4*margin, height - 4*margin)
        h.rect(x, y, margin, margin)
    for _ in range(150):
        margin = 8
        stroke(magenta)
        x = randint(margin, width - margin)
        y = randint(12*margin, height - 12*margin)
        h.rect(x, y, margin, margin)
    for _ in range(4):
        margin = 100
        stroke(darkgrey)
        x = randint(margin/2 + 10, width - margin/2 - 10)
        y = randint(margin + 10, height - margin - 10)
        h.rect(x, y, margin, margin)
