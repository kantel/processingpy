def setup():
    size(400, 300)
    frameRate(20)
    background(255)
    noStroke()

def draw():
    xPos = random(width)
    yPos = random(height)
    groesse = random(10, 50)
    rot = random(255)
    gruen = random(255)
    blau = random(255)
    a = random(255)
    fill(color(rot, gruen, blau, a))
    ellipse(xPos, yPos, groesse, groesse)
             
    