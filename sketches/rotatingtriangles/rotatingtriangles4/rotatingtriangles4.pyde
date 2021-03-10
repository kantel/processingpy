# rotating triangles 4
# after Roger Antonsen (University of Oslo)
# and Peter Farrell (Math Adventures with Python, p. 93ff.)

t = 0

def setup():
    size(600, 600)
    this.surface.setTitle("90 Rotating Equilateral Triangles")
    rectMode(CENTER)
    background(234, 218, 184)
    noLoop()

    
def draw():
    global t
    noFill()
    stroke(150, 100, 100)    
    translate(width/2, height/2)
    colorMode(HSB)
    for i in range(90):
        rotate(radians(360/90))
        with pushMatrix():
            translate(200, 0)
            rotate(radians(t + 2*i*360/90))
            stroke(2*i, 255, 180)
            strokeWeight(2)
            tri(100)
    t += 0.5

def tri(length):
    triangle(0, -length,
             -length*sqrt(3)/2, length/2,
             length*sqrt(3)/2, length/2)
