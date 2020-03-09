t = 0

def setup():
    size(600, 600)
    this.surface.setTitle("Geometrie")
    rectMode(CENTER)
    colorMode(HSB)

def draw():
    global t
    background("#605080")
    translate(width/2, height/2)
    rotate(radians(t))
    for i in range(12):
        with pushMatrix():
            translate(200, 0)
            rotate(radians(2*t))
            fill(0.2*t%255, 255, 255)
            rect(0, 0, 50, 50)
        rotate(radians(360/12))
    t += 1
    
