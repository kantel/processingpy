# rotating triangle 1

t = 0

def setup():
    size(600, 600)
    rectMode(CENTER)
    background(234, 218, 184)
    
def draw():
    global t
    noFill()
    translate(width/2, height/2)
    rotate(radians(t))
    stroke(150, 100, 250)
    triangle(0, 0, 100, 100, 200, -200)
    t += 1.5
