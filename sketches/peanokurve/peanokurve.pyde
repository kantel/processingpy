add_library('Turtle')
import math

num_gen = 3
ds = 1

def setup():
    global p
    size(400, 400)
    this.surface.setTitle("Peano-Kurve")
    background(50)
    strokeWeight(2)
    stroke(150, 255, 100)
    p = Turtle(this)
    p.right(90)
    noLoop()

def draw():
    p.penUp()
    p.goToPoint(25, 200)
    p.penDown()
    peano(p, num_gen, 300)
    print("I did it, Babe")
    
def peano(p, n, s):
    if n == 0:
        p.forward(s)
    else:
        peano(p, n-1, s/3)
        p.left(45)
        p.forward(ds*math.sqrt(2))
        p.left(45)
        peano(p, n-1, s/3)
        p.right(45)
        p.forward(ds*math.sqrt(2))
        p.right(45)
        peano(p, n-1, s/3)
        p.right(45)
        p.forward(ds*math.sqrt(2))
        p.right(45)
        peano(p, n-1, s/3)
        p.right(45)
        p.forward(ds*math.sqrt(2))
        p.right(45)
        peano(p, n-1, s/3)
        p.left(45)
        p.forward(ds*math.sqrt(2))
        p.left(45)
        peano(p, n-1, s/3)
        p.left(45)
        p.forward(ds*math.sqrt(2))
        p.left(45)
        peano(p, n-1, s/3)
        p.left(45)
        p.forward(ds*math.sqrt(2))
        p.left(45)
        peano(p, n-1, s/3)
        p.right(45)
        p.forward(ds*math.sqrt(2))
        p.right(45)
        peano(p, n-1, s/3)
    
