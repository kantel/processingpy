n = 6
d = 71

def setup():
    size(420, 420)
    this.surface.setTitle("Maurer Rose")
    noFill()
    noLoop()

def draw():
    global n, d
    background(235, 215, 182)
    translate(width/2, height/2)
    
    stroke(255, 0, 0)
    strokeWeight(4)
    with beginClosedShape():
        i = 0
        while (i < d*TWO_PI):
            r = 200*sin(radians(n*i))
            x = r*cos(radians(i))
            y = r*sin(radians(i))*-1
            vertex(x, y)
            i += 1

    stroke(0, 0, 255, 150)
    strokeWeight(1)
    with beginClosedShape():
        i = 0
        while (i < d*TWO_PI):
            k = i*d
            r = 200*sin(radians(n*k))
            x = r*cos(radians(k))
            y = r*sin(radians(k))*-1
            vertex(x, y)
            i += 1
