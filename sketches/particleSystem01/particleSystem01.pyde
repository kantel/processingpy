# Single Particle
from particle import Particle

particles = []

def setup():
    size(640, 480)
    loc = PVector(width/2, 50)
    for i in range(100):
        particles.append(Particle(loc))

def draw():
    background(96)
    for particle in particles:
        particle.run()