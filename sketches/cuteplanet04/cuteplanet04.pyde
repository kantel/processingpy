#Spaceship

from spaceship import Spaceship

planet = Spaceship("planet.png", 500, 350)
rocket = Spaceship("rocketship.png", 300, 300)
octopussy = Spaceship("octopussy.png", 400, 150)
beetle = Spaceship("beetleship.png", 200, 100)

ships = [planet, rocket, octopussy, beetle]

def setup():
    size(640, 480)
    planet.loadPic()
    planet.dx = 1
    rocket.loadPic()
    rocket.dx = 10
    octopussy.loadPic()
    octopussy.dx = -5
    beetle.loadPic()
    beetle.dx = 5

def draw():
    background(0, 80, 125)
    for i in range(len(ships)):
        ships[i].move()
        ships[i].display()
