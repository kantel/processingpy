def setup():
    global akt
    size(400, 640)
    this.surface.setTitle("Quadrate-Akt")
    akt = loadImage("akt50x80.jpg")
    background(255)
    noLoop()

def draw():
    global akt
    for gridX in range(akt.width):
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
            # pixel color to stroke, greyscale to strokeWeight
            strokeWeight(map(greyscale, 0, 255, 7, 0))
            stroke(cc)
            w = tileWidth             
            # w = map(greyscale, 0, 255, 12, 0)
            rect(posX, posY, w, w)
    
    
