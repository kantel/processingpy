FACTOR = 1
from random import randint

def setup():
    global akt
    size(800, 640)
    this.surface.setTitle("Dithering mit Zufalls-Schwellwert")
    akt = loadImage("akt.jpg");
    image(akt, 0, 0)
    noLoop()

def index(x, y):
    return(x + y * akt.width)
    
def draw():
    akt.filter(GRAY)
    akt.loadPixels()
    
    for y in range(akt.height - 1):
        for x in range(1, akt.width - 1):
            r = randint(0, 255)
            pix = akt.pixels[index(x, y)]
            c = red(pix)
            if c <= r:
                akt.pixels[index(x, y)] = color(0)
            else:
                akt.pixels[index(x, y)] = color(255)
    

    akt.updatePixels()
    image(akt, 400, 0)
   
