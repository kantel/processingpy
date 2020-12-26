add_library('Turtle')
from random import randint

turtles = []
colors = [color(18, 184, 116), color(200, 23, 223), color(95, 145, 40),
          color(8, 124, 127)]

def setup():
    size(400, 400)
    this.surface.setTitle(u"Random Walk mit der Schildkröte")
    background(232, 226, 7)
    strokeWeight(2)
    for _ in range(4):
        t = Turtle(this)
        t.setWrapAround(True)
        turtles.append(t)
    
def draw():
    i = 0
    for t in turtles:
        stroke(colors[i % len(turtles)])
        distance = randint(1, 5)
        t.forward(distance)
        angle = randint(0, 360)
        t.right(angle)
        i += 1
    if frameCount >= 5000:
        print("I did it, Babe!")
        noLoop()
    
    
