# coding=utf-8

from particles import Particle

class RectParticle(Particle):
    
    def __init__(self, l):
        Particle.__init__(self, l)
        # super(RectParticle, self).__init__(l)
        rectMode(CENTER)
        self.rota = PI/3
    
    def display(self):
        stroke(0, self.lifespan)
        fill(204, 53, 100, self.lifespan)
        with pushMatrix():
            translate(self.location.x, self.location.y)
            rotate(self.rota)
            rect(0, 0, 20, 20)
            self.rota += random(0.02, .10)
