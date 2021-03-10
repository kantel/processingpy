# rotating triangle 3

t = 0

def setup():
    size(600, 600)
    rectMode(CENTER)
    background(234, 218, 184)
    noLoop()

    
def draw():
    global t
    noFill()
    stroke(150, 100, 100)    
    translate(width/2, height/2)
    for _ in range(90):
        rotate(radians(360/90))
        with pushMatrix():
            translate(200, 0)
            rotate(radians(t))
            tri(90)
    t += 0.5

def tri(length):
    triangle(0, -length,
             -length*sqrt(3)/2, length/2,
             length*sqrt(3)/2, length/2)
