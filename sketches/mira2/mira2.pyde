a = -.48
b = .93

def setup():
    size(400, 400)
    background(235, 215, 182)
    colorMode(HSB, 255, 100, 100)
    stroke(0)
    strokeWeight(1)
    # noStroke()
    this.surface.setTitle("Fantastic Feather Fractal")
    noLoop()

def draw():
    x = 4.
    y = .0
    for i in range(120000):
        x1 = b*y + f(x)
        y = -x + f(x1)
        x = x1
        fill(i%255, 100, 100)
        p = 235 + x*20
        q = 230 - y*20
        circle(p, q, 5)

def f(x):
    return a*x - (1.0 - a)*((2*(x**2))/(1.0 + x**2))
               
