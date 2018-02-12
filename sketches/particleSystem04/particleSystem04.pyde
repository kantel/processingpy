# Single Particle
from particle import Particle
from rectparticle import RectParticle

particles = []


def setup():
    global loc
    size(640, 480)
    loc = PVector(width/2, 50)

def draw():
    global loc
    background("#800080")
    ch = random(10)
    if ch <= 5:
        particles.append(Particle(loc))
    else:
        particles.append(RectParticle(loc))
    for i in range(len(particles) - 1, 0, -1):
        particles[i].run()
        if particles[i].isDead():
            particles.pop(i)
            print(len(particles))