#Spaceship

from spaceship import Spaceship, Octopussy

octopussy = Octopussy("octopussy.png", 800, 150)
planet = Spaceship("planet.png", 500, 350)
rocket = Spaceship("rocketship.png", 300, 300)
beetle = Spaceship("beetleship.png", 200, 100)

ships = [planet, rocket, beetle]

def setup():
    size(920, 480)
    planet.loadPic()
    planet.dx = 1
    rocket.loadPic()
    rocket.dx = 5
    beetle.loadPic()
    beetle.dx = 3
    octopussy.loadPic()
    octopussy.dx = 0
    octopussy.dy = 0

def draw():
    background(0, 80, 125)
    for i in range(len(ships)):
        ships[i].move()
        ships[i].display()
    if keyPressed and key == CODED:
        if keyCode == UP:
            octopussy.y -= 10
        elif keyCode == DOWN:
            octopussy.y += 10
    octopussy.move()
    octopussy.display()

