h = .684
FPS = 900

def setup():
    global x, y
    size(400, 400)
    this.surface.setTitle("Tour Eiffel de Cassel")
    background(235, 215, 182)
    frameRate(FPS)
    x = .1
    y = .8

def draw():
    global x, y
    strokeWeight(1)
    x1 = x + h*(x - x*x + y)
    y  = y + h*(y - y*y + x)
    x = x1
    if frameCount > 10:
        point(map(x, -1.6, 3.6, 0, width), map(y, -1.0, 3.0, height, 0))
    if frameCount < 2400:
        stroke(18, 184, 116)
    elif frameCount < 4800:
        stroke(200, 23, 223)
    elif frameCount < 7200:
        stroke(95, 145, 40)
    else:
        stroke(8, 124, 127)
    if frameCount > 9600:
        print("I did it, Babe!")
        noLoop()
