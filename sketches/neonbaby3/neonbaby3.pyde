add_library("handy")
from random import randint

def setup():
    global h
    size(600, 600)
    this.surface.setTitle("Neonbaby 3")
    h = HandyRenderer(this)
    h.setRoughness(1.0)
    h.setOverrideFillColour(True)
    h.setOverrideStrokeColour(True)
    strokeWeight(2)
    background(51)

def draw():
    a = 30
    x = randint(10, width - 110)
    y = randint(10, height - 110)
    l1 = randint(50,100)
    l2 = randint(50,100)
    stroke_color = color(150, 100, 255)
    mycolor = color(150, 100, 255, a)
    if frameCount > 200:
        x = randint(80, width - 180)
        y = randint(80, height - 180)
        stroke_color = color(255, 100, 150)
        mycolor = color(255, 100, 150, a)
    if frameCount > 300:
        x = randint(150, width - 250)
        y = randint(150, height - 250)
        stroke_color = color(150, 255, 100)
        mycolor = color(150, 255, 100, a)
    if frameCount > 350:
        print("I did it, Neonbaby!")
        noLoop()
    h.setFillGap(4.5)
    h.setFillWeight(2.2)
    h.setStrokeColour(stroke_color)
    h.setFillColour(mycolor)
    h.setBackgroundColour(51)
    h.rect(x, y, l1, l2)
