myMagma = ['#000003', '#140D35', '#3B0F6F', '#63197F', '#8C2980',
           '#B53679', '#DD4968', '#F66E5B', '#FD9F6C', '#FDCD90', '#FBFCBF']

def setup():
    global akt
    size(800, 640)
    this.surface.setTitle("Magma-Akt")
    akt = loadImage("akt.jpg")
    image(akt, 0, 0)
    noLoop()

def index(x, y):
    return(x + y*akt.width)

def draw():
    akt.filter(GRAY)
    akt.filter(POSTERIZE, 11)
    loadPixels()
    for y in range(akt.height):
        for x in range(akt.width):
            pix = akt.pixels[index(x, y)]
            c = floor(red(pix)/20)
            # print(c)
            col = color(myMagma[c])
            # akt.pixels[index(x, y)] = myMagma[c]
    updatePixels()
    image(akt, 400, 0)
