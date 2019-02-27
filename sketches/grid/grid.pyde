import math

# Range of x-values
xmin = -6
xmax = 6

# Range of y-values
ymin = -2
ymax = 2

# Calculate the range
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600, 200)
    this.surface.setTitle("Sinus und Cosinus")
    xscl = width/rangex
    yscl = -height/rangey

def draw():
    global xscl, yscl
    background(255)
    translate(width/2, height/2)
    grid(xscl, yscl)
    graphFunction()

def graphFunction():
    x = xmin
    while x <= xmax:
        stroke(255, 0, 0)
        line(x*xscl, math.sin(x)*yscl, (x + 0.1)*xscl, math.sin(x + 0.1)*yscl)
        stroke(255, 0, 255)
        line(x*xscl, math.cos(x)*yscl, (x + 0.1)*xscl, math.cos(x + 0.1)*yscl)
        x += 0.1
        
def grid(xscl, yscl):
    strokeWeight(1)
    stroke(0, 255, 255)   # Cyan
    for i in range(xmin, xmax + 1):
        line(i*xscl, ymin*yscl, i*xscl, ymax*yscl)
    for i in range(ymin, ymax + 1):
        line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)
    stroke(0)
    line(0, ymin*yscl, 0, ymax*yscl)
    line(xmin*xscl, 0, xmax*xscl, 0)
