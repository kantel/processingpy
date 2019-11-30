from frog import Frog

# bg = None
GRID = 40
dx = dy = 0

def setup():
    global bg, frog
    size(800, 600)
    this.surface.setTitle("Frogger")
    bg = loadImage("background.png")
    frog = Frog(400, 560, GRID)
    
def draw():
    global dx, dy
    image(bg, 0, 0)
    frog.show()

def keyPressed():
    if key == CODED:
        if keyCode == UP: frog.move(0, -GRID)
        elif keyCode == DOWN: frog.move(0, GRID)
        elif keyCode == LEFT: frog.move(-GRID, 0)
        elif keyCode == RIGHT: frog.move(GRID, 0)
 
