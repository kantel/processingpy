from random import randint

def setup():
    size(600, 600)
    this.surface.setTitle("Neonbaby 2")
    strokeWeight(2)
    background(51)

def draw():
    a = 50
    x = randint(10, width - 110)
    y = randint(10, height - 110)
    l1 = randint(50,100)
    l2 = randint(50,100)
    stroke(150, 100, 255)
    mycolor = color(150, 100, 255, a)
    if frameCount > 200:
        x = randint(80, width - 180)
        y = randint(80, height - 180)
        stroke(255, 100, 150)
        mycolor = color(255, 100, 150, a)
    if frameCount > 300:
        x = randint(150, width - 250)
        y = randint(150, height - 250)
        stroke(150, 255, 100)
        mycolor = color(150, 255, 100, a)
    if frameCount > 350:
        noLoop()
    fill(mycolor)
    rect(x, y, l1, l2)
