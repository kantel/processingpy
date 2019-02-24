from random import randint

def setup():
    global x, y, dx, dy
    size(560, 315)
    x = width/2
    y = height/2
    dx = 4
    dy = 4
    background(255)
    noStroke()

def draw():
    global x, y, dx, dy
    fill(random(256), random(256), random(256))
    ellipse(x, y, 25, 25)
    x += dx
    y +=dy
    if x < 30: dx = 4
    if x > width - 30: dx = -4
    if y < 30: dy = 4
    if y > height - 30: dy = -4
    saveFrame("output/circlesnake_####.png")
    dx += randint(-1, 1)
    dy += randint(-1, 1)
    if frameCount > 2000: noLoop()
