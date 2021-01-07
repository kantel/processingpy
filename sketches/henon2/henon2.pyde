import math

a = 1.35
# a = 1.5732
h = 0.02
x0 = .01
y0 = -.02

colors = [color(18, 184, 116), color(200, 23, 223), color(95, 145, 40),
          color(8, 124, 127)]

def setup():
    size(400, 400)
    this.surface.setTitle("Quadratische Henon-Gleichung, a = 1.35")
    background(235, 215, 182)
    strokeWeight(1.25)
    noLoop()

def draw():
    x = x0
    y = y0
    for j in range(50):
        for i in range(1500):
            stroke(colors[(1 + j)%4])
            x1 = x*math.cos(a) - (y - x*x)*math.sin(a)
            y  = x*math.sin(a) + (y - x*x)*math.cos(a)
            x = x1
            p = (x + 1.3)*width/2.667
            q = (1.5 - y)*height/2.667
            point(p, q)
        x = x0 + j*h
        y = y0 + j*h
