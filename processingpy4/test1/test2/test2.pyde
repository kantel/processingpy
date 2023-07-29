# Endless Scrolling Background
# Background Image: »PWL« (https://opengameart.org/content/seamless-desert-background-in-parts)
# Aeroplane: Tappy Plane, Kenney (https://www.kenney.nl/assets/tappy-plane)

BG_WIDTH = 1067     # Breite des Hintergrundbildes
planes = []

def setup():
    global back1, back2, bx, r
    size(720, 420)
    this.windowTitle("Endless Scrolling Background")
    this.windowMove(1300, 30)
    back1 = loadImage("desert.png")
    back2 = back1
    bx = 0
    for i in range(3):
        plane = loadImage("planeRed" + str(i) + ".png")
        planes.append(plane)
    r = 0
    
def draw():
    global bx, r
    image(back1, bx, 0)
    image(back2, BG_WIDTH + bx, 0)
    bx -= 1
    if bx == -BG_WIDTH:
        bx = 0
        # noLoop()
    image(planes[int(r)], 50, 200)
    # saveFrame("output/tappyplane_####.png")
    r += 0.2
    if r >= 3:
        r = 0
