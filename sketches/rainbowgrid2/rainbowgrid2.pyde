# Rainbow Grid handgezeichnet
add_library('handy')

def setup():
    global h
    h = HandyRenderer(this)
    size(600, 600)
    this.surface.setTitle("Rainbow Grid Handy")
    rectMode(CENTER)
    h.setRoughness(1)
    h.setFillWeight(0.9)
    h.setFillGap(0.9)

def draw():
    colorMode(RGB)
    background(235, 215, 182)
    colorMode(HSB)
    translate(12, 12)
    for x in range(20):
        for y in range(20):
            d = dist(30*x, 30*y, mouseX, mouseY)
            fill(0.5*d, 255, 255)
            h.rect(x*30 + 3, y*30 + 3, 24, 24)
    
