from random import randint

def setup():
    size(400, 600)
    this.surface.setTitle("Re-Enactment A. Michael Noll")
    noLoop()
    
def draw():
    background(235, 215, 182)
    margin = 5
    strokeWeight(2)
    x1 = randint(margin, width - margin)
    y1 = randint(margin, height - margin)
    for _ in range(50):
        x2 = randint(margin, width - margin)
        y2 = randint(margin, height - margin)
        line(x1, y1, x1, y2)
        line(x1, y2, x2, y2)
        x1 = x2
        y1 = y2
