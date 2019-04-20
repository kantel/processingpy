from particles import Particle
from rectparticles import RectParticle

loc = PVector(250, 70)
particles = []

def setup():
    size(500, 500)
    this.surface.setTitle("Partikelsysteme 1")

def draw():
    background(235)
    ch = random(10)
    if ch <= 5:
        particles.append(Particle(loc))
    else:
        particles.append(RectParticle(loc))
    for i in range(len(particles) - 1, -1, -1):
        particles[i].run()
        if particles[i].isDead():
            particles.pop(i)
            # print(len(particles))
