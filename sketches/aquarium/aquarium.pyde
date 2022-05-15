from fish import Fish

WIDTH = 640
HEIGHT = 416
NFISHES = 15  # Anzahl der Fische
FPS = 60

fishes = []

def setup():
    global bg
    size(WIDTH, HEIGHT)
    # Processing.py 3
    this.surface.setTitle(u"Jörgs kleines, bonbonbuntes Aquarium")
    # Processing.py 4
    # this.windowTitle(u"Jörgs kleines, bonbonbuntes Aquarium")
    # this.windowMove(1400, 30)
    bg = loadImage("background.png")
    for _ in range(NFISHES):
        fishes.append(Fish())
    frameRate(FPS)
    
def draw():
    background(49, 197, 224) # Himmelblau
    image(bg, 0, 0)
    for fish in fishes:
        fish.show()
        fish.update()
