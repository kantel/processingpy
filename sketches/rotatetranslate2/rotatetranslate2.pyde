t = 0

def setup():
    size(600, 600)
    this.surface.setTitle("Rotate und Translate")
    rectMode(CENTER)

def draw():
    global t
    background(0, 0, 255)
    translate(width/2, height/2)
    rotate(radians(t))
    fill(255, 255, 0)
    for i in range(12):
        with pushMatrix():
            translate(200, 0)
            rotate(radians(3*t))
            rect(0, 0, 50, 50)
        rotate(radians(360/12))
    t += 1
