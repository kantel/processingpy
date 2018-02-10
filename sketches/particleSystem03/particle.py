# coding=utf-8

class Particle(object):
    
    def __init__(self, l):
        self.acceleration = PVector(0, 0.05)
        self.velocity = PVector(random(-1, 1), random(-2, 0))
        self.location = l.get()
        self.lifespan = 255.0
    
    def run(self):
        self.update()
        self.display()
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.location.add(self.velocity)
        self.lifespan -= 0.5
    
    def display(self):
        stroke(0, self.lifespan)
        fill(255, 0, 0, self.lifespan)
        ellipse(self.location.x, self.location.y, 20, 20)
        
    def isDead(self):
        if self.lifespan <= 0:
            return True
        else:
            return False