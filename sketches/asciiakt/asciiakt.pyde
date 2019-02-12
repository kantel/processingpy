gscale1 = "$@B%8&WM#*oahkbdpqZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'´. "
gscale2 = "@%#*+=-:. "

def setup():
    global akt
    size(800, 800)
    akt = loadImage("akt50x80.jpg")
    background(255)
    f = createFont("Courier", 6)
    textFont(f)
    # print(len(gscale2))
    noLoop()

def draw():
    global akt
    fill(0, 0, 0)
    for gridX in range(akt.width):
        lineNr = 100
        zeile = ""
        for gridY in range(akt.height):
            # grid position and tile size
            tileWidth = width/float(akt.width)
            tileHeight = height/float(akt.height)
            posX = tileWidth*gridX
            posY = tileHeight*gridY
            # get current color
            cc = akt.pixels[gridY*akt.width + gridX]
            # greyscale conversion
            greyscale = round(red(cc)*0.222 + green(cc)*0.707 + blue(cc)*0.071)
            # pixel color to fill, greyscale to ellipse size
            w = floor(map(greyscale, 0, 255, len(gscale2), 0))
            zeile += gscale2[w]
        # print(zeile)
        text(zeile, 0, posX)
        lineNr += 1
    print("I did it, Babe!")
