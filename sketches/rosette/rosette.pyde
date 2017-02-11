d = 8.0
n = 5.0

def setup():
    size(400, 400)
    frame.setTitle("Rosetten")
    noFill()

def draw():
    k = n/d
    background(51)
    translate(width/2, height/2)
    with beginClosedShape():
        stroke(255)
        strokeWeight(1)
        a = 0
        while (a < d*TWO_PI):
            r = 200*cos(k*a)
            x = r*cos(a)
            y = r*sin(a)
            vertex(x, y)
            a += 0.02
        
