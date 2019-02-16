FACTOR = 1

def setup():
    global akt
    size(800, 640)
    this.surface.setTitle("Floyd Steinberg Dithering")
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
            pix = akt.pixels[index(x, y)]
            oldC = red(pix)
            newC = round(FACTOR*oldC/255)*(255/FACTOR)
            akt.pixels[index(x, y)] = color(newC)
            
            errC = oldC - newC
            
            ix = index(x + 1, y)
            col = akt.pixels[ix]
            c = red(col)
            c += errC*7/16.0
            akt.pixels[ix] = color(c)
            
            ix = index(x - 1, y + 1)
            col = akt.pixels[ix]
            c = red(col)
            c += errC*3/16.0
            akt.pixels[ix] = color(c)

            ix = index(x, y + 1)
            col = akt.pixels[ix]
            c = red(col)
            c += errC*5/16.0
            akt.pixels[ix] = color(c)

            ix = index(x + 1, y + 1)
            col = akt.pixels[ix]
            c = red(col)
            c += errC*1/16.0
            akt.pixels[ix] = color(c)

    akt.updatePixels()
    image(akt, 400, 0)
   
