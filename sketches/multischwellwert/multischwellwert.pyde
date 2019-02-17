matrix = [[30, 90, 130, 5],
          [110, 235, 210, 70],
          [150, 175, 90, 40],
          [20, 60, 90, 10]]

def setup():
    global akt
    size(800, 640)
    this.surface.setTitle("Dithering im Multischwellwertverfahren")
    akt = loadImage("akt.jpg")
    image(akt, 0, 0)
    noLoop()

def index(x, y):
    return(x + y * akt.width)

def draw():
    akt.filter(GRAY)
    akt.loadPixels()

    for y in range(akt.height):
        ymod = y % 4
        for x in range(akt.width):
            xmod = x % 4
            pix = akt.pixels[index(x, y)]
            c = red(pix)
            if c > matrix[xmod][ymod]:
                akt.pixels[index(x, y)] = color(255)
            else:
                akt.pixels[index(x, y)] = color(0)
    akt.updatePixels()
    image(akt, 400, 0)
