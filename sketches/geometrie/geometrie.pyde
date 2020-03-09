t = 0

def setup():
    size(600, 600)
    this.surface.setTitle("Geometrie")
    rectMode(CENTER)

def draw():
    global t
    colorMode(RGB)
    background(235, 215, 182)
    translate(width/2, height/2)
    rotate(radians(t))
    colorMode(HSB)
    for i in range(12):
        with pushMatrix():
            translate(200, 0)
            rotate(radians(2*t))
            strokeWeight(2)
            fill(0.2*t%255, 255, 255)
            rect(0, 0, 50, 50)
        rotate(radians(360/12))
    t += 1
    
