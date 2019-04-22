cols = 12            # Anzahl der Spalten
rows = 22            # Anzahl der Reihen
tilesize = 32        # Kachelgröße
rotinc = 0.22        # Inkrementwert für die Rotation (in Grad)
rotsum = 0           # Rotation (in Grad)
padding = 3*tilesize # Abstand vom Fensterrand (rechts, links und oben, unten)
dampen = 0.45        # Dämpfungsfaktor

def setup():
    size((cols + 4)*tilesize, (rows + 4)*tilesize)
    this.surface.setTitle("Re-Enactment Georg Nees: Schotter")
    stroke(0)
    strokeWeight(2)
    noFill()
    rectMode(CENTER)
    noLoop()

def draw():
    global rotsum
    background(235, 215, 182)
    for y in range(rows):
        rotsum += y*rotinc
        for x in range(cols):
            with pushMatrix():
                rotval = random(-rotsum, rotsum)
                translate(padding + (x*tilesize) - (0.5*tilesize) + (rotval*dampen),
                          padding + (y*tilesize) - (0.5*tilesize) + (rotval*dampen))
                rotate(radians(rotval))
                rect(0, 0, tilesize, tilesize)
