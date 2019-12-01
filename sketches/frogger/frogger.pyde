from frog import Frog

# bg = None
SAFETY = 0
CAR = 1
FLOAT = 2
GRID = 40
dx = dy = 0

def reset_game():
    global frog
    frog = Frog(400, 560, GRID)
    frog.attach(None)
    
def setup():
    global bg
    size(800, 600)
    this.surface.setTitle("Frogger")
    bg = loadImage("background.png")
    # frog = Frog(400, 560, GRID)
    reset_game()
    
def draw():
    global dx, dy
    image(bg, 0, 0)
    frog.show()
    if (frog.y == 0):
        reset_game()

def keyPressed():
    if key == CODED:
        if keyCode == UP: frog.move(0, -GRID)
        elif keyCode == DOWN: frog.move(0, GRID)
        elif keyCode == LEFT: frog.move(-GRID, 0)
        elif keyCode == RIGHT: frog.move(GRID, 0)
 
