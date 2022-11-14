# Titelzeile in Processing 4

def setup():
    global artist
    size(400, 200)
    this.windowTitle("Hallo Processing.py 4")
    artist = loadImage("artist.png")
    noLoop()
    
    
def draw():
    background(color(230, 226, 204))  # Packpapier
    image(artist, 220, 20)
    print("I did it, Babe!")
