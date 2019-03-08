from config import Settings
from shawn import Sheep
from grass import Grass
from random import randint, choice

s = Settings()
sz = s.PATCHSIZE
sheeps = []
lawn = []
colors = [s.WHITE, s.RED, s.BLUE, s.YELLOW]

def setup():
    size(s.WIDTH, s.HEIGHT)
    this.surface.setTitle("Shawn das Schaf (4): Es kann nur einen geben!")
    frameRate(s.FPS)
    for _ in range(20):
        c = choice(colors)
        sheeps.append(Sheep(randint(50, width - 50), random(50, height - 50), c))
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
        if sheep.energy >= 50:
            sheep.energy -= 30
            sheeps.append(Sheep(sheep.x, sheep.y, sheep.col))
    # print(len(sheeps))
