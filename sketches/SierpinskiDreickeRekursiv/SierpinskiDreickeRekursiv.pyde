# Sierpinski Dreieck
# nach Peter Farrell: Math Adventures with Python, p. 214ff.

from math import sqrt

def setup():
    size(500, 440)
    background(234, 218, 184)
    this.surface.setTitle("Sierpinski Dreieck rekursiv")
    noLoop()
    
def draw():
    # background(234, 218, 184)
    translate(50, 380) # links unten
    noStroke()
    sierpinsky(400, 6)
    
def sierpinsky(sz, level):
    if level == 0:
        fill(0)
        triangle(0, 0, sz, 0, sz/2.0, -sz*sqrt(3)/2.0)
    else:
        for _ in range(3):
            sierpinsky(sz/2.0, level-1)
            translate(sz/2.0, -sz*sqrt(3)/2.0)
            rotate(radians(120))
