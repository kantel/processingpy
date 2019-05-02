matrix = [[176, 48, 144, 16, 168, 40, 136, 8],
          [112, 240, 80, 208, 104, 232, 72, 200],
          [160, 32, 192, 64, 152, 24, 184, 56],
          [96, 224, 128, 256, 88, 216, 120, 248],
          [168, 40, 136, 8, 176, 48, 144, 16],
          [104, 232, 72, 200, 112, 240, 80, 208],
          [152, 24, 284, 56, 160, 32, 192, 64],
          [88, 216, 120, 248, 96, 224, 208, 256]]

def setup():
    global akt
    size(800, 640)
    this.surface.setTitle("8x8 Dithermatrix")
    akt = loadImage("akt.jpg")
    image(akt, 0, 0)
    noLoop()

def index(x, y):
    return(x + y * akt.width)

def draw():
    akt.filter(GRAY)
    akt.loadPixels()

    for y in range(akt.height):
        ymod = y % 8
        for x in range(akt.width):
            xmod = x % 8
            pix = akt.pixels[index(x, y)]
            c = red(pix)
            if c > matrix[xmod][ymod]:
                akt.pixels[index(x, y)] = color(255)
            else:
                akt.pixels[index(x, y)] = color(0)
    akt.updatePixels()
    image(akt, 400, 0)
