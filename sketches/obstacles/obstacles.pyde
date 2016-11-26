# obstacles

tileSize = 32

from sprites import Orc, Wall


def setup():
    global bg
    bg = loadImage("field.png")
    frameRate(30)
    size(320, 320)
    global orc
    orc = Orc(8*tileSize, 0)
    orc.loadPics()
    orc.dx = 2
    orc.dy = 2
    global wall1
    wall1 = Wall(5*tileSize, 3*tileSize)
    wall1.loadPics()

def draw():
    background(bg)
    wall1.display()
    orc.move()
    orc.checkCollision(wall1)
    orc.display()
    
def keyPressed():
    if keyPressed and key == CODED:
        if keyCode == RIGHT:
            orc.dir = 0
        elif keyCode == DOWN:
            orc.dir = 1
        elif keyCode == LEFT:
            orc.dir = 2
        elif keyCode == UP:
            orc.dir = 3