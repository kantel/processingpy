from bouncingball import BouncingBall, BouncingBox

balls = []
boxes = []

def setup():
    size(600, 600)
    for _ in range(60):
        if random(10) < 5:
            balls.append(BouncingBall())
        else:
            boxes.append(BouncingBox())

def draw():
    background("#2b3e50")
    for ball in balls:
        ball.move()
        ball.display()
    for box in boxes:
        box.move()
        box.display()
