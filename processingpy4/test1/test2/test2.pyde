# Endless Scrolling Background
# Background Image: »PWL« (https://opengameart.org/content/seamless-desert-background-in-parts)
# Aeroplane: Tappy Plane, Kenney (https://www.kenney.nl/assets/tappy-plane)

def setup():
    global back1, back2, redBaron, bx
    size(720, 520)
    this.windowTitle("Endless Scrolling Background")
    this.windowMove(1300, 30)
    back1 = loadImage("desert.png")
    back2 = back1
    redBaron = loadImage("planeRed1.png")
    bx = 0
    
def draw():
    global bx
    image(back1, bx, 0)
    image(back2, width + bx, 0)
    image(redBaron, 50, 200)
    bx -= 1
    if bx == -width:
        bx = 0
