# Running Orc 00
from orcs import Orc

orc = Orc(160, -48)


def setup():
    global bg
    bg = loadImage("field.png")
    frameRate(15)
    size(320, 320)
    orc.loadPics()
    orc.dy = 5
    
def draw():
    background(bg)
    orc.move()
    orc.display()
    