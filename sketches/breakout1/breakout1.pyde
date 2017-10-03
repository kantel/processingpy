from gameworld import Paddle, Ball, Brick

bricks = []
playingGame = False

def setup():
    global paddle, ball
    size(605, 400)
    paddle = Paddle()
    ball = Ball()
    for x in range(5, width - 80, 75):
        addBrick(x + 37.5, 50, 3)
        addBrick(x + 37.5, 70, 2)
        addBrick(x + 37.5, 90, 1)
                      
def draw():
    global paddle, ball, bricks, playingGame
    background(0, 0, 0)
    # Bricks
    for i in range(len(bricks)):
        bricks[i].display()
    # Paddle
    paddle.display()
    if playingGame:
        paddle.checkEdges()
        paddle.update()
    # Ball
    if (ball.meets(paddle)):
        if (ball.dir.y > 0):
            ball.dir.y *= -1
    ball.display()
    if playingGame:
        ball.checkEdges()
        ball.update()
    
def keyReleased():
    global paddle
    paddle.isMovingRight = False
    paddle.isMovingLeft = False

def keyPressed():
    global paddle
    if key == "a" or key == "A":
        paddle.isMovingLeft = True
    elif key == "d" or key == "D":
        paddle.isMovingRight = True
    if key == CODED:
        if keyCode == LEFT:
            paddle.isMovingLeft = True
        elif keyCode == RIGHT:
            paddle.isMovingRight = True


def mousePressed():
    global playingGame
    playingGame = True
    
def addBrick(x, y, hits):
    global brick, bricks
    brick = Brick(x, y, hits)
    bricks.append(brick)