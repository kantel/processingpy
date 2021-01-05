add_library('Turtle')
import math

def setup():
    global p
    size(640, 480)
    this.surface.setTitle("Pythagorasbaum")
    background(50)
    strokeWeight(1)
    stroke(150, 255, 100)
    p = Turtle(this)
    noLoop()

def draw():
    p.penUp()
    p.goToPoint(width/2 - 50, height - 50)
    p.penDown()
    tree(100)
    print("I did it, Babe")
    
def tree(s):
    if s < 2:
        return
    quadrat(s)
    p.forward(s)
    s1 = s/math.sqrt(2)
    p.left(45)
    tree(s1)
    p.right(90)
    p.forward(s1)
    tree(s1)
    p.back(s1)
    p.left(45)
    p.back(s)

def quadrat(s):
    for _ in range(4):
        p.forward(s)
        p.right(90)

    
