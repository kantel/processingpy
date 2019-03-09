# coding=utf-8
from random import randint
from config import Settings

s = Settings()

class Sheep():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sz = s.PATCHSIZE     # Shapesize
        self.move = 10
        self.energy = 20
        self.rows = height/self.sz

    
    def update(self, lawn):
        self.energy -= 1
        self.x += randint(-self.move, self.move)
        self.y += randint(-self.move, self.move)
        if self.x >= width - self.sz:
            self.x = width - self.sz
        if self.y >= height - self.sz:
            self.y = height - self.sz
        if self.x <= 0:
            self.x = 0
        if self.y <= 0:
            self.y = 0
        xscl = int(self.x/self.sz)
        yscl = int(self.y/self.sz)
        grass = lawn[xscl*self.rows + yscl]
        if not grass.eaten:
            self.energy += grass.energy
            grass.eaten = True
        fill(s.WHITE)
        circle(self.x, self.y, self.sz)
