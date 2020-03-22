from proband import Proband
from random import randint

FPS = 5

probanden = []

def setup():
    size(600, 600)
    this.surface.setTitle("Pandemie-Simulation")
    frameRate(FPS)
    for _ in range(100):
        rate = randint(0, 100)
        if rate < 1:
            infz = 30
        else:
            infz = 0
        probanden.append(Proband(randint(50, width - 50), randint(50, height - 50), infz))

def draw():
    background(151)
    for p in probanden:
        p.update()
        for other in probanden:
            other.collision(p)
