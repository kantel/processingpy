from settings import *

class Player():
    
    def __init__(self):
        self.pos = PVector(width/2, height/2)
        self.w = self.h = self.d = 32
        self.r = self.d/2  # Radius
        self.max_speed = 3
        self.speed = PVector(0, 0)
        self.img = loadImage("knt1_fr1.gif")
        self.debug = True # False
        
    def update(self):
        self.speed.limit(self.max_speed)
        self.pos.x += self.speed.x
        self.pos.y += self.speed.y
        self.check_boundaries()
        
    def display(self):
        image(self.img, self.pos.x, self.pos.y)
        if self.debug:
            fill(255, 255, 0, 100)
            circle(self.pos.x + self.w/2, self.pos.y + self.h/2, distance*2)
    
    def check_boundaries(self):
        if self.pos.x >= width - self.w:
            self.pos.x = width - self.w
        elif self.pos.x <= 0:
            self.pos.x = 0
        if self.pos.y >= height - self.h:
            self.pos.y = height - self.h
        elif self.pos.y <= 0:
            self.pos.y = 0
    
    # Kreis-Kollision
    def check_collision(self, other):
        distance = dist(self.pos.x, self.pos.y, other.pos.x, other.pos.y)
        if distance < self.r/2 + other.r/2:
            return(True)
        return(False)
