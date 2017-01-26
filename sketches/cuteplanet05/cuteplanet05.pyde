#Spaceship
from spaceship import Spaceship, Octopussy

octopussy = Octopussy("octopussy.png", 800, 150)
planet = Spaceship("planet.png", 500, 350)
rocketboy1 = Spaceship("rocketship.png", 300, 300)
rocketboy2 = Spaceship("rocketship.png", -300, 250)
beetle = Spaceship("beetleship.png", 200, 100)

ships = [planet, rocketboy1, rocketboy2, beetle]
fps = 30

def setup():
    size(920, 480)
    frameRate(fps)
    planet.loadPic()
    rocketboy1.loadPic()
    rocketboy2.loadPic()
    beetle.loadPic()
    octopussy.loadPic()
    rocketboy1.dx = rocketboy2.dx = beetle.dx = planet.dx= 0
    octopussy.dx = 0
    octopussy.dy = 0

def draw():
    background(0, 80, 125)
    for i in range(len(ships)):
        ships[i].move()
        ships[i].display()
    octopussy.move()
    octopussy.display()

def keyPressed():
    if keyPressed and key == CODED:
        planet.dx = 2
        rocketboy1.dx = 8
        rocketboy2.dx = 10
        beetle.dx = 6
        if keyCode == UP:
            octopussy.dy -= 1
        elif keyCode == DOWN:
            octopussy.dy += 1