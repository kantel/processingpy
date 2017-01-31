def setup():
    size(500, 500)
    # colorMode(HSB, 100, 100, 100)
    background(255)
    noFill()
    noLoop()

def draw():
    cheese(width/2, height/2, 500, 6)

def cheese(x, y, r, level):
    # stroke((level*10)%100, 100, 100)
    ellipse(x, y, r, r)
    if (level > 1):
        cheese(x - r/4, y, r/2, level-1)
        cheese(x, y - r/4, r/2, level-1)
        cheese(x + r/4, y, r/2, level-1)
        cheese(x, y + r/4, r/2, level-1)