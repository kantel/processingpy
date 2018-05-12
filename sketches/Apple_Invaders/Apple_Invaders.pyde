from sprites import Actor, Block
gripe = Actor(304, 384)
blocks = []

def setup():
    global bkg
    size(640, 480)
    frameRate(30)    
    bkg = loadImage("bkg0.png")
    for i in range(20):
        block = Block(i*32, 416)
        blocks.append(block)
        blocks[i].loadPics()
    gripe.loadPics()

def draw():
    global bkg
    background(bkg)
    blocks[5].state = "hidden"
    # blocks[18].state = "hidden"
    for block in blocks:
        block.display()
        if gripe.checkWall(block) == False:
            gripe.state = "falling"
            
    gripe.move()
    gripe.display()

def keyPressed():
    if keyPressed and key == CODED:
        if keyCode == RIGHT:
            gripe.state = "walking"
            gripe.dir = "right"
        if keyCode == LEFT:
            gripe.state = "walking"
            gripe.dir = "left"

def keyReleased():
    gripe.state = "standing"
