from sprites import Actor, Apple, Block
import random as r

gripe = Actor(304, 384)
blocks = []
apples = []

def setup():
    global bkg
    size(640, 480)
    frameRate(60)    
    bkg = loadImage("bkg0.png")
    for i in range(20):
        block = Block(i*32, 416)
        blocks.append(block)
        blocks[i].loadPics()
    for i in range(5):
        x = r.randint(32, width-32)
        y = r.randint(-480, -48)
        apple = Apple(x, y)
        apples.append(apple)
        apples[i].loadPics()
    gripe.loadPics()

def draw():
    global bkg
    background(bkg)
    for block in blocks:
        block.display()
        if gripe.checkWall(block) == False:
            gripe.state = "falling"
    
    for apple in apples:
        apple.move()
        if apple.checkCollision(gripe):
            apple.reset()
            gripe.score += 10
        for block in blocks:
            if (block.state == "visible" and apple.checkCollision(block)):
                if apple.state == "red":
                    block.state = "hidden"
                    apple.reset()
                elif apple.state == "green":
                    for block in blocks:
                        block.state = "visible"
                    apple.reset()
        apple.display()
            
    gripe.move()
    if gripe.y > height + 32:
        textSize(50)
        text("Game Over!!!", width/2 - 150, height/2)
        noLoop()
    gripe.display()
    textSize(25)
    text("Score: " + str(gripe.score), 15, 35)

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
