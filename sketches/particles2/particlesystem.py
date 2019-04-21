# coding=utf-8

from particles import Particle
from rectparticles import RectParticle

class ParticleSystem(object):
    
    def __init__(self, l):
        self.location = l.get()
        self.particles = []
    
    def addParticle(self):
        # self.particles.append(Particle(self.location))
        ch = random(10)
        if ch <= 5:
            self.particles.append(Particle(self.location))
        else:
            self.particles.append(RectParticle(self.location))
        
    def run(self):
        for i in range(len(self.particles) - 1, -1, -1):
            self.particles[i].run()
            if self.particles[i].isDead():
                self.particles.pop(i)
        
