aAngle = 0
aVelocity = 0
aAccleration = 0.001

def setup():
    size(400, 400)
    this.surface.setTitle("Tambourstab")

def draw():
    global aAngle, aVelocity, aAccleration
    background(235, 215, 182)
    
    fill(175)
    stroke(0)
    rectMode(CENTER)
    translate(width/2, height/2)
    rotate(aAngle)
    line(-100, 0, 100, 0)
    fill(255, 0, 0)
    ellipse(100, 0, 30, 20)
    ellipse(-100, 0, 30, 20)
    
    aVelocity += aAccleration
    aAngle += aVelocity
    if aVelocity >= 0.4:
        aVelocity = 0
