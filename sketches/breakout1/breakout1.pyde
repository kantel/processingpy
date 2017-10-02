from gameworld import Paddle

def setup():
    global paddle
    size(605, 400)
    paddle = Paddle()

def draw():
    global paddle
    background(0, 0, 0)
    paddle.display()
    paddle.checkEdges()
    paddle.update()
    
def keyReleased():
    global paddle
    paddle.isMovingRight = False
    paddle.isMovingLeft = False

def keyPressed():
    global paddle
    if key == CODED:
        if keyCode == LEFT:
            paddle.isMovingLeft = True
        elif keyCode == RIGHT:
            paddle.isMovingRight = True