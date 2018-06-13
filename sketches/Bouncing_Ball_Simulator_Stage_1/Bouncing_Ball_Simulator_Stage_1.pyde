from bouncingball import BouncingBall

def setup():
    global ball
    size(600, 600)
    col = color(150, 255, 100)
    ball = BouncingBall(width/2, 10, 20, col)

def draw():
    global ball
    background(0, 0, 0)
    ball.move()
    ball.display()
