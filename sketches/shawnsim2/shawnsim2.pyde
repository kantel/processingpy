from shawn import Sheep, Settings
from random import randint

sheeps = []
s = Settings()

def setup():
    size(s.WIDTH, s.HEIGHT)
    this.surface.setTitle("Shawn das Schaf (2)")
    frameRate(s.FPS)
    for _ in range(20):
        sheeps.append(Sheep(randint(50, width - 50), random(50, height - 50)))
    
def draw():
    background(s.GREEN)
    for sheep in sheeps:
        sheep.update()
