cols = 12            # Anzahl der Spalten
rows = 22            # Anzahl der Reihen
tilesize = 32        # Kachelgröße
rotinc = 0.44        # Inkrementwert für die Rotation (in Grad)
rotsum = 0           # Rotation (in Grad)
padding = 3*tilesize # Abstand vom Fensterrand (rechts, links und oben, unten)
dampen = 0.45        # Dämpfungsfaktor

def setup():
    size((cols + 4)*tilesize, (rows + 4)*tilesize)
    this.surface.setTitle("Remixing Schotter: Fade-Out")
    stroke(0)
    strokeWeight(2)
    rectMode(CENTER)
    noLoop()

def draw():
    global rotsum
    background(235, 215, 182)
    for y in range(rows):
        rotsum += y*rotinc
        # fill(y*11, y*11, 255 - (y*22), 255 - (y*11))
        fill(155, 0, 0, 255 - (y*11))
        for x in range(cols):
            with pushMatrix():
                rotval = random(-rotsum, rotsum)
                translate(padding + (x*tilesize) - (0.5*tilesize) + (rotval*dampen),
                          padding + (y*tilesize) - (0.5*tilesize) + (rotval*dampen))
                rotate(radians(rotval))
                rect(0, 0, tilesize, tilesize)
