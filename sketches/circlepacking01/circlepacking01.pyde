from random import randint
from circles import Circle

circles = []
attemps = 0
max_attemps = 400
total = 20

def setup():
    global zebu
    size(400, 400)
    this.surface.setTitle("Animated Circle Packing")
    zebu = loadImage("zebusessel.jpg")
    zebu.loadPixels()

def draw():
    global attemps
    background(51)

    count = 0
    while (count < total):
        new_c = new_circle()
        if (new_c):
            circles.append(new_c)
            count += 1

    attemps += 1
    if (attemps > max_attemps):
        print("I did it, Babe!")
        noLoop()
    
    for c in circles:
        if (c.growing):
            if (c.edges()):
                c.growing = False
            else:
                for other in circles:
                    if (c != other):
                        d = dist(c.x, c.y, other.x, other.y)
                        if (d - 2 < c.r + other.r):
                            c.growing = False
                            break
    
        c.show()
        c.grow()


def new_circle():
    x = randint(0, width - 1)
    y = randint(0, height - 1)
    valid = True
    for c in circles:
        d = dist(x, y, c.x, c.y)
        if (d < c.r):
            valid = False
            break
    if (valid):
        index = x + y * width
        col = zebu.pixels[index]
        return(Circle(x, y, col))
