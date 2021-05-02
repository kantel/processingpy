from fish import Fish

WIDTH = 640
HEIGHT = 416
NFISHES = 12  # Anzahl der Fische
FPS = 60

fishes = []

def setup():
    global bg, fish1
    size(WIDTH, HEIGHT)
    this.surface.setTitle("Mein kleines, bonbonbuntes Aquarium")
    bg = loadImage("background.png")
    for _ in range(NFISHES):
        fishes.append(Fish("fish"))
    frameRate(FPS)
    

def draw():
    background(49, 197, 224) # Himmelblau
    image(bg, 0, 0)
    for fish in fishes:
        fish.show()
        fish.update()
