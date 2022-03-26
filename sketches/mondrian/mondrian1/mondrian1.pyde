from random import randint

WIDTH, HEIGHT = 800, 600
n  = 2     # Rekursionstiefe
sw = 3     # Stroke Weight

# Farbpalette

mondrian2 = [color(38, 71, 124), color(240, 217, 92), color(162, 45, 40),
             color(223, 224, 236), color(223, 224, 236)]

def mondrian(x0, y0, x1, y1, n):
    if n == 0:
        fill(mondrian2[randint(0, len(mondrian2) - 1)])
        strokeWeight(sw)
        rect(x0, y0, x1 - x0 - sw, y1 - y0 - sw)
    else:
        x = randint(x0, x1)
        y = randint(y0, y1)
        mondrian(x0, y0, x, y, n - 1)  # Rechteck links oben
        mondrian(x, y0, x1, y, n - 1)  # Rechteck rechts oben
        mondrian(x0, y, x, y1, n - 1)  # Rechteck links unten
        mondrian(x, y, x1, y1, n - 1)  # Rechteck rechts unten

def setup():
    global ready
    size(WIDTH, HEIGHT)
    this.windowTitle("Hommage an Piet Mondrian")
    this.windowMove(1400, 30)
    background(223, 224, 236)
    mondrian(1, 1, width, height, n)
    ready = False

def draw():
    global ready
    if ready:
        mondrian(1, 1, width, height, n)
        ready = False

def mousePressed():
    global ready
    ready = True
        
    
