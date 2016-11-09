#Spaceship

from spaceship import Spaceship

planet = Spaceship("planet.png", 500, 200)
rocket = Spaceship("rocketship.png", 300, 300)
octopussy = Spaceship("octopussy.png", 400, 400)

def setup():
    size(800, 600)
    planet.loadPic()
    planet.dx = 1
    rocket.loadPic()
    rocket.dx = 10
    octopussy.loadPic()
    octopussy.dx = -5

def draw():
    background(0, 80, 125)
    planet.move()
    planet.display()
    rocket.move()
    rocket.display()
    octopussy.move()
    octopussy.display()