# coding=utf-8
from random import randint
from config import Settings

s = Settings()

class Sheep():
    
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.sz = 10     # Shapesize
        self.move = 10
        self.energy = 20
        self.rows = height/self.sz
        self.col = c

    
    def update(self, lawn):
        self.energy -= 1
        # if self.col == s.RED and randint(0, 1000) < 5:
        #     self.move = 25
        self.x += randint(-self.move, self.move)
        self.y += randint(-self.move, self.move)
        if self.x >= width - self.sz/2:
            self.x = width - self.sz/2
        if self.y >= height - self.sz/2:
            self.y = height - self.sz/2
        if self.x <= self.sz/2:
            self.x = self.sz/2
        if self.y <= self.sz/2:
            self.y = self.sz/2
        xscl = int(self.x/self.sz)
        yscl = int(self.y/self.sz)
        grass = lawn[xscl*self.rows + yscl]
        if not grass.eaten:
            self.energy += grass.energy
            grass.eaten = True
        fill(self.col)
        circle(self.x, self.y, self.sz)
