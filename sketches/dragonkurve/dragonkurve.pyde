add_library('Turtle')
import math

num_gen = 12

def setup():
    global puff
    size(640, 400)
    this.surface.setTitle("Puff, the Magic Dragon")
    background(50)
    strokeWeight(2)
    stroke(150, 255, 100)
    puff = Turtle(this)
    puff.right(90)
    noLoop()

def draw():
    puff.penUp()
    puff.goToPoint(200, 160)
    puff.penDown()
    dragon(puff, 300, num_gen, 1)
    print("I did it, Babe")
    
def dragon(drag, s, n, flag):
    if n == 0:
        drag.forward(s)
    else:
        alpha = 45
        if flag == 1:
            alpha *= -1
            flag *= -1
        drag.left(alpha)
        dragon(drag, s/math.sqrt(2), n-1, -flag)
        drag.right(2*alpha)
        dragon(drag, s/math.sqrt(2), n-1, flag)
        drag.left(alpha)
