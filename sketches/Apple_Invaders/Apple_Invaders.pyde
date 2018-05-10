from sprites import Actor
gripe = Actor(304, 400)
              
def setup():
    size(640, 480)
    gripe.loadPics()

def draw():
    background(158, 214, 112)
    gripe.move()
    gripe.display()

def keyPressed():
    if keyPressed and key == CODED:
        if keyCode == RIGHT:
            gripe.dir = 0
        if keyCode == LEFT:
            gripe.dir = 2

def keyReleased():
    gripe.dir = 5
