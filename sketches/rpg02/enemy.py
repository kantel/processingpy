from settings import *

class Enemy():
    
    def __init__(self):
        self.pos = PVector(random(width - 200) + 100, random(height - 200) + 100)
        self.w = self.h = 32
        self.vel = PVector(0, 0)
        self.img = loadImage("npc3_fr1.gif")
                    
    def update(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
    
    def display(self):
        image(self.img, self.pos.x, self.pos.y)

    def chase(self, p):
        if dist(self.pos.x, self.pos.y, p.x, p.y) > distance:
            self.vel = PVector(0, 0)
            return
        if abs(self.pos.x - p.x) < abs(self.pos.y - p.y):
            # Vertical separation is bigger
            if self.pos.y < p.y:
                self.vel.y = vel
                self.vel.x = 0
            else:
                self.vel.y = -vel
                self.vel.x = 0
        else:
            # Horizontal separation is bigger
            if self.pos.x < p.x:
                self.vel.x = vel
                self.vel.y = 0
            else:
                self.vel.x = -vel
                self.vel.y = 0
        
