# rotating triangle 2

t = 0

def setup():
    size(600, 600)
    rectMode(CENTER)
    background(234, 218, 184)

    
def draw():
    noFill()
    global t
    translate(width/2, height/2)
    rotate(radians(t))
    stroke(150, 100, 250)
    tri(200)
    t += 1.5

def tri(length):
    triangle(0, -length,
             -length*sqrt(3)/2, length/2,
             length*sqrt(3)/2, length/2)
