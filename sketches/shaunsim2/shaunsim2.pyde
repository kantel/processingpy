from config import Settings
from shaun import Sheep
from grass import Grass
from random import randint

s = Settings()
sz = s.PATCHSIZE
sheeps = []
lawn = []

def setup():
    size(s.WIDTH, s.HEIGHT)
    this.surface.setTitle("Shaun das Schaf (2): Vom Schaf zur Schafherde")
    frameRate(s.FPS)
    for _ in range(20):
        sheeps.append(Sheep(randint(50, width - 50), random(50, height - 50)))
    for x in range(0, width, sz):
        for y in range(0, height, sz):
            lawn.append(Grass(x, y, sz))
    
def draw():
    background(s.WHITE)
    for grass in lawn:
        grass.update()
    for sheep in sheeps:
        sheep.update(lawn)
        if sheep.energy <= 0:
            sheeps.remove(sheep)
