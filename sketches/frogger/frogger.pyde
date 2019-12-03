from random import randint, choice
from frog import Frog
from lane import Lane

# bg = None
SAFETY = 0
CAR = 1
FLOAT = 2
GRID = 40
dx = dy = 0
WATER = color(124, 161, 192)
STREET = color(154, 154, 151)
GRASS = color(110, 170, 120)
SPEED = [-0.5, -0.75, 0.5, 0.75]

lanes = []

def reset_game():
    global frog
    frog = Frog(400, 400, GRID)
    frog.attach(None)
    
def setup():
    global bg
    size(800, 440)
    lanes.append(Lane(0, color(0, 0, 0)))
    lanes.append(Lane(1, GRASS))
    for _ in range(2, 5):
        lanes.append(Lane(_, WATER, FLOAT, randint(8, 12), 80, randint(240, 600), random(-0.1, -0.05), i = "float" + str(_ - 1) + ".png"))
    lanes.append(Lane(5, GRASS))
    for _ in range(6, 10):
        lanes.append(Lane(_, STREET, CAR, randint(4, 6), 80, randint(240, 600), choice(SPEED), i = "car" + str(_ - 5) + ".png"))
    lanes.append(Lane(10, GRASS))
    this.surface.setTitle("Frogger")
    reset_game()
    
def draw():
    global dx, dy
    background(0)
    for lane in lanes:
        lane.run()
    frog.show()
    if (frog.y == 0):
        reset_game()

def keyPressed():
    if key == CODED:
        if keyCode == UP: frog.move(0, -GRID)
        elif keyCode == DOWN: frog.move(0, GRID)
        elif keyCode == LEFT: frog.move(-GRID, 0)
        elif keyCode == RIGHT: frog.move(GRID, 0)
 
