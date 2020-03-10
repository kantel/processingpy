t = 0

def setup():
    size(600, 600)
    this.surface.setTitle("Rotationen")
    rectMode(CENTER)

def draw():
    global t
    colorMode(RGB)
    background("#2b3e50")
    translate(width/2, height/2)
    strokeWeight(2)
    colorMode(HSB)
    fill(0.5*t%255, 255, 0.1*t%255)
    ellipse(0, 0, 60, 60)
    rotate(radians(t))
    for _ in range(12):
        with pushMatrix():
            translate(200, 0)
            rotate(radians(2*t))
            strokeWeight(2)
            fill(0.2*t%255, 255, 255)
            rect(0, 0, 50, 50)
        with pushMatrix():
            translate(100, 0)
            rotate(radians(4*t))
            strokeWeight(1)
            fill(0.75*t%255, 255, 255)
            rect(0, 0, 30, 30)
        rotate(radians(360/12))
    t += 1
    
