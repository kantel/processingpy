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
    for i in range(len(particles) - 1, 0, -1):
        particles[i].run()
        if particles[i].isDead():
            particles.pop(i)
            print(len(particles))