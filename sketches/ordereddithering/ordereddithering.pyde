matrix = [[64, 128],
          [192, 0]]

def setup():
    global akt
    size(800, 640)
    this.surface.setTitle("Ordered Dithering")
    akt = loadImage("akt.jpg")
    image(akt, 0, 0)
    noLoop()

def index(x, y):
    return(x + y * akt.width)

def draw():
    akt.filter(GRAY)
    akt.loadPixels()

    for y in range(akt.height):
        ymod = y % 2
        for x in range(akt.width):
            xmod = x % 2
            pix = akt.pixels[index(x, y)]
            c = red(pix)
            if c > matrix[xmod][ymod]:
                akt.pixels[index(x, y)] = color(255)
            else:
                akt.pixels[index(x, y)] = color(0)
    akt.updatePixels()
    image(akt, 400, 0)
