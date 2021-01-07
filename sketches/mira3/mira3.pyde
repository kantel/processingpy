a = .4
b = 1.0

def setup():
    size(600, 600)
    background(60)
    colorMode(HSB, 255, 100, 100)
    strokeWeight(1.5)
    this.surface.setTitle("Mira-Abbildung")
    noLoop()

def draw():
    x = 4.
    y = .0
    for i in range(120000):
        x1 = b*y + f(x)
        y = -x + f(x1)
        x = x1
        stroke(i%255, 100, 100)
        p = 350 + x*26
        q = 300 - y*26
        point(p, q)

def f(x):
    return a*x - (1.0 - a)*((2*(x**2))/(1.0 + x**2))
               
