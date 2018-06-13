from bouncingball import BouncingBall

balls = []

def setup():
    size(600, 600)
    for _ in range(30):
        balls.append(BouncingBall())

def draw():
    background("#2b3e50")
    for ball in balls:
        ball.move()
        ball.display()
