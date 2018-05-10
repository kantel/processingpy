from sprites import Actor
gripe = Actor(304, 384)

def setup():
    global block, bkg
    size(640, 480)
    block = loadImage("block.png")
    bkg = loadImage("bkg0.png")
    gripe.loadPics()

def draw():
    global block, bkg
    # background(158, 214, 112)
    background(bkg)
    i = 0
    while i < 640:
        image(block, i, 416)
        i += 32
    gripe.move()
    gripe.display()

def keyPressed():
    if keyPressed and key == CODED:
        if keyCode == RIGHT:
            gripe.state = 5
            gripe.dir = 0
        if keyCode == LEFT:
            gripe.state = 5
            gripe.dir = 2

def keyReleased():
    gripe.state = 4
