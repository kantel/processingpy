# coding=utf-8

from random import randint

class Sheep():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sz = 10
        self.move = 10
    
    def update(self):
        self.x += randint(-self.move, self.move)
        self.y += randint(-self.move, self.move)
        if self.x > width:
            self.x %= width
        if self.y > height:
            self.y %= height
        if self.x < 0:
            self.x += width
        if self.y < 0:
            self.y += height
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
