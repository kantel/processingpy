# Single Particle
from particle import Particle

particles = []


def setup():
    global loc
    size(640, 480)
    loc = PVector(width/2, 50)

def draw():
    global loc
    background(96)
    particles.append(Particle(loc))
    for particle in particles:
        particle.run()
        if particle.isDead():
            particles.pop()
            print(len(particles))