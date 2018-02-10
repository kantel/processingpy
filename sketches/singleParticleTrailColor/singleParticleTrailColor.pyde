# Single Particle
from particle import Particle

def setup():
    global p
    size(640, 480)
    loc = PVector(width/2, 50)
    p = Particle(loc)

def draw():
    global p
    background(0)
    p.run()