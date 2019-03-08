# coding=utf-8
from random import randint

class Sheep:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sz = 10     # Shapesize
        self.move = 10
    
    def update(self):
        self.x += randint(-self.move, self.move)
        self.y += randint(-self.move, self.move)
        if self.x >= width - self.sz:
            self.x = width - self.sz
        if self.y >= height - self.sz:
            self.y = height - self.sz
        if self.x <= self.sz:
            self.x = self.sz
        if self.y <= self.sz:
            self.y = self.sz
        circle(self.x, self.y, self.sz)

class Settings():
    
    def __init__(self):
        
        # Einige nützliche Konstanten:
        self.WIDTH = 640
        self.HEIGHT = 480
        self.FPS = 5
        
        # Ein paar Farbdefinitionen
        self.WHITE = color(255, 255, 255)
        self.BLACK = color(0, 0, 0)
        self.GREEN = color(0, 100, 0)
