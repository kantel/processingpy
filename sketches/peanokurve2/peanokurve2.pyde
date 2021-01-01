add_library('Turtle')
import math

num_gen = 6
len_seg = 6
a = 90
ds = 1  # 0.866 bei num_gen = 7

def setup():
    global p
    size(450, 450)
    this.surface.setTitle("Peano-Kurve v2")
    background(50)
    strokeWeight(1)
    stroke(150, 255, 100)
    p = Turtle(this)
    noLoop()

def draw():
    p.penUp()
    p.goToPoint(width - 35, height - 35)
    p.penDown()
    peano2(p, num_gen, len_seg, a)
    print("I did it, Babe")
    
def peano2(p, n, s, a):
    if n == 0:
        return
    p.left(a)
    peano2(p, n - 1, ds*s, -a)
    p.forward(s)
    p.right(a)
    peano2(p, n - 1, ds*s, a)
    p.forward(s)
    peano2(p, n - 1, ds*s, a)
    p.right(a)
    p.forward(s)
    peano2(p, n - 1, ds*s, -a)
    p.left(a)
    
    
    
